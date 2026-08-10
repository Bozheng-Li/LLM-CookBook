from __future__ import annotations

import asyncio
import json
import os
import re
from collections.abc import AsyncIterator
from pathlib import Path
from typing import Literal
from uuid import uuid4

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

load_dotenv(Path(__file__).resolve().parents[2] / ".env")


class Settings(BaseModel):
    api_base: str = os.getenv("LLM_API_BASE", "https://api.openai.com/v1")
    api_key: str = os.getenv("LLM_API_KEY", "")
    model: str = os.getenv("LLM_MODEL", "gpt-4.1-mini")
    allowed_origins: list[str] = [
        item.strip()
        for item in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
        if item.strip()
    ]


SETTINGS = Settings()


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1, max_length=20_000)


class ChatRequest(BaseModel):
    messages: list[Message] = Field(min_length=1, max_length=50)
    use_rag: bool = True
    top_k: int = Field(default=3, ge=1, le=6)


class DocumentInput(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    text: str = Field(min_length=20, max_length=100_000)


class SearchInput(BaseModel):
    query: str = Field(min_length=1, max_length=2_000)
    top_k: int = Field(default=3, ge=1, le=10)


class Citation(BaseModel):
    id: str
    title: str
    excerpt: str
    score: float


DOCUMENTS: list[dict[str, str]] = []

app = FastAPI(title="Cookbook Full-stack LLM", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=SETTINGS.allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["Content-Type"],
)


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9_]+|[\u4e00-\u9fff]", text.lower()))


def split_document(text: str, limit: int = 700) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        # Keep the demo's chunk-size contract even when one paragraph is oversized.
        pieces = [paragraph[index : index + limit] for index in range(0, len(paragraph), limit)]
        for piece in pieces:
            if current and len(current) + len(piece) + 1 > limit:
                chunks.append(current)
                current = ""
            current = f"{current}\n{piece}".strip()
    if current:
        chunks.append(current)
    return chunks


def search_documents(query: str, top_k: int) -> list[Citation]:
    query_tokens = tokens(query)
    ranked: list[Citation] = []
    for item in DOCUMENTS:
        item_tokens = tokens(item["text"])
        overlap = len(query_tokens & item_tokens)
        if overlap == 0:
            continue
        score = overlap / max(1, len(query_tokens))
        ranked.append(
            Citation(
                id=item["id"],
                title=item["title"],
                excerpt=item["text"][:220],
                score=round(score, 4),
            )
        )
    ranked.sort(key=lambda item: item.score, reverse=True)
    return ranked[:top_k]


def sse(event: str, payload: dict[str, object]) -> str:
    return f"event: {event}\ndata: {json.dumps(payload, ensure_ascii=False)}\n\n"


async def demo_stream(question: str, citations: list[Citation]) -> AsyncIterator[str]:
    if citations:
        answer = (
            "已从本地知识库检索到相关片段。这个演示使用可替换的检索边界："
            "前端只接收标准引用对象，后端可以在不改 UI 的情况下换成 Embedding 与 pgvector。"
        )
    else:
        answer = (
            f"当前是无密钥演示模式。你问的是“{question[:80]}”。"
            "配置 LLM_API_KEY 后，后端会把同一请求流式转发给 OpenAI-compatible 模型服务。"
        )
    for piece in re.findall(r".{1,8}", answer):
        yield sse("token", {"text": piece})
        await asyncio.sleep(0.025)


async def provider_stream(messages: list[dict[str, str]]) -> AsyncIterator[str]:
    endpoint = f"{SETTINGS.api_base.rstrip('/')}/chat/completions"
    payload = {"model": SETTINGS.model, "messages": messages, "stream": True, "temperature": 0.2}
    headers = {"Authorization": f"Bearer {SETTINGS.api_key}", "Content-Type": "application/json"}
    timeout = httpx.Timeout(60, connect=10)
    async with httpx.AsyncClient(timeout=timeout) as client:
        async with client.stream("POST", endpoint, json=payload, headers=headers) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                try:
                    token = json.loads(data)["choices"][0]["delta"].get("content")
                except (KeyError, IndexError, TypeError, json.JSONDecodeError):
                    continue
                if token:
                    yield sse("token", {"text": token})


@app.get("/api/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "mode": "provider" if SETTINGS.api_key else "demo", "model": SETTINGS.model}


@app.post("/api/documents")
async def add_document(document: DocumentInput) -> dict[str, object]:
    document_id = str(uuid4())
    chunks = split_document(document.text)
    for index, chunk in enumerate(chunks):
        DOCUMENTS.append({"id": f"{document_id}:{index}", "title": document.title, "text": chunk})
    return {"id": document_id, "title": document.title, "chunks": len(chunks)}


@app.delete("/api/documents")
async def clear_documents() -> dict[str, int]:
    count = len(DOCUMENTS)
    DOCUMENTS.clear()
    return {"removedChunks": count}


@app.post("/api/search", response_model=list[Citation])
async def search(request: SearchInput) -> list[Citation]:
    return search_documents(request.query, request.top_k)


@app.post("/api/chat")
async def chat(request: ChatRequest) -> StreamingResponse:
    question = next((message.content for message in reversed(request.messages) if message.role == "user"), "")
    if not question:
        raise HTTPException(status_code=422, detail="A user message is required")
    citations = search_documents(question, request.top_k) if request.use_rag else []
    messages = [message.model_dump() for message in request.messages]
    if citations:
        context = "\n\n".join(f"[{index + 1}] {item.title}\n{item.excerpt}" for index, item in enumerate(citations))
        messages.insert(0, {"role": "system", "content": f"只基于下列证据回答；证据不足时明确说明。\n\n{context}"})

    async def stream() -> AsyncIterator[str]:
        if citations:
            yield sse("citations", {"items": [item.model_dump() for item in citations]})
        try:
            source = provider_stream(messages) if SETTINGS.api_key else demo_stream(question, citations)
            async for event in source:
                yield event
            yield sse("done", {"ok": True})
        except (httpx.HTTPError, asyncio.TimeoutError):
            yield sse("error", {"message": "模型服务暂时不可用，请检查端点、密钥和网络后重试。"})

    return StreamingResponse(
        stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
