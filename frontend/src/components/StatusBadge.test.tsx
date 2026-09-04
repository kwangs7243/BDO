import { render, screen } from '@testing-library/react'
import { expect, test } from 'vitest'
import { StatusBadge } from './StatusBadge'

test('검증 상태를 한국어로 구분해 표시한다', () => {
  render(<StatusBadge status="needs_review" />)
  expect(screen.getByText('재검토 필요')).toHaveClass('badge-needs_review')
})
