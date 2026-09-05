import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import type { LifeContent, LifeHub } from '../../types'
import { LifeHubPage } from './LifeHubPage'

vi.mock('../../api', () => ({
  api: {
    life: vi.fn(),
  },
}))

function content(slug: string, name_ko: string): LifeContent {
  return {
    slug,
    name_ko,
    category: 'life',
    subcategory: null,
    summary: `${name_ko} 설명`,
    verification_status: 'verified',
    last_verified_at: '2026-09-03',
    user_state: {
      state: 'not_started',
      priority: null,
      note: null,
      updated_at: null,
    },
  }
}

const hub: LifeHub = {
  foundations: [content('life-family-levels', '가문 통합 생활 레벨')],
  economy_contents: [content('worker-current-system', '일꾼 현재 시스템')],
  skills: [
    {
      key: 'gathering',
      name_ko: '채집',
      summary: '채집 분야 설명',
      verification_status: 'verified',
      last_verified_at: '2026-09-03',
      content_count: 5,
      user_progress: {
        total: 5,
        tracked: 4,
        not_started: 1,
        foundation: 1,
        in_progress: 1,
        completed: 1,
        paused: 0,
        ignored: 1,
      },
      entry_content_slug: 'gathering-current-system',
    },
  ],
}

beforeEach(() => {
  vi.mocked(api.life).mockReset()
})

test('공통 기반, 분야 카드, 검증일과 진행 상태 및 경제 Content 링크를 표시한다', async () => {
  vi.mocked(api.life).mockResolvedValue(hub)
  render(<MemoryRouter><LifeHubPage /></MemoryRouter>)

  expect(await screen.findByRole('heading', { name: /생활,/ })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: '생활 공통 기반' })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: '가문 통합 생활 레벨' })).toBeInTheDocument()
  expect(screen.getByRole('heading', { name: '채집' })).toBeInTheDocument()
  expect(screen.getByText('4개 중 완료 1')).toBeInTheDocument()
  expect(screen.getByText(/관심 없음 1개는 진행률에서 제외/)).toBeInTheDocument()
  expect(screen.getAllByText('검증일 2026-09-03').length).toBeGreaterThan(0)
  expect(screen.getByRole('link', { name: '분야 보기' })).toHaveAttribute('href', '/life/gathering')
  expect(screen.getByRole('link', { name: /일꾼 현재 시스템/ })).toHaveAttribute(
    'href',
    '/content/worker-current-system',
  )
})

test('로딩과 오류 상태를 구분한다', async () => {
  vi.mocked(api.life).mockImplementation(() => new Promise(() => undefined))
  const view = render(<MemoryRouter><LifeHubPage /></MemoryRouter>)
  expect(screen.getByText('생활 허브를 불러오는 중입니다.')).toBeInTheDocument()

  view.unmount()
  vi.mocked(api.life).mockRejectedValue(new Error('생활 API 오류'))
  render(<MemoryRouter><LifeHubPage /></MemoryRouter>)
  expect(await screen.findByRole('alert')).toHaveTextContent('생활 API 오류')
})
