import asyncio

import httpx

from app.main import DOCUMENTS, app, split_document


def request(method: str, path: str, **kwargs: object) -> httpx.Response:
    async def run() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            return await client.request(method, path, **kwargs)

    return asyncio.run(run())


def setup_function() -> None:
    DOCUMENTS.clear()


def test_health_reports_mode() -> None:
    response = request("GET", "/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["mode"] in {"demo", "provider"}


def test_document_can_be_retrieved() -> None:
    added = request(
        "POST",
        "/api/documents",
        json={"title": "部署说明", "text": "生产环境使用蓝绿部署。发布前必须运行评测回归和健康检查。"},
    )
    assert added.status_code == 200
    response = request("POST", "/api/search", json={"query": "发布前要运行什么检查", "top_k": 3})
    assert response.status_code == 200
    assert response.json()[0]["title"] == "部署说明"


def test_demo_chat_streams_sse() -> None:
    response = request(
        "POST",
        "/api/chat",
        json={"messages": [{"role": "user", "content": "如何接入模型？"}], "use_rag": False},
    )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")
    assert "event: token" in response.text
    assert "event: done" in response.text


def test_oversized_paragraph_is_chunked() -> None:
    chunks = split_document("x" * 1_501, limit=700)
    assert [len(chunk) for chunk in chunks] == [700, 700, 101]


def test_rag_chat_sends_citations_before_tokens() -> None:
    request("POST", "/api/documents", json={"title": "运行手册", "text": "发布前执行健康检查和回归评测，失败时停止发布。"})
    response = request(
        "POST",
        "/api/chat",
        json={"messages": [{"role": "user", "content": "发布前执行什么？"}], "use_rag": True},
    )
    assert response.status_code == 200
    assert response.text.index("event: citations") < response.text.index("event: token")


def test_invalid_chat_and_clear_documents() -> None:
    invalid = request("POST", "/api/chat", json={"messages": [{"role": "assistant", "content": "没有问题"}]})
    assert invalid.status_code == 422
    request("POST", "/api/documents", json={"title": "临时", "text": "这是一个用于清理测试的文档片段，正文长度满足入库校验。"})
    cleared = request("DELETE", "/api/documents")
    assert cleared.status_code == 200
    assert cleared.json()["removedChunks"] == 1
    assert DOCUMENTS == []
