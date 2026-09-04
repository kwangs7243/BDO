import { api } from '../api'
import type { ChecklistInstance } from '../types'

interface Props {
  instances: ChecklistInstance[]
  onChange: () => void
}

export function ChecklistGroup({ instances, onChange }: Props) {
  if (!instances.length) return <p className="empty">이 기간에 활성화된 체크리스트가 없습니다.</p>

  async function toggle(id: number, completed: boolean) {
    await api.updateChecklist(id, completed)
    onChange()
  }

  return (
    <div className="checklist-stack">
      {instances.map((instance) => (
        <section className="checklist-card" key={instance.id}>
          <div className="checklist-heading">
            <h3>{instance.template_name}</h3>
            <code>{instance.period_key}</code>
          </div>
          {instance.items.map((item) => (
            <label className={item.completed ? 'check-row completed' : 'check-row'} key={item.id}>
              <input
                type="checkbox"
                checked={item.completed}
                onChange={(event) => void toggle(item.id, event.target.checked)}
              />
              <span><strong>{item.label}</strong>{item.details && <small>{item.details}</small>}</span>
            </label>
          ))}
        </section>
      ))}
    </div>
  )
}

