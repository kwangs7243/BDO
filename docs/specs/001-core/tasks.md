# Tasks — first implementation milestone

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
- [ ] Project/material tables
- [ ] Migrate Carrack Advance data
- [ ] Carrack detail with stage checklist and shortages
- [ ] Weekly reset groups
- [ ] Sunday payout group
- [ ] Life hub + Gathering/Fishing/Sailing seed pages
- [ ] JSON export/import

## Milestone C: broad catalog
- [ ] Blood Altar
- [ ] Black Shrine variants (verify current rules before seed)
- [ ] Pit of Undying
- [ ] Atoraxxion regions
- [ ] Last Gladiius
- [ ] Garmoth/Vell
- [ ] Dark Rift (non-weekly recurring)
- [ ] guild bosses
- [ ] adventure logs
- [ ] Magnus
- [ ] fairy/pets/workers/nodes
- [ ] remaining life skills

## Definition of done for any content seed
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
- [ ] Carrack project에서 current materials + shortages + recurring status prompt 생성
- [x] Weekly page에서 남은 숙제 + reset/deadline prompt 생성
- [x] `verified`/`needs_review`/`conflict` 분리 검증
