import { FormEvent, useEffect, useRef, useState } from 'react';
import { Activity, BookOpen, Database, FilePlus2, Send, Square, Trash2 } from 'lucide-react';

type Role = 'user' | 'assistant';
type Citation = { id: string; title: string; excerpt: string; score: number };
type Message = { id: string; role: Role; content: string; citations?: Citation[] };
type Health = { status: string; mode: string; model: string };

const starter: Message = {
  id: 'starter',
  role: 'assistant',
  content: '模型连接已就绪。添加一段文档后，可以验证检索、引用与流式回答。',
};

function parseEvent(block: string): { event: string; data: Record<string, unknown> } | null {
  const event = block.match(/^event:\s*(.+)$/m)?.[1];
  const data = block.match(/^data:\s*(.+)$/m)?.[1];
  if (!event || !data) return null;
  try {
    return { event, data: JSON.parse(data) as Record<string, unknown> };
  } catch {
    return null;
  }
}

export default function App() {
  const [messages, setMessages] = useState<Message[]>([starter]);
  const [question, setQuestion] = useState('');
  const [documentTitle, setDocumentTitle] = useState('');
  const [documentText, setDocumentText] = useState('');
  const [documentCount, setDocumentCount] = useState(0);
  const [health, setHealth] = useState<Health | null>(null);
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState('');
  const endRef = useRef<HTMLDivElement>(null);
  const controllerRef = useRef<AbortController | null>(null);
  const autoScrollRef = useRef(false);

  useEffect(() => {
    fetch('/api/health').then((response) => response.json()).then(setHealth).catch(() => setHealth(null));
  }, []);
  useEffect(() => {
    if (autoScrollRef.current) endRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  async function addDocument(event: FormEvent) {
    event.preventDefault();
    setNotice('');
    try {
      const response = await fetch('/api/documents', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: documentTitle, text: documentText }),
      });
      if (!response.ok) {
        setNotice('文档写入失败，请确认标题和正文长度。');
        return;
      }
      const result = await response.json() as { chunks: number };
      setDocumentCount((count) => count + result.chunks);
      setDocumentTitle('');
      setDocumentText('');
      setNotice(`已写入 ${result.chunks} 个检索片段。`);
    } catch {
      setNotice('文档写入失败：后端未连接。');
    }
  }

  async function clearDocuments() {
    try {
      const response = await fetch('/api/documents', { method: 'DELETE' });
      if (!response.ok) throw new Error('clear failed');
      setDocumentCount(0);
      setNotice('知识库已清空。');
    } catch {
      setNotice('清空失败：后端未连接。');
    }
  }

  function cancelGeneration() {
    controllerRef.current?.abort();
  }

  async function send(event: FormEvent) {
    event.preventDefault();
    const input = question.trim();
    if (!input || busy) return;
    const userMessage: Message = { id: crypto.randomUUID(), role: 'user', content: input };
    const assistantId = crypto.randomUUID();
    autoScrollRef.current = true;
    setMessages((items) => [...items, userMessage, { id: assistantId, role: 'assistant', content: '' }]);
    setQuestion('');
    setBusy(true);
    const controller = new AbortController();
    controllerRef.current = controller;

    try {
      const history = [...messages.filter((message) => message.id !== 'starter'), userMessage]
        .map(({ role, content }) => ({ role, content }));
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: history, use_rag: true, top_k: 3 }),
        signal: controller.signal,
      });
      if (!response.ok || !response.body) throw new Error('stream unavailable');
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      while (true) {
        const { value, done } = await reader.read();
        buffer += decoder.decode(value || new Uint8Array(), { stream: !done });
        const blocks = buffer.split('\n\n');
        buffer = blocks.pop() || '';
        for (const block of blocks) {
          const item = parseEvent(block);
          if (!item) continue;
          if (item.event === 'token') {
            setMessages((items) => items.map((message) => message.id === assistantId
              ? { ...message, content: message.content + String(item.data.text || '') }
              : message));
          }
          if (item.event === 'citations') {
            setMessages((items) => items.map((message) => message.id === assistantId
              ? { ...message, citations: item.data.items as Citation[] }
              : message));
          }
          if (item.event === 'error') throw new Error(String(item.data.message || 'request failed'));
        }
        if (done) break;
      }
    } catch (error) {
      const errorMessage = error instanceof DOMException && error.name === 'AbortError'
        ? '已停止生成。'
        : error instanceof Error ? error.message : '请求失败，请稍后重试。';
      setMessages((items) => items.map((message) => message.id === assistantId
        ? { ...message, content: errorMessage }
        : message));
    } finally {
      controllerRef.current = null;
      setBusy(false);
    }
  }

  return (
    <div className="app-shell">
      <aside className="knowledge-panel">
        <div className="product-mark"><BookOpen size={19} /><span>LLM Workspace</span></div>
        <div className="service-state" aria-live="polite">
          <Activity size={15} />
          <span>{health ? `${health.mode} · ${health.model}` : '后端未连接'}</span>
        </div>
        <section aria-labelledby="knowledge-title">
          <div className="section-heading">
            <div><span className="eyebrow">Knowledge</span><h2 id="knowledge-title">知识库</h2></div>
            <span className="chunk-count">{documentCount} chunks</span>
          </div>
          <form className="document-form" onSubmit={addDocument}>
            <label>标题<input value={documentTitle} onChange={(event) => setDocumentTitle(event.target.value)} required maxLength={120} /></label>
            <label>正文<textarea value={documentText} onChange={(event) => setDocumentText(event.target.value)} required minLength={20} rows={8} /></label>
            <button className="primary-action" type="submit"><FilePlus2 size={16} />写入知识库</button>
          </form>
          <button className="quiet-action" type="button" onClick={clearDocuments} disabled={!documentCount}><Trash2 size={15} />清空知识库</button>
          <p className="notice" aria-live="polite">{notice}</p>
        </section>
      </aside>

      <main className="conversation" id="main-content" tabIndex={-1}>
        <header className="conversation-header">
          <div><span className="eyebrow">Conversation</span><h1>引用型问答</h1></div>
          <div className="rag-state"><Database size={15} />RAG on</div>
        </header>
        <div className="message-list" aria-live="polite">
          {messages.map((message) => (
            <article className={`message ${message.role}`} key={message.id}>
              <div className="message-role">{message.role === 'user' ? '你' : '助手'}</div>
              <div className="message-body">{message.content || <span className="typing">正在生成</span>}</div>
              {message.citations && message.citations.length > 0 && (
                <div className="citations">
                  {message.citations.map((citation, index) => (
                    <details key={citation.id}>
                      <summary>[{index + 1}] {citation.title}</summary>
                      <p>{citation.excerpt}</p>
                    </details>
                  ))}
                </div>
              )}
            </article>
          ))}
          <div ref={endRef} />
        </div>
        <form className="composer" onSubmit={send}>
          <label className="sr-only" htmlFor="question">输入问题</label>
          <textarea id="question" value={question} onChange={(event) => setQuestion(event.target.value)} onKeyDown={(event) => { if (event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); event.currentTarget.form?.requestSubmit(); } }} placeholder="询问知识库中的内容" rows={2} disabled={busy} />
          <button type={busy ? 'button' : 'submit'} onClick={busy ? cancelGeneration : undefined} aria-label={busy ? '停止生成' : '发送'} title={busy ? '停止生成' : '发送'} disabled={!busy && !question.trim()}>{busy ? <Square size={16} /> : <Send size={18} />}</button>
        </form>
      </main>
    </div>
  );
}
