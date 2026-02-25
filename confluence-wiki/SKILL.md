---
name: confluence-wiki
description: |
  Generates professional Confluence wiki documents. Optionally includes draw.io diagrams when architecture or structural visualization is needed.
  Supports ac:layout, section/column, 7 color themes, and 10+ diagram types.
  Triggers: /confluence, /wiki, /cwiki, confluence 문서, 위키 작성, 컨플루언스, 위키 문서 만들어줘, draw.io 다이어그램
---

# Confluence Wiki Document Generator v3

사용자 콘텐츠를 **일잘하는 직원 수준의** Confluence 위키 문서로 생성한다.
Draw.io 다이어그램은 **아키텍처, 시스템 구성도, 인프라 토폴로지 등 시각화가 필수인 경우에만** 생성하며, 최대 **1-2개**로 제한한다.

---

## PHASE 1: 분석 및 결정

### 1.1 문서 유형 → 출력 형식

| 유형 | 출력 형식 |
|------|-----------|
| 기술문서, 스터디, 보고서, 회의록 | Wiki Markup (.wiki) |
| 아키텍처, 대시보드, 온보딩, 발표 | XHTML (.xhtml) |
| 장애보고서 | XHTML (ac:layout 활용) |

**형식 판단 기준:**
- Wiki Markup: 텍스트+테이블+상태뱃지 위주, 코드블록 중심
- XHTML: ac:layout 필요, 탭 네비게이션, KPI 대시보드

### 1.2 Draw.io 다이어그램 필요 여부 판단

> **기본 원칙: 다이어그램은 선택사항이다.** 텍스트+테이블로 충분히 전달 가능하면 생성하지 않는다.

**생성하는 경우** (아래 조건에 해당할 때만):
- 시스템 아키텍처/인프라 구성을 시각적으로 설명해야 할 때
- 네트워크 토폴로지, 데이터 흐름 등 구조가 복잡하여 텍스트만으로 이해가 어려울 때
- 사용자가 명시적으로 다이어그램을 요청한 경우

**생성하지 않는 경우**:
- 회의록, 스터디 노트, 일반 보고서, 가이드 문서
- 단순 프로세스 (테이블이나 번호 목록으로 충분)
- 코드 설명, API 문서, 설정 가이드

**생성 시 제한: 문서당 최대 1-2개.** 가장 핵심적인 구조만 다이어그램으로 표현한다.

| 다이어그램 유형 | 판별 키워드 | pageSize |
|----------------|-------------|----------|
| 아키텍처 개요 | 시스템 구성, 인프라, 클라우드 | 1200x800 |
| 플로우차트 | 프로세스, 의사결정 분기, 승인 | 1000x600 |
| 네트워크 토폴로지 | 방화벽, VPN, DMZ, 서브넷 | 1400x900 |
| CI/CD 파이프라인 | 빌드, 배포, Jenkins, GitHub Actions | 1600x350 |
| 데이터 파이프라인 | ETL, 스트리밍, BigQuery, Kafka | 1400x500 |
| 마이크로서비스 | API Gateway, 서비스 메시, gRPC | 1400x900 |
| 스윔레인 | 부서간 협업, 역할별 프로세스 | 1200x800 |
| C4 모델 | Context, Container, Component | 1200x800 |
| ERD | 엔티티, 테이블, 관계 | 1200x900 |
| 쿠버네티스 | Pod, Deployment, Ingress, Helm | 1400x800 |
| 시퀀스형 | 요청/응답 흐름, API 호출 순서 | 1000x800 |

→ 다이어그램별 스타일 패턴: `references/drawio-diagram-templates.md`

### 1.3 색상 테마 선택

미지정 시 기본 Ocean Blue. → 상세 hex 값: `references/design-system.md`

| 테마 | Primary | Background | 권장 용도 |
|------|---------|------------|-----------|
| Ocean Blue | #2c5282 | #eff6ff | 기술문서, 아키텍처 |
| Forest Green | #276749 | #f0fdf4 | 운영, 모니터링 |
| Soft Purple | #553c9a | #f5f3ff | 스터디, 리서치 |
| Warm Amber | #92400e | #fffbeb | 보안, 인시던트 |
| Slate Gray | #334155 | #f8fafc | 보고서, 회의록 |
| Soft Rose | #9f1239 | #fff1f2 | 마케팅, 디자인 |
| Teal | #115e59 | #f0fdfa | 데이터, 분석 |

---

## PHASE 2: 문서 생성

### 2.1 출력물
```
{문서제목-kebab-case}.wiki 또는 .xhtml
{다이어그램명-kebab-case}.drawio (필요 시)
```

### 2.2 Confluence 고유 주의사항 (MUST READ)

모델이 이미 Wiki Markup/XHTML 문법을 알고 있으므로, **Confluence 서버 고유 함정**만 기록:

1. 줄 시작 `*` = 불릿으로 인식됨 → 줄 시작 볼드는 `{*}텍스트{*}` 사용
2. 상태뱃지: 반드시 `subtle=true` 사용, 테이블 `|`와 같은 줄 배치
3. `{code}` 매크로는 새 줄에서 시작 필수
4. **패널 중첩 금지** — 패널 안에 패널 넣으면 렌더링 깨짐
5. 특수문자 `[ ] { }` 는 `\`로 이스케이프
6. `{toc}` 반드시 독립 줄에 단독 배치
7. 링크: `[텍스트|URL]` (마크다운과 반대 순서)
8. 한 문서에 Wiki Markup과 XHTML 혼용 불가
9. ac:macro-id는 매크로마다 고유하게 (형식: `{기능}-{순번}`)
10. Draw.io 매크로의 `diagramName`은 .drawio 파일명(확장자 제외)과 정확히 일치

### 2.3 ac:layout 페이지 레이아웃 (XHTML 전용)

Confluence 기본 내장. 서드파티 앱 불필요.

```xml
<ac:layout>
    <ac:layout-section ac:type="TYPE">
        <ac:layout-cell>콘텐츠</ac:layout-cell>
    </ac:layout-section>
</ac:layout>
```

| 타입 | 비율 | 셀 수 | 대표 용도 |
|------|------|-------|-----------|
| `single` | 100% | 1 | 제목, TOC, 전체 테이블, 푸터 |
| `two_equal` | 50/50 | 2 | AS-IS/TO-BE, Before/After |
| `two_left_sidebar` | 30/70 | 2 | Quick Info + 메인 상세 |
| `two_right_sidebar` | 70/30 | 2 | 메인 + 사이드 참고 |
| `three_equal` | 33/33/33 | 3 | KPI 카드 3열 |
| `three_with_sidebars` | 20/60/20 | 3 | 양쪽 사이드바 + 중앙 |

**ac:layout vs section/column**: ac:layout은 고정 비율(최대 3열), section/column은 자유 비율(무제한 열). 페이지 전체 구조는 ac:layout, 특정 섹션 내 다단은 section/column. 중첩 가능.

**복합 레이아웃 패턴:**
```
대시보드:   single → three_equal → two_equal → single
기술문서:   single → two_left_sidebar → single → two_equal → single
장애보고서: single → three_equal → single → two_equal → single
```

→ ac:layout 실전 XHTML 패턴: `references/design-system.md` §5

### 2.4 Draw.io 매크로 삽입 (XHTML)
```xml
<ac:structured-macro ac:name="drawio" ac:schema-version="0" ac:macro-id="drawio-1">
    <ac:parameter ac:name="diagramName">파일명-확장자제외</ac:parameter>
    <ac:parameter ac:name="simpleViewer">false</ac:parameter>
    <ac:parameter ac:name="diagramWidth">1200</ac:parameter>
    <ac:parameter ac:name="lbox">true</ac:parameter>
    <ac:parameter ac:name="revision">1</ac:parameter>
</ac:structured-macro>
```

---

## PHASE 3: Draw.io 다이어그램 생성 (조건부)

> **§1.2에서 다이어그램이 필요하다고 판단된 경우에만 이 PHASE를 실행한다.**
> 다이어그램 불필요 시 PHASE 4로 건너뛴다.

### 3.1 디자인 원칙
1. 한 장 다이어그램 (멀티페이지 X)
2. 번호 매긴 화살표로 흐름 표시 (① ② ③)
3. 영역별 일관된 색상 코딩
4. 하단 요약 푸터 바 (핵심 포인트 colored dot)
5. 폰트 계층: 제목 20px > 이름 11px > 설명 9px > 서브 7px
6. 요소 간 최소 30px 간격, grid=10 기반 정렬

### 3.2 GCP 아이콘 + 스타일

→ prIcon 전체 목록, 컨테이너 스타일, 화살표 스타일, SVG 아이콘: `references/drawio-gcp-reference.md`

핵심 스타일 요약:

**GCP hexIcon:**
```
shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE;fillColor=#5184F3;strokeColor=none;
```

**주요 컬러:**
- GCP 아이콘: #5184F3, 연결선: #4284F3
- 외부 영역: fill=#f8f9fa, stroke=#dee2e6
- 내부 영역: fill=#f0fdf4, stroke=#22c55e
- 보안 영역: stroke=#f97316
- Region: fill=#fff2cc, stroke=#d6b656
- 성공: #22c55e, 실패: #ef4444

→ 다이어그램 유형별 셰이프/스타일 패턴: `references/drawio-diagram-templates.md`

---

## PHASE 4: 적용 가이드

출력 완료 후 반드시 안내:

- **Wiki Markup**: 에디터 `+` → "마크업 삽입" → "Confluence Wiki" 선택 → 붙여넣기
- **XHTML**: 에디터 `</>` (소스코드 에디터) → 붙여넣기 → 저장
- **Draw.io** (생성한 경우에만): 페이지에서 draw.io 매크로 삽입 → "Extras" → "Edit Diagram" (Ctrl+Shift+X) → XML 붙여넣기

---

## Design Constraints

| 규칙 | 제한 |
|------|------|
| h1 | 문서당 1회 |
| h2 | 3-7개 |
| 패널 | 최대 2개 (ac:layout 셀 내 패널은 별도) |
| 테이블 컬럼 | 최대 6 |
| 상태뱃지 | 항상 subtle=true |
| 패널 중첩 | 금지 |
| 색상 스키마 | 하나의 테마만 일관 유지 |
| Wiki+XHTML 혼용 | 금지 |
| 섹션 구분 | `----` 수평선 사용 |
| Draw.io 다이어그램 | 필요 시에만, 문서당 최대 1-2개 |

---

## Quality Checklist

- [ ] h1 1회, 매크로 태그 정상 열림/닫힘
- [ ] ac:macro-id 고유, 특수문자 이스케이프
- [ ] ac:layout-cell 수 = 레이아웃 타입 일치
- [ ] (Draw.io 포함 시) diagramName = .drawio 파일명 일치, XML well-formed, mxCell id 고유
- [ ] 색상이 선택 테마 팔레트 내에서 일관
- [ ] 상태뱃지 subtle=true, 패널 2개 이하

---

## Reference Files

- `references/drawio-gcp-reference.md` — GCP prIcon 목록, 스타일 문자열, SVG 아이콘, 컨테이너/화살표 패턴
- `references/drawio-diagram-templates.md` — 다이어그램 유형별 핵심 셰이프 스타일 (플로우차트, 네트워크, CI/CD 등)
- `references/design-system.md` — 7종 색상 팔레트 hex 값, ac:layout 실전 XHTML 패턴
