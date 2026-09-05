import { fireEvent, render, screen, waitFor, within } from '@testing-library/react'
import { beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import { PromptPage } from './PromptPage'

vi.mock('../../api', () => ({
  api: {
    contents: vi.fn(),
    projects: vi.fn(),
    renderPrompt: vi.fn(),
  },
}))

beforeEach(() => {
  vi.mocked(api.contents).mockReset()
  vi.mocked(api.projects).mockReset()
  vi.mocked(api.renderPrompt).mockReset()
  vi.mocked(api.contents).mockResolvedValue([
    {
      slug: 'garmoth',
      name_ko: '가모스',
      category: 'boss',
      summary: null,
      status: 'active',
      last_verified_at: '2026-09-04',
      verification_status: 'verified',
    },
  ])
  vi.mocked(api.projects).mockResolvedValue([
    {
      slug: 'carrack-advance',
      name_ko: '에페리아 중범선: 점진',
      content_slug: 'carrack-advance',
      active: true,
      completed_stage_count: 0,
      total_stage_count: 4,
      shortage_material_count: 9,
    },
  ])
  vi.mocked(api.renderPrompt).mockResolvedValue({
    markdown: '# project preview',
    character_count: 17,
    estimated_tokens: 5,
    over_budget: false,
  })
})

test('API 프로젝트 목록을 선택하고 해당 slug로 project prompt를 생성한다', async () => {
  render(<PromptPage />)

  expect((await screen.findAllByRole('option', {
    name: '에페리아 중범선: 점진',
  }))[0]).toBeInTheDocument()
  fireEvent.click(screen.getByRole('button', { name: '프로젝트 프롬프트 만들기' }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'project_optimizer',
    content_slug: undefined,
    project_slug: 'carrack-advance',
    user_question: '',
  }))
  expect(await screen.findByDisplayValue('# project preview')).toBeInTheDocument()
})

test('프로젝트가 없으면 안내하고 project prompt 실행을 비활성화한다', async () => {
  vi.mocked(api.projects).mockResolvedValue([])
  render(<PromptPage />)

  expect(await screen.findByText('사용할 수 있는 프로젝트가 없습니다.')).toBeInTheDocument()
  expect(screen.getByRole('button', { name: '프로젝트 프롬프트 만들기' })).toBeDisabled()
})

test('전역 next action은 content/project slug 없이 요청한다', async () => {
  render(<PromptPage />)
  await screen.findAllByRole('option', { name: '가모스' })

  fireEvent.click(screen.getByRole('button', {
    name: '지금 할 일 프롬프트 만들기',
  }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'next_action',
    content_slug: undefined,
    project_slug: undefined,
    user_question: '',
  }))
})

test('content next action은 generic content 목록에서 선택한 slug를 요청한다', async () => {
  render(<PromptPage />)
  await screen.findAllByRole('option', { name: '가모스' })
  const section = screen.getByRole('heading', { name: '지금 할 일 질문' }).closest('section')!

  fireEvent.change(within(section).getByLabelText('대상 종류'), {
    target: { value: 'content' },
  })
  fireEvent.click(within(section).getByRole('button', {
    name: '지금 할 일 프롬프트 만들기',
  }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'next_action',
    content_slug: 'garmoth',
    project_slug: undefined,
    user_question: '',
  }))
})

test('project next action은 generic project 목록에서 선택한 slug를 요청한다', async () => {
  render(<PromptPage />)
  await screen.findAllByRole('option', { name: '에페리아 중범선: 점진' })
  const section = screen.getByRole('heading', { name: '지금 할 일 질문' }).closest('section')!

  fireEvent.change(within(section).getByLabelText('대상 종류'), {
    target: { value: 'project' },
  })
  fireEvent.click(within(section).getByRole('button', {
    name: '지금 할 일 프롬프트 만들기',
  }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'next_action',
    content_slug: undefined,
    project_slug: 'carrack-advance',
    user_question: '',
  }))
})

test('Verify Latest content target은 선택한 content slug를 요청한다', async () => {
  render(<PromptPage />)
  await screen.findAllByRole('option', { name: '가모스' })
  const section = screen.getByRole('heading', { name: '최신 정보 검증 질문' }).closest('section')!

  fireEvent.click(within(section).getByRole('button', {
    name: '최신 정보 검증 프롬프트 만들기',
  }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'verify_latest',
    content_slug: 'garmoth',
    project_slug: undefined,
    user_question: '',
  }))
})

test('Verify Latest project target은 선택한 project slug를 요청한다', async () => {
  render(<PromptPage />)
  await screen.findAllByRole('option', { name: '에페리아 중범선: 점진' })
  const section = screen.getByRole('heading', { name: '최신 정보 검증 질문' }).closest('section')!

  fireEvent.change(within(section).getByLabelText('대상 종류'), {
    target: { value: 'project' },
  })
  fireEvent.click(within(section).getByRole('button', {
    name: '최신 정보 검증 프롬프트 만들기',
  }))

  await waitFor(() => expect(api.renderPrompt).toHaveBeenCalledWith({
    mode: 'verify_latest',
    content_slug: undefined,
    project_slug: 'carrack-advance',
    user_question: '',
  }))
})
