export type VerificationStatus = 'verified' | 'needs_review' | 'conflict' | 'superseded' | 'unverified'
export type UserContentStateValue = 'not_started' | 'foundation' | 'in_progress' | 'completed' | 'paused' | 'ignore'

export interface ContentSummary {
  slug: string
  name_ko: string
  category: string
  summary: string | null
  status: string
  last_verified_at: string | null
  verification_status: VerificationStatus
}

export interface SourceEvidence {
  evidence_id: number
  evidence_seed_key: string | null
  id: string
  title: string
  url: string
  publisher: string | null
  source_type: string
  published_at: string | null
  retrieved_at: string | null
  region: string
  entity_type: string
  entity_id: string
  claim_key: string
  verification_status: VerificationStatus
  last_verified_at: string
  evidence_note: string | null
  active: boolean
  is_active: boolean
}

export interface Schedule {
  id: number
  seed_key: string | null
  rule_type: string
  recurrence_type: string
  weekday: number | null
  time_local: string | null
  fixed_datetime: string | null
  timezone: string
  notes: string | null
  next_occurrence: string | null
}

export interface ContentRequirement {
  seed_key: string
  kind: string
  title: string | null
  description: string
  structured_value: unknown
  requirement_level: string
  order_no: number
}

export interface ContentStep {
  seed_key: string
  phase: string
  order_no: number
  title: string
  description: string
  checkable: boolean
}

export interface Reward {
  seed_key: string
  name: string
  reward_type: string
  amount: number | null
  min_amount: number | null
  max_amount: number | null
  unit: string | null
  is_choice: boolean
  choice_group: string | null
  recommendation: string | null
  notes: string | null
  order_no: number
}

export interface ContentSection {
  seed_key: string
  section_type: string
  title: string
  body_markdown: string
  order_no: number
}

export interface ContentRelation {
  seed_key: string
  direction: 'outgoing' | 'incoming'
  relation_type: string
  note: string | null
  order_no: number
  content_slug: string
  content_name_ko: string
  content_category: string
}

export interface UserContentState {
  state: UserContentStateValue
  priority: number | null
  note: string | null
  updated_at: string | null
}

export interface ContentDetail extends ContentSummary {
  purpose: string | null
  party_type: string | null
  difficulty: string | null
  requirements: ContentRequirement[]
  sections: ContentSection[]
  steps: ContentStep[]
  schedules: Schedule[]
  rewards: Reward[]
  checklists: ChecklistInstance[]
  related_contents: ContentRelation[]
  user_state: UserContentState
  sources: SourceEvidence[]
}

export interface ChecklistItem {
  id: number
  template_item_id: number
  seed_key: string | null
  label: string
  details: string | null
  completed: boolean
  completed_at: string | null
  note: string | null
}

export interface ChecklistInstance {
  id: number
  template_id: number
  template_seed_key: string | null
  template_name: string
  content_slug: string | null
  period_key: string
  period_start: string
  period_end: string
  items: ChecklistItem[]
}

export interface PromptRender {
  markdown: string
  character_count: number
  estimated_tokens: number
  original_estimated_tokens: number
  compacted: boolean
  omitted_counts: Record<string, number>
  over_budget: boolean
}

export interface ProjectSummary {
  slug: string
  name_ko: string
  content_slug: string | null
  active: boolean
  completed_stage_count: number
  total_stage_count: number
  shortage_material_count: number
}

export interface ProjectMaterialSource {
  seed_key: string
  content_slug: string
  content_name_ko: string
  quantity_per_completion: number | null
  notes: string | null
  order_no: number
}

export interface ProjectMaterial {
  seed_key: string
  material_key: string
  name_ko: string
  unit: string
  stage_seed_key: string | null
  required_quantity: number
  owned_quantity: number
  shortage: number
  inventory_note: string | null
  inventory_updated_at: string | null
  notes: string | null
  order_no: number
  source_entity_type: string | null
  source_entity_seed_key: string | null
  sources: ProjectMaterialSource[]
}

export interface ProjectStage {
  id: number
  seed_key: string
  name: string
  description: string | null
  order_no: number
  completed: boolean
  completed_at: string | null
  note: string | null
  dependencies: string[]
}

export interface ProjectDetail {
  slug: string
  name_ko: string
  content_slug: string | null
  summary: string | null
  active: boolean
  stages: ProjectStage[]
  materials: ProjectMaterial[]
}

export interface MaterialInventory {
  material_key: string
  quantity: number
  note: string | null
  updated_at: string
}

export interface ProjectStageState {
  project_slug: string
  stage_id: number
  completed: boolean
  completed_at: string | null
  note: string | null
  updated_at: string
}
