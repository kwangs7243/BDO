import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import { DashboardPage } from './DashboardPage'

vi.mock('../../api', () => ({
  api: {
    dashboard: vi.fn(),
    renderPrompt: vi.fn(),
  },
}))

beforeEach(() => {
  vi.mocked(api.dashboard).mockResolvedValue({
    now: '2026-09-05T10:00:00+09:00',
    reset_groups: [],
    daily: [],
    weekly: [],
  })
  vi.mocked(api.renderPrompt).mockResolvedValue({
    markdown: '# next action',
    character_count: 13,
    estimated_tokens: 4,
    over_budget: false,
  })
})

test('Dashboard에서 target 없는 global next action prompt를 연다', async () => {
  render(
    <MemoryRouter>
      <DashboardPage />
    </MemoryRouter>,
  )

  fireEvent.click(await screen.findByRole('button', {
    name: '지금 할 일 ChatGPT에 물어보기',
  }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'next_action',
    content_slug: undefined,
    project_slug: undefined,
    user_question: '',
  }))
  expect(await screen.findByDisplayValue('# next action')).toBeInTheDocument()
})
