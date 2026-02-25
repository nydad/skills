# Confluence Design System — 색상 팔레트 + ac:layout 패턴

## 1. 기본 팔레트 (Ocean Blue)

| 용도 | Hex |
|------|-----|
| 패널 헤더, 주요 테두리 | #2c5282 |
| 패널 배경 | #f7fafc |
| 미세한 테두리 | #e2e8f0 |
| Success | #38a169 |
| Warning | #dd6b20 |
| Error | #dc2626 |
| 탭 네비게이션 | #403294 |
| 링크 | #2684ff |

상태뱃지: Green/Yellow/Red/Blue/Grey (항상 subtle=true)

---

## 2. 테마별 색상 팔레트 (7종)

각 테마 7계층: Primary → Accent → Background → Surface → Border → Text → Muted

### Ocean Blue (기본)
`#2c5282` · `#3182ce` · `#eff6ff` · `#dbeafe` · `#93c5fd` · `#1e3a5f` · `#64748b`

패널: `titleBGColor=#2c5282|titleColor=#ffffff|bgColor=#eff6ff|borderColor=#2c5282`

### Forest Green (운영/모니터링)
`#276749` · `#38a169` · `#f0fdf4` · `#dcfce7` · `#86efac` · `#14532d` · `#6b7280`

패널: `titleBGColor=#276749|titleColor=#ffffff|bgColor=#f0fdf4|borderColor=#276749`

### Soft Purple (스터디/리서치)
`#553c9a` · `#6b46c1` · `#f5f3ff` · `#ede9fe` · `#c4b5fd` · `#3b0764` · `#78716c`

패널: `titleBGColor=#553c9a|titleColor=#ffffff|bgColor=#f5f3ff|borderColor=#553c9a`

### Warm Amber (보안/인시던트)
`#92400e` · `#d97706` · `#fffbeb` · `#fef3c7` · `#fbbf24` · `#78350f` · `#a16207`

패널: `titleBGColor=#92400e|titleColor=#ffffff|bgColor=#fffbeb|borderColor=#92400e`

### Slate Gray (보고서/회의록)
`#334155` · `#64748b` · `#f8fafc` · `#f1f5f9` · `#cbd5e1` · `#0f172a` · `#94a3b8`

패널: `titleBGColor=#334155|titleColor=#ffffff|bgColor=#f8fafc|borderColor=#334155`

### Soft Rose (마케팅/디자인)
`#9f1239` · `#e11d48` · `#fff1f2` · `#ffe4e6` · `#fda4af` · `#881337` · `#9ca3af`

패널: `titleBGColor=#9f1239|titleColor=#ffffff|bgColor=#fff1f2|borderColor=#9f1239`

### Teal (데이터/분석)
`#115e59` · `#14b8a6` · `#f0fdfa` · `#ccfbf1` · `#5eead4` · `#134e4a` · `#6b7280`

패널: `titleBGColor=#115e59|titleColor=#ffffff|bgColor=#f0fdfa|borderColor=#115e59`

---

## 3. 테마별 KPI 카드 색상

| 테마 | bgColor | borderColor |
|------|---------|-------------|
| Ocean Blue | #eff6ff | #2c5282 |
| Forest Green | #f0fdf4 | #276749 |
| Soft Purple | #f5f3ff | #553c9a |
| Warm Amber | #fffbeb | #92400e |
| Slate Gray | #f8fafc | #334155 |
| Soft Rose | #fff1f2 | #9f1239 |
| Teal | #f0fdfa | #115e59 |

---

## 4. XHTML 테이블 스타일링

헤더 배경색 + 교대 행:
```xml
<tr><th style="background-color: #2c5282; color: #ffffff;">헤더</th></tr>
<tr style="background-color: #f7fafc;"><td>교대 행</td></tr>
```

---

## 5. ac:layout 실전 XHTML 패턴

### 5.1 KPI 카드 3열 (three_equal + panel)
```xml
<ac:layout>
    <ac:layout-section ac:type="three_equal">
        <ac:layout-cell>
            <ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="kpi-1">
                <ac:parameter ac:name="bgColor">#f0fdf4</ac:parameter>
                <ac:parameter ac:name="borderColor">#22c55e</ac:parameter>
                <ac:parameter ac:name="borderWidth">2</ac:parameter>
                <ac:rich-text-body>
                    <h3><span style="color: #22c55e;">Uptime</span></h3>
                    <p style="font-size: 28px; font-weight: bold;">99.97%</p>
                    <p style="color: #6c757d;">Last 30 days</p>
                </ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
        <!-- 나머지 2개 셀도 동일 패턴, 색상만 변경 -->
    </ac:layout-section>
</ac:layout>
```

### 5.2 AS-IS / TO-BE 비교 (two_equal)
```xml
<ac:layout>
    <ac:layout-section ac:type="two_equal">
        <ac:layout-cell>
            <ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="asis-1">
                <ac:parameter ac:name="title">AS-IS</ac:parameter>
                <ac:parameter ac:name="titleBGColor">#dc2626</ac:parameter>
                <ac:parameter ac:name="titleColor">#ffffff</ac:parameter>
                <ac:parameter ac:name="bgColor">#fef2f2</ac:parameter>
                <ac:parameter ac:name="borderColor">#dc2626</ac:parameter>
                <ac:rich-text-body><p>현재 상태</p></ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
        <ac:layout-cell>
            <ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="tobe-1">
                <ac:parameter ac:name="title">TO-BE</ac:parameter>
                <ac:parameter ac:name="titleBGColor">#22c55e</ac:parameter>
                <ac:parameter ac:name="titleColor">#ffffff</ac:parameter>
                <ac:parameter ac:name="bgColor">#f0fdf4</ac:parameter>
                <ac:parameter ac:name="borderColor">#22c55e</ac:parameter>
                <ac:rich-text-body><p>목표 상태</p></ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```

### 5.3 사이드바 + 메인 (two_left_sidebar)
```xml
<ac:layout>
    <ac:layout-section ac:type="two_left_sidebar">
        <ac:layout-cell>
            <ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="side-1">
                <ac:parameter ac:name="title">Quick Info</ac:parameter>
                <ac:parameter ac:name="titleBGColor">#2c5282</ac:parameter>
                <ac:parameter ac:name="titleColor">#ffffff</ac:parameter>
                <ac:parameter ac:name="bgColor">#f7fafc</ac:parameter>
                <ac:rich-text-body>
                    <p><strong>Status:</strong> Production</p>
                    <p><strong>Owner:</strong> Platform Team</p>
                </ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
        <ac:layout-cell>
            <h2>상세 내용</h2>
            <p>70% 너비 메인 영역</p>
        </ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```

### 5.4 복합 대시보드 (single → three_equal → two_equal → single)
```xml
<ac:layout>
    <ac:layout-section ac:type="single">
        <ac:layout-cell><h1>대시보드</h1><hr /></ac:layout-cell>
    </ac:layout-section>
    <ac:layout-section ac:type="three_equal">
        <ac:layout-cell><!-- KPI 1 --></ac:layout-cell>
        <ac:layout-cell><!-- KPI 2 --></ac:layout-cell>
        <ac:layout-cell><!-- KPI 3 --></ac:layout-cell>
    </ac:layout-section>
    <ac:layout-section ac:type="two_equal">
        <ac:layout-cell><!-- 차트/그래프 --></ac:layout-cell>
        <ac:layout-cell><!-- 상세 테이블 --></ac:layout-cell>
    </ac:layout-section>
    <ac:layout-section ac:type="single">
        <ac:layout-cell><hr /><p style="color: #6c757d;">Last updated by Platform Team</p></ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```

### 5.5 ac:layout 내 section/column 중첩 (4열 이상 필요 시)
```xml
<ac:layout>
    <ac:layout-section ac:type="single">
        <ac:layout-cell>
            <ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="sec-1">
                <ac:rich-text-body>
                    <ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="col-1">
                        <ac:parameter ac:name="width">25%</ac:parameter>
                        <ac:rich-text-body><p>Col 1</p></ac:rich-text-body>
                    </ac:structured-macro>
                    <!-- col-2, col-3, col-4 동일 패턴 -->
                </ac:rich-text-body>
            </ac:structured-macro>
        </ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```
