import { afterEach, expect, test, vi } from 'vitest'
import { api } from '../../api'

afterEach(() => {
  vi.unstubAllGlobals()
})

test('backup export와 validation을 지정 endpoint로 요청한다', async () => {
  const backup = {
    format: 'bdo-companion-user-backup',
    version: 1,
    exported_at: '2026-09-06T03:00:00Z',
    data: {
      content_states: [],
      checklist_instances: [],
      material_inventory: [],
      project_stage_states: [],
    },
  }
  const fetchMock = vi.fn()
    .mockResolvedValueOnce({ ok: true, json: async () => backup })
    .mockResolvedValueOnce({
      ok: true,
      json: async () => ({ valid: true, errors: [], warnings: [] }),
    })
  vi.stubGlobal('fetch', fetchMock)

  await api.exportUserBackup()
  await api.validateUserBackup(backup)

  expect(fetchMock).toHaveBeenNthCalledWith(1, '/api/settings/backup', {
    headers: { 'Content-Type': 'application/json' },
  })
  expect(fetchMock).toHaveBeenNthCalledWith(2, '/api/settings/backup/validate', {
    method: 'POST',
    body: JSON.stringify(backup),
    headers: { 'Content-Type': 'application/json' },
  })
})

test('backup import mode와 payload를 wrapper에 담아 전송한다', async () => {
  const backup = { format: 'bdo-companion-user-backup', version: 1 }
  const fetchMock = vi.fn().mockResolvedValue({
    ok: true,
    json: async () => ({ mode: 'replace' }),
  })
  vi.stubGlobal('fetch', fetchMock)

  await api.importUserBackup(backup, 'replace')

  expect(fetchMock).toHaveBeenCalledWith('/api/settings/backup/import', {
    method: 'POST',
    body: JSON.stringify({ backup, mode: 'replace' }),
    headers: { 'Content-Type': 'application/json' },
  })
})

test('import validation report의 stable-key errors를 읽을 수 있는 메시지로 만든다', async () => {
  const fetchMock = vi.fn().mockResolvedValue({
    ok: false,
    status: 422,
    json: async () => ({
      detail: {
        valid: false,
        errors: [
          'unknown content_slug: removed-content',
          'unknown material_key: removed-material',
        ],
      },
    }),
  })
  vi.stubGlobal('fetch', fetchMock)

  await expect(api.importUserBackup({}, 'merge')).rejects.toThrow(
    'unknown content_slug: removed-content; unknown material_key: removed-material',
  )
})
