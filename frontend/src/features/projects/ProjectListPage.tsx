import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { api } from '../../api'
import type { ProjectSummary } from '../../types'

export function ProjectListPage() {
  const [projects, setProjects] = useState<ProjectSummary[] | null>(null)
  const [error, setError] = useState('')

  useEffect(() => {
    api.projects()
      .then(setProjects)
      .catch((reason: Error) => setError(reason.message))
  }, [])

  return (
    <div>
      <header className="page-header">
        <div>
          <p className="eyebrow">PROJECT TRACKER</p>
          <h1>프로젝트</h1>
          <p className="subtitle">단계 진행과 보유 재료, 서버가 계산한 부족량을 함께 확인합니다.</p>
        </div>
      </header>

      {error && <p className="error" role="alert">{error}</p>}
      {!error && projects === null && <p className="loading">프로젝트를 불러오는 중입니다.</p>}
      {!error && projects?.length === 0 && <p className="empty">등록된 프로젝트가 없습니다.</p>}

      {projects && projects.length > 0 && (
        <div className="project-grid">
          {projects.map((project) => (
            <article className="project-card" key={project.slug}>
              <div className="card-top">
                <span className="category">ACTIVE PROJECT</span>
                <span className={project.shortage_material_count > 0 ? 'project-status shortage' : 'project-status ready'}>
                  {project.shortage_material_count > 0 ? '재료 부족' : '충족'}
                </span>
              </div>
              <h2>{project.name_ko}</h2>
              <div className="project-metrics">
                <div><strong>{project.completed_stage_count}/{project.total_stage_count}</strong><span>완료 단계</span></div>
                <div><strong>{project.shortage_material_count}</strong><span>부족 재료 종류</span></div>
              </div>
              <div className="project-card-actions">
                {project.content_slug && (
                  <Link to={`/content/${project.content_slug}`}>연결된 콘텐츠</Link>
                )}
                <Link className="button primary" to={`/projects/${project.slug}`}>프로젝트 열기</Link>
              </div>
            </article>
          ))}
        </div>
      )}
    </div>
  )
}
