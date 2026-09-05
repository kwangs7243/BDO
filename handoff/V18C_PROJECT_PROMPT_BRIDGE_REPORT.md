# V1.8C — Project Prompt Bridge 완료 보고

기준일: 2026-09-05
브랜치: `feature/v1.8c-project-prompt`

## 완료 범위

- `project_optimizer` Prompt mode와 `project_slug` 요청 계약을 추가했다.
- Project Prompt는 기존 `get_project_detail` 응답의 stage, material, owned quantity, shortage, inventory note를 그대로 사용한다.
- Carrack Advance의 4개 stage와 9개 material을 결정적 순서로 `PROJECT_STATE`에 직렬화한다.
- stage 완료 상태·완료 시각·메모·dependency와 material required/owned/shortage·재고 메모를 포함한다.
- Project에 직접 연결된 Content와 material acquisition Content를 중복 없이 수집한다.
- 관련 Content의 현재 daily/weekly checklist만 Content 이름과 실제 완료 상태를 붙여 포함한다.
- acquisition Content의 canonical schedule만 verification 상태와 함께 포함한다.
- material lineage는 `content_requirement → description`, `content_section → body` claim으로 evidence를 매핑한다.
- 수량이 알려진 acquisition source는 material 이름과 amount가 일치하는 Reward의 `reward` evidence를 사용한다.
- 수량이 없는 acquisition source는 값을 만들지 않고 `확인되지 않음`으로 직렬화한다.
- verified가 아닌 claim은 `OPEN_QUESTIONS_OR_CONFLICTS`로 분리한다.
- source는 `evidence_id` 기준으로 중복 제거하고 기존 current/historical 의미를 보존한다.
- Project Detail과 전역 Prompt 화면에서 project prompt dialog를 열 수 있다.
- 전역 Prompt 화면의 Project 목록은 `GET /api/projects` 결과를 사용하며 특정 project를 하드코딩하지 않는다.
- 기존 content onboarding과 weekly review 계약을 유지한다.
- 외부 LLM/API/network 호출을 추가하지 않았다.

## API 계약

`POST /api/prompt/context`와 `POST /api/prompt/render`는 다음 요청을 지원한다.

```json
{
  "mode": "project_optimizer",
  "project_slug": "carrack-advance",
  "user_question": "이번 주 안에 최대한 빨리 끝내는 순서를 짜줘",
  "as_of": "2026-09-02T23:00:00+09:00"
}
```

- `project_slug` 누락: 422
- 존재하지 않는 project: 404 `Project not found`
- schema, migration, seed 형식 변경: 없음

## Evidence와 필터링

- Project material의 required quantity는 Project seed가 가리키는 기존 Requirement/Section claim evidence로 분류한다.
- acquisition quantity는 source Content의 실제 Reward와 이름·amount가 일치할 때만 해당 Reward evidence로 분류한다.
- evidence가 없거나 verified가 아니면 verified FACT로 승격하지 않는다.
- checklist는 Project 연결/acquisition Content 범위로 제한한다.
- schedule은 acquisition Content 범위로 제한한다.
- source 목록은 관련 Content에서 가져온 evidence를 deterministic key로 정렬하고 `evidence_id`로 deduplicate한다.

## UI

- Project Detail: `이 프로젝트를 ChatGPT에 물어보기` 버튼 추가
- 전역 Prompt 화면: API 기반 Project selector와 `프로젝트 프롬프트 만들기` launcher 추가
- Project 질문 placeholder: `이번 주 안에 최대한 빨리 끝내는 순서를 짜줘`
- 기존 Markdown preview, copy, download, 문자/token 추정 UI 재사용
- Project가 없으면 안내 문구를 표시하고 launcher를 비활성화

## 테스트

### Backend

- project slug 누락 422 / unknown project 404
- 동일 상태·동일 시각의 deterministic Markdown
- Carrack Advance 4 stages / 9 materials
- Project Detail에서 받은 shortage 사용
- inventory note와 stage completion/note 반영
- 알려진 획득 수량의 Reward evidence 연결
- conflict lineage의 unresolved 분리
- 관련 checklist 필터와 실제 완료/미완료 상태
- source `evidence_id` 중복 제거
- outbound network 호출 없음
- golden snapshot: `backend/tests/golden/carrack_project_optimizer.md`

결과: `167 passed` (warning 1건: TestClient의 upstream deprecation 안내)

### Frontend

- Project Detail button/dialog/request/preview
- project 전용 placeholder
- 전역 Project selector와 선택한 slug 전달
- 빈 Project 목록 처리
- project API POST body와 `as_of`
- 기존 content onboarding / weekly review 계약 회귀

결과: `8 files, 21 passed`

추가 검증:

- frontend typecheck: 통과
- frontend lint: 통과
- frontend production build: 통과
- `git diff --check`: 통과

## DB 및 변경 금지 영역

- 작업 전 `backend/bdo.db` SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 작업 후 `backend/bdo.db` SHA-256:
  `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
- 동일 여부: 동일
- seed, migration, DB schema, 실제 SQLite DB 변경: 없음

## V1.8C 범위 밖의 기존 미완료 항목

- `next_action`, `verify_latest`를 포함한 5개 preset 전체
- size budget 초과 시 자동 truncation 정책
- context-only/full prompt 선택
- weekly review golden snapshot

위 항목은 기존 Prompt Bridge 계획에 남아 있으며 V1.8C 완료로 과장하지 않았다.
