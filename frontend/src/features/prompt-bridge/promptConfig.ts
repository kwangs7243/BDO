import type { PromptMode, PromptSection } from '../../api'

export const promptPlaceholders: Record<PromptMode, string> = {
  project_optimizer: '이번 주 안에 최대한 빨리 끝내는 순서를 짜줘',
  content_onboarding: '지금 내 상태에서 무엇부터 하면 돼?',
  weekly_review: '이번 주 남은 일의 우선순위를 정해줘',
  next_action: '지금 내 상태에서 무엇부터 하면 돼?',
  verify_latest: '미검증 항목을 최신 KR 공식 자료로 확인해줘',
}

export const promptSectionLabels: Record<PromptSection, string> = {
  user_state: '내 상태/메모',
  requirements: '요구사항',
  canonical_facts: '검증된 지식 (FACT/STRATEGY/MEASUREMENT)',
  steps: '진행 단계',
  schedules: '일정/초기화',
  rewards: '보상',
  warnings: '주의사항',
  checklist: '체크리스트',
  related_contents: '관련 콘텐츠',
  project_state: '프로젝트 상태',
  open_questions_or_conflicts: '미검증/충돌',
  sources: '출처',
}

const contentSections: PromptSection[] = [
  'user_state',
  'requirements',
  'canonical_facts',
  'steps',
  'schedules',
  'rewards',
  'warnings',
  'checklist',
  'related_contents',
  'open_questions_or_conflicts',
  'sources',
]

const projectSections: PromptSection[] = [
  'canonical_facts',
  'schedules',
  'checklist',
  'related_contents',
  'project_state',
  'open_questions_or_conflicts',
  'sources',
]

export function defaultPromptSections(
  mode: PromptMode,
  contentSlug?: string,
  projectSlug?: string,
): PromptSection[] {
  if (mode === 'weekly_review') return ['schedules', 'checklist']
  if (mode === 'verify_latest') {
    return projectSlug
      ? ['canonical_facts', 'project_state', 'open_questions_or_conflicts', 'sources']
      : ['canonical_facts', 'open_questions_or_conflicts', 'sources']
  }
  if (mode === 'project_optimizer' || (mode === 'next_action' && projectSlug)) {
    return [...projectSections]
  }
  if (mode === 'content_onboarding' || (mode === 'next_action' && contentSlug)) {
    return [...contentSections]
  }
  return ['schedules', 'checklist']
}
