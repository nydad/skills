# Excalidraw Component Library

## Table of Contents

1. [Service Box](#1-service-box)
2. [Database / Data Store](#2-database--data-store)
3. [Message Queue / Event Bus](#3-message-queue--event-bus)
4. [Load Balancer / Router](#4-load-balancer--router)
5. [User / Client](#5-user--client)
6. [Cloud Provider Container](#6-cloud-provider-container)
7. [Labeled Arrow](#7-labeled-arrow)
8. [Layout Templates](#8-layout-templates)

---

## 1. Service Box

Standard rectangle with bound text label. Used for services, apps, APIs, and modules.

```json
[
  {
    "id": "svc-example",
    "type": "rectangle",
    "x": 100,
    "y": 200,
    "width": 180,
    "height": 70,
    "strokeColor": "#40c057",
    "backgroundColor": "#b2f2bb",
    "fillStyle": "solid",
    "strokeWidth": 2,
    "strokeStyle": "solid",
    "roughness": 1,
    "opacity": 100,
    "angle": 0,
    "groupIds": [],
    "frameId": null,
    "index": "a0",
    "roundness": { "type": 3 },
    "seed": 100001,
    "version": 1,
    "versionNonce": 200001,
    "isDeleted": false,
    "boundElements": [
      { "id": "svc-example-label", "type": "text" }
    ],
    "updated": 1700000000000,
    "link": null,
    "locked": false
  },
  {
    "id": "svc-example-label",
    "type": "text",
    "x": 130,
    "y": 220,
    "width": 120,
    "height": 30,
    "angle": 0,
    "strokeColor": "#1e1e1e",
    "backgroundColor": "transparent",
    "fillStyle": "solid",
    "strokeWidth": 1,
    "strokeStyle": "solid",
    "roughness": 0,
    "opacity": 100,
    "groupIds": [],
    "frameId": null,
    "index": "a1",
    "roundness": null,
    "seed": 100002,
    "version": 1,
    "versionNonce": 200002,
    "isDeleted": false,
    "boundElements": null,
    "updated": 1700000000000,
    "link": null,
    "locked": false,
    "text": "API Gateway",
    "fontSize": 18,
    "fontFamily": 1,
    "textAlign": "center",
    "verticalAlign": "middle",
    "containerId": "svc-example",
    "originalText": "API Gateway",
    "autoResize": true,
    "lineHeight": 1.25
  }
]
```

**Variants by layer** -- change `strokeColor` and `backgroundColor`:
- UI: `#339af0` / `#a5d8ff`
- API: `#40c057` / `#b2f2bb`
- Service: `#fa5252` / `#ffc9c9`
- Data: `#fd7e14` / `#ffd8a8`
- Infra: `#7950f2` / `#d0bfff`
- External: `#868e96` / `#e9ecef`

---

## 2. Database / Data Store

Ellipse shape to visually distinguish data stores from services.

```json
[
  {
    "id": "db-postgres",
    "type": "ellipse",
    "x": 300,
    "y": 500,
    "width": 160,
    "height": 80,
    "strokeColor": "#fd7e14",
    "backgroundColor": "#ffd8a8",
    "fillStyle": "solid",
    "strokeWidth": 2,
    "strokeStyle": "solid",
    "roughness": 1,
    "opacity": 100,
    "angle": 0,
    "groupIds": [],
    "frameId": null,
    "index": "a2",
    "roundness": { "type": 2 },
    "seed": 100003,
    "version": 1,
    "versionNonce": 200003,
    "isDeleted": false,
    "boundElements": [
      { "id": "db-postgres-label", "type": "text" }
    ],
    "updated": 1700000000000,
    "link": null,
    "locked": false
  },
  {
    "id": "db-postgres-label",
    "type": "text",
    "x": 330,
    "y": 525,
    "width": 100,
    "height": 30,
    "angle": 0,
    "strokeColor": "#1e1e1e",
    "backgroundColor": "transparent",
    "fillStyle": "solid",
    "strokeWidth": 1,
    "strokeStyle": "solid",
    "roughness": 0,
    "opacity": 100,
    "groupIds": [],
    "frameId": null,
    "index": "a3",
    "roundness": null,
    "seed": 100004,
    "version": 1,
    "versionNonce": 200004,
    "isDeleted": false,
    "boundElements": null,
    "updated": 1700000000000,
    "link": null,
    "locked": false,
    "text": "PostgreSQL",
    "fontSize": 16,
    "fontFamily": 1,
    "textAlign": "center",
    "verticalAlign": "middle",
    "containerId": "db-postgres",
    "originalText": "PostgreSQL",
    "autoResize": true,
    "lineHeight": 1.25
  }
]
```

**Also use ellipse for:** Redis, MongoDB, S3, Elasticsearch, any data store.

---

## 3. Message Queue / Event Bus

Rectangle with yellow/amber theme and a distinctive label pattern.

```json
[
  {
    "id": "mq-kafka",
    "type": "rectangle",
    "x": 500,
    "y": 350,
    "width": 200,
    "height": 50,
    "strokeColor": "#fab005",
    "backgroundColor": "#fff3bf",
    "fillStyle": "solid",
    "strokeWidth": 2,
    "strokeStyle": "solid",
    "roughness": 1,
    "opacity": 100,
    "angle": 0,
    "groupIds": [],
    "frameId": null,
    "index": "a4",
    "roundness": { "type": 3 },
    "seed": 100005,
    "version": 1,
    "versionNonce": 200005,
    "isDeleted": false,
    "boundElements": [
      { "id": "mq-kafka-label", "type": "text" }
    ],
    "updated": 1700000000000,
    "link": null,
    "locked": false
  },
  {
    "id": "mq-kafka-label",
    "type": "text",
    "x": 540,
    "y": 360,
    "width": 120,
    "height": 30,
    "angle": 0,
    "strokeColor": "#1e1e1e",
    "backgroundColor": "transparent",
    "fillStyle": "solid",
    "strokeWidth": 1,
    "strokeStyle": "solid",
    "roughness": 0,
    "opacity": 100,
    "groupIds": [],
    "frameId": null,
    "index": "a5",
    "roundness": null,
    "seed": 100006,
    "version": 1,
    "versionNonce": 200006,
    "isDeleted": false,
    "boundElements": null,
    "updated": 1700000000000,
    "link": null,
    "locked": false,
    "text": "Kafka",
    "fontSize": 16,
    "fontFamily": 1,
    "textAlign": "center",
    "verticalAlign": "middle",
    "containerId": "mq-kafka",
    "originalText": "Kafka",
    "autoResize": true,
    "lineHeight": 1.25
  }
]
```

**Also use this pattern for:** RabbitMQ, SQS, EventBridge, NATS, Pub/Sub.

---

## 4. Load Balancer / Router

Diamond shape for decision/routing points.

```json
[
  {
    "id": "lb-main",
    "type": "diamond",
    "x": 400,
    "y": 100,
    "width": 120,
    "height": 100,
    "strokeColor": "#7950f2",
    "backgroundColor": "#d0bfff",
    "fillStyle": "solid",
    "strokeWidth": 2,
    "strokeStyle": "solid",
    "roughness": 1,
    "opacity": 100,
    "angle": 0,
    "groupIds": [],
    "frameId": null,
    "index": "a6",
    "roundness": { "type": 2 },
    "seed": 100007,
    "version": 1,
    "versionNonce": 200007,
    "isDeleted": false,
    "boundElements": [
      { "id": "lb-main-label", "type": "text" }
    ],
    "updated": 1700000000000,
    "link": null,
    "locked": false
  },
  {
    "id": "lb-main-label",
    "type": "text",
    "x": 420,
    "y": 135,
    "width": 80,
    "height": 30,
    "angle": 0,
    "strokeColor": "#1e1e1e",
    "backgroundColor": "transparent",
    "fillStyle": "solid",
    "strokeWidth": 1,
    "strokeStyle": "solid",
    "roughness": 0,
    "opacity": 100,
    "groupIds": [],
    "frameId": null,
    "index": "a7",
    "roundness": null,
    "seed": 100008,
    "version": 1,
    "versionNonce": 200008,
    "isDeleted": false,
    "boundElements": null,
    "updated": 1700000000000,
    "link": null,
    "locked": false,
    "text": "LB",
    "fontSize": 16,
    "fontFamily": 1,
    "textAlign": "center",
    "verticalAlign": "middle",
    "containerId": "lb-main",
    "originalText": "LB",
    "autoResize": true,
    "lineHeight": 1.25
  }
]
```

**Also use diamond for:** API Router, CDN edge, DNS resolver.

---

## 5. User / Client

Rectangle with distinct external/gray styling to represent external actors.

```json
[
  {
    "id": "user-client",
    "type": "rectangle",
    "x": 50,
    "y": 50,
    "width": 140,
    "height": 60,
    "strokeColor": "#868e96",
    "backgroundColor": "#e9ecef",
    "fillStyle": "solid",
    "strokeWidth": 2,
    "strokeStyle": "solid",
    "roughness": 1,
    "opacity": 100,
    "angle": 0,
    "groupIds": [],
    "frameId": null,
    "index": "a8",
    "roundness": { "type": 3 },
    "seed": 100009,
    "version": 1,
    "versionNonce": 200009,
    "isDeleted": false,
    "boundElements": [
      { "id": "user-client-label", "type": "text" }
    ],
    "updated": 1700000000000,
    "link": null,
    "locked": false
  },
  {
    "id": "user-client-label",
    "type": "text",
    "x": 70,
    "y": 65,
    "width": 100,
    "height": 30,
    "angle": 0,
    "strokeColor": "#1e1e1e",
    "backgroundColor": "transparent",
    "fillStyle": "solid",
    "strokeWidth": 1,
    "strokeStyle": "solid",
    "roughness": 0,
    "opacity": 100,
    "groupIds": [],
    "frameId": null,
    "index": "a9",
    "roundness": null,
    "seed": 100010,
    "version": 1,
    "versionNonce": 200010,
    "isDeleted": false,
    "boundElements": null,
    "updated": 1700000000000,
    "link": null,
    "locked": false,
    "text": "Browser",
    "fontSize": 16,
    "fontFamily": 1,
    "textAlign": "center",
    "verticalAlign": "middle",
    "containerId": "user-client",
    "originalText": "Browser",
    "autoResize": true,
    "lineHeight": 1.25
  }
]
```

---

## 6. Cloud Provider Container

Large dashed rectangle that encloses child components, with a title label.

```json
[
  {
    "id": "container-aws",
    "type": "rectangle",
    "x": 80,
    "y": 120,
    "width": 800,
    "height": 500,
    "strokeColor": "#7950f2",
    "backgroundColor": "#f3f0ff",
    "fillStyle": "solid",
    "strokeWidth": 2,
    "strokeStyle": "dashed",
    "roughness": 0,
    "opacity": 40,
    "angle": 0,
    "groupIds": [],
    "frameId": null,
    "index": "Z0",
    "roundness": { "type": 3 },
    "seed": 100011,
    "version": 1,
    "versionNonce": 200011,
    "isDeleted": false,
    "boundElements": null,
    "updated": 1700000000000,
    "link": null,
    "locked": false
  },
  {
    "id": "container-aws-title",
    "type": "text",
    "x": 100,
    "y": 130,
    "width": 200,
    "height": 30,
    "angle": 0,
    "strokeColor": "#7950f2",
    "backgroundColor": "transparent",
    "fillStyle": "solid",
    "strokeWidth": 1,
    "strokeStyle": "solid",
    "roughness": 0,
    "opacity": 100,
    "groupIds": [],
    "frameId": null,
    "index": "Z1",
    "roundness": null,
    "seed": 100012,
    "version": 1,
    "versionNonce": 200012,
    "isDeleted": false,
    "boundElements": null,
    "updated": 1700000000000,
    "link": null,
    "locked": false,
    "text": "AWS Cloud",
    "fontSize": 20,
    "fontFamily": 1,
    "textAlign": "left",
    "verticalAlign": "top",
    "containerId": null,
    "originalText": "AWS Cloud",
    "autoResize": true,
    "lineHeight": 1.25
  }
]
```

**Key rules for containers:**
- Set `index` to a value that sorts BEFORE child elements (e.g., `"Z0"` sorts before `"a0"`)
- Use `opacity: 40` so children are clearly visible on top
- Use `strokeStyle: "dashed"` for visual container distinction
- Use `roughness: 0` for clean container borders
- Title text is a separate, unbound text element positioned at top-left inside

**Also use for:** VPC, Kubernetes Cluster, Subnet, Region, Availability Zone.

---

## 7. Labeled Arrow

Arrow connecting two elements with a text label.

```json
[
  {
    "id": "arrow-api-to-db",
    "type": "arrow",
    "x": 290,
    "y": 235,
    "width": 200,
    "height": 280,
    "angle": 0,
    "strokeColor": "#495057",
    "backgroundColor": "transparent",
    "fillStyle": "solid",
    "strokeWidth": 2,
    "strokeStyle": "solid",
    "roughness": 1,
    "opacity": 100,
    "groupIds": [],
    "frameId": null,
    "index": "b0",
    "roundness": { "type": 2 },
    "seed": 100013,
    "version": 1,
    "versionNonce": 200013,
    "isDeleted": false,
    "boundElements": [
      { "id": "arrow-api-to-db-label", "type": "text" }
    ],
    "updated": 1700000000000,
    "link": null,
    "locked": false,
    "points": [[0, 0], [200, 280]],
    "startBinding": {
      "elementId": "svc-example",
      "focus": 0,
      "gap": 5,
      "fixedPoint": null
    },
    "endBinding": {
      "elementId": "db-postgres",
      "focus": 0,
      "gap": 5,
      "fixedPoint": null
    },
    "startArrowhead": null,
    "endArrowhead": "arrow",
    "elbowed": true
  },
  {
    "id": "arrow-api-to-db-label",
    "type": "text",
    "x": 340,
    "y": 365,
    "width": 60,
    "height": 20,
    "angle": 0,
    "strokeColor": "#495057",
    "backgroundColor": "#ffffff",
    "fillStyle": "solid",
    "strokeWidth": 1,
    "strokeStyle": "solid",
    "roughness": 0,
    "opacity": 100,
    "groupIds": [],
    "frameId": null,
    "index": "b1",
    "roundness": null,
    "seed": 100014,
    "version": 1,
    "versionNonce": 200014,
    "isDeleted": false,
    "boundElements": null,
    "updated": 1700000000000,
    "link": null,
    "locked": false,
    "text": "SQL",
    "fontSize": 14,
    "fontFamily": 1,
    "textAlign": "center",
    "verticalAlign": "middle",
    "containerId": "arrow-api-to-db",
    "originalText": "SQL",
    "autoResize": true,
    "lineHeight": 1.25
  }
]
```

**Common arrow labels:** REST, gRPC, GraphQL, SQL, Redis, HTTP, WebSocket, Event, Pub/Sub, S3.

---

## 8. Layout Templates

### 8.1 Three-Tier Architecture (Top-Down)

```
Y=50:   [        Title Text         ]
Y=120:  |---- Frontend Container ----|  (x=80, w=800)
Y=180:     [React App]   [Admin UI]
Y=320:  |---- API Container ---------|
Y=380:     [API GW]  [Auth Svc]
Y=520:  |---- Data Container ---------|
Y=580:     (PostgreSQL)  (Redis)
```

**Coordinates guide:**
- Canvas width: ~1000px, centered content
- Each layer container: x=80, width=800
- Layer spacing: 200px between container tops
- Component spacing: 40px horizontal gap within layer
- Container height: 140-160px per layer

### 8.2 Microservices Grid

```
Y=50:   [        Title Text         ]
Y=100:  |------ Gateway Layer -------|
Y=160:     [API Gateway]   ◇[LB]
Y=300:  |------ Services Layer ------|
Y=360:     [Svc A]  [Svc B]  [Svc C]
Y=460:     [Svc D]  [Svc E]  [Svc F]
Y=620:  |------ Data Layer ---------|
Y=680:     (DB A)   (DB B)  (Cache)
```

**Grid rules:**
- Services arranged in rows of 3-4
- Horizontal gap: 60px
- Vertical gap: 40px within same layer
- Each service box: 160x70px

### 8.3 Pipeline / Data Flow (Left-to-Right)

```
X=50      X=300     X=550     X=800     X=1050
[Source] → [Ingest] → [Process] → [Store] → [Serve]
  ↓          ↓          ↓          ↓          ↓
(Raw DB)  (Queue)   (Spark)    (DW)     (API)
```

**Pipeline rules:**
- Horizontal spacing: 250px between stages
- Each stage is a service box: 180x70px
- Arrows: elbowed, left-to-right
- Supporting components (databases, queues) positioned 100px below their stage

### 8.4 Hub-Spoke (Central Event Bus)

```
             [Svc A]
               ↑
[Svc D] ← [Event Bus] → [Svc B]
               ↓
             [Svc C]
```

**Hub-spoke rules:**
- Central element at canvas center (x=400, y=300)
- Spoke elements at 200-250px radius
- Arrows: all connect to/from central hub
- Use dashed arrows for async event connections
