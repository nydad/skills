---
name: meta-loop-protocol
description: "Meta Loop Protocol — /loop 장기 자율 작업용 판단 프레임워크. 인자로 작업을 전달하면 자동 Setup + /loop 시작. Context Drift, Monotonic Escalation, Literal Execution, Session Amnesia 방지. Windows Git Bash 호환."
user-invocable: true
args: "[작업 설명]"
---

# Meta Loop Protocol

에이전트를 **실행자에서 판단자로** 전환하는 프레임워크. `/loop` 장기 자율 작업의 4가지 실패 모드를 방지한다.

| 실패 모드 | 증상 | 해결책 |
|-----------|------|--------|
| Context Drift | 수정된 코드가 새 기준선이 됨 | BASELINE.md — 원본 스냅샷과 항상 비교 |
| Monotonic Escalation | "개선" = "숫자 증가" | Self-Audit — 인플레이션 감지, 재보정 |
| Literal Execution | 지시 그대로만 수행, 설계 의도 무시 | WHY.md — 목적과 철학 앵커 |
| Session Amnesia | 세션 리셋 시 판단 맥락 소실 | PROGRESS.md + DECISIONS.md — 배턴 전달 |

---

## 실행 흐름 (자동)

사용자가 `/meta-loop-protocol [작업 설명]`을 입력하면:

### A) `.meta-loop/` 없음 → 자동 Setup + 시작

1. **Hook 설치** — `.claude/hooks/`에 스크립트 3개 복사, `settings.json`에 등록
2. **외부 메모리 초기화** — `.meta-loop/` 디렉토리 생성
3. **WHY.md 자동 생성** — 사용자 인자에서 목적/원칙 추론. 핵심 사항이 불명확하면 1-2개 질문
4. **BASELINE.md 자동 생성** — 프로젝트 현재 상태 스냅샷
5. **작업 주입** — 사용자 인자를 `loop-prompt.md`의 Specific Work Instructions에 자동 삽입
6. **`/loop` 자동 시작** — `Skill("loop", args="5m cat .meta-loop/loop-prompt.md")` 호출

> Hooks는 세션 시작 시 로드되므로 첫 실행에서는 hook 경고가 동작하지 않음.
> 하지만 **loop-prompt.md의 프로토콜 지시가 1차 메커니즘**이므로 작업 수행에는 문제 없음.
> 다음 세션부터 hooks가 자동 활성화됨.

### B) `.meta-loop/` 있음 → 즉시 Runtime

1. **작업 주입** — 사용자 인자가 있으면 `loop-prompt.md`의 Specific Work Instructions 업데이트
2. **`/loop` 자동 시작** — 즉시 시작

### C) 인자 없이 실행 → Runtime (기존 작업 계속)

1. `.meta-loop/` 확인. 없으면 에러: "작업 설명을 인자로 전달하세요"
2. 있으면 기존 `loop-prompt.md`로 `/loop` 자동 시작

---

## Setup 상세 (Phase A에서 자동 수행)

### Hook 스크립트

이 스킬의 `scripts/` 디렉토리에서 3개 파일을 읽어 프로젝트의 `.claude/hooks/`에 복사:

| File | Event | Purpose |
|------|-------|---------|
| check-progress.sh | PreToolUse (Edit\|Write\|MultiEdit) | PROGRESS.md에 iteration objective 없으면 경고 |
| checkpoint.sh | Stop | iteration 종료 시 체크포인트 알림 |
| audit-trigger.sh | PostToolUse (Edit\|Write\|MultiEdit) | N회 edit마다 self-audit 트리거 |

> Windows 환경 — `chmod` 불필요. Git Bash가 .sh 직접 실행.

### settings.json Hook 등록

프로젝트의 `.claude/settings.json`을 읽고(없으면 `{}` 시작) 아래 hooks를 **병합** — 기존 hooks 덮어쓰지 않음:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [{"type": "command", "command": "bash {PROJECT_ROOT}/.claude/hooks/check-progress.sh"}]
      }
    ],
    "Stop": [
      {
        "hooks": [{"type": "command", "command": "bash {PROJECT_ROOT}/.claude/hooks/checkpoint.sh"}]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [{"type": "command", "command": "bash {PROJECT_ROOT}/.claude/hooks/audit-trigger.sh"}]
      }
    ]
  }
}
```

> **`{PROJECT_ROOT}`**: 설치 시 실제 프로젝트 절대경로로 치환 (예: `E:/workspace/my-project`).
> Hook 실행 시 CWD가 프로젝트 루트가 아닐 수 있어 절대경로 필수.
> Hook 스크립트 내부에서 `.meta-loop/` 디렉토리를 PWD 기준 상향 탐색하므로 git 의존 없음.

### 외부 메모리 파일

`.meta-loop/` 디렉토리를 프로젝트 루트에 생성:

#### WHY.md (North Star — immutable)

사용자 인자에서 아래 항목을 추론하여 자동 생성:

```markdown
# WHY — North Star

## Purpose
(사용자 인자에서 추론한 작업 목적)

## Success Criteria
(사용자 인자에서 추론한 성공 기준)

## Non-Negotiable Principles
(코드베이스 분석에서 추론한 핵심 원칙)

## Scope Boundaries
(사용자 인자에서 추론한 범위 제한)
```

추론이 불확실한 항목이 있으면 사용자에게 1-2개 질문.
WHY.md 작성 후 사용자에게 보여주고 확인 요청.
확인 후에는 **절대 수정하지 않음** (immutable).

#### BASELINE.md (Origin Snapshot — immutable)

프로젝트 현재 상태를 자동 서베이:
- 디렉토리/파일 구조
- 핵심 수치 값 (밸런스, 성능 메트릭 등)
- 코어 아키텍처/패턴
- 알려진 이슈

#### PROGRESS.md, DECISIONS.md, AUDIT.md, .gitignore

기본 템플릿으로 자동 생성.

### loop-prompt.md 자동 구성

이 스킬의 `references/loop-prompt-template.md`에서 템플릿을 읽어 `.meta-loop/loop-prompt.md`로 복사하되,
`<!-- Add project-specific work instructions below -->` 부분을 **사용자 인자의 작업 설명**으로 대체.

---

## Runtime Protocol

`.meta-loop/`가 이미 존재할 때 매 loop iteration에서 따르는 프로토콜.
상세는 `references/runtime-protocol.md`, self-audit은 `references/self-audit.md` 참조.

### Iteration 순서 (필수 — 건너뛸 수 없음)

1. **WHY.md 읽기** → 목적 확인
2. **PROGRESS.md 읽기** → 현재 상태와 다음 작업 파악
3. **DECISIONS.md 읽기** → 이전 판단 검토 (반복/번복 방지)
4. **BASELINE.md vs 현재 상태 비교** → delta 계산
5. **PROGRESS.md에 이번 iteration objective 기록** → 작업 시작
6. **판단 시마다 DECISIONS.md 기록**
7. **완료 후 PROGRESS.md 업데이트** → 다음 작업 명시
8. **컨텍스트가 길면 /compact 자율 실행**

### 판단 원칙

- "이 변경이 WHY.md의 의도에 부합하는가?"
- "BASELINE 대비 올바른 방향인가?"
- "값이 한쪽으로만 올라가는가 (인플레이션)?"
- "자기 검증이 필요한 시점인가?"

WHY.md 의도에서 벗어나는 변경은 하지 않음.
Monotonic escalation 감지 시 BASELINE 기준으로 재보정.
복잡한 변경은 subagent로 Writer/Reviewer 분리.
/compact, /simplify 등 자율 사용.
리소스 무제한 — 정확성을 위한 전체 프로젝트 재분석 허용.

### Self-Audit

PostToolUse hook이 N회 edit마다 자동 트리거. 상세는 `references/self-audit.md`.

---

## /loop 자동 시작

Setup 또는 작업 주입 완료 후, 아래를 자동 실행:

```
Skill("loop", args="5m cat .meta-loop/loop-prompt.md")
```

interval 기본값: 5분. 사용자가 인자에서 interval을 명시하면 해당 값 사용.
예: `/meta-loop-protocol 10m Dragon 밸런스 조정` → 10분 interval.

---

## Deactivation / Cleanup

프로토콜 제거:

1. `.claude/settings.json`에서 hook 항목 삭제 (Step에서 추가한 3개 항목)
2. `.claude/hooks/check-progress.sh`, `checkpoint.sh`, `audit-trigger.sh` 삭제
3. `.meta-loop/` 디렉토리 삭제 (또는 기록용으로 유지)
4. 세션 재시작
