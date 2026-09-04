import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../../api'
import { StatusBadge } from '../../components/StatusBadge'
import type { ContentSummary } from '../../types'

export function ContentExplorerPage() {
  const [contents, setContents] = useState<ContentSummary[]>([])
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState('all')
  const [error, setError] = useState('')
  useEffect(() => { api.contents().then(setContents).catch((reason: Error) => setError(reason.message)) }, [])
  const categories = [...new Set(contents.map((item) => item.category))].sort()
  const filtered = contents.filter((item) => {
    const textMatches = `${item.name_ko} ${item.summary ?? ''}`.toLowerCase().includes(query.toLowerCase())
    return textMatches && (category === 'all' || item.category === category)
  })

  return (
    <div>
      <header className="page-header"><div><p className="eyebrow">KNOWLEDGE INDEX</p><h1>콘텐츠 탐색</h1><p className="subtitle">출처와 검증 상태를 함께 확인하세요.</p></div></header>
      <div className="filters">
        <input aria-label="콘텐츠 검색" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="콘텐츠 이름이나 설명 검색" />
        <select aria-label="카테고리" value={category} onChange={(event) => setCategory(event.target.value)}>
          <option value="all">모든 카테고리</option>
          {categories.map((item) => <option value={item} key={item}>{item}</option>)}
        </select>
      </div>
      {error && <p className="error">{error}</p>}
      <div className="content-grid">
        {filtered.map((item) => (
          <Link className="content-card" to={`/content/${item.slug}`} key={item.slug}>
            <div className="card-top"><span className="category">{item.category}</span><StatusBadge status={item.verification_status} /></div>
            <h2>{item.name_ko}</h2>
            <p>{item.summary || '구조화된 설명이 아직 없습니다.'}</p>
            <small>검증일 {item.last_verified_at ?? '미확인'}</small>
          </Link>
        ))}
      </div>
    </div>
  )
}
