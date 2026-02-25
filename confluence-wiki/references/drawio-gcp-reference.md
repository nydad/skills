# Draw.io GCP 스타일 레퍼런스 — 아이콘 + 스타일 문자열

모델이 draw.io XML 구조(`<mxfile>`, `<mxGraphModel>`, `<mxCell>`)를 알고 있으므로 생략.
여기에는 **모델이 외울 수 없는 정확한 스타일 값과 아이콘 이름**만 기록.

---

## 1. GCP hexIcon 스타일

**독립 아이콘 (50x42, 라벨 아래):**
```
html=1;fillColor=#5184F3;strokeColor=none;verticalAlign=top;labelPosition=center;
verticalLabelPosition=bottom;align=center;spacingTop=-6;fontSize=11;fontStyle=1;
fontColor=#999999;shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE_NAME
```

**카드 내 아이콘 (44x39, 라벨 오른쪽):**
```
dashed=0;connectable=0;html=1;fillColor=#5184F3;strokeColor=none;
shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE_NAME;part=1;labelPosition=right;
verticalLabelPosition=middle;align=left;verticalAlign=middle;spacingLeft=5;
fontColor=#999999;fontSize=12;
```

---

## 2. prIcon 전체 목록

### Compute
compute_engine, app_engine, cloud_functions, cloud_run, container_engine, container_optimized_os, gpu, gke_on_prem

### Storage & Database
cloud_storage, cloud_sql, cloud_bigtable, cloud_spanner, cloud_datastore, cloud_firestore, cloud_memorystore, cloud_filestore, persistent_disk, transfer_appliance

### Networking
cloud_load_balancing, cloud_dns, cloud_cdn, virtual_private_cloud, cloud_vpn, cloud_nat, cloud_armor, cloud_router, cloud_network, cloud_external_ip_addresses, cloud_routes, cloud_firewall_rules, dedicated_interconnect, partner_interconnect, standard_network_tier, premium_network_tier, traffic_director, cloud_service_mesh

### Data & Analytics
bigquery, cloud_dataflow, cloud_pubsub, cloud_dataproc, cloud_dataprep, cloud_datalab, cloud_data_catalog, cloud_data_fusion, data_studio, genomics

### AI & Machine Learning
cloud_machine_learning, cloud_vision_api, cloud_natural_language_api, cloud_translation_api, cloud_speech_api, cloud_video_intelligence_api, cloud_jobs_api, ai_hub, automl_vision, automl_natural_language, automl_translation, automl_tables, automl_video_intelligence, recommendations_ai, cloud_inference_api

### Security & Identity
cloud_iam, key_management_service, cloud_security_scanner, data_loss_prevention_api, cloud_armor, beyondcorp, identity_aware_proxy, security_key_enforcement

### Developer Tools
container_builder, container_registry, cloud_test_lab, cloud_code, cloud_tools_for_powershell

### Operations
stackdriver, cloud_deployment_manager, logging, error_reporting, trace, profiler, cloud_apis, cloud_tasks

### API Management
api_analytics, apigee_sense, api_monetization, cloud_endpoints, apigee_api_platform, developer_portal

### IoT
cloud_iot_core, cloud_iot_edge

---

## 3. GCP 디바이스 아이콘

```
shape=mxgraph.gcp2.laptop           노트북 (38x25)
shape=mxgraph.gcp2.phone            모바일 (22x35)
shape=mxgraph.gcp2.users            사용자 그룹 (35x22)
shape=mxgraph.gcp2.desktop_and_mobile  데스크탑+모바일
shape=mxgraph.gcp2.application      애플리케이션
shape=mxgraph.gcp2.database         데이터베이스
shape=mxgraph.gcp2.storage          스토리지
shape=mxgraph.gcp2.report           리포트
shape=mxgraph.gcp2.google_cloud_platform  GCP 로고 뱃지
```

디바이스 기본 스타일:
```
dashed=0;html=1;fillColor=#757575;strokeColor=none;labelPosition=center;
verticalLabelPosition=bottom;align=center;verticalAlign=top;fontSize=11;fontColor=#999999;
```

---

## 4. 컨테이너 스타일

**GCP 플랫폼 컨테이너:**
```
fillColor=#F6F6F6;strokeColor=none;shadow=0;fontSize=14;align=left;spacing=10;
fontColor=#717171;verticalAlign=top;spacingTop=-4;fontStyle=0;spacingLeft=40;html=1;
```
→ GCP 로고 뱃지: `shape=mxgraph.gcp2.google_cloud_platform;fillColor=#F6F6F6;strokeColor=none;` (32x32)

**Region:**
```
rounded=1;absoluteArcSize=1;arcSize=2;html=1;strokeColor=#d6b656;fillColor=#fff2cc;
fontSize=12;align=left;verticalAlign=top;spacing=10;spacingTop=-4;
```

**Network/VPC:**
```
rounded=1;absoluteArcSize=1;arcSize=2;html=1;strokeColor=#d79b00;fillColor=#ffe6cc;
fontSize=12;align=left;verticalAlign=top;spacing=10;spacingTop=-4;
```

**Subnet:**
```
rounded=1;absoluteArcSize=1;arcSize=2;html=1;strokeColor=#666666;fillColor=#f5f5f5;
fontSize=12;fontColor=#333333;align=left;verticalAlign=top;spacing=10;spacingTop=-4;
```

**Dashed Zone (논리 그룹):**
```
strokeColor=#4284F3;dashed=1;strokeWidth=2;fillColor=none;fontSize=14;fontColor=#4284F3;
verticalAlign=top;align=left;spacingLeft=10;spacingTop=-4;html=1;rounded=1;arcSize=2;
```

**커스텀 영역:**
```
외부:  fillColor=#f8f9fa;strokeColor=#dee2e6;strokeWidth=2;rounded=1;verticalAlign=top;arcSize=8;
내부:  fillColor=#f0fdf4;strokeColor=#22c55e;strokeWidth=2;rounded=1;verticalAlign=top;arcSize=4;
보안:  fillColor=#ffffff;strokeColor=#f97316;strokeWidth=2;rounded=1;arcSize=6;
카드:  fillColor=#ffffff;strokeColor=#2684ff;strokeWidth=2;rounded=1;arcSize=8;
```

---

## 5. 화살표 스타일

```
실선 (주요 흐름):    endArrow=classic;html=1;rounded=0;strokeColor=#4284F3;strokeWidth=2;
점선 (외부/선택):    endArrow=classic;html=1;rounded=0;strokeColor=#9ca3af;strokeWidth=2;dashed=1;dashPattern=5 3;
직각 라우팅:         edgeStyle=orthogonalEdgeStyle;strokeColor=#4284F3;strokeWidth=1;
곡선 반환 (loop):   endArrow=classic;html=1;rounded=1;strokeColor=#22c55e;strokeWidth=2;
```

**번호 레이블 (화살표 위):**
```
edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];
fontSize=9;fontStyle=1;fontColor=#2684ff;
```
→ parent를 화살표 id로 설정, `<mxGeometry x="-0.1" relative="1">` + `<mxPoint y="-12" as="offset" />`

---

## 6. 텍스트 스타일

```
제목 (20px):   text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=20;fontStyle=1;fontColor=#1a1a2e;
영역 라벨:     text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=10;fontStyle=1;fontColor=#COLOR;letterSpacing=2;
컴포넌트명:    text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;fontSize=11;fontStyle=1;fontColor=#1a1a2e;
부가 설명:     text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;fontSize=9;fontColor=#6c757d;
서브 라벨:     text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=bottom;fontSize=7;fontColor=#a3a3a3;
```

---

## 7. 요약 푸터 바

```xml
<!-- 배경 -->
style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#e2e8f0;strokeWidth=1;arcSize=15;"

<!-- colored dot -->
style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=8;fontColor=#22c55e;"
→ value="●"

<!-- 포인트 텍스트 -->
style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=10;fontColor=#475569;"
```
포인트 간격: x 좌표 약 240px씩 증가

---

## 8. 서비스 카드 패턴

```xml
<!-- 카드 컨테이너 -->
style="strokeColor=#dddddd;shadow=1;strokeWidth=1;rounded=1;absoluteArcSize=1;arcSize=2;"

<!-- 카드 내 아이콘 (parent=카드ID) -->
style="dashed=0;connectable=0;html=1;fillColor=#5184F3;strokeColor=none;
shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE;part=1;labelPosition=right;
verticalLabelPosition=middle;align=left;verticalAlign=middle;spacingLeft=5;
fontColor=#999999;fontSize=12;"
→ <mxGeometry width="44" height="39" relative="1"><mxPoint x="5" y="11" as="offset"/></mxGeometry>
```

---

## 9. 도구 카드 + Pass/Fail 패턴

**도구 카드:**
```
rounded=1;fillColor=#fef3c7;strokeColor=#fbbf24;strokeWidth=1;fontSize=9;fontStyle=1;fontColor=#92400e;arcSize=15;
```

**Pass 인디케이터:**
```
dot:   ellipse;aspect=fixed;fillColor=#22c55e;strokeColor=none; (12x12)
label: fontSize=11;fontStyle=1;fontColor=#166534;
```

**Fail 인디케이터:**
```
dot:   ellipse;aspect=fixed;fillColor=#ef4444;strokeColor=none; (12x12)
label: fontSize=11;fontStyle=1;fontColor=#dc2626;
```

---

## 10. GCP 컬러 팔레트 요약

| 용도 | Hex |
|------|-----|
| 아이콘 채움 | #5184F3 |
| 연결선 | #4284F3 |
| 컨테이너 배경 | #F6F6F6 |
| 컨테이너 라벨 | #717171 |
| 서비스 라벨 | #999999 |
| 카드 테두리 | #dddddd |
| Region fill/stroke | #fff2cc / #d6b656 |
| Network fill/stroke | #ffe6cc / #d79b00 |
| Subnet fill/stroke | #f5f5f5 / #666666 |
| 디바이스 | #757575 |
| 외부 fill/stroke | #f8f9fa / #dee2e6 |
| 내부 fill/stroke | #f0fdf4 / #22c55e |
| 보안 stroke | #f97316 |
| 성공 | #22c55e |
| 실패 | #ef4444 |
| 도구카드 fill/stroke/text | #fef3c7 / #fbbf24 / #92400e |
