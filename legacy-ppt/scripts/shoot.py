#!/usr/bin/env python3
"""덱 단독 파일(.html)을 헤드리스 Chromium으로 열어 슬라이드별 PNG, 6장 단위 몽타주를 남기고 흔한 결함을 검사한다.
   python shoot.py deck.html out_dir [--states]      (macOS/Linux: python3)

   1장은 처음 열린 상태(모션 꺼짐) 그대로, 2장부터는 실제 발표처럼 키보드 이동으로 넘긴 뒤
   등장 모션을 끝까지 돌린 상태를 찍는다. 모션이 남긴 스타일이 상호작용을 막는 문제도 여기서 드러난다.

   --states: 슬라이드마다 상호작용 상태를 더 찍고 검사한다
     sNN_alt.png     보기 전환(.seg[data-view-target])의 두 번째 상태
     sNN_filter.png  필터(.seg[data-filter-target])의 두 번째 버튼
     연결선 강조      data-hover-links 그림에서 첫 노드를 가리켰을 때 나머지 선이 흐려지는지

   검사 항목: 콘솔 오류·경고([deck]로 시작하면 JSON 오류나 없는 id), 본문(.s-body) 밖으로 나간 요소,
   제목·거버닝 메시지 줄바꿈(한 줄이어야 함), 머리말이 본문을 침범하는지, 템플릿 예시(ORBIT) 흔적.
   Chromium 경로는 PLAYWRIGHT_BROWSERS_PATH를 따른다. 지정이 없고 /opt/pw-browsers가 있으면 그곳(샌드박스),
   없으면 Playwright 기본 위치를 쓴다. 문제가 하나라도 있으면 종료 코드 1."""
import os, sys, glob, pathlib
if os.path.isdir('/opt/pw-browsers'):
    os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

FINISH = '''() => { document.getAnimations().forEach(a => { try { a.finish(); } catch (e) {} }); }'''

LINES = '''(el) => { if (!el) return 0; const r = document.createRange(); r.selectNodeContents(el);
  const tops = new Set([...r.getClientRects()].filter(q => q.width > 1).map(q => Math.round(q.top / 4))); return tops.size; }'''

CHECK = '''(LINES) => {
  const lines = eval(LINES), out = [];
  const all = [...document.querySelectorAll('.slide')];
  document.querySelectorAll('.slide.content').forEach((s) => {
    const p = 'p' + (all.indexOf(s) + 1), b = s.querySelector('.s-body'), h = s.querySelector('.s-head');
    if (h && b && h.getBoundingClientRect().bottom > b.getBoundingClientRect().top + 1) out.push(p + ': 머리말이 본문을 침범');
    if (lines(s.querySelector('.s-title')) > 1) out.push(p + ': 제목이 두 줄');
    if (lines(s.querySelector('.gmsg')) > 1) out.push(p + ': 거버닝 메시지가 두 줄');
    if (!b) return;
    const r = b.getBoundingClientRect(), bad = [];
    b.querySelectorAll('*').forEach((e) => { const q = e.getBoundingClientRect(); if (e.closest('.tip') || getComputedStyle(e).opacity === '0') return;
      if (q.width && (q.bottom > r.bottom + 2 || q.right > r.right + 2 || q.left < r.left - 2)) bad.push(e.getAttribute('class') || e.tagName); });
    if (bad.length) out.push(p + ': 본문 넘침 ' + [...new Set(bad)].slice(0, 4).join(', '));
  });
  return out;
}'''

HOVER = '''() => {
  const s = document.querySelector('.slide.is-active'), res = [];
  s.querySelectorAll('[data-hover-links]').forEach((host) => {
    const n = [...host.querySelectorAll('[data-hover]')].find((x) => x.id && host.querySelector(`.edge[data-from="${x.id}"], .edge[data-to="${x.id}"]`));
    if (!n || host.querySelectorAll('.edge').length < 2) return;
    res.push('#' + n.id);
  });
  return res;
}'''

HOVER_OK = '''(host) => [...document.querySelectorAll('.slide.is-active [data-hover-links].hovering .edge:not(.on)')]
  .every((g) => parseFloat(getComputedStyle(g).opacity) < .5)'''


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    src, out = os.path.abspath(sys.argv[1]), sys.argv[2]
    states = '--states' in sys.argv
    os.makedirs(out, exist_ok=True)
    for f in glob.glob(os.path.join(out, '*.png')): os.remove(f)
    errs, issues = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1632, 'height': 968})
        pg.on('console', lambda m: errs.append(f'{m.type}: {m.text}') if m.type in ('error', 'warning') else None)
        pg.on('pageerror', lambda e: errs.append(f'pageerror: {e}'))
        pg.goto(pathlib.Path(src).as_uri()); pg.wait_for_timeout(900)
        n = pg.evaluate('window.__deck ? window.__deck.N : 0')
        clip = {'x': 16, 'y': 14, 'width': 1600, 'height': 900}
        pg.mouse.move(2, 2)
        for i in range(n):
            if i == 0:
                pg.evaluate('window.__deck.set(0)'); pg.wait_for_timeout(300)
            else:
                pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(120)
                pg.evaluate(FINISH)
                has_count = pg.evaluate("!!document.querySelector('.slide.is-active [data-count]')")
                pg.wait_for_timeout(1000 if has_count else 250)
            tag = f's{i+1:02d}'
            pg.screenshot(path=f'{out}/{tag}.png', clip=clip)
            if not states:
                continue
            seg = '.slide.is-active .seg[data-view-target]'
            if pg.query_selector(f'{seg} button:nth-child(2)'):
                pg.click(f'{seg} button:nth-child(2)'); pg.wait_for_timeout(500)
                pg.screenshot(path=f'{out}/{tag}_alt.png', clip=clip)
                pg.click(f'{seg} button:nth-child(1)'); pg.wait_for_timeout(300)
            seg = '.slide.is-active .seg[data-filter-target]'
            if pg.query_selector(f'{seg} button:nth-child(2)'):
                pg.click(f'{seg} button:nth-child(2)'); pg.wait_for_timeout(400)
                pg.screenshot(path=f'{out}/{tag}_filter.png', clip=clip)
                pg.click(f'{seg} button:nth-child(1)'); pg.wait_for_timeout(200)
            for sel in pg.evaluate(HOVER):
                pg.hover(f'.slide.is-active {sel}'); pg.wait_for_timeout(350)
                if not pg.evaluate(HOVER_OK, None):
                    issues.append(f'p{i+1}: {sel}에 마우스를 올려도 나머지 연결선이 흐려지지 않음')
                pg.mouse.move(2, 2); pg.wait_for_timeout(200)
        issues += pg.evaluate(CHECK, LINES)
        if 'ORBIT' not in (pg.evaluate("(document.getElementById('deck-config')||{}).textContent||''") or ''):
            hits = pg.evaluate('''() => [...document.querySelectorAll('.slide')].map((s, i) => /ORBIT/.test(s.textContent) ? 'p' + (i + 1) : null).filter(Boolean)''')
            if hits: issues.append('템플릿 예시(ORBIT) 흔적: ' + ', '.join(hits))
        b.close()
    try:
        from PIL import Image
        fs = sorted(glob.glob(os.path.join(out, 's[0-9][0-9].png')))
        for k in range(0, len(fs), 6):
            grp = fs[k:k+6]; W, H = 800, 450
            m = Image.new('RGB', (W*2+10, (H+10)*((len(grp)+1)//2)), 'white')
            for i, f in enumerate(grp):
                m.paste(Image.open(f).convert('RGB').resize((W, H)), ((i % 2)*(W+10), (i//2)*(H+10)))
            m.save(os.path.join(out, f'contact-{k//6+1}.png'))
    except ImportError:
        pass
    print(f'slides: {n}')
    print('console:', errs or '없음')
    print('검사:', ('\n  ' + '\n  '.join(issues)) if issues else '이상 없음')
    return 1 if (issues or errs) else 0


if __name__ == '__main__':
    sys.exit(main())
