import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, beforeEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import type {
  UserBackup,
  UserBackupImportResult,
  UserBackupValidation,
} from '../../types'
import { SettingsPage } from './SettingsPage'

vi.mock('../../api', () => ({
  api: {
    exportUserBackup: vi.fn(),
    validateUserBackup: vi.fn(),
    importUserBackup: vi.fn(),
  },
}))

const backup: UserBackup = {
  format: 'bdo-companion-user-backup',
  version: 1,
  exported_at: '2026-09-06T03:00:00Z',
  data: {
    content_states: [{
      content_slug: 'garmoth',
      state: 'completed',
      priority: 1,
      note: '완료',
      updated_at: '2026-09-06T03:00:00Z',
    }],
    checklist_instances: [],
    material_inventory: [],
    project_stage_states: [],
  },
}

const validReport: UserBackupValidation = {
  valid: true,
  format: 'bdo-companion-user-backup',
  version: 1,
  content_states: 14,
  checklist_instances: 37,
  checklist_items: 112,
  material_inventory: 9,
  project_stage_states: 4,
  errors: [],
  warnings: [],
}

const importResult: UserBackupImportResult = {
  mode: 'merge',
  content_states_upserted: 14,
  checklist_instances_upserted: 37,
  checklist_items_upserted: 112,
  material_inventory_upserted: 9,
  project_stage_states_upserted: 4,
  deleted_counts: {
    content_states: 0,
    checklist_instances: 0,
    checklist_items: 0,
    material_inventory: 0,
    project_stage_states: 0,
  },
}

function backupFile(contents = JSON.stringify(backup)) {
  const file = new File([contents], 'backup.json', { type: 'application/json' })
  Object.defineProperty(file, 'text', {
    value: vi.fn().mockResolvedValue(contents),
  })
  return file
}

async function chooseValidBackup() {
  fireEvent.change(screen.getByLabelText('JSON 백업 파일'), {
    target: { files: [backupFile()] },
  })
  await screen.findByText('복원 가능한 백업입니다.')
}

beforeEach(() => {
  vi.mocked(api.exportUserBackup).mockReset()
  vi.mocked(api.validateUserBackup).mockReset()
  vi.mocked(api.importUserBackup).mockReset()
  vi.mocked(api.exportUserBackup).mockResolvedValue(backup)
  vi.mocked(api.validateUserBackup).mockResolvedValue(validReport)
  vi.mocked(api.importUserBackup).mockResolvedValue(importResult)
})

afterEach(() => {
  vi.restoreAllMocks()
  vi.unstubAllGlobals()
})

test('사용자 데이터 범위 설명과 export button을 표시한다', () => {
  render(<SettingsPage />)

  expect(screen.getByRole('button', { name: 'JSON 백업 다운로드' })).toBeEnabled()
  expect(screen.getByText(/canonical 게임 정보와 출처는 포함하지 않습니다/)).toBeInTheDocument()
  expect(screen.getByLabelText('JSON 백업 파일')).toHaveAttribute(
    'accept',
    'application/json,.json',
  )
})

test('export API 결과를 날짜가 포함된 JSON Blob으로 다운로드한다', async () => {
  const createObjectURL = vi.fn().mockReturnValue('blob:backup')
  const revokeObjectURL = vi.fn()
  vi.stubGlobal('URL', { createObjectURL, revokeObjectURL })
  const click = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(
    () => undefined,
  )
  render(<SettingsPage />)

  fireEvent.click(screen.getByRole('button', { name: 'JSON 백업 다운로드' }))

  await waitFor(() => expect(api.exportUserBackup).toHaveBeenCalledTimes(1))
  expect(createObjectURL).toHaveBeenCalledWith(expect.any(Blob))
  expect(click).toHaveBeenCalled()
  expect(revokeObjectURL).toHaveBeenCalledWith('blob:backup')
  expect(screen.getByRole('status')).toHaveTextContent('백업을 다운로드했습니다')
})

test('선택한 JSON을 validate하고 summary와 기본 merge mode를 표시한다', async () => {
  render(<SettingsPage />)

  await chooseValidBackup()

  expect(api.validateUserBackup).toHaveBeenCalledWith(backup)
  expect(screen.getByText('콘텐츠 상태').parentElement).toHaveTextContent('14개')
  expect(screen.getByText('체크리스트 기간').parentElement).toHaveTextContent('37개')
  expect(screen.getByText('체크 상태').parentElement).toHaveTextContent('112개')
  expect(screen.getByText('재료 재고').parentElement).toHaveTextContent('9개')
  expect(screen.getByText('프로젝트 단계').parentElement).toHaveTextContent('4개')
  expect(screen.getByRole('radio', { name: /병합/ })).toBeChecked()
  expect(screen.getByRole('button', { name: '백업 병합' })).toBeEnabled()
})

test('잘못된 browser JSON parse를 구체적으로 표시하고 import를 막는다', async () => {
  render(<SettingsPage />)

  fireEvent.change(screen.getByLabelText('JSON 백업 파일'), {
    target: { files: [backupFile('{broken')] },
  })

  expect(await screen.findByRole('alert')).toHaveTextContent(
    '올바른 JSON 백업 파일이 아닙니다.',
  )
  expect(api.validateUserBackup).not.toHaveBeenCalled()
  expect(screen.getByRole('button', { name: '백업 병합' })).toBeDisabled()
})

test('validation 오류와 stable key를 표시하고 import를 막는다', async () => {
  vi.mocked(api.validateUserBackup).mockResolvedValue({
    ...validReport,
    valid: false,
    errors: ['unknown material_key: removed-material'],
  })
  render(<SettingsPage />)

  fireEvent.change(screen.getByLabelText('JSON 백업 파일'), {
    target: { files: [backupFile()] },
  })

  expect(await screen.findByText('백업을 복원할 수 없습니다.')).toBeInTheDocument()
  expect(screen.getByText('unknown material_key: removed-material')).toBeInTheDocument()
  expect(screen.getByRole('button', { name: '백업 병합' })).toBeDisabled()
})

test('replace는 명시적 confirmation 전 비활성이고 확인 후 실행한다', async () => {
  vi.mocked(api.importUserBackup).mockResolvedValue({
    ...importResult,
    mode: 'replace',
    deleted_counts: {
      content_states: 2,
      checklist_instances: 3,
      checklist_items: 7,
      material_inventory: 1,
      project_stage_states: 1,
    },
  })
  render(<SettingsPage />)
  await chooseValidBackup()

  fireEvent.click(screen.getByRole('radio', { name: /전체 복원/ }))
  const restore = screen.getByRole('button', { name: '전체 복원 실행' })
  expect(restore).toBeDisabled()

  fireEvent.click(screen.getByRole('checkbox', {
    name: /기존 사용자 진행 상태와 체크리스트 기록/,
  }))
  expect(restore).toBeEnabled()
  fireEvent.click(restore)

  await waitFor(() => expect(api.importUserBackup).toHaveBeenCalledWith(
    backup,
    'replace',
  ))
  expect(await screen.findByText('백업 내용으로 전체 복원했습니다.')).toBeInTheDocument()
  expect(screen.getByText(/교체 전 제거:/)).toHaveTextContent(
    '체크리스트 기간 3개',
  )
})

test('merge import 성공 결과를 사용자에게 표시한다', async () => {
  render(<SettingsPage />)
  await chooseValidBackup()

  fireEvent.click(screen.getByRole('button', { name: '백업 병합' }))

  await waitFor(() => expect(api.importUserBackup).toHaveBeenCalledWith(
    backup,
    'merge',
  ))
  expect(await screen.findByText('복원 결과')).toBeInTheDocument()
  expect(screen.getByText('콘텐츠 상태 14개')).toBeInTheDocument()
  expect(screen.getByText('체크 상태 112개')).toBeInTheDocument()
  expect(screen.getByText('백업을 병합했습니다.')).toBeInTheDocument()
})

test('import 실패를 raw traceback 없이 오류 메시지로 표시한다', async () => {
  vi.mocked(api.importUserBackup).mockRejectedValue(
    new Error('복원 요청이 거부되었습니다.'),
  )
  render(<SettingsPage />)
  await chooseValidBackup()

  fireEvent.click(screen.getByRole('button', { name: '백업 병합' }))

  expect(await screen.findByRole('alert')).toHaveTextContent(
    '복원 요청이 거부되었습니다.',
  )
  expect(screen.queryByText('Traceback')).not.toBeInTheDocument()
})
