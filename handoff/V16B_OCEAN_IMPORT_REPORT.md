# V1.6B Ocean Seed Import Report

검증일: 2026-09-03 KST

## 1. 적용 범위

Ocean Seed Pack의 완전 병합 canonical 파일 두 개만 프로젝트에 반영했다.

- BDO_V16B_OCEAN_SEED_PACK/data/seed_sources.json → data/seed_sources.json
- BDO_V16B_OCEAN_SEED_PACK/data/seed_contents.json → data/seed_contents.json

코드, DB schema, migration, API, UI, 디자인, Prompt Bridge/AI 기능은 변경하지 않았다. 실제 사용자 backend/bdo.db에는 migration이나 seed import를 실행하지 않았다.

적용 파일 SHA-256:

- seed_sources.json: C145552DD81C379A079723EDCF8DA00702E4B3552A914B3948E6061A3FBB2DCF
- seed_contents.json: DE24914A2666FC9B6896AC25675C9BD20DE3001B6257F8A781D5C4AC3F177451

## 2. Canonical 데이터 결과

- Source: 기존 15 → 현재 23
- Content: 기존 7 → 현재 27
- 신규 Source: 8
- 신규 Ocean Content: 20
- 기본 필드가 갱신된 기존 Content: carrack-advance 1
- 제거된 Source/Content: 0

현재 seed 선언/DB active row 합계:

| 종류 | 현재 수 |
|---|---:|
| Content | 27 |
| Source | 23 |
| ScheduleRule | 26 |
| ContentRequirement | 22 |
| ContentStep | 30 |
| Reward | 61 |
| ContentSection | 24 |
| ContentRelation | 20 |
| ChecklistTemplate | 22 |
| ChecklistTemplateItem | 22 |
| Evidence claim 선언 | 234 |
| Evidence source 연결 DB 행 | 343 |

## 3. 이전 V1.6A 대비 신규/갱신/제거

아래 갱신은 동일 stable seed_key에서 값이 변경된 건수다. 제거는 import 시 archive 후보가 되는 canonical key 수다.

| 종류 | 신규 | 갱신 | 제거 |
|---|---:|---:|---:|
| Source | 8 | 0 | 0 |
| Content 기본 필드 | 20 | 1 | 0 |
| Requirement | 20 | 1 | 0 |
| Section | 19 | 1 | 0 |
| Step | 28 | 1 | 0 |
| Reward | 60 | 0 | 0 |
| Schedule | 23 | 0 | 0 |
| Checklist template | 18 | 0 | 0 |
| Checklist item | 18 | 0 | 0 |
| Relation | 19 | 0 | 0 |
| Evidence claim 선언 | 211 | 5 | 0 |

동일 key에서 갱신된 중첩 행은 모두 carrack-advance 범위다.

- carrack-advance.starting-ship
- carrack-advance.why
- carrack-advance.confirm-upgrade-path
- carrack-advance의 기존 evidence claim 5개

기존 carrack-advance stable seed_key 누락은 0개다. 이전 V1.6A DB를 구성한 뒤 Ocean seed로 갱신한 검사에서 기존 carrack 구조화/evidence DB 행 8개의 ID가 모두 유지됐다.

## 4. JSON/참조 validation

통과 항목:

- seed_sources.json JSON parse
- seed_contents.json JSON parse
- Source id 중복 없음
- Content slug 중복 없음
- nested seed_key의 content slug prefix 확인
- Evidence가 참조하는 unknown source: 0
- Relation이 참조하는 unknown content: 0
- Evidence가 참조하는 unknown entity seed_key: 0
- 현재 importer의 enum/구조 validation 통과
- fresh in-memory SQLite import 통과

Evidence 분포:

- claim 선언: 234
- source 연결: 343
- entity type: content, content_requirement, content_section, content_step, reward, schedule_rule, content_relation

## 5. Migration 및 실제 DB 임시 복사 검증

원본 backend/bdo.db 확인값:

- Alembic revision: 20260902_0001
- Content: 7
- ChecklistInstance: 4
- ChecklistItemState: 4
- UserContentState: 0

원본 파일은 수정하지 않고 임시 복사본에서 다음 순서로 검증했다.

1. Alembic 20260902_0001 → 20260903_0002 migration
2. V1.6B canonical seed 첫 import
3. 동일 seed 두 번째 import
4. canonical row count, 기존 checklist history, archive 상태 비교
5. 임시 DB 삭제

결과:

- migration revision: 20260903_0002
- 첫/두 번째 import의 모든 canonical 테이블 count 동일
- 기존 ChecklistInstance 4개 보존
- 기존 ChecklistItemState 4개 ID/완료값/메모 보존
- Source 23, Content 27, Evidence 343
- 예상치 못한 active=false archive: 모든 seed 관리 테이블에서 0

## 6. V1.6A 개인 상태/이력 회귀 검증

별도 임시 DB에서 이전 V1.6A seed를 먼저 import하고 다음 테스트 데이터를 만들었다.

- 현재 주간 checklist instance/state 4개
- 완료 상태와 history marker 1개
- carrack-advance UserContentState 1개

그 후 Ocean seed를 두 번 import했다.

결과:

- checklist state 4개 보존
- 완료값/history marker 보존
- UserContentState state/priority/note 보존
- 기존 carrack stable row ID 보존
- 두 번째 import 후 row count 동일
- archive 0

UserContentState는 seed importer 입력 대상이 아니므로 신규 pack이 사용자 상태를 덮어쓰지 않았다.

## 7. 테스트 결과

실행 결과:

- JSON parse: 통과
- pack 자체 fresh import + 2회 idempotence: 통과
- backend seed test: 4 passed
- backend 전체 test: 28 passed
- 실제 DB 임시 복사 migration/import/idempotence: 통과
- 이전 V1.6A seed → Ocean seed history/UserContentState 회귀: 통과

프런트엔드와 기능 코드는 변경하지 않아 별도 UI build 변경 검증은 수행하지 않았다.

## 8. 오류 및 schema gap

Blocking 오류는 없다. 현재 V1.6A schema/importer로 Ocean Seed Pack 전체가 import됐다.

확인된 비차단 범위:

- project/material 전용 모델은 여전히 없으며 이번 import에서 추가하지 않았다.
- 다중 출현 시각용 새 schedule schema나 RRULE 엔진을 추가하지 않았다.
- 실제 사용자 backend/bdo.db는 현재도 원래 revision/데이터 상태이며, 별도 승인 전에는 Ocean seed가 적용되지 않는다.
- pack의 게임 데이터 내용은 전달본을 그대로 반영했으며 일반 지식으로 수량·보상·일정을 보정하지 않았다.

