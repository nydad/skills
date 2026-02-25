# Draw.io 다이어그램 유형별 핵심 셰이프 스타일

모델이 draw.io XML 구조를 이미 알고 있으므로, 각 다이어그램 유형별 **고유 셰이프 스타일**과 **색상 가이드**만 기록.

---

## §1 플로우차트 (Flowchart)

**핵심 셰이프:**
```
시작/종료 (원형):    ellipse;whiteSpace=wrap;html=1;fillColor=#4284F3;fontColor=#ffffff;strokeColor=none;
프로세스 (둥근사각):  rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4284F3;strokeWidth=2;arcSize=10;
분기점 (마름모):     rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;strokeWidth=2;
입출력 (평행사변형):  shape=parallelogram;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#22c55e;
```

**화살표:** 실선 `strokeColor=#4284F3;strokeWidth=2;`, Yes/No 레이블 `fontSize=9;fontStyle=1;fontColor=#22c55e` / `fontColor=#dc2626`

---

## §2 네트워크 토폴로지

**계층 컨테이너 (위→아래):**
```
Internet 영역:   fillColor=#f8f9fa;strokeColor=#dee2e6;rounded=1;verticalAlign=top;
DMZ 영역:        fillColor=#fffbeb;strokeColor=#d97706;rounded=1;verticalAlign=top;
Internal 영역:   fillColor=#f0fdf4;strokeColor=#22c55e;rounded=1;verticalAlign=top;
```

**핵심 아이콘:** Firewall=방패SVG(#f97316), LB=`cloud_load_balancing`, Server=`compute_engine`, DB=`cloud_sql`

**화살표:** 외부→DMZ 점선(#9ca3af dashed), DMZ→Internal 실선(#4284F3), 차단 빨간점선(#dc2626 dashed)

---

## §3 CI/CD 파이프라인

**가로 흐름 (좌→우), 단계 카드:**
```
단계 카드:       rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4284F3;strokeWidth=2;arcSize=8;
활성 단계:       rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2c5282;strokeWidth=2;arcSize=8;fontStyle=1;
게이트 (다이아):  rhombus;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#fbbf24;strokeWidth=2;fontSize=9;
```

**단계 라벨:** ① Source → ② Build → ③ Test → ④ Stage → ⑤ Deploy → ⑥ Monitor
**Pass/Fail:** 원형 인디케이터 fillColor=#22c55e (Pass) / #ef4444 (Fail)

---

## §4 데이터 파이프라인

**핵심 셰이프:**
```
데이터소스 (실린더):   shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#dbeafe;strokeColor=#2c5282;size=15;
변환 프로세스:         rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#22c55e;strokeWidth=2;
스트리밍 (번개):       shape=mxgraph.electrical.signal_sources.ac_source;fillColor=#fbbf24;strokeColor=#92400e;
데이터 웨어하우스:     shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2c5282;size=20;strokeWidth=2;
```

**흐름:** Extract(회색) → Transform(녹색) → Load(파랑) → Serve(보라)
**GCP 서비스:** `cloud_pubsub`, `cloud_dataflow`, `bigquery`, `cloud_storage`

---

## §5 마이크로서비스 아키텍처

**핵심 셰이프:**
```
API Gateway:     rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2c5282;strokeWidth=2;arcSize=4;fontStyle=1;
서비스 카드:      rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4284F3;strokeWidth=1;arcSize=8;shadow=1;
메시지 큐:       shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;size=10;
서비스 메시:      strokeColor=#14b8a6;dashed=1;strokeWidth=2;fillColor=none;rounded=1;arcSize=4;verticalAlign=top;
```

**통신 패턴:** 동기(실선 #4284F3), 비동기(점선 #d97706), 이벤트(점선 #22c55e)
**GCP 서비스:** `cloud_run`, `container_engine`, `cloud_pubsub`, `cloud_load_balancing`

---

## §6 스윔레인 (Cross-functional)

**레인 구성:**
```
레인 헤더:       fillColor=#2c5282;fontColor=#ffffff;fontStyle=1;fontSize=12;verticalAlign=middle;
레인 영역:       fillColor=none;strokeColor=#e2e8f0;strokeWidth=1;
교대 레인 배경:   fillColor=#f8fafc;strokeColor=#e2e8f0;
```

**구분선:** 가로 `line;strokeWidth=1;strokeColor=#e2e8f0;` , 세로 시간축 `strokeColor=#cbd5e1;dashed=1;`
**프로세스:** 둥근 사각형(일반), 마름모(분기), 문서 셰이프(산출물)

---

## §7 C4 모델

**레벨별 셰이프:**
```
Person:          shape=mxgraph.c4.person2;html=1;fillColor=#08427B;fontColor=#ffffff;
시스템 (내부):    rounded=1;whiteSpace=wrap;html=1;fillColor=#438DD5;fontColor=#ffffff;strokeColor=none;arcSize=10;
시스템 (외부):    rounded=1;whiteSpace=wrap;html=1;fillColor=#999999;fontColor=#ffffff;strokeColor=none;arcSize=10;
Container:       rounded=1;whiteSpace=wrap;html=1;fillColor=#438DD5;fontColor=#ffffff;strokeColor=#3C7FC0;arcSize=10;
Component:       rounded=1;whiteSpace=wrap;html=1;fillColor=#85BBF0;fontColor=#000000;strokeColor=#78A8D8;arcSize=10;
DB Container:    shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#438DD5;fontColor=#ffffff;strokeColor=#3C7FC0;size=15;
```

**경계 박스:** `strokeColor=#444444;dashed=1;strokeWidth=2;fillColor=none;fontSize=16;fontStyle=1;verticalAlign=bottom;`
**화살표:** `strokeColor=#666666;strokeWidth=1;` + 설명 라벨 `fontSize=9;fontColor=#666666;`

---

## §8 ERD (Entity Relationship)

**엔티티 (테이블 스타일):**
```
헤더:    swimlane;fontStyle=1;align=center;startSize=26;html=1;fillColor=#2c5282;fontColor=#ffffff;strokeColor=#2c5282;rounded=1;arcSize=4;
행:      text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;fontSize=11;html=1;
PK 행:  text;strokeColor=none;fillColor=#eff6ff;align=left;verticalAlign=middle;spacingLeft=4;fontSize=11;fontStyle=1;html=1;
```

**관계선:**
```
1:1  endArrow=ERone;startArrow=ERone;strokeColor=#4284F3;
1:N  endArrow=ERmany;startArrow=ERone;strokeColor=#4284F3;
M:N  endArrow=ERmany;startArrow=ERmany;strokeColor=#4284F3;
```

---

## §9 쿠버네티스 배포

**계층 컨테이너:**
```
Cluster:     fillColor=#326CE5;strokeColor=none;fontColor=#ffffff;rounded=1;arcSize=4;verticalAlign=top;fontStyle=1;
Namespace:   fillColor=#E8F0FE;strokeColor=#326CE5;dashed=1;rounded=1;arcSize=4;verticalAlign=top;
Node:        fillColor=#ffffff;strokeColor=#326CE5;strokeWidth=2;rounded=1;arcSize=4;verticalAlign=top;
```

**워크로드:**
```
Deployment:   rounded=1;fillColor=#ffffff;strokeColor=#326CE5;strokeWidth=2;arcSize=8;
Pod:          rounded=1;fillColor=#E8F0FE;strokeColor=#326CE5;strokeWidth=1;arcSize=15;fontSize=10;
Service:      shape=hexagon;fillColor=#326CE5;fontColor=#ffffff;strokeColor=none;size=0.15;
Ingress:      shape=trapezoid;fillColor=#326CE5;fontColor=#ffffff;strokeColor=none;size=0.2;
ConfigMap:    rounded=1;fillColor=#fef3c7;strokeColor=#d97706;arcSize=4;fontSize=10;
Secret:       rounded=1;fillColor=#fda4af;strokeColor=#9f1239;arcSize=4;fontSize=10;
```

**K8s 색상:** Primary=#326CE5, Light=#E8F0FE

---

## §10 시퀀스형 다이어그램

**핵심 셰이프:**
```
참여자 박스:    rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2c5282;strokeWidth=2;arcSize=4;fontStyle=1;
라이프라인:    endArrow=none;dashed=1;strokeColor=#cbd5e1;strokeWidth=1;
활성화 박스:   fillColor=#dbeafe;strokeColor=#2c5282;strokeWidth=1;
```

**메시지 화살표:**
```
동기 요청:    endArrow=block;strokeColor=#4284F3;strokeWidth=2;endFill=1;
동기 응답:    endArrow=open;strokeColor=#4284F3;strokeWidth=1;dashed=1;
비동기:       endArrow=open;strokeColor=#22c55e;strokeWidth=1;dashed=1;dashPattern=5 3;
```

**레이블:** `fontSize=9;fontStyle=1;fontColor=#2c5282;` 화살표 위에 배치

---

## §11 추가 SVG 인라인 아이콘

모델이 생성할 수 없는 base64 인코딩 아이콘. `shape=image;image=data:image/svg+xml,BASE64;` 형식 사용.

**사용자 (Person)** fill=#374151:
```
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzM3NDE1MSI+PGNpcmNsZSBjeD0iMTIiIGN5PSI4IiByPSI0Ii8+PHBhdGggZD0iTTEyIDEyYy00LjQyIDAtOCAyLjI0LTggNXYzaDEydi0zYzAtMi43Ni0zLjU4LTUtOC01eiIvPjwvc3ZnPg==
```

**모니터 (Computer)** fill=#6466f1:
```
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzY0NjZmMSI+PHBhdGggZD0iTTIwIDNINGMtMS4xIDAtMiAuOS0yIDJ2MTFjMCAxLjEuOSAyIDIgMmg3bC0yIDNoNmwtMi0zaDdjMS4xIDAgMi0uOSAyLTJWNWMwLTEuMS0uOS0yLTItMnptMCAxM0g0VjVoMTZ2MTF6Ii8+PC9zdmc+
```

**방패 (Security)** fill=#f97316:
```
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iI2Y5NzMxNiI+PHBhdGggZD0iTTEyIDFMMyA1djZjMCA1LjU1IDMuODQgMTAuNzQgOSAxMiA1LjE2LTEuMjYgOS02LjQ1IDktMTJWNWwtOS00em0wIDEwLjk5aDdjLS41MyA0LjEyLTMuMjggNy43OS03IDguOTRWMTJINXYtNS43bDctMy4xMXY4LjhoeiIvPjwvc3ZnPg==
```

SVG 아이콘 스타일:
```
shape=image;verticalLabelPosition=bottom;labelBackgroundColor=default;verticalAlign=top;aspect=fixed;imageAspect=0;image=data:image/svg+xml,BASE64;
```

GCP 디바이스 아이콘 (내장):
```
shape=mxgraph.gcp2.laptop           노트북 (38x25)
shape=mxgraph.gcp2.phone            모바일 (22x35)
shape=mxgraph.gcp2.users            사용자 그룹 (35x22)
shape=mxgraph.gcp2.application      애플리케이션
shape=mxgraph.gcp2.database         데이터베이스
```
