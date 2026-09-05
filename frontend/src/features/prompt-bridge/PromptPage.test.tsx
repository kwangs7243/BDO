import { fireEvent, render, screen, waitFor } from '@testing-library/react'
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

  expect(await screen.findByRole('option', {
    name: '에페리아 중범선: 점진',
  })).toBeInTheDocument()
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
