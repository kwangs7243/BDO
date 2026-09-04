# UI / Information Architecture

## Global navigation

- `/` 대시보드
- `/today` 오늘
- `/weekly` 이번 주
- `/content` 콘텐츠 탐색
- `/content/:slug` 콘텐츠 상세
- `/life` 생활 허브
- `/life/:skill` 생활 상세
- `/projects` 프로젝트
- `/projects/:slug` 프로젝트 상세
- `/growth` 성장/내실
- `/characters` 캐릭터/역할
- `/sources` 근거/검증
- `/prompt` ChatGPT 프롬프트 생성기
- `/settings` 설정/백업

## Dashboard layout

### A. Next resets
카드 3~5개:
- 오늘 00시
- 목요일 00시 주간 초기화
- 일요일 00시 기록/보상
- 가장 가까운 이벤트 종료

### B. 오늘 할 일
사용자가 활성화한 daily templates만.

### C. 이번 주
reset group별 컬럼/섹션. 모든 주간을 한 리스트로 섞지 않는다.

### D. 진행 프로젝트
중범선 등 `next actionable stage` 표시.

### E. 기반 점검
미착수/기반 필요인 생활·내실 항목 최대 5개.

## Content Detail wireframe

[제목] [상태] [최종 검증일]
[한줄 목적] [파티/스펙/소요/주기]

### 지금 이걸 왜 하나
핵심 가치/보상.

### 시작 전 준비
선행퀘 / 스펙 / 아이템 / 위치.

### 처음 하는 사람 순서
checkable 단계.

### 반복 플레이
주기, 초기화, 보상 지급 규칙을 타임라인으로.

### 보상
고정 / 선택 / 추천.

### 내 진행도
사용자 상태, 개인 메모, 활성 숙제 토글.

### 연결된 콘텐츠
선행/후속/프로젝트.

### 근거
공식 우선, 최신/충돌 표시.

## Life detail 추가 섹션
- 공통 생활장비와 해당 분야 전용 슬롯
- 최소 세팅 / 가성비 / 목표 세팅
- 레벨·숙련도 단계별 목표
- 재료/거점/일꾼 의존성
- 입문 루트와 돈벌이 루트 분리

## UX 금지
- 페이지 진입하자마자 거대한 raw DB 표 노출
- 의미 없는 5단계 폴더 구조
- 같은 링크 반복
- 정보 없는 빈 하위 페이지 대량 생성


## Prompt Bridge
상세 페이지 우측 상단 또는 액션 영역에 `ChatGPT에 물어보기` 버튼을 둔다.

Drawer/페이지 구성:
1. 질문 목적 preset
2. 포함 컨텍스트 토글
3. 현재 페이지에서 자동 수집된 facts/progress preview
4. 사용자 질문 입력
5. 생성 prompt 미리보기
6. 문자/token 추정
7. `복사` / `Markdown 저장`

금지:
- API key 입력칸
- `ChatGPT로 전송`처럼 외부 서비스에 자동 전송하는 버튼
- 미검증 정보를 verified와 같은 섹션에 섞는 UI
