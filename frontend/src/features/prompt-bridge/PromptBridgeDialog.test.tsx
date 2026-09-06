import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import { PromptBridgeDialog } from './PromptBridgeDialog'
import { defaultPromptSections } from './promptConfig'

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
    original_estimated_tokens: 3,
    compacted: false,
    omitted_counts: {},
    over_budget: false,
  })
})

afterEach(() => {
  vi.restoreAllMocks()
  vi.unstubAllGlobals()
})

test('content onboarding 요청 계약을 유지한다', async () => {
  render(<PromptBridgeDialog mode="content_onboarding" contentSlug="garmoth" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'content_onboarding',
    content_slug: 'garmoth',
    project_slug: undefined,
    user_question: '',
    include_sections: defaultPromptSections('content_onboarding', 'garmoth'),
    output_mode: 'full_prompt',
    size_mode: 'auto',
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
    include_sections: defaultPromptSections('weekly_review'),
    output_mode: 'full_prompt',
    size_mode: 'auto',
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
    include_sections: defaultPromptSections('next_action', 'garmoth'),
    output_mode: 'full_prompt',
    size_mode: 'auto',
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
    include_sections: defaultPromptSections(
      'verify_latest',
      undefined,
      'carrack-advance',
    ),
    output_mode: 'full_prompt',
    size_mode: 'auto',
  }))
})

test('selector를 표시하고 checkbox 해제를 include_sections에 반영한다', async () => {
  render(<PromptBridgeDialog mode="content_onboarding" contentSlug="garmoth" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))

  expect(screen.getByText('포함할 컨텍스트')).toBeInTheDocument()
  const verifiedKnowledge = screen.getByRole('checkbox', {
    name: '검증된 지식 (FACT/STRATEGY/MEASUREMENT)',
  })
  expect(verifiedKnowledge).toBeChecked()
  const requirements = screen.getByRole('checkbox', { name: '요구사항' })
  expect(requirements).toBeChecked()
  fireEvent.click(requirements)

  await waitFor(() => {
    const latest = vi.mocked(api.renderPrompt).mock.calls.at(-1)?.[0]
    expect(latest?.include_sections).toContain('canonical_facts')
    expect(latest?.include_sections).not.toContain('requirements')
  })
})

test('질문 변경은 selector를 초기화하지 않는다', async () => {
  render(<PromptBridgeDialog mode="content_onboarding" contentSlug="garmoth" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))
  const requirements = screen.getByRole('checkbox', { name: '요구사항' })
  fireEvent.click(requirements)
  fireEvent.change(screen.getByLabelText('추가 질문'), {
    target: { value: '오늘 할 일' },
  })

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalled())
  expect(requirements).not.toBeChecked()
})

test('target 변경은 새 target의 기본 selector로 초기화한다', async () => {
  const view = render(
    <PromptBridgeDialog mode="next_action" contentSlug="garmoth" />,
  )
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))
  fireEvent.click(screen.getByRole('checkbox', { name: '요구사항' }))
  expect(screen.getByRole('checkbox', { name: '요구사항' })).not.toBeChecked()

  view.rerender(
    <PromptBridgeDialog mode="next_action" projectSlug="carrack-advance" />,
  )

  await waitFor(() => {
    expect(screen.queryByRole('checkbox', { name: '요구사항' })).not.toBeInTheDocument()
    expect(screen.getByRole('checkbox', { name: '프로젝트 상태' })).toBeChecked()
  })
})

test('context-only는 질문을 숨기고 질문 없이 요청한다', async () => {
  render(<PromptBridgeDialog mode="weekly_review" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))
  fireEvent.click(screen.getByRole('radio', { name: '컨텍스트만' }))

  expect(screen.queryByLabelText('추가 질문')).not.toBeInTheDocument()
  expect(screen.getByText(
    '컨텍스트만 출력할 때는 질문과 응답 지침을 포함하지 않습니다.',
  )).toBeInTheDocument()
  await waitFor(() => {
    const latest = vi.mocked(api.renderPrompt).mock.calls.at(-1)?.[0]
    expect(latest).toMatchObject({
      output_mode: 'context_only',
      user_question: '',
    })
  })
})

test('detailed size mode를 요청하고 초과 경고를 표시한다', async () => {
  vi.mocked(api.renderPrompt).mockResolvedValue({
    markdown: '# detailed',
    character_count: 50_000,
    estimated_tokens: 12_500,
    original_estimated_tokens: 12_500,
    compacted: false,
    omitted_counts: {},
    over_budget: true,
  })
  render(<PromptBridgeDialog mode="weekly_review" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))
  fireEvent.click(screen.getByRole('radio', { name: '상세하게' }))

  await waitFor(() => {
    const latest = vi.mocked(api.renderPrompt).mock.calls.at(-1)?.[0]
    expect(latest?.size_mode).toBe('detailed')
  })
  expect(await screen.findByText('권장 크기 초과')).toBeInTheDocument()
})

test('자동 축약과 축약 전 token 및 생략 수를 표시한다', async () => {
  vi.mocked(api.renderPrompt).mockResolvedValue({
    markdown: '# compacted',
    character_count: 46_000,
    estimated_tokens: 11_500,
    original_estimated_tokens: 14_200,
    compacted: true,
    omitted_counts: { related_contents: 2, sources: 3 },
    over_budget: false,
  })
  render(<PromptBridgeDialog mode="weekly_review" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))

  expect(await screen.findByText(/자동 축약됨/)).toHaveTextContent(
    '약 11,500 tokens · 자동 축약됨 (축약 전 약 14,200)',
  )
  expect(screen.getByText(
    '생략: related_contents 2, sources 3',
  )).toBeInTheDocument()
})

test('생성 결과를 clipboard에 복사한다', async () => {
  const writeText = vi.fn().mockResolvedValue(undefined)
  vi.stubGlobal('navigator', { clipboard: { writeText } })
  render(<PromptBridgeDialog mode="weekly_review" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))
  await screen.findByDisplayValue('# preview')
  fireEvent.click(screen.getByRole('button', { name: '복사' }))

  await waitFor(() => expect(writeText).toHaveBeenCalledWith('# preview'))
})

test('생성 결과를 Markdown 파일로 다운로드한다', async () => {
  const createObjectURL = vi.fn().mockReturnValue('blob:prompt')
  const revokeObjectURL = vi.fn()
  vi.stubGlobal('URL', { createObjectURL, revokeObjectURL })
  const click = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(() => undefined)
  render(<PromptBridgeDialog mode="weekly_review" />)
  fireEvent.click(screen.getByRole('button', { name: 'ChatGPT에 물어보기' }))
  await screen.findByDisplayValue('# preview')
  fireEvent.click(screen.getByRole('button', { name: 'Markdown 저장' }))

  expect(createObjectURL).toHaveBeenCalled()
  expect(click).toHaveBeenCalled()
  expect(revokeObjectURL).toHaveBeenCalledWith('blob:prompt')
})
