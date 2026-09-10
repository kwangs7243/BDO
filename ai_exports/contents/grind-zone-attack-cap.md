<!-- GENERATED FILE — DO NOT EDIT BY HAND.
Canonical source: BDO Companion seed/domain services.
Regenerate with: cd backend && uv run python -m app.ai_export write
-->

# 사냥터 공격력 제한

## Identity

- slug: "grind-zone-attack-cap"
- name_ko: "사냥터 공격력 제한"
- category: "combat_pve"
- status: "active"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- party_type: null
- difficulty: null

## Overview

- summary: "공격력 제한 사냥터에서는 제한을 초과한 공격력의 일부만 적용된다."
- purpose: "사냥터별 공격력 제한을 장비 성장과 사냥터 선택에 반영한다."

## Requirements

### `grind-zone-attack-cap.excess`

- seed_key: "grind-zone-attack-cap.excess"
- kind: "stat"
- requirement_level: "required"
- title: "제한 초과분 적용"
- description: "사냥터 공격력 제한을 넘는 공격력은 초과분의 5%만 적용된다."
- structured_value:

```json
{
  "excess_ap_applied_percent": 5,
  "knowledge_role": "fact",
  "zone_specific_cap": true
}
```

## Steps

- None

## Schedules

- None

## Rewards

- None

## Sections

- None

## Related Contents

### `black-energy-overflow-zone.attack-cap`

- seed_key: "black-energy-overflow-zone.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "black-energy-overflow-zone"
- content_name_ko: "검은 기운 범람지"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/black-energy-overflow-zone.md"
### `city-of-the-dead.attack-cap`

- seed_key: "city-of-the-dead.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "city-of-the-dead"
- content_name_ko: "죽은 자들의 도시"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/city-of-the-dead.md"
### `darkseekers-retreat.attack-cap`

- seed_key: "darkseekers-retreat.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "darkseekers-retreat"
- content_name_ko: "어둠 추종자 침소"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/darkseekers-retreat.md"
### `dehkia-ash-ii.attack-cap`

- seed_key: "dehkia-ash-ii.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "dehkia-ash-ii"
- content_name_ko: "[데키아 II] 잿빛 숲"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/dehkia-ash-ii.md"
### `dehkia-gyfin-upper.attack-cap`

- seed_key: "dehkia-gyfin-upper.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "dehkia-gyfin-upper"
- content_name_ko: "[데키아] 가이핀라시아 사원 지상"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/dehkia-gyfin-upper.md"
### `dehkia-miru.attack-cap`

- seed_key: "dehkia-miru.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "dehkia-miru"
- content_name_ko: "[데키아] 미루목 유적지"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/dehkia-miru.md"
### `dehkia-olun-ii.attack-cap`

- seed_key: "dehkia-olun-ii.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "dehkia-olun-ii"
- content_name_ko: "[데키아 II] 올룬의 계곡"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/dehkia-olun-ii.md"
### `dokkebi-forest.attack-cap`

- seed_key: "dokkebi-forest.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "dokkebi-forest"
- content_name_ko: "도깨비숲"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/dokkebi-forest.md"
### `gabinya-coastal-cliff.attack-cap`

- seed_key: "gabinya-coastal-cliff.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "gabinya-coastal-cliff"
- content_name_ko: "가비냐 해안 절벽"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/gabinya-coastal-cliff.md"
### `golden-pig-cave.attack-cap`

- seed_key: "golden-pig-cave.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "golden-pig-cave"
- content_name_ko: "금돼지굴"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/golden-pig-cave.md"
### `hexe-sanctuary-elvia.attack-cap`

- seed_key: "hexe-sanctuary-elvia.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "hexe-sanctuary-elvia"
- content_name_ko: "[엘비아] 헥세 성역"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/hexe-sanctuary-elvia.md"
### `tungrad-ruins.attack-cap`

- seed_key: "tungrad-ruins.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "tungrad-ruins"
- content_name_ko: "툰그라드 유적지"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/tungrad-ruins.md"
### `yzrahid-highlands.attack-cap`

- seed_key: "yzrahid-highlands.attack-cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "yzrahid-highlands"
- content_name_ko: "이스라히드 고원"
- content_category: "combat"
- note: null
- order_no: 1
- relative_path: "../contents/yzrahid-highlands.md"
### `grind-zone-recommendation-system.cap`

- seed_key: "grind-zone-recommendation-system.cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "grind-zone-recommendation-system"
- content_name_ko: "사냥터 추천 시스템"
- content_category: "combat_pve"
- note: "추천 범위와 개별 사냥터 공격력 제한은 별도 규칙이다."
- order_no: 2
- relative_path: "../contents/grind-zone-recommendation-system.md"
### `pve-crystal-strategy.cap`

- seed_key: "pve-crystal-strategy.cap"
- direction: "incoming"
- relation_type: "related"
- content_slug: "pve-crystal-strategy"
- content_name_ko: "PvE 수정 구성 전략"
- content_category: "combat_pve"
- note: "사냥터 제한 이후 효율을 비교한다."
- order_no: 2
- relative_path: "../contents/pve-crystal-strategy.md"

## Evidence and Sources

### Current evidence

### `grind-zone-attack-cap.claim.excess::combat-system-rework-2025-07-23`

- evidence_seed_key: "grind-zone-attack-cap.claim.excess::combat-system-rework-2025-07-23"
- source_id: "combat-system-rework-2025-07-23"
- title: "7월 23일(수) 업데이트 안내 (최종 수정 : 2025-09-03 17:16)"
- url: "https://www.kr.playblackdesert.com/ko-KR/News/Detail?countryType=ko-KR&groupContentNo=14289"
- publisher: "Pearl Abyss"
- source_type: "official_patch"
- published_at: "2025-07-23"
- retrieved_at: "2026-09-07T12:00:00+00:00"
- region: "KR"
- entity_type: "content"
- entity_id: "grind-zone-attack-cap.excess"
- claim_key: "requirement:grind-zone-attack-cap.excess"
- verification_status: "verified"
- last_verified_at: "2026-09-04"
- evidence_note: null
- active: true
- is_active: true

### Historical / inactive evidence

- None
