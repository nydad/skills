# internal-skills — 내부망 Claude Code 이전용 스킬 번들

내부망(인트라넷) Claude Code 환경으로 그대로 옮겨 쓰는 **자기완결적 스킬 모음**.
GitHub 플러그인 마켓플레이스 접근이 안 되는 환경을 전제로, 외부 플러그인을 plain 스킬로
vendoring 해서 담았다. **Codex(OpenAI) 의존 없음 — Claude Code 단독 동작.**

## 구성 (스킬 19개)

### 개인 스킬 (3) — 직접 작성/큐레이션
| 스킬 | 용도 |
|---|---|
| `confluence-wiki` | Confluence 위키 문서 + draw.io 다이어그램 생성 (Wiki Markup/XHTML, 7색 테마) |
| `html-slides` | 단일 HTML 프레젠테이션 생성 (블랙 에디토리얼 디자인) |
| `meta-loop-protocol` | `/loop` 장기 자율 작업용 판단 프레임워크 (Windows Git Bash 호환) |

### superpowers — 개발 워크플로우 (14) · `obra/superpowers` v5.1.0
| 분류 | 스킬 |
|---|---|
| 기획/설계 | `brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `dispatching-parallel-agents` |
| 구현 | `test-driven-development`, `systematic-debugging`, `verification-before-completion` |
| 리뷰 | `requesting-code-review`, `receiving-code-review` |
| Git/브랜치 | `using-git-worktrees`, `finishing-a-development-branch` |
| 메타 | `using-superpowers`, `writing-skills` |

### superpowers 부가 (2)
| 스킬 | 출처 | 비고 |
|---|---|---|
| `remembering-conversations` | `obra/episodic-memory` v1.4.1 | ⚠️ episodic-memory MCP 서버 필요 (아래 참고) |
| `browsing` | `obra/superpowers-chrome` v2.1.0 | ⚠️ Node.js + Chrome 필요 (CLI 모드 자기완결) |

## 설치 (내부망 Claude Code)

이 디렉터리의 스킬 폴더들을 내부망 머신의 `~/.claude/skills/` 아래로 복사한다.

```bash
# Git Bash / Linux / macOS
cp -r internal-skills/*/  ~/.claude/skills/

# Windows PowerShell
Copy-Item internal-skills\* $HOME\.claude\skills\ -Recurse -Exclude README.md,LICENSE.superpowers
```

`README.md` 와 `LICENSE.superpowers` 는 스킬이 아니므로 복사 대상에서 제외한다.
복사 후 Claude Code를 재시작하면 스킬이 자동 인식된다.

## 동작 전제 / 주의

- **Codex 제거 완료** — 이 번들에 OpenAI Codex 의존 구성은 없다. (superpowers 스킬 본문에
  남아있는 "Codex" 언급은 upstream의 멀티플랫폼 안내 문구일 뿐, 동작에 영향 없음.)
- `browsing` — Node.js와 Chrome가 설치돼 있으면 CLI 모드(`chrome-ws`)로 자기완결 동작.
  MCP 모드는 별도 MCP 서버가 있어야 하므로 내부망에선 CLI 모드 권장.
- `remembering-conversations` — episodic-memory MCP 서버(과거 대화 시맨틱 검색)가 있어야
  실제 동작한다. 서버 없이는 안내 문서로만 존재. 내부망에 MCP 서버를 띄울 계획이 없으면
  이 스킬은 빼고 복사해도 무방.
- superpowers 스킬 간 상호 참조는 plugin 네임스페이스(`superpowers:`)를 제거해
  plain 스킬 이름으로 정리했다 — `~/.claude/skills/` 에 함께 두면 그대로 해석된다.

## 출처 / 라이선스

- 개인 스킬 3종: 사용자 자체 작성.
- `superpowers` / `episodic-memory` / `superpowers-chrome`: © 2025 Jesse Vincent,
  **MIT License** — 전문은 `LICENSE.superpowers` 참고. 원본: https://github.com/obra/superpowers

## 업데이트 절차

superpowers upstream이 갱신되면, 외부망 머신에서 플러그인을 업데이트한 뒤
`~/.claude/plugins/cache/superpowers-marketplace/*/*/skills/` 의 스킬을 다시 이 디렉터리로
복사하고 `superpowers:` 접두어를 제거(`sed -i 's/superpowers://g'`)한 후 재배포한다.
