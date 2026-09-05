import { useEffect, useState } from 'react'
import { api } from '../../api'
import type { ContentSummary, ProjectSummary } from '../../types'
import { PromptBridgeDialog } from './PromptBridgeDialog'

export function PromptPage() {
  const [contents, setContents] = useState<ContentSummary[]>([])
  const [contentSlug, setContentSlug] = useState('')
  const [projects, setProjects] = useState<ProjectSummary[]>([])
  const [projectSlug, setProjectSlug] = useState('')

  useEffect(() => {
    let active = true
    void api.contents()
      .then((items) => {
        if (!active) return
        setContents(items)
        setContentSlug(items[0]?.slug ?? '')
      })
      .catch(() => undefined)
    void api.projects()
      .then((items) => {
        if (!active) return
        setProjects(items)
        setProjectSlug(items[0]?.slug ?? '')
      })
      .catch(() => undefined)
    return () => { active = false }
  }, [])

  return (
    <div>
      <header className="page-header">
        <div>
          <p className="eyebrow">COPY, DON'T SEND</p>
          <h1>Prompt Bridge</h1>
          <p className="subtitle">로컬 데이터를 Markdown으로 만들고, 직접 복사해 사용합니다.</p>
        </div>
      </header>

      <section className="prompt-launcher">
        <p className="eyebrow">PROJECT OPTIMIZER</p>
        <h2>프로젝트 진행 순서 질문</h2>
        <label className="field-label" htmlFor="project-select">프로젝트 선택</label>
        <select
          id="project-select"
          value={projectSlug}
          disabled={projects.length === 0}
          onChange={(event) => setProjectSlug(event.target.value)}
        >
          {projects.map((item) => (
            <option value={item.slug} key={item.slug}>{item.name_ko}</option>
          ))}
        </select>
        {projects.length === 0 && <p className="empty">사용할 수 있는 프로젝트가 없습니다.</p>}
        <PromptBridgeDialog
          mode="project_optimizer"
          projectSlug={projectSlug}
          triggerLabel="프로젝트 프롬프트 만들기"
          disabled={!projectSlug}
        />
      </section>

      <section className="prompt-launcher">
        <p className="eyebrow">CONTENT ONBOARDING</p>
        <h2>콘텐츠 입문 질문</h2>
        <label className="field-label" htmlFor="content-select">콘텐츠 선택</label>
        <select
          id="content-select"
          value={contentSlug}
          onChange={(event) => setContentSlug(event.target.value)}
        >
          {contents.map((item) => (
            <option value={item.slug} key={item.slug}>{item.name_ko}</option>
          ))}
        </select>
        <PromptBridgeDialog
          mode="content_onboarding"
          contentSlug={contentSlug}
          triggerLabel="입문 프롬프트 만들기"
        />
      </section>

      <section className="prompt-launcher">
        <p className="eyebrow">WEEKLY REVIEW</p>
        <h2>이번 주 우선순위 질문</h2>
        <p>현재 기간의 완료·미완료 체크 상태를 포함합니다.</p>
        <PromptBridgeDialog mode="weekly_review" triggerLabel="주간 프롬프트 만들기" />
      </section>
    </div>
  )
}
