# Draw.io GCP Style Reference — Icons + Style Strings

The model already knows draw.io XML structure (`<mxfile>`, `<mxGraphModel>`, `<mxCell>`), so that is omitted.
Only **exact style values and icon names that the model cannot memorize** are documented here.

**Table of Contents**
- §1 GCP hexIcon Style
- §2 Full prIcon List
- §3 GCP Device Icons
- §4 Container Styles
- §5 Arrow Styles
- §6 Text Styles
- §7 Summary Footer Bar
- §8 Service Card Pattern
- §9 Tool Card + Pass/Fail Pattern
- §10 GCP Color Palette Summary

---

## 1. GCP hexIcon Style

**Standalone icon (50x42, label below):**
```
html=1;fillColor=#5184F3;strokeColor=none;verticalAlign=top;labelPosition=center;
verticalLabelPosition=bottom;align=center;spacingTop=-6;fontSize=11;fontStyle=1;
fontColor=#999999;shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE_NAME
```

**In-card icon (44x39, label right):**
```
dashed=0;connectable=0;html=1;fillColor=#5184F3;strokeColor=none;
shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE_NAME;part=1;labelPosition=right;
verticalLabelPosition=middle;align=left;verticalAlign=middle;spacingLeft=5;
fontColor=#999999;fontSize=12;
```

---

## 2. Full prIcon List

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

## 3. GCP Device Icons

```
shape=mxgraph.gcp2.laptop           Laptop (38x25)
shape=mxgraph.gcp2.phone            Mobile (22x35)
shape=mxgraph.gcp2.users            User group (35x22)
shape=mxgraph.gcp2.desktop_and_mobile  Desktop+Mobile
shape=mxgraph.gcp2.application      Application
shape=mxgraph.gcp2.database         Database
shape=mxgraph.gcp2.storage          Storage
shape=mxgraph.gcp2.report           Report
shape=mxgraph.gcp2.google_cloud_platform  GCP logo badge
```

Device default style:
```
dashed=0;html=1;fillColor=#757575;strokeColor=none;labelPosition=center;
verticalLabelPosition=bottom;align=center;verticalAlign=top;fontSize=11;fontColor=#999999;
```

---

## 4. Container Styles

**GCP Platform container:**
```
fillColor=#F6F6F6;strokeColor=none;shadow=0;fontSize=14;align=left;spacing=10;
fontColor=#717171;verticalAlign=top;spacingTop=-4;fontStyle=0;spacingLeft=40;html=1;
```
→ GCP logo badge: `shape=mxgraph.gcp2.google_cloud_platform;fillColor=#F6F6F6;strokeColor=none;` (32x32)

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

**Dashed Zone (logical group):**
```
strokeColor=#4284F3;dashed=1;strokeWidth=2;fillColor=none;fontSize=14;fontColor=#4284F3;
verticalAlign=top;align=left;spacingLeft=10;spacingTop=-4;html=1;rounded=1;arcSize=2;
```

**Custom zones:**
```
External:  fillColor=#f8f9fa;strokeColor=#dee2e6;strokeWidth=2;rounded=1;verticalAlign=top;arcSize=8;
Internal:  fillColor=#f0fdf4;strokeColor=#22c55e;strokeWidth=2;rounded=1;verticalAlign=top;arcSize=4;
Security:  fillColor=#ffffff;strokeColor=#f97316;strokeWidth=2;rounded=1;arcSize=6;
Card:      fillColor=#ffffff;strokeColor=#2684ff;strokeWidth=2;rounded=1;arcSize=8;
```

---

## 5. Arrow Styles

```
Solid (main flow):       endArrow=classic;html=1;rounded=0;strokeColor=#4284F3;strokeWidth=2;
Dashed (external/opt):   endArrow=classic;html=1;rounded=0;strokeColor=#9ca3af;strokeWidth=2;dashed=1;dashPattern=5 3;
Orthogonal routing:      edgeStyle=orthogonalEdgeStyle;strokeColor=#4284F3;strokeWidth=1;
Curved return (loop):    endArrow=classic;html=1;rounded=1;strokeColor=#22c55e;strokeWidth=2;
```

**Numbered labels (on arrows):**
```
edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];
fontSize=9;fontStyle=1;fontColor=#2684ff;
```
→ Set parent to arrow ID, `<mxGeometry x="-0.1" relative="1">` + `<mxPoint y="-12" as="offset" />`

---

## 6. Text Styles

```
Title (20px):        text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=20;fontStyle=1;fontColor=#1a1a2e;
Zone label:          text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=10;fontStyle=1;fontColor=#COLOR;letterSpacing=2;
Component name:      text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;fontSize=11;fontStyle=1;fontColor=#1a1a2e;
Description:         text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=top;fontSize=9;fontColor=#6c757d;
Sub label:           text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=bottom;fontSize=7;fontColor=#a3a3a3;
```

---

## 7. Summary Footer Bar

```xml
<!-- Background -->
style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#e2e8f0;strokeWidth=1;arcSize=15;"

<!-- Colored dot -->
style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=8;fontColor=#22c55e;"
→ value="●"

<!-- Point text -->
style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=10;fontColor=#475569;"
```
Point spacing: x-coordinate increments of ~240px

---

## 8. Service Card Pattern

```xml
<!-- Card container -->
style="strokeColor=#dddddd;shadow=1;strokeWidth=1;rounded=1;absoluteArcSize=1;arcSize=2;"

<!-- In-card icon (parent=cardID) -->
style="dashed=0;connectable=0;html=1;fillColor=#5184F3;strokeColor=none;
shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE;part=1;labelPosition=right;
verticalLabelPosition=middle;align=left;verticalAlign=middle;spacingLeft=5;
fontColor=#999999;fontSize=12;"
→ <mxGeometry width="44" height="39" relative="1"><mxPoint x="5" y="11" as="offset"/></mxGeometry>
```

---

## 9. Tool Card + Pass/Fail Pattern

**Tool card:**
```
rounded=1;fillColor=#fef3c7;strokeColor=#fbbf24;strokeWidth=1;fontSize=9;fontStyle=1;fontColor=#92400e;arcSize=15;
```

**Pass indicator:**
```
dot:   ellipse;aspect=fixed;fillColor=#22c55e;strokeColor=none; (12x12)
label: fontSize=11;fontStyle=1;fontColor=#166534;
```

**Fail indicator:**
```
dot:   ellipse;aspect=fixed;fillColor=#ef4444;strokeColor=none; (12x12)
label: fontSize=11;fontStyle=1;fontColor=#dc2626;
```

---

## 10. GCP Color Palette Summary

| Purpose | Hex |
|---------|-----|
| Icon fill | #5184F3 |
| Connector | #4284F3 |
| Container background | #F6F6F6 |
| Container label | #717171 |
| Service label | #999999 |
| Card border | #dddddd |
| Region fill/stroke | #fff2cc / #d6b656 |
| Network fill/stroke | #ffe6cc / #d79b00 |
| Subnet fill/stroke | #f5f5f5 / #666666 |
| Device | #757575 |
| External fill/stroke | #f8f9fa / #dee2e6 |
| Internal fill/stroke | #f0fdf4 / #22c55e |
| Security stroke | #f97316 |
| Success | #22c55e |
| Failure | #ef4444 |
| Tool card fill/stroke/text | #fef3c7 / #fbbf24 / #92400e |
