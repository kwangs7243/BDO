import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, expect, test, vi } from 'vitest'
import { api } from '../../api'
import { ContentStateEditor } from './ContentStateEditor'

afterEach(() => vi.restoreAllMocks())

test('로컬 콘텐츠 상태와 메모를 저장한다', async () => {
  const saved = {
    state: 'in_progress' as const,
    priority: 1,
    note: '다음 단계 확인',
    updated_at: '2026-09-03T00:00:00Z',
  }
  const update = vi.spyOn(api, 'updateContentState').mockResolvedValue(saved)
  const onSaved = vi.fn()
  render(
    <ContentStateEditor
      contentSlug="carrack-advance"
      initialState={{ state: 'not_started', priority: null, note: null, updated_at: null }}
      onSaved={onSaved}
    />,
  )

  fireEvent.change(screen.getByRole('combobox'), { target: { value: 'in_progress' } })
  fireEvent.change(screen.getByRole('spinbutton'), { target: { value: '1' } })
  fireEvent.change(screen.getByRole('textbox'), { target: { value: '다음 단계 확인' } })
  fireEvent.click(screen.getByRole('button', { name: '상태 저장' }))

  await waitFor(() => expect(update).toHaveBeenCalledWith(
    'carrack-advance',
    'in_progress',
    1,
    '다음 단계 확인',
  ))
  expect(onSaved).toHaveBeenCalledWith(saved)
  expect(await screen.findByText('저장했습니다.')).toBeInTheDocument()
})

