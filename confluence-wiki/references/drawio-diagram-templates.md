# Draw.io Diagram Type Shape Styles

The model already knows draw.io XML structure. Only **type-specific shape styles** and **color guides** are documented here.

**Table of Contents**
- §1 Flowchart
- §2 Network Topology
- §3 CI/CD Pipeline
- §4 Data Pipeline
- §5 Microservices Architecture
- §6 Swimlane (Cross-functional)
- §7 C4 Model
- §8 ERD (Entity Relationship)
- §9 Kubernetes Deployment
- §10 Sequence Diagram
- §11 Additional SVG Inline Icons
- §12 Architecture Overview

---

## §1 Flowchart

**Key shapes:**
```
Start/End (ellipse):       ellipse;whiteSpace=wrap;html=1;fillColor=#4284F3;fontColor=#ffffff;strokeColor=none;
Process (rounded rect):    rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4284F3;strokeWidth=2;arcSize=10;
Decision (diamond):        rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;strokeWidth=2;
I/O (parallelogram):       shape=parallelogram;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#22c55e;
```

**Arrows:** Solid `strokeColor=#4284F3;strokeWidth=2;`, Yes/No labels `fontSize=9;fontStyle=1;fontColor=#22c55e` / `fontColor=#dc2626`

---

## §2 Network Topology

**Layered containers (top → bottom):**
```
Internet zone:   fillColor=#f8f9fa;strokeColor=#dee2e6;rounded=1;verticalAlign=top;
DMZ zone:        fillColor=#fffbeb;strokeColor=#d97706;rounded=1;verticalAlign=top;
Internal zone:   fillColor=#f0fdf4;strokeColor=#22c55e;rounded=1;verticalAlign=top;
```

**Key icons:** Firewall=Shield SVG(#f97316), LB=`cloud_load_balancing`, Server=`compute_engine`, DB=`cloud_sql`

**Arrows:** External→DMZ dashed(#9ca3af dashed), DMZ→Internal solid(#4284F3), Blocked red-dashed(#dc2626 dashed)

---

## §3 CI/CD Pipeline

**Horizontal flow (left → right), stage cards:**
```
Stage card:        rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4284F3;strokeWidth=2;arcSize=8;
Active stage:      rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2c5282;strokeWidth=2;arcSize=8;fontStyle=1;
Gate (diamond):    rhombus;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#fbbf24;strokeWidth=2;fontSize=9;
```

**Stage labels:** ① Source → ② Build → ③ Test → ④ Stage → ⑤ Deploy → ⑥ Monitor
**Pass/Fail:** Circle indicator fillColor=#22c55e (Pass) / #ef4444 (Fail)

---

## §4 Data Pipeline

**Key shapes:**
```
Data source (cylinder):    shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#dbeafe;strokeColor=#2c5282;size=15;
Transform process:         rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#22c55e;strokeWidth=2;
Streaming (lightning):     shape=mxgraph.electrical.signal_sources.ac_source;fillColor=#fbbf24;strokeColor=#92400e;
Data warehouse:            shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2c5282;size=20;strokeWidth=2;
```

**Flow:** Extract(gray) → Transform(green) → Load(blue) → Serve(purple)
**GCP services:** `cloud_pubsub`, `cloud_dataflow`, `bigquery`, `cloud_storage`

---

## §5 Microservices Architecture

**Key shapes:**
```
API Gateway:      rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2c5282;strokeWidth=2;arcSize=4;fontStyle=1;
Service card:     rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#4284F3;strokeWidth=1;arcSize=8;shadow=1;
Message queue:    shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;size=10;
Service mesh:     strokeColor=#14b8a6;dashed=1;strokeWidth=2;fillColor=none;rounded=1;arcSize=4;verticalAlign=top;
```

**Communication patterns:** Sync(solid #4284F3), Async(dashed #d97706), Event(dashed #22c55e)
**GCP services:** `cloud_run`, `container_engine`, `cloud_pubsub`, `cloud_load_balancing`

---

## §6 Swimlane (Cross-functional)

**Lane structure:**
```
Lane header:             fillColor=#2c5282;fontColor=#ffffff;fontStyle=1;fontSize=12;verticalAlign=middle;
Lane area:               fillColor=none;strokeColor=#e2e8f0;strokeWidth=1;
Alternating lane bg:     fillColor=#f8fafc;strokeColor=#e2e8f0;
```

**Dividers:** Horizontal `line;strokeWidth=1;strokeColor=#e2e8f0;`, Vertical timeline `strokeColor=#cbd5e1;dashed=1;`
**Processes:** Rounded rect (standard), Diamond (decision), Document shape (deliverable)

---

## §7 C4 Model

**Level-specific shapes:**
```
Person:              shape=mxgraph.c4.person2;html=1;fillColor=#08427B;fontColor=#ffffff;
System (internal):   rounded=1;whiteSpace=wrap;html=1;fillColor=#438DD5;fontColor=#ffffff;strokeColor=none;arcSize=10;
System (external):   rounded=1;whiteSpace=wrap;html=1;fillColor=#999999;fontColor=#ffffff;strokeColor=none;arcSize=10;
Container:           rounded=1;whiteSpace=wrap;html=1;fillColor=#438DD5;fontColor=#ffffff;strokeColor=#3C7FC0;arcSize=10;
Component:           rounded=1;whiteSpace=wrap;html=1;fillColor=#85BBF0;fontColor=#000000;strokeColor=#78A8D8;arcSize=10;
DB Container:        shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#438DD5;fontColor=#ffffff;strokeColor=#3C7FC0;size=15;
```

**Boundary box:** `strokeColor=#444444;dashed=1;strokeWidth=2;fillColor=none;fontSize=16;fontStyle=1;verticalAlign=bottom;`
**Arrows:** `strokeColor=#666666;strokeWidth=1;` + description label `fontSize=9;fontColor=#666666;`

---

## §8 ERD (Entity Relationship)

**Entity (table style):**
```
Header:    swimlane;fontStyle=1;align=center;startSize=26;html=1;fillColor=#2c5282;fontColor=#ffffff;strokeColor=#2c5282;rounded=1;arcSize=4;
Row:       text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;fontSize=11;html=1;
PK row:    text;strokeColor=none;fillColor=#eff6ff;align=left;verticalAlign=middle;spacingLeft=4;fontSize=11;fontStyle=1;html=1;
```

**Relationship lines:**
```
1:1  endArrow=ERone;startArrow=ERone;strokeColor=#4284F3;
1:N  endArrow=ERmany;startArrow=ERone;strokeColor=#4284F3;
M:N  endArrow=ERmany;startArrow=ERmany;strokeColor=#4284F3;
```

---

## §9 Kubernetes Deployment

**Layered containers:**
```
Cluster:     fillColor=#326CE5;strokeColor=none;fontColor=#ffffff;rounded=1;arcSize=4;verticalAlign=top;fontStyle=1;
Namespace:   fillColor=#E8F0FE;strokeColor=#326CE5;dashed=1;rounded=1;arcSize=4;verticalAlign=top;
Node:        fillColor=#ffffff;strokeColor=#326CE5;strokeWidth=2;rounded=1;arcSize=4;verticalAlign=top;
```

**Workloads:**
```
Deployment:   rounded=1;fillColor=#ffffff;strokeColor=#326CE5;strokeWidth=2;arcSize=8;
Pod:          rounded=1;fillColor=#E8F0FE;strokeColor=#326CE5;strokeWidth=1;arcSize=15;fontSize=10;
Service:      shape=hexagon;fillColor=#326CE5;fontColor=#ffffff;strokeColor=none;size=0.15;
Ingress:      shape=trapezoid;fillColor=#326CE5;fontColor=#ffffff;strokeColor=none;size=0.2;
ConfigMap:    rounded=1;fillColor=#fef3c7;strokeColor=#d97706;arcSize=4;fontSize=10;
Secret:       rounded=1;fillColor=#fda4af;strokeColor=#9f1239;arcSize=4;fontSize=10;
```

**K8s colors:** Primary=#326CE5, Light=#E8F0FE

---

## §10 Sequence Diagram

**Key shapes:**
```
Participant box:     rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#2c5282;strokeWidth=2;arcSize=4;fontStyle=1;
Lifeline:            endArrow=none;dashed=1;strokeColor=#cbd5e1;strokeWidth=1;
Activation box:      fillColor=#dbeafe;strokeColor=#2c5282;strokeWidth=1;
```

**Message arrows:**
```
Sync request:    endArrow=block;strokeColor=#4284F3;strokeWidth=2;endFill=1;
Sync response:   endArrow=open;strokeColor=#4284F3;strokeWidth=1;dashed=1;
Async:           endArrow=open;strokeColor=#22c55e;strokeWidth=1;dashed=1;dashPattern=5 3;
```

**Labels:** `fontSize=9;fontStyle=1;fontColor=#2c5282;` placed above arrows

---

## §11 Additional SVG Inline Icons

Base64-encoded icons that the model cannot generate. Use `shape=image;image=data:image/svg+xml,BASE64;` format.

**Person** fill=#374151:
```
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzM3NDE1MSI+PGNpcmNsZSBjeD0iMTIiIGN5PSI4IiByPSI0Ii8+PHBhdGggZD0iTTEyIDEyYy00LjQyIDAtOCAyLjI0LTggNXYzaDEydi0zYzAtMi43Ni0zLjU4LTUtOC01eiIvPjwvc3ZnPg==
```

**Monitor (Computer)** fill=#6466f1:
```
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iIzY0NjZmMSI+PHBhdGggZD0iTTIwIDNINGMtMS4xIDAtMiAuOS0yIDJ2MTFjMCAxLjEuOSAyIDIgMmg3bC0yIDNoNmwtMi0zaDdjMS4xIDAgMi0uOSAyLTJWNWMwLTEuMS0uOS0yLTItMnptMCAxM0g0VjVoMTZ2MTF6Ii8+PC9zdmc+
```

**Shield (Security)** fill=#f97316:
```
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iI2Y5NzMxNiI+PHBhdGggZD0iTTEyIDFMMyA1djZjMCA1LjU1IDMuODQgMTAuNzQgOSAxMiA1LjE2LTEuMjYgOS02LjQ1IDktMTJWNWwtOS00em0wIDEwLjk5aDdjLS41MyA0LjEyLTMuMjggNy43OS03IDguOTRWMTJINXYtNS43bDctMy4xMXY4LjhoeiIvPjwvc3ZnPg==
```

SVG icon style:
```
shape=image;verticalLabelPosition=bottom;labelBackgroundColor=default;verticalAlign=top;aspect=fixed;imageAspect=0;image=data:image/svg+xml,BASE64;
```

> **GCP device icons:** See `drawio-gcp-reference.md` §3 for the full list of built-in GCP device shapes (`mxgraph.gcp2.laptop`, `mxgraph.gcp2.phone`, etc.).

---

## §12 Architecture Overview

> Covers "Architecture Overview" in SKILL.md §1.2. Use for system topology, cloud infrastructure, and high-level service maps.

**pageSize: 1200x800**

**Layered zone containers (top → bottom or outside → inside):**
```
External zone:   fillColor=#f8f9fa;strokeColor=#dee2e6;strokeWidth=2;rounded=1;verticalAlign=top;arcSize=8;
GCP Platform:    fillColor=#F6F6F6;strokeColor=none;shadow=0;fontSize=14;align=left;verticalAlign=top;spacingTop=-4;spacingLeft=40;html=1;fontColor=#717171;
Region:          rounded=1;absoluteArcSize=1;arcSize=2;html=1;strokeColor=#d6b656;fillColor=#fff2cc;fontSize=12;align=left;verticalAlign=top;spacing=10;spacingTop=-4;
Network/VPC:     rounded=1;absoluteArcSize=1;arcSize=2;html=1;strokeColor=#d79b00;fillColor=#ffe6cc;fontSize=12;align=left;verticalAlign=top;spacing=10;spacingTop=-4;
Internal zone:   fillColor=#f0fdf4;strokeColor=#22c55e;strokeWidth=2;rounded=1;verticalAlign=top;arcSize=4;
```

**Service components (GCP hexIcon):**
```
shape=mxgraph.gcp2.hexIcon;prIcon=SERVICE_NAME;fillColor=#5184F3;strokeColor=none;
```
→ See `drawio-gcp-reference.md` §1-2 for full hexIcon style and prIcon list.

**Typical layout:**
1. External zone (users, external services) at top or left
2. GCP Platform container wrapping Region → VPC → Subnet layers
3. Service cards with hexIcons inside subnet zones
4. Numbered arrows (① ② ③) showing request/data flow
5. Summary footer bar at bottom with key points

**Arrows:**
```
User → LB:        endArrow=classic;strokeColor=#9ca3af;strokeWidth=2;dashed=1;dashPattern=5 3;
LB → Service:     endArrow=classic;strokeColor=#4284F3;strokeWidth=2;
Service → DB:     endArrow=classic;strokeColor=#4284F3;strokeWidth=2;
Cross-region:     endArrow=classic;strokeColor=#22c55e;strokeWidth=2;dashed=1;
```

**Font hierarchy:** Title 20px > Zone label 12px > Service name 11px > Description 9px > Sub 7px
