import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import { ProjectListPage } from './ProjectListPage'

vi.mock('../../api', () => ({
  api: {
    projects: vi.fn(),
  },
}))

function renderPage() {
  return render(<MemoryRouter><ProjectListPage /></MemoryRouter>)
}

beforeEach(() => {
  vi.mocked(api.projects).mockReset()
})

test('프로젝트 진행률과 부족 재료 수 및 상세 링크를 표시한다', async () => {
  vi.mocked(api.projects).mockResolvedValue([{
    slug: 'carrack-project',
    name_ko: '중범선 제작 프로젝트',
    content_slug: 'carrack-progression',
    active: true,
    completed_stage_count: 1,
    total_stage_count: 4,
    shortage_material_count: 7,
  }])

  renderPage()

  expect(await screen.findByRole('heading', { name: '중범선 제작 프로젝트' })).toBeInTheDocument()
  expect(screen.getByText('1/4')).toBeInTheDocument()
  expect(screen.getByText('7')).toBeInTheDocument()
  expect(screen.getByRole('link', { name: '연결된 콘텐츠' })).toHaveAttribute('href', '/content/carrack-progression')
  expect(screen.getByRole('link', { name: '프로젝트 열기' })).toHaveAttribute('href', '/projects/carrack-project')
})

test('목록 로딩, 빈 상태, 오류 상태를 구분한다', async () => {
  vi.mocked(api.projects).mockImplementation(() => new Promise(() => undefined))
  const view = renderPage()
  expect(screen.getByText('프로젝트를 불러오는 중입니다.')).toBeInTheDocument()

  view.unmount()
  vi.mocked(api.projects).mockResolvedValue([])
  const emptyView = renderPage()
  expect(await screen.findByText('등록된 프로젝트가 없습니다.')).toBeInTheDocument()

  emptyView.unmount()
  vi.mocked(api.projects).mockRejectedValue(new Error('목록 오류'))
  renderPage()
  expect(await screen.findByRole('alert')).toHaveTextContent('목록 오류')
})
