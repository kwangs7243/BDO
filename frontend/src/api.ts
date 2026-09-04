import type {
  ChecklistInstance,
  ContentDetail,
  ContentSummary,
  PromptRender,
  UserContentState,
  UserContentStateValue,
} from './types'

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(path, {
    ...init,
    headers: { 'Content-Type': 'application/json', ...init?.headers },
  })
  if (!response.ok) {
    const body = await response.json().catch(() => null)
    throw new Error(body?.detail ?? `요청 실패 (${response.status})`)
  }
  return response.json() as Promise<T>
}

export const api = {
  contents: () => request<ContentSummary[]>('/api/contents'),
  content: (slug: string) => request<ContentDetail>(`/api/contents/${encodeURIComponent(slug)}`),
  updateContentState: (
    slug: string,
    state: UserContentStateValue,
    priority: number | null,
    note: string | null,
  ) => request<UserContentState>(`/api/contents/${encodeURIComponent(slug)}/state`, {
    method: 'PUT',
    body: JSON.stringify({ state, priority, note }),
  }),
  checklists: (scope: 'daily' | 'weekly') =>
    request<ChecklistInstance[]>(`/api/checklists/current?scope=${scope}`),
  updateChecklist: (id: number, completed: boolean, note: string | null = null) =>
    request(`/api/checklists/states/${id}`, {
      method: 'PATCH',
      body: JSON.stringify({ completed, note }),
    }),
  dashboard: () => request<DashboardData>('/api/dashboard'),
  renderPrompt: (body: {
    mode: 'content_onboarding' | 'weekly_review'
    content_slug?: string
    user_question: string
  }) => request<PromptRender>('/api/prompt/render', {
    method: 'POST',
    body: JSON.stringify({ ...body, as_of: new Date().toISOString() }),
  }),
}

export interface DashboardData {
  now: string
  reset_groups: Array<{ kind: string; label: string; next_at: string }>
  daily: ChecklistInstance[]
  weekly: ChecklistInstance[]
}
