import { useState } from 'react'
import { api } from '../../api'
import type {
  UserBackup,
  UserBackupImportResult,
  UserBackupValidation,
} from '../../types'

type ImportMode = 'merge' | 'replace'

function downloadBackup(backup: UserBackup) {
  const blob = new Blob([JSON.stringify(backup, null, 2)], {
    type: 'application/json',
  })
  const url = URL.createObjectURL(blob)
  const anchor = document.createElement('a')
  anchor.href = url
  anchor.download = `bdo-companion-backup-${backup.exported_at.slice(0, 10)}.json`
  anchor.click()
  URL.revokeObjectURL(url)
}

export function SettingsPage() {
  const [backup, setBackup] = useState<unknown | null>(null)
  const [report, setReport] = useState<UserBackupValidation | null>(null)
  const [mode, setMode] = useState<ImportMode>('merge')
  const [replaceConfirmed, setReplaceConfirmed] = useState(false)
  const [result, setResult] = useState<UserBackupImportResult | null>(null)
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)

  async function exportBackup() {
    setBusy(true)
    setError('')
    setMessage('')
    try {
      const exported = await api.exportUserBackup()
      downloadBackup(exported)
      setMessage('사용자 데이터 백업을 다운로드했습니다.')
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : '백업 다운로드에 실패했습니다.')
    } finally {
      setBusy(false)
    }
  }

  async function selectFile(file: File | undefined) {
    setBackup(null)
    setReport(null)
    setResult(null)
    setError('')
    setMessage('')
    setReplaceConfirmed(false)
    if (!file) return
    try {
      const parsed: unknown = JSON.parse(await file.text())
      setBackup(parsed)
      const validation = await api.validateUserBackup(parsed)
      setReport(validation)
    } catch (reason) {
      setError(
        reason instanceof SyntaxError
          ? '올바른 JSON 백업 파일이 아닙니다.'
          : reason instanceof Error
            ? reason.message
            : '백업 파일을 읽지 못했습니다.',
      )
    }
  }

  async function restoreBackup() {
    if (!backup || !report?.valid || (mode === 'replace' && !replaceConfirmed)) return
    setBusy(true)
    setError('')
    setMessage('')
    setResult(null)
    try {
      const imported = await api.importUserBackup(backup, mode)
      setResult(imported)
      setMessage(mode === 'merge' ? '백업을 병합했습니다.' : '백업 내용으로 전체 복원했습니다.')
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : '백업 복원에 실패했습니다.')
    } finally {
      setBusy(false)
    }
  }

  const importDisabled = (
    busy
    || !backup
    || !report?.valid
    || (mode === 'replace' && !replaceConfirmed)
  )

  return (
    <div>
      <header className="page-header hero settings-hero">
        <div>
          <p className="eyebrow">LOCAL BACKUP</p>
          <h1>설정과 <em>사용자 데이터 백업</em></h1>
          <p className="subtitle">
            진행 상태, 체크 기록, 재료 재고와 프로젝트 단계 상태만 JSON으로 보관합니다.
          </p>
        </div>
      </header>

      {error && <p className="error" role="alert">{error}</p>}
      {message && <p className="success" role="status">{message}</p>}

      <section className="settings-panel">
        <p className="eyebrow">EXPORT</p>
        <h2>사용자 데이터 백업</h2>
        <p>
          canonical 게임 정보와 출처는 포함하지 않습니다. 이 PC에 저장된 내 진행 상태,
          전체 체크 기록, 재고와 프로젝트 단계 상태를 로컬 JSON 파일로 다운로드합니다.
        </p>
        <button className="button primary" onClick={exportBackup} disabled={busy}>
          JSON 백업 다운로드
        </button>
      </section>

      <section className="settings-panel">
        <p className="eyebrow">RESTORE</p>
        <h2>백업 검증과 복원</h2>
        <label className="backup-file">
          JSON 백업 파일
          <input
            type="file"
            accept="application/json,.json"
            onChange={(event) => void selectFile(event.target.files?.[0])}
            disabled={busy}
          />
        </label>

        {report && (
          <div className={report.valid ? 'validation-report valid' : 'validation-report invalid'}>
            <h3>{report.valid ? '복원 가능한 백업입니다.' : '백업을 복원할 수 없습니다.'}</h3>
            <dl className="backup-counts">
              <div><dt>콘텐츠 상태</dt><dd>{report.content_states}개</dd></div>
              <div><dt>체크리스트 기간</dt><dd>{report.checklist_instances}개</dd></div>
              <div><dt>체크 상태</dt><dd>{report.checklist_items}개</dd></div>
              <div><dt>재료 재고</dt><dd>{report.material_inventory}개</dd></div>
              <div><dt>프로젝트 단계</dt><dd>{report.project_stage_states}개</dd></div>
            </dl>
            {report.errors.length > 0 && (
              <div>
                <strong>오류</strong>
                <ul>{report.errors.map((item) => <li key={item}>{item}</li>)}</ul>
              </div>
            )}
            {report.warnings.length > 0 && (
              <div>
                <strong>경고</strong>
                <ul>{report.warnings.map((item) => <li key={item}>{item}</li>)}</ul>
              </div>
            )}
          </div>
        )}

        <fieldset className="backup-mode" disabled={!report?.valid || busy}>
          <legend>복원 방식</legend>
          <label>
            <input
              type="radio"
              name="backup-mode"
              checked={mode === 'merge'}
              onChange={() => {
                setMode('merge')
                setReplaceConfirmed(false)
              }}
            />
            <span><strong>병합</strong> — 백업에 없는 현재 상태는 유지합니다.</span>
          </label>
          <label>
            <input
              type="radio"
              name="backup-mode"
              checked={mode === 'replace'}
              onChange={() => setMode('replace')}
            />
            <span><strong>전체 복원</strong> — 현재 사용자 데이터를 백업 내용으로 교체합니다.</span>
          </label>
        </fieldset>

        {mode === 'replace' && (
          <label className="replace-confirm">
            <input
              type="checkbox"
              checked={replaceConfirmed}
              onChange={(event) => setReplaceConfirmed(event.target.checked)}
              disabled={!report?.valid || busy}
            />
            기존 사용자 진행 상태와 체크리스트 기록을 백업 내용으로 교체합니다.
          </label>
        )}

        <button
          className="button primary"
          onClick={restoreBackup}
          disabled={importDisabled}
        >
          {mode === 'merge' ? '백업 병합' : '전체 복원 실행'}
        </button>

        {result && (
          <div className="import-result" role="status">
            <h3>복원 결과</h3>
            <ul>
              <li>콘텐츠 상태 {result.content_states_upserted}개</li>
              <li>체크리스트 기간 {result.checklist_instances_upserted}개</li>
              <li>체크 상태 {result.checklist_items_upserted}개</li>
              <li>재료 재고 {result.material_inventory_upserted}개</li>
              <li>프로젝트 단계 {result.project_stage_states_upserted}개</li>
            </ul>
            {result.mode === 'replace' && (
              <p>
                교체 전 제거: 콘텐츠 상태 {result.deleted_counts.content_states}개,
                체크리스트 기간 {result.deleted_counts.checklist_instances}개,
                체크 상태 {result.deleted_counts.checklist_items}개,
                재료 재고 {result.deleted_counts.material_inventory}개,
                프로젝트 단계 {result.deleted_counts.project_stage_states}개
              </p>
            )}
          </div>
        )}
      </section>
    </div>
  )
}
