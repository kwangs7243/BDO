# V1.9K — Guild Boss Current System & Weekly Raid Closure

## 결과

- Source: 177 → 180
- Content: 274 → 280 active
- FACT: 220 → 250
- STRATEGY: 63 유지
- MEASUREMENT: 11 유지
- Relation: 490 → 500
- schema / migration / frontend 기능 변경 없음
- 실제 backend/bdo.db 변경 없음

## 구현 범위

guild-boss-current-system 공통 허브와 기존 khan-guild-boss stable Content 제자리 갱신, 오르그·모굴리스·페리드·거대한 진흙 괴물·길드 명성 구미호/두억시니 FACT를 반영했다. 소환 권한, 전용 레이드 지역, 입장 제한, 월요일 00:00 횟수·조각 reset과 표준 우두머리별 기본 1회/명성 재충전 1회를 분리했다.

## Source와 경계

신규 공식 Source는 현행 가이드, 2026-01-07 전용 레이드 개편, 2019-12-04 월요일 reset 패치다. 기존 2026-08-05 전체 업데이트 Source는 ID와 URL을 유지한 채 domain-neutral title로 정규화해 길드 명성 Evidence에 재사용했다. 2026-08-12 명성 2인조, 2026-06-17 모굴리스 패치도 기존 Source를 재사용했다.

표준 우두머리는 기본 주 1회와 우두머리별 명성 재충전 주 1회가 별도다. 단일 boolean checklist는 추가 소환 가능성을 숨겨 생성하지 않았다. 명성 2인조의 정확한 reset 시각은 별도 공식 명시가 없어 Schedule을 만들지 않았다.

## 보존과 제외

- 기존 Khan 및 nested stable seed_key 유지
- 고대의 푸투룸은 현행 명단 제외 사실만 기록하고 archive/delete하지 않음
- 사용자 길드 상태, 명성 재고, 길드 권한 모델 없음
- 동적 확률·수익·전투 최적화 전략 없음
- schema, migration, UI, Prompt mode 변경 없음

## 검증

- V1.9K + V1.9J 지정 회귀: 13 passed
- 전체 backend: 316 passed
- frontend: 14 files / 57 tests passed
- frontend typecheck: passed
- frontend lint: passed
- frontend build: passed
- `git diff --check`: passed
- historical V1.9J → V1.9K 임시 DB import: passed
- 동일 seed 2회 reimport: passed
- Khan Content stable ID 보존: passed
- Khan nested stable IDs 보존: passed
- `UserContentState` history 보존: passed
- 실제 `backend/bdo.db` 변경 없음
- DB SHA-256 전후 동일: `E9EB175F1069B3A93B64181623A79CAE9FFBEE22F46FD7A706DD041DA34148A5`
