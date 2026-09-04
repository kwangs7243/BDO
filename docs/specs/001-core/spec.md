# Feature Spec 001 — BDO Companion Core

## Product statement
검은사막의 방대한 콘텐츠를 "무엇인지 알아보기 → 기반 준비 → 최초 완료 → 반복 관리 → 장기 성장"으로 연결하는 개인용 로컬 웹앱.

## Personas
- 복귀/성장 중인 1인 사용자
- 많은 콘텐츠를 한 번에 완벽히 외우기보다, 필요할 때 페이지를 열어 진행하려는 사용자
- 최신 패치로 과거 공략이 자주 무효화되는 게임 특성 때문에 출처/검증일이 필요한 사용자

## Functional requirements

### FR-1 Dashboard
- 오늘 할 일, 이번 주 할 일, 다음 초기화까지 남은 시간
- `목요일 00:00`, `일요일 00:00`, 이벤트 종료 등 서로 다른 deadline 그룹 표시
- 진행 중 프로젝트의 다음 행동 3~5개
- 미완료 생활 기반 항목 요약
- 중요한 기간제 이벤트

### FR-2 Content Explorer
필터:
- 카테고리: 전투/PvE, 생활, 성장/내실, 대양, 월드/길드, 장비, 캐릭터, 이벤트
- 주기: 일일/주간/시즌/비정기/일회성
- 파티: 솔로/파티/길드
- 상태: 미착수/기반 준비/진행/완료/보류/관심없음
- 난이도, 권장 스펙, 예상 소요, 보상 목적

### FR-3 Content Detail
섹션:
1. 한눈에 보기
2. 왜 하는가 / 핵심 보상
3. 선행조건
4. 준비 세팅
5. 시작 위치/NPC/UI 경로
6. 최초 진입 체크리스트
7. 실제 진행 순서
8. 반복 규칙 및 초기화
9. 보상 / 선택 보상 추천
10. 흔한 실수
11. 관련 프로젝트/콘텐츠
12. 내 상태/메모
13. 출처 및 검증 상태

V1.6A에서는 위 섹션을 `ContentRequirement`, `ContentStep`, `Reward`, `ContentSection`, `ContentRelation`으로 구조화하며, 단일 로컬 사용자의 `UserContentState`를 상세 화면에서 직접 저장한다. 빈 구조화 섹션은 큰 빈 영역으로 렌더링하지 않는다.

### FR-4 Recurring Checklist Engine
- template과 instance 분리
- 일일 00:00 KST
- 기본 주간 목요일 00:00 KST
- 콘텐츠별 커스텀 period rule
- checklist template은 nullable `period_rule_id`로 특정 reset-like schedule을 소유할 수 있음
- daily는 로컬 시각, weekly는 요일과 로컬 시각을 설정 가능
- reward payout은 별도 schedule로 표시
- `reward_payout`/`record_cutoff`은 checklist period를 생성하지 않음
- 자동 초기화가 아니라 현재 period instance 조회/생성
- 과거 주차 기록 열람

### FR-5 Life Foundation
각 생활 분야(채집/낚시/수렵/요리/연금/가공/조련/재배/항해/교역/무역 상태 확인)에 대해:
- 입문 목적
- 추천 캐릭터/캐릭터 역할(사용자 메모 기반)
- 필수/권장 장비 슬롯
- 도구/의상/액세서리/유물·광명석/연금석
- 숙련도·경험치 개념
- 입문 퀘/아카데미/기초 노드
- 최소 기반 체크리스트
- 중급 확장 체크리스트
- 관련 반복 수익/주간/이벤트

### FR-6 Project Tracker
예: 중범선 : 점진
- 단계 DAG
- 재료 목표/보유/부족
- 재료별 수급처
- 수급처가 반복 콘텐츠면 해당 체크리스트로 링크
- 선택상자/교환권 사용 전략 메모
- 단계 완료 checkbox

### FR-7 Growth / Account Foundation
- 메인 의뢰 지역별
- 모험일지
- 마그누스
- 가문 공방/능력치
- 펫/요정
- 수정/유물
- 일꾼/노드
- 월드보스 부캐
- 지식/기운/공헌도
- 보물 아이템 프로젝트
각 항목은 `왜/효과/선행/체크`를 가진다.

### FR-8 Source & Evidence
- claim/source relationship
- source priority와 freshness
- `verified`, `needs_review`, `superseded`, `conflict` 상태
- 현재 verification 집계는 active evidence만 사용하고, superseded/archived 근거는 이력으로 보존
- UI에 "검증일"과 대표 공식 링크
- source conflict 화면

### FR-9 Search
한글 콘텐츠명/아이템명/의뢰명/NPC/보상으로 통합 검색.

### FR-10 User Data
- 체크 상태
- 콘텐츠 관심 상태
- 캐릭터 역할
- 보유 장비/프로젝트 재고
- 개인 메모
- export/import JSON

V1.6A는 인증 없는 단일 로컬 사용자의 콘텐츠 상태·우선순위·메모와 기존 checklist 상태까지만 구현한다. 캐릭터/프로젝트 재고/export·import는 후속 milestone이다.

### FR-11 ChatGPT Prompt Bridge (V1.5)
- 앱 내부 LLM 호출 없이 현재 페이지 관련 데이터와 사용자 상태를 수집
- V1.6A 구현 preset은 `content_onboarding`, `weekly_review` 두 가지이며, 나머지는 관련 도메인 모델 구현 후 추가
- verified / needs_review / conflict를 구분하여 context에 포함
- `content_onboarding`은 구조화 선행조건·단계·보상·일정·주의사항·개인 상태를 포함
- 공식 출처 URL/검증일 포함
- clipboard 복사 및 Markdown 다운로드
- 자세한 요구사항은 `docs/specs/002-prompt-bridge/spec.md` 참조

## Non-functional
- localhost 응답: 일반 페이지 300ms 내 목표
- DB가 비어 있어도 seed import로 복구 가능
- 데이터와 코드 배포 분리
- 날짜/시간 계산 timezone aware
- 모바일 폭에서도 체크 가능하나 데스크톱 우선
- V1.5 runtime은 LLM/OpenAI API에 의존하지 않음
