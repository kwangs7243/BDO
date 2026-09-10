# V1.9Q Cooking Recipe Foundation — Research

조사일: 2026-09-10, KR 기준. 이 문서는 신규 4개 Recipe의 근거 경계만 기록한다.

## 현행 공식 가이드와 검증 범위

기존 stable Source `cooking-guide`의 [공식 요리 가이드](https://www.kr.playblackdesert.com/ko-KR/Wiki?wikiNo=102)를 재사용했다. 요리 과정의 1회분 재료 투입, 대체품 분류, recipe/substitute별 필요량 차이 경고, 대체품 목록을 확인했다. 대량 요리의 10회 재료 소비나 가변 결과물 수를 Recipe 1회 option quantity와 혼동하지 않는다.

그룹 membership Evidence와 각 Recipe의 `per_attempt` claim은 verified다. 그룹은 소속만 표현하며 모든 레시피에서 동일 수량으로 바꿀 수 있다는 보증은 아니다.

| Group | 초기 Material members |
| --- | --- |
| grain | wheat, barley, potato, sweet-potato, corn |
| fruit | grape, strawberry, apple, cherry, pear, banana, pineapple |
| vegetable | pumpkin, olive, tomato, paprika, cabbage |
| bird-meat | kuku-bird-meat, flamingo-meat, chicken-meat |

## 정확한 배합의 Source hierarchy

| Recipe | 배합·skill의 보조 근거 | 채택 경계 |
| --- | --- | --- |
| beer | [2019 커뮤니티 글](https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=12232), [BDO Codex 9213](https://bdocodex.com/kr/item/9213/) | 곡물 5, 물 슬롯 생수 6 또는 정제수 3, 발효제 2, 설탕 1; beginner 1 |
| vinegar | [2020 커뮤니티 글](https://www.kr.playblackdesert.com/ko-KR/Forum/ForumTopic/Detail?_topicNo=26907), [BDO Codex 9066](https://bdocodex.com/kr/item/9066/) | 곡물 1, 과일 1, 발효제 1, 설탕 1; beginner 1 |
| pickled-vegetables | [2021 공식 라라 이벤트](https://www.kr.playblackdesert.com/ko-KR/News/Detail?groupContentNo=5469), 위 2020 글, [BDO Codex 9202](https://bdocodex.com/kr/item/9202/) | 채소 8, 식초 4, 발효제 2, 설탕 2; apprentice 1 |
| grilled-bird-meat | [BDO Codex 9492](https://bdocodex.com/kr/item/9492/) | 새고기 2, 기름 슬롯 튀김용 오일 6 또는 면실유 6, 요리용 와인 2, 소금 1; beginner 1 |

공식 라라 이벤트는 당시 채소 절임의 양배추 배합과 견습 Lv.1을 명시하지만 과거 이벤트 자료이지 현행 전체 대체품 formula의 확정 근거는 아니다. Pearl Abyss 도메인의 이용자 글은 community_guide이지 공식 FACT가 아니다. BDO Codex는 third_party_database다. 새로운 Source 7개와 기존 cooking-guide를 재사용하며 URL identity를 중복 생성하지 않았다.

초기 4개 exact formula, skill requirement, option quantity는 모두 needs_review다. 특히 정제수 3과 면실유 6 대안은 지시서의 초기 배합을 보존하되 이번 조회에서 현행 공식 KR exact quantity를 확인하지 못했다. 새구이 KR Codex 본문에서 면실유 대체가 명시적으로 재확인되지 않았으며, 해외 표기를 KR 공식 확정 근거로 승격하지 않았다. 원본 공식 가이드의 물 대체 가능성도 6:3이라는 전역 비율을 뜻하지 않는다.

## 의도적으로 제외

고급/특상품 global multiplier, white-equivalent 환산, 혼합 대체, 고정 결과 수량, 성공·상위 결과 확률, 가격·수익, 전체 recipe catalog는 추가하지 않았다. 수량은 각 Recipe option에만 속하고 결과 Material은 identity만 가진다. 공식 가이드의 unrelated old gear/경제 표기를 이번 Recipe seed에 복제하지 않았다.

검증 상태는 구조적 validation 통과와 별개다. 향후 공식 현행 배합이 확인되면 해당 claim의 Evidence를 갱신하고 과거 근거를 보존한다.
