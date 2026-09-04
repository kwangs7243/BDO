import { fireEvent, render, screen, waitFor, within } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import { beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import type { ProjectDetail, ProjectMaterial, ProjectStage } from '../../types'
import { ProjectDetailPage } from './ProjectDetailPage'

vi.mock('../../api', () => ({
  api: {
    project: vi.fn(),
    updateMaterialInventory: vi.fn(),
    updateProjectStageState: vi.fn(),
  },
}))

const stages: ProjectStage[] = [
  { id: 1, seed_key: 'carrack.base', name: '증축 기반', description: '기반 선박을 준비한다.', order_no: 1, completed: false, completed_at: null, note: null, dependencies: [] },
  { id: 2, seed_key: 'carrack.blue', name: '파란색 장비', description: '장비를 강화한다.', order_no: 2, completed: false, completed_at: null, note: null, dependencies: ['carrack.base'] },
  { id: 3, seed_key: 'carrack.body', name: '선체 재료', description: '증축 재료를 모은다.', order_no: 3, completed: false, completed_at: null, note: null, dependencies: ['carrack.base'] },
  { id: 4, seed_key: 'carrack.upgrade', name: '최종 증축', description: '중범선으로 증축한다.', order_no: 4, completed: false, completed_at: null, note: null, dependencies: ['carrack.blue', 'carrack.body'] },
]

const materialNames = ['달의 핏줄이 새겨진 아교', '심해의 눈물', '콕스해적단의 유물', '순수한 진주 결정', '파도빛이 감도는 규격 각목', '강화된 섬나무 증착합판', '대양의 견고한 현철', '빛나는 코발트 주괴', '화려한 암염 주괴']

function material(name: string, index: number): ProjectMaterial {
  const key = `material-${index + 1}`
  return {
    seed_key: `carrack.${key}`,
    material_key: key,
    name_ko: name,
    unit: '개',
    stage_seed_key: index < 4 ? 'carrack.blue' : 'carrack.body',
    required_quantity: index === 0 ? 180 : 10 + index,
    owned_quantity: index === 0 ? 30 : 0,
    shortage: index === 0 ? 150 : 10 + index,
    inventory_note: index === 0 ? '저장된 재고 메모' : null,
    inventory_updated_at: index === 0 ? '2026-09-05T09:00:00Z' : null,
    notes: index === 0 ? '선박 증축 재료' : null,
    order_no: index + 1,
    source_entity_type: null,
    source_entity_seed_key: null,
    sources: index === 0 ? [
      { seed_key: 'source-known', content_slug: 'ocean-daily', content_name_ko: '대양 일일 의뢰', quantity_per_completion: 3, notes: '일일 보상', order_no: 1 },
      { seed_key: 'source-unknown', content_slug: 'crow-coin-shop', content_name_ko: '까마귀 주화 상점', quantity_per_completion: null, notes: null, order_no: 2 },
    ] : [],
  }
}

const fixture: ProjectDetail = {
  slug: 'carrack-project',
  name_ko: '중범선 제작 프로젝트',
  content_slug: 'carrack-progression',
  summary: '중범선 증축 진행도를 관리한다.',
  active: true,
  stages,
  materials: materialNames.map(material),
}

function renderPage() {
  return render(
    <MemoryRouter initialEntries={['/projects/carrack-project']}>
      <Routes><Route path='/projects/:slug' element={<ProjectDetailPage />} /></Routes>
    </MemoryRouter>,
  )
}

beforeEach(() => {
  vi.mocked(api.project).mockReset()
  vi.mocked(api.updateMaterialInventory).mockReset()
  vi.mocked(api.updateProjectStageState).mockReset()
  vi.mocked(api.project).mockResolvedValue(structuredClone(fixture))
})

test('4단계와 9재료, 서버 계산 수치, 획득처를 표시한다', async () => {
  renderPage()

  expect(await screen.findByRole('heading', { name: '중범선 제작 프로젝트' })).toBeInTheDocument()
  expect(screen.getAllByRole('checkbox')).toHaveLength(4)
  expect(screen.getAllByRole('heading', { level: 4 })).toHaveLength(9)
  expect(screen.getByRole('link', { name: '기존 콘텐츠 상세' })).toHaveAttribute('href', '/content/carrack-progression')

  const firstCard = screen.getByRole('heading', { name: materialNames[0] }).closest('article')
  expect(firstCard).not.toBeNull()
  const card = within(firstCard!)
  expect(card.getByText('180')).toBeInTheDocument()
  expect(card.getByDisplayValue('30')).toBeInTheDocument()
  expect(card.getByText('150')).toBeInTheDocument()
  expect(card.getByRole('link', { name: /대양 일일 의뢰/ })).toHaveAttribute('href', '/content/ocean-daily')
  expect(card.getByText('1회 3개')).toBeInTheDocument()
  expect(card.getByText('수량 미확인')).toBeInTheDocument()
  expect(card.queryByText('1회 0개')).not.toBeInTheDocument()

  expect(screen.getAllByText('선행 단계: carrack.base')).toHaveLength(2)
  expect(screen.getByRole('checkbox', { name: '파란색 장비 완료' })).toBeEnabled()
})

test('최초 렌더링에서 저장된 inventory note를 복원한다', async () => {
  renderPage()

  expect(await screen.findByRole('textbox', {
    name: `${materialNames[0]} 사용자 메모`,
  })).toHaveValue('저장된 재고 메모')
})

test('명시적 저장 뒤 서버가 반환한 보유량과 부족량으로 다시 표시한다', async () => {
  const updated = structuredClone(fixture)
  updated.materials[0].owned_quantity = 100
  updated.materials[0].shortage = 77
  updated.materials[0].inventory_note = '이번 주 재고'
  vi.mocked(api.project)
    .mockResolvedValueOnce(structuredClone(fixture))
    .mockResolvedValueOnce(updated)
  vi.mocked(api.updateMaterialInventory).mockResolvedValue({
    material_key: 'material-1', quantity: 100, note: '이번 주 재고', updated_at: '2026-09-05T10:00:00Z',
  })

  renderPage()
  const input = await screen.findByRole('spinbutton', { name: `${materialNames[0]} 보유량` })
  fireEvent.change(input, { target: { value: '100' } })
  fireEvent.change(screen.getByRole('textbox', { name: `${materialNames[0]} 사용자 메모` }), { target: { value: '이번 주 재고' } })
  expect(api.updateMaterialInventory).not.toHaveBeenCalled()

  const firstCard = screen.getByRole('heading', { name: materialNames[0] }).closest('article')!
  fireEvent.click(within(firstCard).getByRole('button', { name: '재고 저장' }))

  await waitFor(() => expect(api.updateMaterialInventory).toHaveBeenCalledWith('material-1', 100, '이번 주 재고'))
  await waitFor(() => expect(within(firstCard).getByDisplayValue('100')).toBeInTheDocument())
  expect(within(firstCard).getByText('77')).toBeInTheDocument()
  expect(screen.getByRole('textbox', { name: `${materialNames[0]} 사용자 메모` })).toHaveValue('이번 주 재고')
})

test('재고 입력에서 음수와 소수를 거부한다', async () => {
  renderPage()
  const input = await screen.findByRole('spinbutton', { name: `${materialNames[0]} 보유량` })
  const firstCard = screen.getByRole('heading', { name: materialNames[0] }).closest('article')!

  fireEvent.change(input, { target: { value: '1.5' } })
  fireEvent.click(within(firstCard).getByRole('button', { name: '재고 저장' }))
  expect(await screen.findByRole('alert')).toHaveTextContent('0 이상의 정수')
  expect(api.updateMaterialInventory).not.toHaveBeenCalled()

  fireEvent.change(input, { target: { value: '-1' } })
  fireEvent.click(within(firstCard).getByRole('button', { name: '재고 저장' }))
  expect(api.updateMaterialInventory).not.toHaveBeenCalled()
})

test('단계를 완료하고 해제할 때 각각 서버에 저장한 뒤 재조회한다', async () => {
  const completed = structuredClone(fixture)
  completed.stages[0].completed = true
  completed.stages[0].completed_at = '2026-09-05T10:00:00Z'
  const reopened = structuredClone(fixture)
  vi.mocked(api.project)
    .mockResolvedValueOnce(structuredClone(fixture))
    .mockResolvedValueOnce(completed)
    .mockResolvedValueOnce(reopened)
  vi.mocked(api.updateProjectStageState).mockResolvedValue({
    project_slug: 'carrack-project', stage_id: 1, completed: true, completed_at: '2026-09-05T10:00:00Z', note: null, updated_at: '2026-09-05T10:00:00Z',
  })

  renderPage()
  const checkbox = await screen.findByRole('checkbox', { name: '증축 기반 완료' })
  const inventoryNote = screen.getByRole('textbox', { name: `${materialNames[0]} 사용자 메모` })
  fireEvent.change(inventoryNote, { target: { value: '저장 전 초안' } })
  fireEvent.click(checkbox)
  await waitFor(() => expect(api.updateProjectStageState).toHaveBeenCalledWith('carrack-project', 1, true, null))
  await waitFor(() => expect(checkbox).toBeChecked())
  expect(inventoryNote).toHaveValue('저장 전 초안')

  fireEvent.click(checkbox)
  await waitFor(() => expect(api.updateProjectStageState).toHaveBeenLastCalledWith('carrack-project', 1, false, null))
  await waitFor(() => expect(checkbox).not.toBeChecked())
})

test('저장 실패 시 완료 상태를 바꾸지 않고 오류를 표시한다', async () => {
  vi.mocked(api.updateProjectStageState).mockRejectedValue(new Error('단계 저장 실패'))
  renderPage()
  const checkbox = await screen.findByRole('checkbox', { name: '증축 기반 완료' })

  fireEvent.click(checkbox)

  expect(await screen.findByRole('alert')).toHaveTextContent('단계 저장 실패')
  expect(checkbox).not.toBeChecked()
  expect(api.project).toHaveBeenCalledTimes(1)
})

test('상세 로딩과 오류 상태를 표시한다', async () => {
  vi.mocked(api.project).mockImplementation(() => new Promise(() => undefined))
  const view = renderPage()
  expect(screen.getByText('프로젝트를 불러오는 중입니다.')).toBeInTheDocument()

  view.unmount()
  vi.mocked(api.project).mockRejectedValue(new Error('프로젝트 없음'))
  renderPage()
  expect(await screen.findByRole('alert')).toHaveTextContent('프로젝트 없음')
})
