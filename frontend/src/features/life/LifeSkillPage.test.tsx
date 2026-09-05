import { render, screen } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import { beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import type { LifeContent, LifeSkillDetail } from '../../types'
import { LifeSkillPage } from './LifeSkillPage'

vi.mock('../../api', () => ({
  api: {
    lifeSkill: vi.fn(),
    renderPrompt: vi.fn(),
  },
}))

function content(slug: string, name_ko: string, state: LifeContent['user_state']['state']): LifeContent {
  return {
    slug,
    name_ko,
    category: 'life',
    subcategory: null,
    summary: `${name_ko} 설명`,
    verification_status: 'verified',
    last_verified_at: '2026-09-03',
    user_state: {
      state,
      priority: null,
      note: null,
      updated_at: null,
    },
  }
}

const detail: LifeSkillDetail = {
  key: 'gathering',
  name_ko: '채집',
  summary: '채집 분야 설명',
  verification_status: 'verified',
  last_verified_at: '2026-09-03',
  content_count: 3,
  user_progress: {
    total: 3,
    tracked: 3,
    not_started: 1,
    foundation: 0,
    in_progress: 1,
    completed: 1,
    paused: 0,
    ignored: 0,
  },
  entry_content_slug: 'gathering-current-system',
  foundation_contents: [content('life-mastery-foundation', '생활 숙련도 기반', 'completed')],
  getting_started: [content('gathering-current-system', '채집 현재 시스템', 'in_progress')],
  equipment: [],
  core_systems: [],
  recurring_contents: [],
  advanced_contents: [],
  related_economy: [content('production-node-current-system', '생산 거점 현재 시스템', 'not_started')],
  related_projects: [{
    slug: 'carrack-advance',
    name_ko: '에페리아 중범선 : 점진',
    summary: '중범선 프로젝트',
    content_slug: 'carrack-advance',
  }],
}

function renderPage() {
  return render(
    <MemoryRouter initialEntries={['/life/gathering']}>
      <Routes><Route path="/life/:skill" element={<LifeSkillPage />} /></Routes>
    </MemoryRouter>,
  )
}

beforeEach(() => {
  vi.mocked(api.lifeSkill).mockReset()
})

test('선택 분야를 실제 Content section으로 묶고 빈 section은 표시하지 않는다', async () => {
  vi.mocked(api.lifeSkill).mockResolvedValue(detail)
  renderPage()

  expect(await screen.findByRole('heading', { name: '채집' })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: '분야 기반' })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: '시작하기' })).toBeInTheDocument()
  expect(screen.queryByRole('heading', { name: '장비와 세팅' })).not.toBeInTheDocument()
  expect(screen.getByRole('heading', { name: '관련 생활 기반과 경제' })).toBeInTheDocument()
  expect(screen.getByRole('link', { name: /채집 현재 시스템/ })).toHaveAttribute(
    'href',
    '/content/gathering-current-system',
  )
  expect(screen.getByRole('heading', { name: '채집 현재 시스템' }).closest('article')).toHaveTextContent(
    '진행 중',
  )
  expect(screen.getByLabelText('내 진행 상태')).toHaveTextContent('완료')
})

test('entry Content용 기존 Prompt Bridge와 실제 연결 Project를 노출한다', async () => {
  vi.mocked(api.lifeSkill).mockResolvedValue(detail)
  renderPage()

  expect(await screen.findByRole('button', { name: '입문 질문 만들기' })).toBeInTheDocument()
  expect(screen.getByRole('button', { name: '다음 할 일 묻기' })).toBeInTheDocument()
  expect(screen.getByRole('link', { name: /에페리아 중범선 : 점진/ })).toHaveAttribute(
    'href',
    '/projects/carrack-advance',
  )
})

test('존재하지 않는 분야의 API 오류를 표시한다', async () => {
  vi.mocked(api.lifeSkill).mockRejectedValue(new Error('Life skill not found'))
  renderPage()
  expect(await screen.findByRole('alert')).toHaveTextContent('Life skill not found')
})
