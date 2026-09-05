import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../../api'
import { StatusBadge } from '../../components/StatusBadge'
import type { LifeHub } from '../../types'
import { LifeContentCard } from './LifeContentCard'

export function LifeHubPage() {
  const [hub, setHub] = useState<LifeHub | null>(null)
  const [error, setError] = useState('')

  useEffect(() => {
    api.life()
      .then(setHub)
      .catch((reason: Error) => setError(reason.message))
  }, [])

  if (error) return <p className="error" role="alert">{error}</p>
  if (!hub) return <p className="loading">생활 허브를 불러오는 중입니다.</p>

  return (
    <div>
      <header className="page-header hero">
        <div>
          <p className="eyebrow">LIFE HUB</p>
          <h1>생활, <em>어디서부터?</em></h1>
          <p className="subtitle">
            공통 기반을 먼저 확인하고 관심 분야로 들어가 현재 데이터와 내 진행 상태를 함께 살펴보세요.
          </p>
        </div>
      </header>

      <section>
        <div className="section-heading">
          <div><p className="eyebrow">FOUNDATION</p><h2>생활 공통 기반</h2></div>
        </div>
        <div className="life-content-grid">
          {hub.foundations.map((content) => (
            <LifeContentCard content={content} key={content.slug} />
          ))}
        </div>
      </section>

      <section>
        <div className="section-heading">
          <div><p className="eyebrow">SKILLS</p><h2>분야 선택</h2></div>
        </div>
        <div className="life-skill-grid">
          {hub.skills.map((skill) => (
            <article className="life-skill-card" key={skill.key}>
              <div className="card-top">
                <span className="category">{skill.content_count} CONTENTS</span>
                <StatusBadge status={skill.verification_status} />
              </div>
              <h3>{skill.name_ko}</h3>
              {skill.summary && <p>{skill.summary}</p>}
              <div className="life-progress-line">
                <strong>{skill.user_progress.tracked}개 중 완료 {skill.user_progress.completed}</strong>
                <span>
                  진행 {skill.user_progress.in_progress} · 기반 {skill.user_progress.foundation}
                  {' '}· 미시작 {skill.user_progress.not_started}
                </span>
                {skill.user_progress.ignored > 0 && (
                  <small>관심 없음 {skill.user_progress.ignored}개는 진행률에서 제외</small>
                )}
              </div>
              <footer>
                <small>검증일 {skill.last_verified_at ?? '미확인'}</small>
                <Link className="button primary" to={`/life/${skill.key}`}>분야 보기</Link>
              </footer>
            </article>
          ))}
        </div>
      </section>

      {hub.economy_contents.length > 0 && (
        <section>
          <div className="section-heading">
            <div><p className="eyebrow">FOUNDATION & ECONOMY</p><h2>생활 기반과 경제</h2></div>
          </div>
          <p className="section-intro">
            공헌도, 거점, 일꾼, 주거지, 창고와 물류처럼 여러 생활 분야가 함께 사용하는 기반입니다.
          </p>
          <div className="life-link-list">
            {hub.economy_contents.map((content) => (
              <Link to={`/content/${content.slug}`} key={content.slug}>
                <span>
                  <strong>{content.name_ko}</strong>
                  {content.summary && <small>{content.summary}</small>}
                </span>
                <StatusBadge status={content.verification_status} />
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  )
}
