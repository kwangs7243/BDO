import { useEffect, useId, useMemo, useRef, useState } from 'react'
import {
  api,
  type PromptMode,
  type PromptOutputMode,
  type PromptSection,
  type PromptSizeMode,
} from '../../api'
import {
  defaultPromptSections,
  promptPlaceholders,
  promptSectionLabels,
} from './promptConfig'

interface Props {
  mode: PromptMode
  contentSlug?: string
  projectSlug?: string
  triggerLabel?: string
  disabled?: boolean
  variant?: 'primary' | 'ghost'
}

export function PromptBridgeDialog({
  mode,
  contentSlug,
  projectSlug,
  triggerLabel = 'ChatGPT에 물어보기',
  disabled = false,
  variant = 'primary',
}: Props) {
  const controlId = useId()
  const [open, setOpen] = useState(false)
  const [question, setQuestion] = useState('')
  const selectionKey = [mode, contentSlug ?? '', projectSlug ?? ''].join(':')
  const defaultSections = useMemo(
    () => defaultPromptSections(mode, contentSlug, projectSlug),
    [mode, contentSlug, projectSlug],
  )
  const [selection, setSelection] = useState({
    key: selectionKey,
    sections: defaultSections,
  })
  if (selection.key !== selectionKey) {
    setSelection({ key: selectionKey, sections: defaultSections })
  }
  const includeSections = selection.key === selectionKey
    ? selection.sections
    : defaultSections
  const [outputMode, setOutputMode] = useState<PromptOutputMode>('full_prompt')
  const [sizeMode, setSizeMode] = useState<PromptSizeMode>('auto')
  const [preview, setPreview] = useState('')
  const [stats, setStats] = useState({
    characters: 0,
    tokens: 0,
    originalTokens: 0,
    compacted: false,
    omittedCounts: {} as Record<string, number>,
    overBudget: false,
  })
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
        user_question: outputMode === 'full_prompt' ? question : '',
        include_sections: includeSections,
        output_mode: outputMode,
        size_mode: sizeMode,
      })
        .then((result) => {
          setPreview(result.markdown)
          setStats({
            characters: result.character_count,
            tokens: result.estimated_tokens,
            originalTokens: result.original_estimated_tokens,
            compacted: result.compacted,
            omittedCounts: result.omitted_counts,
            overBudget: result.over_budget,
          })
        })
        .catch((error: Error) => setStatus(error.message))
        .finally(() => setLoading(false))
    }, 150)
    return () => window.clearTimeout(timer)
  }, [
    open,
    question,
    mode,
    contentSlug,
    projectSlug,
    includeSections,
    outputMode,
    sizeMode,
  ])

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

  const availableSections = defaultPromptSections(mode, contentSlug, projectSlug)
  const omittedSummary = Object.entries(stats.omittedCounts)
    .map(([section, count]) => section + ' ' + count)
    .join(', ')

  function toggleSection(section: PromptSection, checked: boolean) {
    setSelection((current) => ({
      key: selectionKey,
      sections: checked
        ? availableSections.filter(
          (item) => item === section || current.sections.includes(item),
        )
        : current.sections.filter((item) => item !== section),
    }))
  }

  return (
    <>
      <button className={`button ${variant}`} disabled={disabled} onClick={() => setOpen(true)}>
        {triggerLabel}
      </button>
      {open && (
        <div className="dialog-backdrop" role="presentation" onMouseDown={() => setOpen(false)}>
          <section className="dialog" role="dialog" aria-modal="true" aria-label="Prompt Bridge" onMouseDown={(event) => event.stopPropagation()}>
            <header className="dialog-header">
              <div><p className="eyebrow">LOCAL PROMPT BRIDGE</p><h2>ChatGPT 질문 준비</h2></div>
              <button className="icon-button" aria-label="닫기" onClick={() => setOpen(false)}>×</button>
            </header>
            <details className="prompt-controls" open>
              <summary>포함할 컨텍스트</summary>
              <div className="prompt-section-grid">
                {availableSections.map((section) => (
                  <label key={section}>
                    <input
                      type="checkbox"
                      checked={includeSections.includes(section)}
                      onChange={(event) => toggleSection(section, event.target.checked)}
                    />
                    {promptSectionLabels[section]}
                  </label>
                ))}
              </div>
            </details>
            <div className="prompt-mode-controls">
              <fieldset>
                <legend>출력 형식</legend>
                <label htmlFor={controlId + '-full'}>
                  <input
                    id={controlId + '-full'}
                    type="radio"
                    name={controlId + '-output'}
                    checked={outputMode === 'full_prompt'}
                    onChange={() => setOutputMode('full_prompt')}
                  />
                  전체 프롬프트
                </label>
                <label htmlFor={controlId + '-context'}>
                  <input
                    id={controlId + '-context'}
                    type="radio"
                    name={controlId + '-output'}
                    checked={outputMode === 'context_only'}
                    onChange={() => setOutputMode('context_only')}
                  />
                  컨텍스트만
                </label>
              </fieldset>
              <fieldset>
                <legend>크기</legend>
                <label htmlFor={controlId + '-auto'}>
                  <input
                    id={controlId + '-auto'}
                    type="radio"
                    name={controlId + '-size'}
                    checked={sizeMode === 'auto'}
                    onChange={() => setSizeMode('auto')}
                  />
                  자동 크기 조절
                </label>
                <label htmlFor={controlId + '-detailed'}>
                  <input
                    id={controlId + '-detailed'}
                    type="radio"
                    name={controlId + '-size'}
                    checked={sizeMode === 'detailed'}
                    onChange={() => setSizeMode('detailed')}
                  />
                  상세하게
                </label>
              </fieldset>
            </div>
            {outputMode === 'full_prompt' ? (
              <>
                <label className="field-label" htmlFor={controlId + '-question'}>추가 질문</label>
                <textarea
                  id={controlId + '-question'}
                  className="question-input"
                  value={question}
                  onChange={(event) => setQuestion(event.target.value)}
                  placeholder={promptPlaceholders[mode]}
                />
              </>
            ) : (
              <p className="context-only-note">
                컨텍스트만 출력할 때는 질문과 응답 지침을 포함하지 않습니다.
              </p>
            )}
            <div className="preview-meta">
              <span>
                {loading ? '생성 중…' : (
                  <>
                    {stats.characters.toLocaleString()}자 · 약 {stats.tokens.toLocaleString()} tokens
                    {stats.compacted && (
                      <> · 자동 축약됨 (축약 전 약 {stats.originalTokens.toLocaleString()})</>
                    )}
                  </>
                )}
              </span>
              {stats.overBudget && <strong>권장 크기 초과</strong>}
            </div>
            {omittedSummary && (
              <p className="omitted-summary">생략: {omittedSummary}</p>
            )}
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
