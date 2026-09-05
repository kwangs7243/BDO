import { fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { expect, test, vi } from 'vitest'
import { api } from './api'
import App from './App'
import type { LifeHub, LifeSkillDetail } from './types'

vi.mock('./api', () => ({
  api: {
    life: vi.fn(),
    lifeSkill: vi.fn(),
    renderPrompt: vi.fn(),
    exportUserBackup: vi.fn(),
    validateUserBackup: vi.fn(),
    importUserBackup: vi.fn(),
  },
}))

const progress = {
  total: 1,
  tracked: 1,
  not_started: 1,
  foundation: 0,
  in_progress: 0,
  completed: 0,
  paused: 0,
  ignored: 0,
}

const hub: LifeHub = {
  foundations: [],
  economy_contents: [],
  skills: [{
    key: 'gathering',
    name_ko: '채집',
    summary: '채집 설명',
    verification_status: 'verified',
    last_verified_at: '2026-09-03',
    content_count: 1,
    user_progress: progress,
    entry_content_slug: 'gathering-current-system',
  }],
}

const detail: LifeSkillDetail = {
  ...hub.skills[0],
  foundation_contents: [],
  getting_started: [],
  equipment: [],
  core_systems: [],
  recurring_contents: [],
  advanced_contents: [],
  related_economy: [],
  related_projects: [],
}

test('전역 생활 navigation에서 hub와 skill route로 이동한다', async () => {
  vi.mocked(api.life).mockResolvedValue(hub)
  vi.mocked(api.lifeSkill).mockResolvedValue(detail)
  render(<MemoryRouter initialEntries={['/life']}><App /></MemoryRouter>)

  expect(await screen.findByRole('heading', { name: /생활,/ })).toBeInTheDocument()
  expect(screen.getByRole('link', { name: '생활' })).toHaveAttribute('href', '/life')
  fireEvent.click(screen.getByRole('link', { name: '분야 보기' }))
  expect(await screen.findByRole('heading', { name: '채집' })).toBeInTheDocument()
  expect(api.lifeSkill).toHaveBeenCalledWith('gathering')
})

test('전역 설정/백업 navigation과 settings route를 제공한다', () => {
  render(<MemoryRouter initialEntries={['/settings']}><App /></MemoryRouter>)

  expect(screen.getByRole('heading', {
    level: 1,
    name: /사용자 데이터 백업/,
  })).toBeInTheDocument()
  expect(screen.getByRole('link', { name: '설정/백업' })).toHaveAttribute(
    'href',
    '/settings',
  )
})
