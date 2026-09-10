# V1.9R — Cooking Recipe Evidence Verification Research

## 조사 범위

- 조사일: 2026-09-11 (KR)
- 대상: 맥주, 식초, 채소 절임, 새구이
- 목적: V1.9Q에서 `needs_review`로 남긴 exact formula, 요구 숙련, option 수량을 claim별로 재검증
- 비목표: 새 Recipe/Material/IngredientGroup, 전역 대체 비율, 품질 환산, 혼합 대체, 산출량, 계산기

`verified`는 현재 canonical 값으로 사용할 만큼 근거가 교차검증됐다는 뜻이다. 최신 Pearl Abyss 공식 페이지가 모든 숫자를 직접 적었다는 뜻은 아니며, 공식 여부는 각 Source의 `publisher`와 `source_type`으로 별도 표현한다.

## 공식 current 요리 규칙

Pearl Abyss KR 요리 가이드(페이지 표시 최근 수정 2026-02-06)를 다시 확인했다.

- 재료는 요리 1회분을 넣는다.
- 대량 요리는 10회분 재료를 한꺼번에 소비한다.
- 곡물: 밀, 보리, 감자, 고구마, 옥수수
- 채소: 호박, 올리브, 토마토, 파프리카, 양배추
- 과일: 포도, 딸기, 사과, 체리, 배, 바나나, 파인애플
- 새고기: 쿠쿠새 고기, 홍학 고기, 닭고기
- 물: 요리용 생수, 정제수
- 대체재는 Recipe에 따라 원래 재료보다 더 많은 수량이 필요할 수 있다.

따라서 `IngredientGroup`은 대체 가능 관계만 표현하고, 수량은 각 `RecipeIngredientOption`에 남긴다. 공식 current 가이드를 개별 Recipe의 exact formula 표처럼 사용하지 않는다.

## Recipe별 결론

| Recipe | 현재 배합 근거 | 공식 직접 근거 | 보조 현재 근거 | 최종 상태 |
| --- | --- | --- | --- | --- |
| 맥주 | 곡물 5; 요리용 생수 6 또는 정제수 3; 발효제 2; 설탕 1; 초급 1 | 현재 공식 exact 배합표는 찾지 못함. 공식 current 가이드는 곡물·물 대체 관계와 1회분 의미를 지원 | current BDO Codex와 Pearl Abyss 도메인의 `community_guide`를 교차확인. 정제수 3은 current game-data 확인 범위 | `verified` |
| 식초 | 곡물 1; 과일 1; 발효제 1; 설탕 1; 초급 1 | 현재 공식 exact 배합표는 찾지 못함. 공식 current 가이드는 곡물·과일 대체 관계와 1회분 의미를 지원 | current BDO Codex와 Pearl Abyss 도메인의 `community_guide`가 동일 배합을 지원 | `verified` |
| 채소 절임 | 채소 8; 식초 4; 발효제 2; 설탕 2; 견습 1 | 2021 Pearl Abyss 이벤트에 양배추 8 exact 배합과 요구 숙련이 직접 기록됨. current 가이드는 양배추의 채소 그룹 소속을 지원 | current BDO Codex가 동일 배합을 지원 | `verified` |
| 새구이 | 새고기 2; 튀김용 오일 6 또는 면실유 6; 조리용 와인 2; 소금 1; 초급 1 | 2018 Pearl Abyss 업데이트에 닭고기 2, 튀김용 오일 6, 와인 2, 소금 1, 초급 1이 직접 기록됨 | current BDO Codex가 전체 배합과 면실유 6 대안을 지원 | `verified` |

## Source hierarchy와 경계

### BDO Codex current cross-check

조사 당시 BDO Codex 업데이트 기록에는 2026-09-09 Korean section이 최신 게임 버전으로 갱신됐다고 표시됐다. 2026-09-11 current cross-check에 사용할 수 있는 보조 근거로 판단했지만 Source는 계속 `third_party_database`다. Pearl Abyss 공식 Source로 승격하지 않는다.

### Pearl Abyss 도메인의 이용자 게시글

맥주와 식초 교차자료는 Pearl Abyss 도메인에 있어도 이용자 작성 글이다. Source type은 계속 `community_guide`이며 공식 exact formula라고 표현하지 않는다.

### 새구이 2018 공식 Source

신규 `cooking-grilled-bird-meat-official-2018`은 다음 claim에만 연결한다.

- `required_skill`: 초급 1
- 새고기 base option: 닭고기 2
- 튀김용 오일: 6
- 조리용 와인: 2
- 소금: 1

공식 자료에 없는 면실유 6 claim과, 면실유까지 포함하는 전체 formula claim에는 연결하지 않는다. 면실유는 current BDO Codex 근거로만 검증한다.

## Evidence 결과

- V1.9Q claim 정의: 34
- V1.9Q Source-linked Evidence: 39 (`verified` 8 / `needs_review` 31)
- V1.9R Source-linked Evidence: 44 (`verified` 44 / `needs_review` 0)
- 증가한 5개 연결은 새구이 2018 공식 Source가 직접 지원하는 기존 claim에 대한 연결이다.
- 기존 Recipe 수치, 슬롯, option, Material identity는 변경하지 않았다.

## 남긴 제한

- 맥주의 6 대 3 수량을 Pearl Abyss current 공식 표가 직접 확인했다고 주장하지 않는다.
- 채소 그룹 소속을 모든 품질 등급의 전역 수량 환산으로 확대하지 않는다.
- 새구이 2018 자료를 면실유 근거로 사용하지 않는다.
- V1.9Q 연구 문서는 당시 조사와 `needs_review` 결정의 역사 기록으로 유지한다.
