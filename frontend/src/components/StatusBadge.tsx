import type { VerificationStatus } from '../types'

const labels: Record<VerificationStatus, string> = {
  verified: '검증됨',
  needs_review: '재검토 필요',
  conflict: '근거 충돌',
  superseded: '대체됨',
  unverified: '미검증',
}

export function StatusBadge({ status }: { status: VerificationStatus }) {
  return <span className={`badge badge-${status}`}>{labels[status]}</span>
}

