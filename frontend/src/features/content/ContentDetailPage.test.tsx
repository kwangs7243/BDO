import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import { beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import type { ContentDetail } from '../../types'
import { ContentDetailPage } from './ContentDetailPage'

vi.mock('../../api', () => ({
  api: {
    content: vi.fn(),
    updateContentState: vi.fn(),
    updateChecklist: vi.fn(),
    renderPrompt: vi.fn(),
  },
}))

const fixture: ContentDetail = {
  slug: 'blood-altar',
  name_ko: '피의 제단',
  category: 'combat_pve',
  summary: '단계형 3인 콘텐츠',
  purpose: '주간 기록 보상',
  party_type: 'party',
  difficulty: null,
  status: 'active',
  last_verified_at: '2026-09-02',
  verification_status: 'verified',
  requirements: [{ seed_key: 'blood-altar.party', kind: 'party', title: '파티', description: '3인 콘텐츠다.', structured_value: { party_size: 3 }, requirement_level: 'required', order_no: 1 }],
  sections: [
    { seed_key: 'blood-altar.prep', section_type: 'preparation', title: '준비', body_markdown: '파티 구성을 확인한다.', order_no: 1 },
    { seed_key: 'blood-altar.warning', section_type: 'common_mistakes', title: '주의', body_markdown: '보상 지급과 reset을 구분한다.', order_no: 2 },
  ],
  steps: [{ seed_key: 'blood-altar.repeat', phase: 'repeat', order_no: 1, title: '기록 진행', description: '최고 기록을 남긴다.', checkable: false }],
  schedules: [{ id: 1, seed_key: 'blood-altar.payout', rule_type: 'reward_payout', recurrence_type: 'weekly', weekday: 6, time_local: '00:00', fixed_datetime: null, timezone: 'Asia/Seoul', notes: '일요일 지급', next_occurrence: null }],
  rewards: [{ seed_key: 'blood-altar.reward', name: '주간 최고 기록 보상', reward_type: 'weekly_reward', amount: null, min_amount: null, max_amount: null, unit: null, is_choice: false, choice_group: null, recommendation: null, notes: '일요일 지급', order_no: 1 }],
  checklists: [],
  related_contents: [{ seed_key: 'blood-altar.system', direction: 'outgoing', relation_type: 'related', note: null, order_no: 1, content_slug: 'weekly-quest-framework', content_name_ko: '주간 의뢰 공통 규칙', content_category: 'system' }],
  user_state: { state: 'not_started', priority: null, note: null, updated_at: null },
  sources: [{ evidence_id: 1, evidence_seed_key: 'blood-altar.summary::source', id: 'source', title: '피의 제단 공식 가이드', url: 'https://example.invalid', publisher: 'Pearl Abyss', source_type: 'official_guide', published_at: null, retrieved_at: null, region: 'KR', entity_type: 'content', entity_id: 'blood-altar', claim_key: 'summary', verification_status: 'verified', last_verified_at: '2026-09-02', evidence_note: '공식 근거', active: true, is_active: true }],
}

function renderPage() {
  return render(
    <MemoryRouter initialEntries={['/content/blood-altar']}>
      <Routes><Route path="/content/:slug" element={<ContentDetailPage />} /></Routes>
    </MemoryRouter>,
  )
}

beforeEach(() => {
  vi.mocked(api.renderPrompt).mockReset()
  vi.mocked(api.content).mockResolvedValue(structuredClone(fixture))
  vi.mocked(api.renderPrompt).mockResolvedValue({
    markdown: '# verify content',
    character_count: 16,
    estimated_tokens: 4,
    over_budget: false,
  })
})

test('구조화된 상세 섹션을 지정된 순서의 제목으로 렌더링한다', async () => {
  renderPage()
  expect(await screen.findByRole('heading', { name: '피의 제단' })).toBeInTheDocument()
  const headings = screen.getAllByRole('heading', { level: 2 }).map((item) => item.textContent)
  expect(headings).toEqual([
    '한눈에 보기 / 내 상태',
    '왜 하는가',
    '선행조건',
    '준비',
    '반복 진행',
    '일정과 초기화',
    '보상과 선택 추천',
    '실수와 주의',
    '관련 콘텐츠',
    '근거와 검증 상태',
  ])
  expect(screen.getByText('3인 콘텐츠다.')).toBeInTheDocument()
  expect(screen.getByText('주간 최고 기록 보상')).toBeInTheDocument()
  expect(screen.getByText('피의 제단 공식 가이드')).toBeInTheDocument()
})

test('데이터가 없는 상세 섹션은 빈 박스로 렌더링하지 않는다', async () => {
  vi.mocked(api.content).mockResolvedValue({
    ...structuredClone(fixture),
    purpose: null,
    requirements: [],
    sections: [],
    steps: [],
    schedules: [],
    rewards: [],
    related_contents: [],
  })
  renderPage()
  await screen.findByRole('heading', { name: '피의 제단' })
  expect(screen.queryByRole('heading', { name: '보상과 선택 추천' })).not.toBeInTheDocument()
  expect(screen.queryByRole('heading', { name: '선행조건' })).not.toBeInTheDocument()
  expect(screen.getByText('등록된 구조화 데이터가 없는 섹션은 숨겨져 있습니다.')).toBeInTheDocument()
})

test('Content Detail에서 현재 content slug로 최신 정보 검증 prompt를 연다', async () => {
  renderPage()
  fireEvent.click(await screen.findByRole('button', {
    name: '최신 정보 검증 프롬프트',
  }))

  expect(screen.getByPlaceholderText(
    '미검증 항목을 최신 KR 공식 자료로 확인해줘',
  )).toBeInTheDocument()
  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'verify_latest',
    content_slug: 'blood-altar',
    project_slug: undefined,
    user_question: '',
  }))
})
