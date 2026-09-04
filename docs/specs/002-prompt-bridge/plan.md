# Implementation Plan — Prompt Bridge V1.5

## Phase PB-0 Contract first
- `PromptContextBundle` Pydantic schema 정의
- prompt mode enum 정의
- context serializer snapshot test 작성
- no-network invariant test 작성

## Phase PB-1 Backend context builder
- current content/project/checklist/user state 조회
- verified evidence 정렬
- unresolved claims 분리
- size budget 적용
- `/api/prompt/context` endpoint
- `/api/prompt/render` endpoint

## Phase PB-2 Frontend
- `PromptBridgeDrawer`
- preset selector
- context section toggles
- user question textarea
- preview
- copy/download
- size estimate badge

## Phase PB-3 Entry points
- content detail
- project detail
- today/weekly
- life detail
- global prompt page

## Phase PB-4 Quality
- project optimizer fixture: Carrack Advance
- content onboarding fixture: Sailing/Barter
- weekly review fixture
- conflict fixture
- clipboard fallback test
