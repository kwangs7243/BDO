# Codex Import Instruction — V1.6B Ocean Seed Pack

프로젝트의 기존 V1.6A 구현과 `AGENTS.md`, `docs/data/SEED_FORMAT.md`를 먼저 읽는다.

이 패키지의:

- `data/seed_sources.json`
- `data/seed_contents.json`

은 **부분 diff가 아니라 기존 seed를 포함한 완전한 merged canonical 파일**이다. 두 파일을 프로젝트의 동일 경로에 반영한다.

## 작업 범위

1. 두 JSON을 프로젝트 `data/`에 반영한다.
2. 코드/스키마/UI를 임의로 변경하지 않는다.
3. JSON parse 및 현재 seed validator/importer 테스트를 실행한다.
4. 실제 사용자 `backend/bdo.db`는 직접 변경하지 말고, 임시 SQLite DB 복사본 또는 테스트 DB에서 migration + seed import를 검증한다.
5. idempotence: 같은 seed를 2회 import했을 때 중복 canonical row가 생기지 않는지 확인한다.
6. 기존 V1.5/V1.6A checklist instance/UserContentState가 보존되는지 가능한 범위에서 회귀 테스트한다.
7. `carrack-advance`의 기존 stable seed_key가 유지되었는지 확인한다.
8. 신규 content 개수, archive된 row가 예상치 않게 발생했는지, evidence unknown source가 없는지 보고한다.

## 하지 말 것

- 데이터 내용을 일반 지식으로 임의 수정하지 않는다.
- 디자인 개편 금지.
- 프로젝트/재료 새 모델 추가 금지.
- API/LLM 추가 금지.
- 출처가 없는 수량 보정 금지.

## 완료 보고

`handoff/V16B_OCEAN_IMPORT_REPORT.md`를 만들고:

- validation/test 결과
- contents/source 총 개수
- 신규/갱신/archived 건수
- migration/seed import 결과
- 오류 또는 schema gap

을 기록한다.
