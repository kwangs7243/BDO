import type {
  ChecklistInstance,
  ContentDetail,
  ContentSummary,
  MaterialInventory,
  ProjectDetail,
  ProjectStageState,
  ProjectSummary,
  PromptRender,
  UserContentState,
  UserContentStateValue,
} from './types'

export type PromptMode =
  | 'content_onboarding'
  | 'weekly_review'
  | 'project_optimizer'
  | 'next_action'
  | 'verify_latest'

export type PromptOutputMode = 'full_prompt' | 'context_only'
export type PromptSizeMode = 'auto' | 'detailed'
export type PromptSection =
  | 'user_state'
  | 'requirements'
  | 'canonical_facts'
  | 'steps'
  | 'schedules'
  | 'rewards'
  | 'warnings'
  | 'checklist'
  | 'related_contents'
  | 'project_state'
  | 'open_questions_or_conflicts'
  | 'sources'

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
  projects: () => request<ProjectSummary[]>('/api/projects'),
  project: (slug: string) =>
    request<ProjectDetail>(`/api/projects/${encodeURIComponent(slug)}`),
  updateMaterialInventory: (
    materialKey: string,
    quantity: number,
    note: string | null,
  ) => request<MaterialInventory>(
    `/api/materials/${encodeURIComponent(materialKey)}/inventory`,
    {
      method: 'PUT',
      body: JSON.stringify({ quantity, note }),
    },
  ),
  updateProjectStageState: (
    projectSlug: string,
    stageId: number,
    completed: boolean,
    note: string | null,
  ) => request<ProjectStageState>(
    `/api/projects/${encodeURIComponent(projectSlug)}/stages/${stageId}/state`,
    {
      method: 'PUT',
      body: JSON.stringify({ completed, note }),
    },
  ),
  renderPrompt: (body: {
    mode: PromptMode
    content_slug?: string
    project_slug?: string
    user_question: string
    include_sections: PromptSection[]
    output_mode: PromptOutputMode
    size_mode: PromptSizeMode
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
