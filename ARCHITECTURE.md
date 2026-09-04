# Architecture

## Data flow

```text
KR 공식 가이드 / 패치 / GM노트
        │
        ▼
Research Staging
(raw source + extracted claims + unresolved conflicts)
        │ 검증
        ▼
Canonical Knowledge DB
(content / requirements / steps / schedules / rewards / evidence)
        │
        ├──────────────► Search / Content pages
        │
        ▼
User State DB
(checklist instances / progress / materials / notes / characters)
        │
        ▼
Dashboard / Today / Weekly / Projects / Life
        │
        └──────────────► Prompt Context Builder
                          │
                          ▼
                    Markdown Prompt
                    (copy/download only)
```

## Frontend

- React + TypeScript + Vite
- route-level code splitting
- feature folders:
  - `features/dashboard`
  - `features/content`
  - `features/checklists`
  - `features/projects`
  - `features/life`
  - `features/sources`
- API client는 UI 컴포넌트와 분리

## Backend

FastAPI modules:
- `content`: canonical knowledge
- `schedule`: period/reset computation
- `checklist`: template/instance/state
- `project`: stage/material/inventory
- `user`: local preferences and notes
- `research`: source/evidence/admin tools
- `search`: unified index
- `prompt_bridge`: deterministic context selection + Markdown prompt rendering (V1.5, no LLM call)

## Database strategy

`.env`:
- SQLite: `DATABASE_URL=sqlite:///./bdo.db`
- MySQL: `DATABASE_URL=mysql+pymysql://USER:PASSWORD@127.0.0.1/bdo_companion?charset=utf8mb4`

MySQL이 설치되어 있어도 앱 자체는 SQLite로 바로 부팅 가능해야 한다. 사용자가 MySQL을 원하면 migration 후 동일 API로 전환한다.

## Reset engine

배경 작업이 매일 checkbox를 지우지 않는다.

`get_current_period(rule, now_kst)` → `{period_key, start, end}`

현재 period의 checklist instance가 없으면 생성하고, 있으면 재사용한다. 이 구조는 앱을 일주일 꺼두어도 기록이 꼬이지 않는다.

### Different clocks
- Daily task window
- Thursday weekly quest window
- Sunday reward payout
- Boss spawn schedule
- Event fixed deadline

이들은 모두 다른 `schedule_rule` row다.

## Knowledge freshness

Canonical entity 자체에 단일 source URL을 박지 않는다. `evidence`가 claim 단위로 source와 연결된다.

예:
- claim `weekly_reset = Thu 00:00` → official patch evidence
- claim `reward_payout = Sun 00:00` → current guide evidence
- claim `easy_strategy = ...` → community consensus evidence

UI는 authoritative claim과 community tip을 시각적으로 구분한다.

## Data update philosophy

앱 런타임에서 공식 사이트 scraping을 필수로 하지 않는다.
대신 별도 research command/importer가 source snapshot을 만들고, 검증 후 canonical seed/update migration을 생성한다.


## V1.5 Prompt Bridge architecture

```text
User question + current page
        │
        ▼
Context Resolver
  ├─ canonical content
  ├─ schedules
  ├─ user progress/checklists
  ├─ project shortages
  └─ evidence / unresolved claims
        │
        ▼
Context Budgeter
(verified first, duplicates removed)
        │
        ▼
Prompt Renderer
(next_action / onboarding / optimizer / weekly / verify)
        │
        ▼
Preview → Clipboard / .md
```

V1.5에는 outbound LLM transport layer가 존재하지 않는다. 향후 V2에서 추가하더라도 `PromptContextBundle` 계약 뒤에 adapter로 붙여 core retrieval을 변경하지 않는 것을 목표로 한다.
