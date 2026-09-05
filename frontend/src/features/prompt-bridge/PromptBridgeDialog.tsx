import { useEffect, useRef, useState } from 'react'
import { api } from '../../api'

interface Props {
  mode: 'content_onboarding' | 'weekly_review' | 'project_optimizer'
  contentSlug?: string
  projectSlug?: string
  triggerLabel?: string
  disabled?: boolean
}

export function PromptBridgeDialog({
  mode,
  contentSlug,
  projectSlug,
  triggerLabel = 'ChatGPT에 물어보기',
  disabled = false,
}: Props) {
  const [open, setOpen] = useState(false)
  const [question, setQuestion] = useState('')
  const [preview, setPreview] = useState('')
  const [stats, setStats] = useState({ characters: 0, tokens: 0, overBudget: false })
  const [status, setStatus] = useState('')
  const [loading, setLoading] = useState(false)
  const previewRef = useRef<HTMLTextAreaElement>(null)

  useEffect(() => {
    if (!open) return
    const timer = window.setTimeout(() => {
      setLoading(true)
      setStatus('')
      void api.renderPrompt({
        mode,
        content_slug: contentSlug,
        project_slug: projectSlug,
        user_question: question,
      })
        .then((result) => {
          setPreview(result.markdown)
          setStats({
            characters: result.character_count,
            tokens: result.estimated_tokens,
            overBudget: result.over_budget,
          })
        })
        .catch((error: Error) => setStatus(error.message))
        .finally(() => setLoading(false))
    }, 150)
    return () => window.clearTimeout(timer)
  }, [open, question, mode, contentSlug, projectSlug])

  async function copy() {
    try {
      await navigator.clipboard.writeText(preview)
      setStatus('클립보드에 복사했습니다.')
    } catch {
      previewRef.current?.focus()
      previewRef.current?.select()
      setStatus('자동 복사가 차단되었습니다. 선택된 텍스트를 직접 복사해 주세요.')
    }
  }

  function download() {
    const blob = new Blob([preview], { type: 'text/markdown;charset=utf-8' })
    const url = URL.createObjectURL(blob)
    const anchor = document.createElement('a')
    anchor.href = url
    anchor.download = `bdo-${mode}.md`
    anchor.click()
    URL.revokeObjectURL(url)
  }

  return (
    <>
      <button className="button primary" disabled={disabled} onClick={() => setOpen(true)}>
        {triggerLabel}
      </button>
      {open && (
        <div className="dialog-backdrop" role="presentation" onMouseDown={() => setOpen(false)}>
          <section className="dialog" role="dialog" aria-modal="true" aria-label="Prompt Bridge" onMouseDown={(event) => event.stopPropagation()}>
            <header className="dialog-header">
              <div><p className="eyebrow">LOCAL PROMPT BRIDGE</p><h2>ChatGPT 질문 준비</h2></div>
              <button className="icon-button" aria-label="닫기" onClick={() => setOpen(false)}>×</button>
            </header>
            <label className="field-label" htmlFor="question">추가 질문</label>
            <textarea
              id="question"
              className="question-input"
              value={question}
              onChange={(event) => setQuestion(event.target.value)}
              placeholder={
                mode === 'project_optimizer'
                  ? '이번 주 안에 최대한 빨리 끝내는 순서를 짜줘'
                  : mode === 'weekly_review'
                    ? '이번 주 남은 일의 우선순위를 정해줘'
                    : '지금 내 상태에서 무엇부터 하면 돼?'
              }
            />
            <div className="preview-meta">
              <span>{loading ? '생성 중…' : `${stats.characters.toLocaleString()}자 · 약 ${stats.tokens.toLocaleString()} tokens`}</span>
              {stats.overBudget && <strong>권장 크기 초과</strong>}
            </div>
            <textarea ref={previewRef} className="prompt-preview" value={preview} readOnly aria-label="생성된 Markdown 프롬프트" />
            <div className="dialog-actions">
              <span className="status-message" role="status">{status}</span>
              <button className="button ghost" onClick={download} disabled={!preview}>Markdown 저장</button>
              <button className="button primary" onClick={() => void copy()} disabled={!preview}>복사</button>
            </div>
            <p className="privacy-line">이 기능은 외부로 전송하지 않습니다. 복사 후 사용자가 직접 붙여넣습니다.</p>
          </section>
        </div>
      )}
    </>
  )
}
