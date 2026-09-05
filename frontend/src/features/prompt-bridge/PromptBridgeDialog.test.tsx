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

test('next action의 target 계약과 placeholder를 명시적으로 사용한다', async () => {
  render(
    <PromptBridgeDialog
      mode="next_action"
      contentSlug="garmoth"
      triggerLabel="다음 행동"
    />,
  )
  fireEvent.click(screen.getByRole('button', { name: '다음 행동' }))

  expect(screen.getByPlaceholderText(
    '지금 내 상태에서 무엇부터 하면 돼?',
  )).toBeInTheDocument()
  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'next_action',
    content_slug: 'garmoth',
    project_slug: undefined,
    user_question: '',
  }))
})

test('verify latest의 project 계약과 placeholder를 명시적으로 사용한다', async () => {
  render(
    <PromptBridgeDialog
      mode="verify_latest"
      projectSlug="carrack-advance"
      triggerLabel="최신 검증"
    />,
  )
  fireEvent.click(screen.getByRole('button', { name: '최신 검증' }))

  expect(screen.getByPlaceholderText(
    '미검증 항목을 최신 KR 공식 자료로 확인해줘',
  )).toBeInTheDocument()
  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'verify_latest',
    content_slug: undefined,
    project_slug: 'carrack-advance',
    user_question: '',
  }))
})
