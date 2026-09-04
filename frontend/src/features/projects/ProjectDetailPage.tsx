import { useCallback, useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { api } from '../../api'
import type { ProjectDetail, ProjectMaterial, ProjectStage } from '../../types'

function formatQuantity(value: number) {
  return Number.isInteger(value) ? value.toLocaleString('ko-KR') : value.toLocaleString('ko-KR', { maximumFractionDigits: 2 })
}

function formatCompletedAt(value: string | null) {
  if (!value) return null
  return new Intl.DateTimeFormat('ko-KR', {
    dateStyle: 'medium',
    timeStyle: 'short',
    timeZone: 'Asia/Seoul',
  }).format(new Date(value))
}

export function ProjectDetailPage() {
  const { slug = '' } = useParams()
  const [project, setProject] = useState<ProjectDetail | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [mutationError, setMutationError] = useState('')
  const [inventoryDrafts, setInventoryDrafts] = useState<Record<string, string>>({})
  const [inventoryNotes, setInventoryNotes] = useState<Record<string, string>>({})
  const [stageNotes, setStageNotes] = useState<Record<number, string>>({})
  const [savingMaterial, setSavingMaterial] = useState<string | null>(null)
  const [savingStage, setSavingStage] = useState<number | null>(null)

  const applyProject = useCallback((nextProject: ProjectDetail) => {
    setError('')
    setProject(nextProject)
    setInventoryDrafts(Object.fromEntries(
      nextProject.materials.map((material) => [material.material_key, String(material.owned_quantity)]),
    ))
    setInventoryNotes((current) => Object.fromEntries(
      nextProject.materials.map((material) => [
        material.material_key,
        current[material.material_key] ?? material.inventory_note ?? '',
      ]),
    ))
    setStageNotes(Object.fromEntries(
      nextProject.stages.map((stage) => [stage.id, stage.note ?? '']),
    ))
  }, [])

  const load = useCallback(async () => {
    try {
      applyProject(await api.project(slug))
    } catch (reason) {
      setError((reason as Error).message)
    }
  }, [applyProject, slug])

  useEffect(() => {
    let active = true
    api.project(slug)
      .then((nextProject) => {
        if (active) applyProject(nextProject)
      })
      .catch((reason: Error) => {
        if (active) setError(reason.message)
      })
      .finally(() => {
        if (active) setLoading(false)
      })
    return () => { active = false }
  }, [applyProject, slug])

  const saveInventory = async (material: ProjectMaterial) => {
    const draft = inventoryDrafts[material.material_key] ?? ''
    const quantity = Number(draft)
    if (draft.trim() === '' || !Number.isFinite(quantity) || quantity < 0 || !Number.isInteger(quantity)) {
      setMutationError(`${material.name_ko}: 보유량은 0 이상의 정수로 입력해 주세요.`)
      return
    }
    setMutationError('')
    setSavingMaterial(material.material_key)
    try {
      await api.updateMaterialInventory(
        material.material_key,
        quantity,
        inventoryNotes[material.material_key]?.trim() || null,
      )
      await load()
    } catch (reason) {
      setMutationError((reason as Error).message)
    } finally {
      setSavingMaterial(null)
    }
  }

  const saveStage = async (stage: ProjectStage, completed: boolean) => {
    setMutationError('')
    setSavingStage(stage.id)
    try {
      await api.updateProjectStageState(
        slug,
        stage.id,
        completed,
        stageNotes[stage.id]?.trim() || null,
      )
      await load()
    } catch (reason) {
      setMutationError((reason as Error).message)
    } finally {
      setSavingStage(null)
    }
  }

  if (loading) return <p className="loading">프로젝트를 불러오는 중입니다.</p>
  if (error || !project) {
    return (
      <div>
        <Link className="back-link" to="/projects">← 프로젝트 목록</Link>
        <p className="error" role="alert">{error || '프로젝트를 찾을 수 없습니다.'}</p>
      </div>
    )
  }

  const completedStageCount = project.stages.filter((stage) => stage.completed).length
  const shortageMaterialCount = project.materials.filter((material) => material.shortage > 0).length
  const materialGroups = project.stages
    .map((stage) => ({
      stage,
      materials: project.materials.filter((material) => material.stage_seed_key === stage.seed_key),
    }))
    .filter((group) => group.materials.length > 0)
  const unassignedMaterials = project.materials.filter((material) => material.stage_seed_key === null)

  return (
    <div>
      <Link className="back-link" to="/projects">← 프로젝트 목록</Link>
      <header className="page-header detail-header project-header">
        <div>
          <p className="eyebrow">PROJECT DETAIL</p>
          <h1>{project.name_ko}</h1>
          <p className="subtitle">{project.summary || '프로젝트 설명이 없습니다.'}</p>
        </div>
        {project.content_slug && (
          <Link className="button" to={`/content/${project.content_slug}`}>기존 콘텐츠 상세</Link>
        )}
      </header>

      <div className="project-overview" aria-label="프로젝트 진행 요약">
        <div><strong>{completedStageCount}/{project.stages.length}</strong><span>완료 단계</span></div>
        <div><strong>{shortageMaterialCount}</strong><span>부족 재료 종류</span></div>
      </div>

      {mutationError && <p className="error" role="alert">{mutationError}</p>}

      <section className="detail-section">
        <p className="eyebrow">STAGES</p>
        <h2>진행 단계</h2>
        {project.stages.length === 0 && <p className="empty">등록된 단계가 없습니다.</p>}
        <div className="project-stage-list">
          {project.stages.map((stage) => (
            <article className={stage.completed ? 'project-stage completed' : 'project-stage'} key={stage.seed_key}>
              <div className="project-stage-heading">
                <label>
                  <input
                    type="checkbox"
                    checked={stage.completed}
                    disabled={savingStage === stage.id}
                    onChange={(event) => { void saveStage(stage, event.target.checked) }}
                    aria-label={`${stage.name} 완료`}
                  />
                  <span>{stage.order_no}</span>
                  <strong>{stage.name}</strong>
                </label>
                <span className={stage.completed ? 'project-status ready' : 'project-status pending'}>
                  {stage.completed ? '완료' : '미완료'}
                </span>
              </div>
              {stage.description && <p>{stage.description}</p>}
              {stage.completed_at && <small>완료 시각 {formatCompletedAt(stage.completed_at)}</small>}
              {stage.dependencies.length > 0 && (
                <p className="dependency-note">선행 단계: {stage.dependencies.join(', ')}</p>
              )}
              <div className="stage-note-editor">
                <label>
                  단계 메모
                  <input
                    value={stageNotes[stage.id] ?? ''}
                    onChange={(event) => setStageNotes({ ...stageNotes, [stage.id]: event.target.value })}
                  />
                </label>
                <button
                  className="button"
                  disabled={savingStage === stage.id}
                  onClick={() => { void saveStage(stage, stage.completed) }}
                >
                  {savingStage === stage.id ? '저장 중…' : '메모 저장'}
                </button>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="detail-section">
        <p className="eyebrow">MATERIALS</p>
        <h2>재료 현황</h2>
        {project.materials.length === 0 && <p className="empty">등록된 재료가 없습니다.</p>}
        <div className="material-groups">
          {[
            ...materialGroups,
            ...(unassignedMaterials.length > 0
              ? [{ stage: null, materials: unassignedMaterials }]
              : []),
          ].map((group) => (
            <div className="material-group" key={group.stage?.seed_key ?? 'unassigned'}>
              <h3>{group.stage?.name ?? '공통 재료'}</h3>
              <div className="material-list">
                {group.materials.map((material) => (
                  <article className={material.shortage > 0 ? 'material-card shortage' : 'material-card ready'} key={material.seed_key}>
                    <div className="material-heading">
                      <div>
                        <span className={material.shortage > 0 ? 'project-status shortage' : 'project-status ready'}>
                          {material.shortage > 0 ? '부족' : '충족'}
                        </span>
                        <h4>{material.name_ko}</h4>
                      </div>
                      <span className="material-unit">단위 {material.unit}</span>
                    </div>
                    <div className="material-metrics">
                      <div><span>필요</span><strong>{formatQuantity(material.required_quantity)}</strong></div>
                      <div><span>보유</span><strong>{formatQuantity(material.owned_quantity)}</strong></div>
                      <div><span>부족</span><strong>{formatQuantity(material.shortage)}</strong></div>
                    </div>
                    {material.notes && <p className="material-note">{material.notes}</p>}

                    <div className="inventory-editor">
                      <label>
                        보유량
                        <input
                          type="number"
                          min="0"
                          step="1"
                          inputMode="numeric"
                          aria-label={`${material.name_ko} 보유량`}
                          value={inventoryDrafts[material.material_key] ?? ''}
                          onChange={(event) => setInventoryDrafts({
                            ...inventoryDrafts,
                            [material.material_key]: event.target.value,
                          })}
                        />
                      </label>
                      <label>
                        사용자 메모
                        <input
                          aria-label={`${material.name_ko} 사용자 메모`}
                          value={inventoryNotes[material.material_key] ?? ''}
                          onChange={(event) => setInventoryNotes({
                            ...inventoryNotes,
                            [material.material_key]: event.target.value,
                          })}
                        />
                      </label>
                      <button
                        className="button primary"
                        disabled={savingMaterial === material.material_key}
                        onClick={() => { void saveInventory(material) }}
                      >
                        {savingMaterial === material.material_key ? '저장 중…' : '재고 저장'}
                      </button>
                    </div>

                    <div className="material-sources">
                      <strong>획득처</strong>
                      {material.sources.length === 0 && <p className="empty">연결된 획득처가 없습니다.</p>}
                      {material.sources.map((source) => (
                        <Link to={`/content/${source.content_slug}`} key={source.seed_key}>
                          <span>{source.content_name_ko}</span>
                          <small>
                            {source.quantity_per_completion === null
                              ? '수량 미확인'
                              : `1회 ${formatQuantity(source.quantity_per_completion)}${material.unit}`}
                          </small>
                          {source.notes && <p>{source.notes}</p>}
                        </Link>
                      ))}
                    </div>
                  </article>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}
