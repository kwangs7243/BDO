import { Link } from 'react-router-dom'
import { StatusBadge } from '../../components/StatusBadge'
import type { LifeContent } from '../../types'

const stateLabels = {
  not_started: '미시작',
  foundation: '기반 준비',
  in_progress: '진행 중',
  completed: '완료',
  paused: '보류',
  ignore: '관심 없음',
} as const

export function LifeContentCard({ content }: { content: LifeContent }) {
  return (
    <article className="life-content-card">
      <div className="card-top">
        <span className="category">{stateLabels[content.user_state.state]}</span>
        <StatusBadge status={content.verification_status} />
      </div>
      <h3>{content.name_ko}</h3>
      {content.summary && <p>{content.summary}</p>}
      <footer>
        <small>검증일 {content.last_verified_at ?? '미확인'}</small>
        <Link
          to={`/content/${content.slug}`}
          aria-label={`${content.name_ko} 자세히 보기`}
        >
          자세히 보기
        </Link>
      </footer>
    </article>
  )
}
