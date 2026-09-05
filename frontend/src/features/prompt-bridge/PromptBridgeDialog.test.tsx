import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import { PromptBridgeDialog } from './PromptBridgeDialog'

vi.mock('../../api', () => ({
  api: {
    renderPrompt: vi.fn(),
  },
}))

beforeEach(() => {
  vi.mocked(api.renderPrompt).mockReset()
  vi.mocked(api.renderPrompt).mockResolvedValue({
    markdown: '# preview',
    character_count: 9,
    estimated_tokens: 3,
    over_budget: false,
  })
})

test('content onboarding 요청 계약을 유지한다', async () => {
  render(<PromptBridgeDialog mode="content_onboarding" contentSlug="garmoth" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'content_onboarding',
    content_slug: 'garmoth',
    project_slug: undefined,
    user_question: '',
  }))
  expect(await screen.findByDisplayValue('# preview')).toBeInTheDocument()
})

test('weekly review 요청 계약과 placeholder를 유지한다', async () => {
  render(<PromptBridgeDialog mode="weekly_review" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))

  expect(screen.getByPlaceholderText('이번 주 남은 일의 우선순위를 정해줘')).toBeInTheDocument()
  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'weekly_review',
    content_slug: undefined,
    project_slug: undefined,
    user_question: '',
  }))
})
