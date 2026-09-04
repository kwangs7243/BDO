import { afterEach, expect, test, vi } from 'vitest'
import { api } from '../../api'

afterEach(() => {
  vi.unstubAllGlobals()
})

test('재고 갱신을 올바른 endpoint와 PUT body로 전송한다', async () => {
  const payload = {
    material_key: 'moon vein flax',
    quantity: 100,
    note: '이번 주 재고',
    updated_at: '2026-09-05T10:00:00Z',
  }
  const fetchMock = vi.fn().mockResolvedValue({
    ok: true,
    json: async () => payload,
  })
  vi.stubGlobal('fetch', fetchMock)

  await expect(api.updateMaterialInventory('moon vein flax', 100, '이번 주 재고')).resolves.toEqual(payload)
  expect(fetchMock).toHaveBeenCalledWith(
    '/api/materials/moon%20vein%20flax/inventory',
    {
      method: 'PUT',
      body: JSON.stringify({ quantity: 100, note: '이번 주 재고' }),
      headers: { 'Content-Type': 'application/json' },
    },
  )
})

test('stage 완료와 해제를 올바른 endpoint에 PUT한다', async () => {
  const payload = {
    project_slug: 'carrack project',
    stage_id: 4,
    completed: false,
    completed_at: null,
    note: null,
    updated_at: '2026-09-05T10:00:00Z',
  }
  const fetchMock = vi.fn().mockResolvedValue({
    ok: true,
    json: async () => payload,
  })
  vi.stubGlobal('fetch', fetchMock)

  await expect(api.updateProjectStageState('carrack project', 4, false, null)).resolves.toEqual(payload)
  expect(fetchMock).toHaveBeenCalledWith(
    '/api/projects/carrack%20project/stages/4/state',
    {
      method: 'PUT',
      body: JSON.stringify({ completed: false, note: null }),
      headers: { 'Content-Type': 'application/json' },
    },
  )
})
