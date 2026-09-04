# V1.7B Grind Spot Deep Pack 검증 보고서

기준 시점: 2026-09-04 (KR, Asia/Seoul)

## 결과 요약

V1.7A 데이터 구조를 변경하지 않고 V1.7B 사냥터 데이터 팩을 반영했다. 공식 수치인 FACT, 시점 의존 공략인 STRATEGY, 개별 관측인 MEASUREMENT를 `structured_value.knowledge_role`로 분리했다. 실제 `backend/bdo.db`에는 migration이나 seed import를 실행하지 않았으며 모든 적재 검증은 임시 SQLite DB에서 수행했다.

| 항목 | V1.7A 기준 | V1.7B 이후 |
| --- | ---: | ---: |
| Source | 112 | 128 |
| Content | 166 | 192 |
| V1.7B 공식 사냥터 Content | - | 25 |
| V1.7B 시스템 Content | - | 1 |
| V1.7B FACT requirement | - | 55 |
| V1.7B STRATEGY requirement | - | 8 |
| V1.7B MEASUREMENT requirement | - | 11 |
| 명시적 AP cap | - | 13 |

전역 총량은 보고용 snapshot일 뿐 테스트의 고정 equality 조건으로 사용하지 않는다.

## 반영 범위

### 중상위 및 2026 사냥터

- 헥세 성역, 이스라히드 고원, 죽은 자들의 도시, 툰그라드 유적지
- 도깨비숲, 어둠 추종자 침소
- 금돼지굴, 행운의 금돼지굴
- 데키아 II 올룬의 계곡, 데키아 II 잿빛 숲
- 데키아 미루목 유적지, 데키아 가이핀라시아 사원 지상
- 검은 기운 범람지, 가비냐 해안 절벽
- 에다니아 외부: 아에테리온 → 님파마레 → 오르비타 → 테네브라움 → 제피로스
- 에다니아 내부: 아프로돈, 에메시아, 마가이아, 아레시온, 심판의 천칭, 사건의 지평선
- 시스템: 마르니의 전투 분석기

에다니아 내부의 최종 공격력 권장값은 명시적 AP cap으로 승격하지 않았다. 외부 사냥터 중 공식 페이지에서 이번 검수 중 직접 확인한 아에테리온·님파마레·오르비타의 표기 권장치만 구조화했고, 테네브라움·제피로스의 미확인 수치는 추정하지 않았다.

## 공식 FACT와 패치 override

현재 cap은 헥세 1130, 이스라히드 1180, 죽은 자들의 도시 1295, 툰그라드 1395, 도깨비숲 1445, 침소 1490, 금돼지굴 1540, 데키아 II 올룬 1490, 데키아 II 잿빛 숲 1540, 데키아 미루목 1595, 데키아 가이핀 지상 1680, 검은 기운 범람지 1880, 가비냐 2020으로 저장했다.

2026-06-10 최신 조정은 다음과 같이 current FACT로 반영했다.

- 이스라히드 동력이 넘치는 킬라르: 잡동사니 200~240, 아그리스 264
- 죽은 자들의 도시: 주요 전령/정예 잡동사니 4~6, 지휘관 220~250, 주요 아그리스 9
- 죽은 자들의 도시: 포식의 정수 획득 확률 +20%, 카부아 유물/파편 추가

사건의 지평선은 2026-09-02 값을 current로 유지한다.

- 잡동사니 수량: 기본 2~4, 절망의 인도자 4~8, 이베도르 25~35, 특수 유실물 30~35
- 아그리스: 기본 18, 절망의 인도자 36, 이베도르 180, 특수 유실물 198
- 잡동사니: 부서진 공허의 장갑, 196,501 은화, 0.3 LT

출시 값은 `event-horizon.legacy-launch-values`로 비활성 보존하고 Evidence를 `superseded` 처리했다.

## Strategy source

날짜가 있는 커뮤니티 자료 4건을 별도 `community_strategy` Source로 추가했다.

- `hexe-pet-bottleneck-2026-07-17`
- `hexe-economy-discussion-2026-08-10`
- `orzekea-dsr-tungrad-2026-06-11`
- `silver-at-1600ap-2026-08-14`

헥세의 광역/이동/펫/밀실/숙련도 편차, 툰그라드의 팩 위치·회수 시점, 침소의 이벤트 편차, 시간당 은화의 시장가격 의존성을 FACT와 분리했다.

## Measurement 구성

| 구분 | 수 |
| --- | ---: |
| Grade A | 4 |
| Grade B | 7 |
| Grade C | 0 |
| 직업 명시 | 5 |
| 직업 미상 | 6 |
| current patch context | 10 |
| pre-balance/historical context | 1 |

모든 측정은 개별 세션 또는 한 작성자의 제한된 비교로 저장했다. 평균값으로 합치지 않았고, FACT requirement에는 `measurement_grade`가 존재하지 않는다. 헥세 18,000, 툰그라드 30,000~35,000, 침소 40,000+ 같은 값은 공식 기대치가 아니라 날짜·직업·Agris·주문서·시간 조건이 붙은 측정이다.

전달 팩에는 각 측정의 원문 URL이 없었다. 따라서 측정 Source는 `community_measurement` 유형의 전달 팩 provenance로 연결하고 모든 측정 Evidence를 `needs_review`로 유지했다. 원문 링크가 확보되기 전에는 `verified`로 승격하지 않는다.

아프로돈 출시일 측정은 8월 19일 조정 이전이므로 `pre_balance_patch`이며 시간당 성능 비교를 금지했다. 사건의 지평선 9월 2일 이전 수익 측정과 이스라히드/죽은 자들의 도시 6월 10일 이전 수익 측정은 current 표본으로 가져오지 않았다.

## Garmoth aggregate 제한

Garmoth의 집계 수치는 개별 세션의 직업, 세팅, 펫, 밀실/필드, 이벤트 발생, 패치 구간을 충분히 설명하지 못할 수 있다. 이번 seed에는 Garmoth 집계값을 MEASUREMENT나 공식 평균으로 적재하지 않았다. 향후 도입할 경우 dated Strategy/Context로만 두고 개별 timestamped session보다 낮은 비교 우선순위를 부여해야 한다.

## Archive와 식별자 보존

V1.7B Content 25개는 모두 `active`이다. 의도적으로 비활성화한 신규 requirement는 아래 2개뿐이다.

- `golden-pig-cave.legacy-release-stats`
- `event-horizon.legacy-launch-values`

두 claim의 Evidence는 `superseded`, `active=false`로 보존했다. 임시 DB에서 V1.7A baseline import 후 V1.7B를 두 번 import해 기존 Content ID, V1.7B Content ID, Requirement/Section/Relation/Evidence nested ID가 바뀌지 않음을 확인했다. importer가 기존 행을 seed key로 갱신했으며 예상치 못한 archive는 없었다.

`UserContentState`에 보존 표식을 넣은 뒤 두 번 재수입해 state, priority, note가 유지됨을 확인했다. 기존 checklist history 보존은 전체 backend의 기존 importer 회귀 테스트와 함께 통과했다.

## Migration 및 idempotency 검증

임시 파일 DB에서 다음 순서로 검증했다.

1. Alembic `20260902_0001` 적용
2. Alembic head(`20260903_0002`) 적용
3. V1.7B 항목을 제외한 V1.7A baseline seed import
4. 전체 V1.7B seed import
5. 전체 V1.7B seed 재import
6. stable Content/nested ID, UserContentState, active/archive 상태 비교

결과는 모두 통과했다.

## Schema gap과 미확인 항목

- Measurement 전용 테이블이 없어 세션 필드는 Requirement의 `structured_value`에 저장된다.
- 사용자 개인 측정을 community Source와 분리해 수용하는 first-class source/session 구조가 없다.
- 패치 구간, measurement grade/freshness, 밀실/필드, 펫, 희귀 드롭을 강제 검증하는 전용 column/enum이 없다.
- 시장가격 snapshot과 세금/희귀품 가치 산식을 분리 저장하는 구조가 없어 시간당 은화를 영구 FACT로 만들 수 없다.
- 전달 팩에 원문 URL이 없는 11개 측정은 원문 확보 전까지 `needs_review`다.
- 금돼지굴 입장/세션 규칙, 행운의 금돼지굴 변형, 도깨비숲 성장 목적 Strategy는 전달 팩 provenance만 있어 `needs_review`다.
- 테네브라움·제피로스의 정확한 현재 권장/최종 수치와 loot은 이번 근거에서 직접 확인하지 못해 비워 두었다.
- context-rich 최신 도깨비숲 측정은 억지로 생성하지 않았다.

이 gap은 이번 milestone의 schema 변경 금지 범위 때문에 기록만 했으며 코드나 모델을 확장하지 않았다.

## 테스트 결과

- V1.7B semantic 및 임시 migration/idempotency 테스트: **9 passed**
- V1.7A + V1.7B combat semantic 테스트: **20 passed**
- backend 전체 테스트: **124 passed**

검증 내용에는 JSON ID/URL/slug 유일성, 대상 존재, AP cap, 6월 10일 override, 에다니아 최신 수치, 9월 2일 사건의 지평선 값, FACT/MEASUREMENT 분리, 측정 provenance, 예상 archive, 외부 진행 순서, stable ID/nested ID, UserContentState 보존, migration 및 2회 import 멱등성이 포함된다.

## 실제 DB 보호

- 작업 전 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 작업 후 SHA-256: `9AABBA6F8884703CEEC1AC2A12D63C224B0072C3369839EFC08C1A7D71EED84C`
- 결과: 실제 `backend/bdo.db` 변경 없음
