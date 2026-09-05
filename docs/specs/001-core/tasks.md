# Tasks — first implementation milestone

> V1.8D 완료 상태를 기준으로 현재 코드, seed, 테스트와 handoff에서 확인된 구현만 반영했다. 미완료 복합 항목에는 부분 구현 범위를 덧붙였으며, 이 문서는 다음 milestone 로드맵을 정의하지 않는다.

## Milestone A: working vertical slice

- [x] Create `frontend/` React+TS+Vite
- [x] Create `backend/` FastAPI
- [x] Add SQLAlchemy + Alembic
- [x] Implement DB URL switch (SQLite/MySQL)
- [x] Implement `/api/health`
- [x] Implement source/content/schedule/checklist tables
- [x] Implement period-key calculator
- [x] Tests: daily KST and Thursday weekly
- [x] Import `data/seed_sources.json`
- [x] Import `data/seed_contents.json`
- [x] API: list content, content detail, current checklist
- [x] UI: Dashboard / Content explorer / Content detail
- [x] UI: source badge with last verified
- [x] UI: checklist state persistence

## Milestone B: user value
- [x] Project/material tables — V1.8A backend foundation과 사용자 재고/단계 상태 분리 구현
- [x] Migrate Carrack Advance data — 검증된 기존 Content 요구량을 `seed_projects.json`의 normalized projection으로 연결
- [x] Carrack detail with stage checklist and shortages — V1.8B generic Project 목록·상세, 재고 저장, stage 완료/해제와 backend shortage 표시 구현
- [x] Weekly reset groups
- [x] Sunday payout group
- [ ] Life hub + Gathering/Fishing/Sailing seed pages — V1.6 해양·생활 seed는 반영되었으나 전용 Life hub 화면은 미구현
- [ ] JSON export/import

## Milestone C: broad catalog
- [x] Blood Altar
- [x] Black Shrine variants (current rules verified in V1.7C seed)
- [x] Pit of Undying
- [x] Atoraxxion regions
- [ ] Last Gladiius
- [x] Garmoth/Vell
- [x] Dark Rift (non-weekly recurring)
- [ ] guild bosses — Khan seed는 반영되었으나 길드 우두머리 전체 범위 완료 근거는 없음
- [ ] adventure logs — V1.7D에서 Foundation과 이고르 바탈리·마가한의 서 대표 데이터는 구현했으나 전체 Adventure Log Deep Pack은 미완료
- [ ] Magnus — V1.7D에서 progression foundation과 주요 checkpoint는 구현했으나 퍼즐·지역별 상세를 포함한 Deep Pack은 미완료
- [ ] fairy/pets/workers/nodes — workers/nodes는 V1.6I에 반영되었으나 fairy/pets는 미완료
- [ ] remaining life skills — V1.6F-H 생활 심화 seed는 반영되었으나 전체 생활 범위 완료로 정의되지 않음

## Definition of done for any content seed

아래 항목은 프로젝트 전체 완료 현황이 아니라 새 Content/seed를 추가할 때마다 적용하는 검수 체크리스트다.
- [ ] summary/purpose
- [ ] prerequisites
- [ ] first-time steps
- [ ] repeat rules if applicable
- [ ] rewards
- [ ] at least one source
- [ ] critical reset/reward claims officially sourced
- [ ] last_verified_at
- [ ] no unresolved conflict exposed as fact


## Milestone V1.5: ChatGPT Prompt Bridge
- [ ] Implement `docs/specs/002-prompt-bridge/tasks.md`
- [x] No API key / LLM SDK dependency
- [x] Content detail에서 onboarding prompt 생성
- [x] Carrack project에서 current materials + shortages + recurring status prompt 생성 — V1.8C에서 stage/inventory 메모, 관련 checklist·schedule·evidence 포함
- [x] Weekly page에서 남은 숙제 + reset/deadline prompt 생성
- [x] Dashboard 전체 또는 선택한 Content/Project에서 현재 상태 기반 `next_action` prompt 생성
- [x] Content/Project의 verified 기준 정보와 unresolved claim을 분리한 `verify_latest` prompt 생성
- [x] 5개 preset과 weekly review golden snapshot
- [x] `verified`/`needs_review`/`conflict` 분리 검증
