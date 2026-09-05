import { useCallback, useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { api } from '../../api'
import { ChecklistGroup } from '../../components/ChecklistGroup'
import { StatusBadge } from '../../components/StatusBadge'
import type { ContentDetail, ContentSection, ContentStep } from '../../types'
import { PromptBridgeDialog } from '../prompt-bridge/PromptBridgeDialog'
import { ContentStateEditor } from './ContentStateEditor'

const scheduleLabels: Record<string, string> = {
  quest_reset: '재수주 초기화',
  attempt_reset: '횟수 초기화',
  record_cutoff: '기록 집계',
  reward_payout: '보상 지급',
  spawn: '출현',
  event_end: '이벤트 종료',
}

const phaseLabels: Record<string, string> = {
  unlock: '해금/시작',
  preparation: '준비',
  first_time: '최초 진행',
  repeat: '반복 진행',
  reward: '보상 수령',
  maintenance: '유지 관리',
}

function ProseItems({ items }: { items: ContentSection[] }) {
  return (
    <div className="knowledge-list">
      {items.map((item) => (
        <article key={item.seed_key}>
          <h3>{item.title}</h3>
          <p className="markdown-body">{item.body_markdown}</p>
        </article>
      ))}
    </div>
  )
}

function StepItems({ items }: { items: ContentStep[] }) {
  return (
    <ol className="knowledge-list numbered">
      {items.map((item) => (
        <li key={item.seed_key}>
          <strong>{item.title}</strong>
          <p>{item.description}</p>
        </li>
      ))}
    </ol>
  )
}

export function ContentDetailPage() {
  const { slug = '' } = useParams()
  const [content, setContent] = useState<ContentDetail | null>(null)
  const [error, setError] = useState('')
  const load = useCallback(() => {
    api.content(slug).then(setContent).catch((reason: Error) => setError(reason.message))
  }, [slug])
  useEffect(load, [load])
  if (error) return <p className="error">{error}</p>
  if (!content) return <p className="loading">불러오는 중…</p>

  const sections = (type: string) => content.sections.filter((item) => item.section_type === type)
  const steps = (phase: string) => content.steps.filter((item) => item.phase === phase)
  const preparationSections = sections('preparation')
  const startSections = sections('start')
  const repeatSections = sections('strategy')
  const noteSections = sections('notes')

  return (
    <div>
      <Link className="back-link" to="/content">← 콘텐츠 탐색</Link>
      <header className="page-header detail-header">
        <div>
          <div className="title-badges">
            <span className="category">{content.category}</span>
            <StatusBadge status={content.verification_status} />
          </div>
          <h1>{content.name_ko}</h1>
          <p className="subtitle">{content.summary}</p>
        </div>
        <div className="project-header-actions">
          <PromptBridgeDialog mode="content_onboarding" contentSlug={content.slug} />
          <PromptBridgeDialog
            mode="verify_latest"
            contentSlug={content.slug}
            triggerLabel="최신 정보 검증 프롬프트"
            variant="ghost"
          />
        </div>
      </header>

      <div className="detail-grid">
        <div>
          <section className="detail-section">
            <p className="eyebrow">OVERVIEW</p>
            <h2>한눈에 보기 / 내 상태</h2>
            {sections('overview').length > 0 && <ProseItems items={sections('overview')} />}
            {noteSections.length > 0 && <ProseItems items={noteSections} />}
            <ContentStateEditor
              contentSlug={content.slug}
              initialState={content.user_state}
              onSaved={(userState) => setContent({ ...content, user_state: userState })}
            />
          </section>

          {(content.purpose || sections('why').length > 0) && (
            <section className="detail-section">
              <p className="eyebrow">WHY</p>
              <h2>왜 하는가</h2>
              {content.purpose && <p>{content.purpose}</p>}
              <ProseItems items={sections('why')} />
            </section>
          )}

          {content.requirements.length > 0 && (
            <section className="detail-section">
              <p className="eyebrow">REQUIREMENTS</p>
              <h2>선행조건</h2>
              <div className="knowledge-list">
                {content.requirements.map((item) => (
                  <article key={item.seed_key}>
                    <small>{item.requirement_level} · {item.kind}</small>
                    <h3>{item.title || '조건'}</h3>
                    <p>{item.description}</p>
                  </article>
                ))}
              </div>
            </section>
          )}

          {(preparationSections.length > 0 || steps('preparation').length > 0) && (
            <section className="detail-section">
              <p className="eyebrow">PREPARATION</p>
              <h2>준비</h2>
              <ProseItems items={preparationSections} />
              <StepItems items={steps('preparation')} />
            </section>
          )}

          {(startSections.length > 0 || steps('unlock').length > 0) && (
            <section className="detail-section">
              <p className="eyebrow">START</p>
              <h2>시작 방법</h2>
              <ProseItems items={startSections} />
              <StepItems items={steps('unlock')} />
            </section>
          )}

          {steps('first_time').length > 0 && (
            <section className="detail-section">
              <p className="eyebrow">FIRST TIME</p>
              <h2>최초 진행</h2>
              <StepItems items={steps('first_time')} />
            </section>
          )}

          {(steps('repeat').length > 0 || steps('maintenance').length > 0 || repeatSections.length > 0 || content.checklists.length > 0) && (
            <section className="detail-section">
              <p className="eyebrow">REPEAT</p>
              <h2>반복 진행</h2>
              <ProseItems items={repeatSections} />
              {(['repeat', 'maintenance'] as const).map((phase) => (
                steps(phase).length > 0 && (
                  <div key={phase}>
                    <h3>{phaseLabels[phase]}</h3>
                    <StepItems items={steps(phase)} />
                  </div>
                )
              ))}
              {content.checklists.length > 0 && (
                <ChecklistGroup instances={content.checklists} onChange={load} />
              )}
            </section>
          )}

          {content.schedules.length > 0 && (
            <section className="detail-section">
              <p className="eyebrow">SCHEDULES</p>
              <h2>일정과 초기화</h2>
              {content.schedules.map((item) => (
                <article className="timeline-item" key={item.id}>
                  <span />
                  <div>
                    <strong>{scheduleLabels[item.rule_type] ?? item.rule_type}</strong>
                    <p>{item.notes || item.recurrence_type}</p>
                    <small>{item.timezone}</small>
                  </div>
                </article>
              ))}
            </section>
          )}

          {(content.rewards.length > 0 || steps('reward').length > 0) && (
            <section className="detail-section">
              <p className="eyebrow">REWARDS</p>
              <h2>보상과 선택 추천</h2>
              <div className="knowledge-list">
                {content.rewards.map((item) => (
                  <article key={item.seed_key}>
                    <small>{item.reward_type}{item.is_choice ? ' · 선택 보상' : ''}</small>
                    <h3>{item.name}</h3>
                    {item.recommendation && <p><strong>추천:</strong> {item.recommendation}</p>}
                    {item.notes && <p>{item.notes}</p>}
                  </article>
                ))}
              </div>
              <StepItems items={steps('reward')} />
            </section>
          )}

          {sections('common_mistakes').length > 0 && (
            <section className="detail-section">
              <p className="eyebrow">WARNINGS</p>
              <h2>실수와 주의</h2>
              <ProseItems items={sections('common_mistakes')} />
            </section>
          )}

          {content.related_contents.length > 0 && (
            <section className="detail-section">
              <p className="eyebrow">RELATED</p>
              <h2>관련 콘텐츠</h2>
              <div className="relation-list">
                {content.related_contents.map((item) => (
                  <Link to={`/content/${item.content_slug}`} key={`${item.direction}-${item.seed_key}`}>
                    <strong>{item.content_name_ko}</strong>
                    <span>{item.relation_type} · {item.direction}</span>
                    {item.note && <p>{item.note}</p>}
                  </Link>
                ))}
              </div>
            </section>
          )}

          <p className="missing-data-note">등록된 구조화 데이터가 없는 섹션은 숨겨져 있습니다.</p>
        </div>

        <aside className="source-panel">
          <p className="eyebrow">EVIDENCE</p>
          <h2>근거와 검증 상태</h2>
          <p className="verified-date">최종 검증일 <strong>{content.last_verified_at ?? '미확인'}</strong></p>
          {content.sources.length ? content.sources.map((source) => (
            <a
              href={source.url}
              target="_blank"
              rel="noreferrer"
              className={source.is_active ? 'source-card' : 'source-card historical'}
              key={source.evidence_id}
            >
              <StatusBadge status={source.verification_status} />
              <strong>{source.title}</strong>
              <span>{source.source_type} · {source.region}</span>
              <small>{source.entity_type}/{source.entity_id} · {source.claim_key}</small>
              {!source.is_active && <small>과거 근거</small>}
              {source.evidence_note && <p>{source.evidence_note}</p>}
            </a>
          )) : <p className="empty">연결된 출처가 없습니다.</p>}
        </aside>
      </div>
    </div>
  )
}
