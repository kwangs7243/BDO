import { type FormEvent, useState } from 'react'
import { api } from '../../api'
import type { UserContentState, UserContentStateValue } from '../../types'

const stateLabels: Record<UserContentStateValue, string> = {
  not_started: '미착수',
  foundation: '기반 준비',
  in_progress: '진행 중',
  completed: '완료',
  paused: '보류',
  ignore: '관심 없음',
}

interface Props {
  contentSlug: string
  initialState: UserContentState
  onSaved: (state: UserContentState) => void
}

export function ContentStateEditor({ contentSlug, initialState, onSaved }: Props) {
  const [state, setState] = useState(initialState.state)
  const [priority, setPriority] = useState(initialState.priority?.toString() ?? '')
  const [note, setNote] = useState(initialState.note ?? '')
  const [message, setMessage] = useState('')
  const [saving, setSaving] = useState(false)

  async function save(event: FormEvent) {
    event.preventDefault()
    setSaving(true)
    setMessage('')
    try {
      const saved = await api.updateContentState(
        contentSlug,
        state,
        priority === '' ? null : Number(priority),
        note.trim() || null,
      )
      onSaved(saved)
      setMessage('저장했습니다.')
    } catch (error) {
      setMessage(error instanceof Error ? error.message : '저장하지 못했습니다.')
    } finally {
      setSaving(false)
    }
  }

  return (
    <form className="state-editor" onSubmit={(event) => void save(event)}>
      <label>
        <span>내 상태</span>
        <select value={state} onChange={(event) => setState(event.target.value as UserContentStateValue)}>
          {Object.entries(stateLabels).map(([value, label]) => (
            <option value={value} key={value}>{label}</option>
          ))}
        </select>
      </label>
      <label>
        <span>우선순위</span>
        <input
          type="number"
          min="0"
          value={priority}
          onChange={(event) => setPriority(event.target.value)}
          placeholder="선택"
        />
      </label>
      <label className="state-note">
        <span>개인 메모</span>
        <textarea value={note} onChange={(event) => setNote(event.target.value)} rows={3} />
      </label>
      <div className="state-actions">
        <span role="status">{message}</span>
        <button className="button ghost" type="submit" disabled={saving}>
          {saving ? '저장 중…' : '상태 저장'}
        </button>
      </div>
    </form>
  )
}

