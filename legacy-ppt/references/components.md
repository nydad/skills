# 컴포넌트 카탈로그

모든 예시의 실제 동작 버전은 `assets/deck-template.html`에 있다. 여기 마크업은 뼈대만 보여주므로, 쓰기 전에 템플릿의 해당 슬라이드를 함께 열어 본다.

## 목차

1. 덱 뼈대: 설정, 표지, 목차, 간지, 본문 슬라이드
2. 요약 행 (Executive Summary)
3. KPI 타일, 차트
4. 노드와 연결선 (공통 규칙, 연결선 JSON 필드)
5. 시스템 구성도
6. 계층 아키텍처 + 문제점 목록
7. TO-BE 아키텍처 (변경점만 보기)
8. 스윔레인 흐름 + 재생
9. 배포 구성도 (평시/장애 전환)
10. 타임라인 + 원인/대책 패널
11. 단계 매트릭스
12. 플로차트 + RACI
13. 기대효과 표 + 요청 카드
14. 명세 표 + 필터
15. data 속성 요약
16. 카탈로그에 없는 장표 만들기

---

## 1. 덱 뼈대

### 설정

```html
<script type="application/json" id="deck-config">
{ "title": "하단 바에 보일 덱 이름", "footer": "대외비 &nbsp;|&nbsp; 조직명" }
</script>
```

### 표지

```html
<section class="slide dark cover" data-title="표지">
  <div class="stamp">대외비</div>
  <div class="cv-mark" aria-hidden="true">2027</div>          <!-- 연도나 짧은 숫자. 없으면 지운다 -->
  <div class="cv-main">
    <div class="kicker" data-a>영문 대문자 한 줄</div>
    <h1 class="cv-title" data-a>제목 1행<br>제목 2행 (안)</h1>
    <p class="cv-sub" data-a>부제 한 줄 (30자 이내)</p>
  </div>
  <div class="cv-meta" data-a><span>2026. 10.</span><span>조직명</span></div>
  <div class="cv-note">※ 예시 수치가 있으면 여기에 표기</div>
</section>
```

### 목차

목록은 엔진이 섹션에서 만든다. 왼쪽 패널 문구만 바꾼다.

```html
<section class="slide toc" data-title="목차">
  <div class="toc-side"><div class="toc-h">Contents</div><div class="toc-k">목차</div>
    <div class="toc-deck">덱 제목<br>두 줄</div></div>
  <div class="toc-list"></div>
</section>
```

### 간지 (섹션 선언)

```html
<section class="slide dark divider" data-section="현황 및 문제점" data-num="Ⅰ"
  data-title="Ⅰ. 현황 및 문제점" data-desc="섹션 설명 1행&lt;br&gt;2행"></section>
```

- `data-section`이 붙은 슬라이드부터 다음 섹션 전까지가 한 섹션이다. 목차 항목은 그 사이 본문 슬라이드의 `data-title`
- 간지 없이 섹션을 시작할 수 있다. 섹션 첫 본문 슬라이드에 `data-section="현황" data-num="Ⅰ"`를 직접 붙인다(Appendix는 `data-num=""`). 목차·간지를 뺀 짧은 덱은 모든 섹션을 이렇게 선언한다
- 첫 섹션보다 앞에 있는 슬라이드(Executive Summary 등)는 섹션이 없어 브레드크럼이 비므로 `<div class="crumb">Summary</div>`처럼 손으로 쓴다
- 목차에서 빼려면 `data-toc="false"`

### 본문 슬라이드

```html
<section class="slide content" data-title="목차에 보일 이름">
  <header class="s-head">
    <div class="crumb"></div>                                  <!-- 비우면 섹션명이 들어감 -->
    <h2 class="s-title">명사형 제목</h2>
    <p class="gmsg">결론 한 문장, 핵심 수치 <b>5분</b>, 문제는 <b class="r">18분</b></p>
  </header>
  <div class="s-body">
    ...                                                         <!-- 1424 × 550 -->
  </div>
  <div class="source">※ 출처 / 기준일 / 조작 힌트 / 수치는 예시</div>
</section>
```

- 꼬리말과 쪽번호는 엔진이 붙인다
- 제목과 거버닝 메시지는 반드시 한 줄이다. 두 줄이 되면 머리말이 본문 첫 줄을 덮는다(shoot.py가 잡는다). 거버닝 메시지는 한글 기준 55자 안팎이 한계
- 등장 순서를 줄 요소에 `data-a`. 위에서 아래, 왼쪽에서 오른쪽 순서로 단다
- 공용 텍스트: `.h3`(블록 소제목) + `<span class="unit">단위: 분</span>`, `.cap`(작은 라벨), `.mono`(기술 표기), `b.hl`(파랑 강조), `b.r`(빨강 문제), `ul.ul`(사각 불릿), `ul.ul.sub`(대시 불릿)

## 2. 요약 행

```html
<div class="sum">                                   <!-- 6행이면 행당 약 92px -->
  <div class="sr" data-a><div class="sr-l">현황</div>
    <ul class="ul"><li>...<b class="hl">14,200건</b>...</li><li>...</li></ul></div>
  <div class="sr" data-a><div class="sr-l">목표 아키텍처</div>
    <div class="chips4"><div class="node change"><b>이름</b><small>설명</small></div> ...4개</div></div>
  <div class="sr" data-a><div class="sr-l">전환 계획</div>
    <div class="chev-row"><div class="chev">P0 준비 <small>'26.4Q</small></div> ... <div class="chev end">...</div></div></div>
  <div class="sr" data-a><div class="sr-l">기대효과</div>
    <div class="stats4"><div class="stat"><strong class="hl">5분</strong><span>피크 대기 (현재 18분)</span></div> ...</div></div>
</div>
```

행 수가 바뀌면 `.sum`의 `grid-template-rows`를 `repeat(행수,1fr)`로 인라인 지정한다.

## 3. KPI 타일, 차트

```html
<div class="tiles" data-a>
  <div class="tile"><span class="t-l">빌드 성공률</span>
    <span class="t-v"><span data-count="91.4" data-dec="1">91.4</span><small>%</small></span>
    <span class="t-d bad">전년 대비 -2.1%p</span></div>   <!-- 나쁜 변화는 .bad -->
</div>
<div class="charts2">
  <div data-a><div class="h3">제목<span class="unit">단위: 천 건</span></div><div class="chart-host" id="chA"></div></div>
  <div data-a>...<div class="chart-host" id="chB"></div></div>
</div>
<script type="application/json" data-kind="chart" data-for="chA">{
  "type": "bar", "h": 344, "max": 16.5, "dec": 1, "unit": "천 건", "delta": "전월 대비", "hi": [11],
  "labels": ["'25.10","11"], "full": ["2025.10","2025.11"], "values": [10.3,10.6]
}</script>
<script type="application/json" data-kind="chart" data-for="chB">{
  "type": "line", "h": 344, "max": 21, "min": 0, "unit": "분", "target": 5, "targetLabel": "목표 5분",
  "labels": [...], "full": [...], "values": [...]
}</script>
```

- 폭은 호스트 폭을 따른다. `max`는 최댓값보다 15~20% 크게 잡아 값 라벨이 들어갈 자리를 둔다
- `hi`: 강조할 막대 인덱스(보통 마지막). `delta`: 툴팁에 직전 대비 증감을 붙일 때 그 문구
- 꺾은선은 마지막 점이 채워진 원으로 강조되고, `target`이 있으면 파란 점선과 라벨이 그려진다
- 기준선 라벨은 오른쪽 끝 선 위에 놓인다. 마지막 두 점이 기준선 근처면 자동으로 왼쪽 끝으로 옮기고, `"targetPos": "left"|"right"`로 고정할 수 있다
- 툴팁의 기준선 대비 문구는 기본 "목표 대비"다. 용량 한계선이면 `"targetTip": "한계 대비"`, 빼려면 `""`
- 그 밖의 필드: `min`(꺾은선 y축 하한, 기본 0), `aria`(스크린리더용 설명), `dec`(소수 자릿수), `full`(툴팁에 보일 긴 라벨)

## 4. 노드와 연결선

```html
<div class="node change"><b>Jenkins 컨트롤러 ×2</b><small>Active-Standby</small></div>
<div class="node db new"><b>오브젝트 스토리지</b><small>S3 호환</small></div>
<div class="node issue" data-k="1"><b>...</b><i class="bdg">1</i></div>          <!-- 빨간 문제 배지 -->
<div class="node new"><b>...</b><i class="bdg fix" data-tip="해소 ② 설명">2</i></div>  <!-- 파란 해소 배지 + 툴팁 -->
```

종류: `keep`(기본, 클래스 없음) `change` `new` `ext` `muted` `core` `issue`, 모양: `db`.

연결선은 노드를 품은 컨테이너(`class="edges-host"`, `id` 필수, `position:relative`) 단위로 선언한다.

```html
<script type="application/json" data-kind="edges" data-for="호스트 id">[
  { "a": "노드A", "as": "r", "b": "노드B", "bs": "l" }
]</script>
```

| 필드 | 뜻 |
|---|---|
| `a`, `b` | 시작·끝 노드 id |
| `as`, `bs` | 붙는 변 `l` `r` `t` `b`. `t@0.75`처럼 변 위 위치(0~1) |
| `r` | 경로: `s` 직선(기본), `hvh` 가로-세로-가로, `vhv` 세로-가로-세로, `hv`, `vh` |
| `mx`, `my` | `hvh`의 꺾는 x, `vhv`의 꺾는 y (호스트 좌표) |
| `ax`/`ay` `"b"` | 시작점 x/y를 끝 노드 중심에 맞춤 (큰 블록 옆면에 수평선을 꽂을 때) |
| `bx`/`by` `"a"` | 끝점 x/y를 시작점에 맞춤 |
| `cls` | `soft`(회색 점선) `both`(양방향) `live`(파랑) `cut`(빨강 점선) `nohead` `alt-cut` `alt-live` `alt-dim`(보기 전환 시) |
| `label` | 선 위 라벨(HTML 허용, `<br>`) |
| `lseg` | 라벨을 놓을 구간 번호(0부터). 없으면 시작·끝 중간 |
| `dx`, `dy` | 라벨 이동. 수평 직선이면 기본으로 16px 위 |
| `lcls` | 라벨 추가 클래스. `yes`는 파랑 굵게(플로차트 "예") |

호스트에 `data-hover-links`, 노드에 `data-hover`를 달면 노드를 가리킬 때 연결된 선만 흐르며 강조된다.

## 5. 시스템 구성도

사용자(왼쪽) → 플랫폼 본체(가운데 남색 블록, 모듈 격자) → 외부 시스템(오른쪽 점선). 아래에 규모 지표 띠.

```html
<div class="ctx-grid edges-host" id="ctx" data-hover-links>      <!-- 290 | 140 | 1fr | 140 | 300, 높이 408 -->
  <div class="ctx-col l" data-a><div class="cap">사용자</div><div class="stack">
    <div class="node muted" id="ctx-dev" data-hover><b>개발자</b><small>620명</small></div> ...</div></div>
  <div class="platform" id="ctx-core" data-a>
    <div class="core-h">ORBIT<span>통합 개발 플랫폼</span></div>
    <div class="mods"><div class="mod"><b>형상관리</b><small>Git</small></div> ...6개</div>
    <div class="core-f mono">기술 스택 한 줄</div></div>
  <div class="ctx-col r" data-a><div class="cap">외부 시스템</div><div class="stack">
    <div class="node ext" id="ctx-jira" data-hover><b>Jira</b><small>이슈 연동</small></div> ...</div></div>
</div>
<!-- 사용자 → 본체: by "a" / 본체 → 외부: ay "b" -->
<div class="kpi-strip" data-a><div><strong>14,200</strong><span>일 평균 빌드</span></div> ...4칸 <strong class="r">미달 값</strong></div>
```

- 노드 높이가 왼쪽 3개(96px), 오른쪽 4개(76px)에 맞춰 고정돼 있다. 개수가 다르면 `<style>` 끝에 `.ctx-col.l .node{height:…}`를 덮어쓴다. 기둥 높이 408 안에서 (408 − 상단 라벨 40 − 간격 합) ÷ 개수
- 왼쪽은 플랫폼을 쓰는 쪽(`muted`), 오른쪽은 플랫폼이 부르는 바깥 시스템(`ext`)이다. 생산자 → 플랫폼 → 소비자처럼 양쪽 모두 사내 시스템이면 둘 다 `keep`(또는 `change`)으로 두고 머리 라벨만 "생산자"/"소비자"로 바꾼다
- `strong`의 강조 색은 `.hl`(파랑), `.r`(빨강) 둘 다 쓸 수 있다

## 6. 계층 아키텍처 + 문제점 목록

```html
<div class="arch-wrap" data-focus>                                  <!-- 1fr | 410 -->
  <div class="layers">
    <div class="layer" style="--h:108px" data-a><div class="ly-l">서비스</div><div class="ly-n">
      <div class="node"><b>Gerrit</b><small>코드 리뷰</small></div>
      <div class="node issue" data-k="1" style="--r:1.25"><b>Jenkins</b><small>단일</small><i class="bdg">1</i></div>
    </div></div>
    <!-- 실행 계층의 고정 풀 표현 -->
    <div class="layer" style="--h:124px" data-a><div class="ly-l">실행</div>
      <div class="pools" data-k="2"><div class="pools-h"><b>제목</b><span>설명</span></div>
        <div class="pool-box" data-cells="12" data-busy="0,1,4" data-label="팀"><i class="bdg">2</i></div></div></div>
  </div>
  <aside class="issues" data-a><div class="h3">문제점</div>
    <ol class="iss"><li data-k="1"><i class="bdg">1</i><div><b>제목</b><p>한 줄 설명</p></div></li> ...</ol>
    <div class="hint">항목을 가리키면 그림에서 위치가 강조됨</div></aside>
</div>
```

- `--h`: 계층 높이, `--r`: 노드 폭 비율(flex)
- `data-focus` 안에서 같은 `data-k`끼리 서로 강조된다. 문제점은 5개 안팎이 읽기 좋다

## 7. TO-BE 아키텍처

6과 같은 격자에 `alt-diff`와 보기 전환을 단다. AS-IS와 계층 이름·순서를 맞춘다.

```html
<div class="layers tobe alt-diff" id="tobe" data-view="base"> ...계층들... </div>
<div class="toolbar" data-a>
  <div class="legend"><span><i></i>유지</span><span><i class="change"></i>변경</span><span><i class="new"></i>신규</span><span><i class="ext"></i>폐기 예정</span></div>
  <div class="seg" data-view-target="#tobe"><button type="button" data-value="base">전체</button><button type="button" data-value="alt">변경점만</button></div>
</div>
```

## 8. 스윔레인 흐름 + 재생

```html
<div class="toolbar" data-a><span class="cap">가로줄은 처리 계층, 번호는 처리 순서</span>
  <div style="display:flex;align-items:center;gap:14px"><span class="elapsed" data-flow-elapsed="flow">경과 0초</span>
  <button type="button" class="btn" data-flow-play="flow"><svg viewBox="0 0 10 10"><path d="M1.5 1 L9 5 L1.5 9 z"/></svg>흐름 재생</button></div></div>
<div class="lanes edges-host" id="flow" data-a></div>
<script type="application/json" data-kind="flow" data-for="flow">{
  "lanes": [["개발자", ""], ["형상 · 리뷰", "Gerrit"]],
  "steps": [ { "lane": 0, "col": 0, "t": "변경 업로드", "s": "git push" },
             { "lane": 1, "col": 1, "t": "리뷰 등록", "s": "이벤트", "kind": "new", "time": "2초", "sec": 2 } ],
  "end": { "lane": 0, "col": 1, "t": "결과 확인", "s": "알림" },
  "done": "재생이 끝났을 때 경과 칸 문구"
}</script>
```

- 단계 노드 id는 `흐름id-1, -2, …`, 끝 노드는 `흐름id-end`. 연결선은 자동(같은 레인은 직선, 다르면 hvh). 직접 지정하려면 같은 id로 edges 블록을 둔다
- 선택 필드: `laneH`(기본 80), `labelW`(176), `nodeW`(150). 열 수는 `col` 최댓값으로 정해진다
- 아래 시간 분해 막대: `.tbar > .tbar-l + .segs > div(style="flex:값")`

## 9. 배포 구성도

절대 좌표 그림이다. 컨테이너에 높이를 주고 존과 노드를 `left/top/width/height`로 놓는다.

```html
<div class="toolbar" data-a>
  <div class="seg" data-view-target="#dep"><button type="button" data-value="base">평시</button><button type="button" data-value="alt">주 센터 장애</button></div>
  <div class="status"><span data-when="base"><b>평시</b> · 설명</span><span data-when="alt"><b class="live">전환 완료</b> · RTO 10분</span></div>
</div>
<div class="dep edges-host" id="dep" data-view="base" data-a>              <!-- 높이 500 -->
  <div class="node core" id="dp-gslb" style="left:612px;top:0;width:200px;height:62px"><b>GSLB</b></div>
  <div class="zone alt-alert" style="left:0;top:112px;width:640px;height:388px"><span class="zone-chip">주 센터</span><span class="down-pill">주 센터 장애</span></div>
  <div class="node change alt-dim" id="dpA-ctl" style="..."><b>컨트롤러</b><small>Active</small></div>
  <div class="node change alt-promote" id="dpB-ctl" style="..."><b>컨트롤러</b><small data-when="base">Standby</small><small data-when="alt">Active (승격)</small></div>
  <div class="runner" style="..."><b>k8s 러너 클러스터<span>노드 16대</span></b><div class="cells" data-n="16"></div></div>
  <div class="gap-note" style="left:640px;width:144px;top:330px">러너는<br>센터별 독립</div>
</div>
```

두 상태 유틸(`data-view="alt"`일 때): `alt-alert`(존 빨간 테두리 + `down-pill` 표시), `alt-dim`(흐리게·흑백), `alt-promote`(파란 링), `alt-solid`(존 실선 파랑), 연결선 `alt-cut`/`alt-live`/`alt-dim`. 존 사이 간격(144)은 복제 연결선 라벨 자리다.

## 10. 타임라인 + 원인/대책 패널

```html
<div class="h3" data-a>제목<span class="unit mono">09:42 ~ 13:10</span></div>
<div class="tl" id="tl" data-a></div>                                     <!-- 높이 262 -->
<script type="application/json" data-kind="timeline" data-for="tl">{
  "start": "09:36", "end": "13:16",
  "band": { "from": "09:58", "to": "13:10", "label": "빌드 중단 3시간 12분", "at": "11:30" },
  "events": [ { "t": "09:42", "title": "제목", "desc": "설명", "kind": "issue|ok|" } ]
}</script>
<div class="panels">                                                       <!-- 5fr | 7fr, 높이 246 -->
  <div class="panel" data-a><div class="h3">원인</div><dl class="cause"><dt>직접 원인</dt><dd>...</dd></dl></div>
  <div class="panel" data-a><div class="h3">재발 방지 대책</div><ul class="acts">
    <li><span class="chip done">완료</span><span>내용</span><span class="when">09.16</span></li>
    <li><span class="chip">진행</span><span>내용</span><span class="when">'27.1Q</span></li></ul></div>
</div>
```

이벤트는 위아래로 번갈아 놓인다. 7개 안팎, 이웃 이벤트 간격이 전체 시간의 8% 이상이어야 라벨이 겹치지 않는다. `band.at`은 아래쪽 이벤트가 없는 시각으로 잡는다.

- 시각은 하루 안의 `HH:MM`만 받는다. 자정을 넘기거나 여러 날에 걸친 경과는 시각을 시작 기준 경과(`00:00`=발생, `26:30`처럼 24 이상도 계산은 됨)로 바꾸고 라벨 `title`에 실제 날짜를 쓰거나, 날짜 단위면 간트(16절)로 그린다
- 라벨 상자는 폭 200px이다. `title`은 12자, `desc`는 16자 안팎을 넘기면 줄이 바뀌어 위쪽 라벨이 위로 자란다
- 아래 패널은 높이 246px이다. 원인은 `dt`/`dd` 두 쌍, 대책은 4행이 한계

## 11. 단계 매트릭스

```html
<div class="mx" data-col-hover data-a>                 <!-- 150 | 1fr×4, 행 높이 70 86 150 100 100 -->
  <div></div>
  <div class="mx-h first" data-col="0"><b>Phase 0 &nbsp;준비</b><small>'26.11 ~ 12</small></div>
  <div class="mx-h" data-col="1">...</div> ... <div class="mx-h end" data-col="3">...</div>
  <div class="mx-l">빌드 트래픽</div>
  <div class="mx-c" data-col="0"><div class="traffic"><i style="--p:30%;--i:0"></i></div><div class="traffic-l">k8s 30%</div></div>
  <div class="mx-l r">롤백 기준</div>                   <!-- 빨간 라벨 -->
  <div class="mx-c last" data-col="0">...</div>          <!-- 마지막 행은 .last -->
</div>
```

열·행 수가 바뀌면 `grid-template-columns`/`grid-template-rows`를 인라인으로 덮어쓴다.

## 12. 플로차트 + RACI

```html
<div class="ops">                                                         <!-- 600 | 1fr -->
  <div class="esc edges-host" id="esc" data-a>                              <!-- 높이 550, 절대 배치 -->
    <div class="h3">장애 대응 절차</div>
    <div class="node core" id="es-l1" style="left:40px;top:120px;width:340px;height:62px"><b>L1</b><small>...</small></div>
    <div class="diamond" id="es-d1" style="left:80px;top:204px;width:260px;height:76px">
      <svg viewBox="0 0 260 76" preserveAspectRatio="none"><polygon points="130,1 259,38 130,75 1,38"/></svg><span>30분 안에 복구?</span></div>
  </div>
  <!-- 결정 분기: { "a": "es-d1", "as": "r", "b": "es-end", "bs": "t", "r": "hv", "label": "예", "lcls": "yes", "lseg": 0, "dy": -14 } -->
  <div data-a><div class="h3">역할 분담 (RACI)</div><div class="raci" id="raci"></div>
    <div class="raci-lg">...범례...</div></div>
</div>
<script type="application/json" data-kind="raci" data-for="raci">{
  "roles": ["운영 당번", "컴포넌트<br>담당"], "first": 210,
  "rows": [ ["장애 초동 대응", ["R", "C"]] ]
}</script>
```

RACI는 행마다 A가 하나여야 한다. 표를 가리키면 행·열 십자 강조가 된다. `head`는 왼쪽 위 머리칸 문구(기본 "활동"), `first`는 첫 열 폭(기본 210).

## 13. 기대효과 표 + 요청 카드

```html
<div class="ben">                                                          <!-- 1fr | 480 -->
  <div data-a><div class="h3">기대효과</div><div class="bt">
    <div class="bh">지표</div><div class="bh c">AS-IS</div><div class="bh c" style="color:var(--elec)">TO-BE</div><div class="bh legend">...</div><div class="bh rgt">변화</div>
    <div class="m">피크 대기 시간</div><div class="a c">18분</div><div class="t c">5분</div>
    <div class="bars2"><i class="as"></i><i class="to" style="--w:27.8%;--i:0"></i></div><div class="p rgt">-72%</div>
  </div></div>
  <div data-a><div class="h3">요청 사항</div><div class="asks">
    <div class="ask"><span class="no">01</span><span class="ok">승인</span><span class="fig">32억 원</span>
      <h4>요청 제목</h4><ul class="ul sub"><li>세부</li></ul></div></div></div>
</div>
```

`--w`는 TO-BE ÷ AS-IS 백분율이다. 등장할 때 막대가 100%에서 이 값으로 줄어든다. 줄어드는 게 좋은 지표(시간, 비용)에만 쓰고, 늘어나는 게 좋은 지표는 `.note`로 문장 처리한다.

## 14. 명세 표 + 필터

```html
<div class="toolbar" data-a><span class="cap">구분을 고르면 해당 행만 진하게 표시</span>
  <div class="seg" data-filter-target="#spec"><button type="button" data-f="">전체</button><button type="button" data-f="new">신규</button></div></div>
<table class="spec" id="spec" data-a>
  <thead><tr><th>계층</th><th>컴포넌트</th>...</tr></thead>
  <tbody>
    <tr data-kind="new"><td class="grp" rowspan="2">접근</td><td class="nm">이름</td><td>역할</td><td class="tech">기술</td><td>구성</td>
      <td class="k"><span class="kind new">신규</span></td><td class="c">담당</td></tr>
    <tr data-kind="keep" class="gl">...</tr>              <!-- 그룹 마지막 행 .gl -->
    <!-- 구분 칩: <span class="kind new|change|keep|ext">, ext는 점선(폐기 예정) -->
  </tbody>
</table>
```

행 높이 35, 12행 정도가 한 장의 한계다.

## 15. data 속성 요약

| 속성 | 위치 | 동작 |
|---|---|---|
| `data-a` | 아무 요소 | 슬라이드 진입 시 순서대로 등장 |
| `data-section`, `data-num`, `data-desc` | 간지(또는 섹션 첫 슬라이드) | 섹션 선언, 목차·간지·진행 막대 생성 |
| `data-title` | 슬라이드 | 목차·썸네일·진행 막대 툴팁 이름 |
| `data-toc="false"` | 슬라이드 | 목차에서 제외 |
| `data-hover-links` / `data-hover` | edges-host / 노드 | 가리킨 노드의 연결선 강조 |
| `data-focus` / `data-k` | 컨테이너 / 요소 | 같은 키끼리 강조, 나머지 흐림 |
| `.seg[data-view-target]` + `button[data-value]` | 툴바 | 대상에 `data-view` 설정, 슬라이드 안 `data-when` 표시 전환 |
| `.seg[data-filter-target]` + `button[data-f]` | 툴바 | 대상 안 `[data-kind]` 일치 행만 진하게 |
| `data-col-hover` / `data-col` | 컨테이너 / 셀 | 같은 열 강조(`.col-on`) |
| `data-cells`, `data-busy`, `data-label` | `.pool-box` | 칸 n개 생성, 일부 채움 |
| `.cells[data-n]` | 러너 블록 | 노드 칸 n개 |
| `data-count`, `data-dec` | 숫자 | 진입 시 0부터 올라감 |
| `data-flow-play` / `data-flow-elapsed` | 버튼 / 표시 칸 | 흐름 재생 |
| `class="tipped" data-tip="…"` | 아무 요소 | 가리키면 위에 남색 툴팁. 요소의 `::after`를 쓰므로 `::after`가 이미 있는 요소에는 못 쓴다 |
| `.bdg[data-tip]` | 배지 | 배지 전용 툴팁(오른쪽 위) |

## 16. 카탈로그에 없는 장표 만들기

경쟁사 비교, SWOT, 전략 체계도, 간트, 조직도처럼 템플릿에 없는 유형도 같은 재료로 짠다.

### 재료

- 레이아웃은 CSS grid로 짜고, 새 클래스에는 장표 접두어를 붙여 `<style>` 끝에 추가한다(`.gt-…`, `.swot-…`)
- 색은 토큰만 쓴다. 비교 대상 중 "우리" 열은 `--ice` 바탕 + `--elec` 머리칸, 나머지는 흰 바탕
- 표 머리행은 남색 채움 대신 굵은 글씨 + 1.5px 남색 밑줄, 행 구분은 `--line` 헤어라인
- 범례 색칸: `.legend i` 기본(흰), `.change` `.new` `.ext` `.soft` `.ink` `.issue` `.dia`(남색 마름모)
- 툴팁: `class="tipped" data-tip="문구"`
- 등장 모션: 있는 키프레임을 재사용한다. `rise`(아래에서 올라옴), `fade`, `bandgrow`(왼쪽에서 늘어남, `transform-origin:left`), `grow`(아래에서 자람). 반드시 `.anim .is-active` 아래에 걸고 fill-mode는 `backwards`로 쓴다. `both`나 `forwards`로 두면 끝난 뒤에도 모션 값이 남아 hover·보기 전환의 opacity를 덮는다
  ```css
  .gt-bar{transform-origin:left}
  .anim .is-active .gt-bar{animation:bandgrow .9s var(--ease) backwards;animation-delay:calc(300ms + var(--i,0) * 90ms)}
  ```
- 하비볼(●◕◑◔○)은 글꼴 의존이 크니 SVG 원과 `path`로 그린다
- 조직도·전략 체계도: 노드 종류를 그대로 쓰고 연결선 JSON으로 잇는다(`vhv` 경로가 트리에 맞다)

### 간트 예

```html
<div class="gt" data-a>                    <!-- 첫 열 220 + 월 12칸, 행 높이 44 → 10행이면 440 + 머리 36 -->
  <div class="gt-h"><span></span><span>1월</span>...<span>12월</span></div>
  <div class="gt-r"><span class="gt-n">브로커 6대 증설</span>
    <div class="gt-track"><i class="gt-bar tipped" style="--s:2;--n:3;--i:0" data-tip="2~4월 · 6대"></i>
      <i class="gt-ms" style="--m:5" title="전환 완료"></i></div></div>
</div>
```
```css
.gt-h,.gt-r{display:grid;grid-template-columns:220px 1fr}
.gt-h{grid-template-columns:220px repeat(12,1fr);font-size:15px;color:var(--slate);border-bottom:1.5px solid var(--ink);height:36px;align-items:center}
.gt-r{height:44px;align-items:center;border-bottom:1px solid var(--line)}
.gt-track{position:relative;height:100%}
.gt-bar{position:absolute;top:13px;height:18px;border-radius:9px;background:var(--soft);
  left:calc((var(--s) - 1) * 100% / 12);width:calc(var(--n) * 100% / 12)}
.gt-bar.key{background:var(--elec)}
.gt-ms{position:absolute;top:15px;width:14px;height:14px;background:var(--ink);transform:rotate(45deg);left:calc(var(--m) * 100% / 12 - 7px)}
```

아래 행의 툴팁이 윗행 라벨을 가리면 그 막대만 `tipped` 대신 막대 옆 작은 글씨 라벨로 바꾼다.

### 피해야 할 클래스 이름

템플릿 CSS가 이미 전역으로 쓰는 이름이다. 새 장표에서 같은 이름을 쓰면 위치·투명도·크기가 엉뚱하게 먹는다.

- 차트 SVG: `.bar` `.line` `.area` `.pt` `.pl` `.val` `.lab` `.grid` `.axis` `.target` `.cross` `.hit` `.chart`
- 공용 부품: `.tip`(전역 absolute, 투명) `.chip` `.hint` `.note` `.legend` `.status` `.panel` `.panels` `.zone` `.step` `.lane` `.lanes` `.cells` `.runner` `.stack` `.btn` `.seg` `.toolbar`
- 목차·타임라인: `.tl`(타임라인) `.tl-sec` `.tl-item`(목차) `.ev` `.tl-band`
- 노드 종류: `core` `new` `change` `ext` `muted` `db` `issue` `keep`

만든 뒤 반드시 shoot.py로 넘침과 겹침을 확인한다.
