import { useCallback, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api, type DashboardData } from '../../api'
import { ChecklistGroup } from '../../components/ChecklistGroup'

export function DashboardPage() {
  const [data, setData] = useState<DashboardData | null>(null)
  const [error, setError] = useState('')
  const load = useCallback(() => {
    api.dashboard().then(setData).catch((reason: Error) => setError(reason.message))
  }, [])
  useEffect(load, [load])

  return (
    <div>
      <header className="page-header hero">
        <div><p className="eyebrow">오늘의 운영 보드</p><h1>놓치지 않고,<br /><em>기록은 남기고.</em></h1></div>
        <Link className="button ghost" to="/content">콘텐츠 둘러보기</Link>
      </header>
      {error && <p className="error">{error}</p>}
      <section>
        <div className="section-heading"><div><p className="eyebrow">NEXT WINDOWS</p><h2>다가오는 경계</h2></div></div>
        <div className="reset-grid">
          {data?.reset_groups.map((group) => (
            <article className="reset-card" key={group.kind}>
              <span className={`reset-mark ${group.kind}`} />
              <p>{group.label}</p>
              <strong>{new Intl.DateTimeFormat('ko-KR', { dateStyle: 'medium', timeStyle: 'short' }).format(new Date(group.next_at))}</strong>
            </article>
          ))}
        </div>
      </section>
      <section>
        <div className="section-heading"><div><p className="eyebrow">CURRENT PERIOD</p><h2>이번 주 체크</h2></div><Link to="/weekly">전체 보기 →</Link></div>
        {data && <ChecklistGroup instances={data.weekly.slice(0, 3)} onChange={load} />}
      </section>
    </div>
  )
}

