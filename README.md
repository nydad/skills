# skills

Claude Code 스킬 저장소.

## legacy-ppt

레거시 업무 보고서 포맷(브레드크럼 · 명사형 제목 · 거버닝 메시지 띠 · 개조식 · ※ 출처 줄 · 간지 ·
Executive Summary · Appendix)에 남색+일렉트릭 블루 마감과 아키텍처 그림 · 차트 인터랙션을 입힌
단일 HTML 발표자료(1600×900, 키보드 넘김)를 만든다.

| 경로 | 내용 |
|---|---|
| `legacy-ppt/SKILL.md` | 작업 순서, 포맷 · 디자인 · 가독성 규칙, 그림 문법, 자주 터지는 문제 |
| `legacy-ppt/assets/deck-template.html` | 엔진 · CSS · 17장 예시(가상의 "ORBIT 운영 고도화 계획") |
| `legacy-ppt/references/components.md` | 장표 유형별 마크업, JSON 설정, data 속성 |
| `legacy-ppt/references/writing.md` | 거버닝 메시지 · 개조식 · 출처 쓰는 법 |
| `legacy-ppt/scripts/build.js` | 소스 → 단독 HTML / 아티팩트 조각 (Pretendard 인라인 · CDN · 없음) |
| `legacy-ppt/scripts/shoot.py` | 슬라이드별 PNG · 몽타주 · 넘침 / 콘솔 오류 검사 |

### 설치

```bash
# Git Bash / macOS / Linux
cp -r legacy-ppt ~/.claude/skills/

# Windows PowerShell
Copy-Item legacy-ppt $HOME\.claude\skills\ -Recurse
```

### 필요 환경

- 빌드: Node.js 18+ (`--font inline`은 최초 1회 `npm pack pretendard`로 폰트를 받음)
- 검사: Python 3 + Playwright (`pip install playwright && playwright install chromium`)

### 빠른 사용

```bash
cp ~/.claude/skills/legacy-ppt/assets/deck-template.html ./deck.src.html   # 슬라이드 수정
node ~/.claude/skills/legacy-ppt/scripts/build.js deck.src.html --font cdn  # → deck.html
python ~/.claude/skills/legacy-ppt/scripts/shoot.py deck.html shots --states
```
