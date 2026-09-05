import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { api } from '../../api'
import { StatusBadge } from '../../components/StatusBadge'
import type { LifeContent, LifeSkillDetail } from '../../types'
import { PromptBridgeDialog } from '../prompt-bridge/PromptBridgeDialog'
import { LifeContentCard } from './LifeContentCard'

const sections: Array<{
  key: keyof Pick<
    LifeSkillDetail,
    | 'foundation_contents'
    | 'getting_started'
    | 'equipment'
    | 'core_systems'
    | 'recurring_contents'
    | 'advanced_contents'
    | 'related_economy'
  >
  eyebrow: string
  title: string
}> = [
  { key: 'foundation_contents', eyebrow: 'FOUNDATION', title: '분야 기반' },
  { key: 'getting_started', eyebrow: 'GETTING STARTED', title: '시작하기' },
  { key: 'equipment', eyebrow: 'EQUIPMENT', title: '장비와 세팅' },
  { key: 'core_systems', eyebrow: 'CORE SYSTEMS', title: '핵심 시스템' },
  { key: 'recurring_contents', eyebrow: 'ROUTINES', title: '반복과 루틴' },
  { key: 'advanced_contents', eyebrow: 'ADVANCED', title: '심화 콘텐츠' },
  { key: 'related_economy', eyebrow: 'ECONOMY', title: '관련 생활 기반과 경제' },
]

function ContentSection({ title, eyebrow, contents }: {
  title: string
  eyebrow: string
  contents: LifeContent[]
}) {
  if (contents.length === 0) return null
  return (
    <section className="detail-section life-section">
      <p className="eyebrow">{eyebrow}</p>
      <h2>{title}</h2>
      <div className="life-content-grid">
        {contents.map((content) => (
          <LifeContentCard content={content} key={content.slug} />
        ))}
      </div>
    </section>
  )
}

export function LifeSkillPage() {
  const { skill = '' } = useParams()
  const [result, setResult] = useState<{ key: string; detail: LifeSkillDetail } | null>(null)
  const [failure, setFailure] = useState<{ key: string; message: string } | null>(null)

  useEffect(() => {
    api.lifeSkill(skill)
      .then((detail) => setResult({ key: skill, detail }))
      .catch((reason: Error) => setFailure({ key: skill, message: reason.message }))
  }, [skill])

  const detail = result?.key === skill ? result.detail : null
  const error = failure?.key === skill ? failure.message : ''
  if (error) return <p className="error" role="alert">{error}</p>
  if (!detail) return <p className="loading">생활 분야를 불러오는 중입니다.</p>

  const progress = detail.user_progress
  return (
    <div>
      <Link className="back-link" to="/life">← 생활 허브</Link>
      <header className="page-header detail-header">
        <div>
          <div className="title-badges">
            <span className="category">LIFE SKILL</span>
            <StatusBadge status={detail.verification_status} />
          </div>
          <h1>{detail.name_ko}</h1>
          {detail.summary && <p className="subtitle">{detail.summary}</p>}
          <small className="verified-date">최종 검증일 {detail.last_verified_at ?? '미확인'}</small>
        </div>
        <div className="project-header-actions">
          <PromptBridgeDialog
            mode="content_onboarding"
            contentSlug={detail.entry_content_slug}
            triggerLabel="입문 질문 만들기"
          />
          <PromptBridgeDialog
            mode="next_action"
            contentSlug={detail.entry_content_slug}
            triggerLabel="다음 할 일 묻기"
            variant="ghost"
          />
        </div>
      </header>

      <section className="life-progress-panel" aria-label="내 진행 상태">
        <div><strong>{progress.tracked}</strong><span>추적 콘텐츠</span></div>
        <div><strong>{progress.completed}</strong><span>완료</span></div>
        <div><strong>{progress.in_progress}</strong><span>진행 중</span></div>
        <div><strong>{progress.foundation}</strong><span>기반 준비</span></div>
        <div><strong>{progress.not_started}</strong><span>미시작</span></div>
        {progress.ignored > 0 && <p>관심 없음 {progress.ignored}개는 추적 수에서 제외했습니다.</p>}
      </section>

      {sections.map((section) => (
        <ContentSection
          key={section.key}
          title={section.title}
          eyebrow={section.eyebrow}
          contents={detail[section.key]}
        />
      ))}

      {detail.related_projects.length > 0 && (
        <section className="detail-section">
          <p className="eyebrow">RELATED PROJECTS</p>
          <h2>관련 프로젝트</h2>
          <div className="life-project-list">
            {detail.related_projects.map((project) => (
              <Link to={`/projects/${project.slug}`} key={project.slug}>
                <strong>{project.name_ko}</strong>
                {project.summary && <p>{project.summary}</p>}
                <span>프로젝트 보기 →</span>
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  )
}
