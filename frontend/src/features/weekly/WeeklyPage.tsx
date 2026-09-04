import { useCallback, useEffect, useState } from 'react'
import { api } from '../../api'
import { ChecklistGroup } from '../../components/ChecklistGroup'
import type { ChecklistInstance } from '../../types'
import { PromptBridgeDialog } from '../prompt-bridge/PromptBridgeDialog'

export function WeeklyPage() {
  const [instances, setInstances] = useState<ChecklistInstance[]>([])
  const [error, setError] = useState('')
  const load = useCallback(() => {
    api.checklists('weekly').then(setInstances).catch((reason: Error) => setError(reason.message))
  }, [])
  useEffect(load, [load])
  const total = instances.flatMap((item) => item.items).length
  const completed = instances.flatMap((item) => item.items).filter((item) => item.completed).length

  return (
    <div>
      <header className="page-header">
        <div><p className="eyebrow">THURSDAY CYCLE</p><h1>이번 주</h1><p className="subtitle">목요일 00:00 KST 기준 · {completed}/{total} 완료</p></div>
        <PromptBridgeDialog mode="weekly_review" />
      </header>
      <div className="notice">일요일 00:00 보상 지급은 주간 체크 초기화와 다른 일정으로 관리됩니다.</div>
      {error && <p className="error">{error}</p>}
      <ChecklistGroup instances={instances} onChange={load} />
    </div>
  )
}

