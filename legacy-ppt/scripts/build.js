#!/usr/bin/env node
// 덱 소스(.src.html) → 게시용 조각(.artifact.html) + 단독 실행 파일(.html)
//   node build.js deck.src.html [--font inline|cdn|none] [--woff2 path/to/PretendardVariable.woff2] [--out dir]
//   inline(기본): Pretendard 가변 폰트를 base64로 넣음. claude.ai 아티팩트는 외부 폰트 CDN을 막으므로 이 방식이 필요
//                 --woff2가 없으면 npm pack pretendard로 내려받음
//   cdn: jsDelivr의 Pretendard CSS를 @import (사내망·로컬 파일용, 아티팩트에서는 막힘)
//   none: 폰트 블록과 Google Fonts 링크 제거, 시스템 폰트(맑은 고딕 등)로 표시. 외부 요청이 하나도 없는 유일한 모드
const fs = require('fs'), path = require('path'), os = require('os'), { execSync } = require('child_process');
const args = process.argv.slice(2);
const src = args.find((a) => !a.startsWith('--') && !['inline', 'cdn', 'none'].includes(a) && a.endsWith('.html'));
if (!src) { console.error('사용법: node build.js deck.src.html [--font inline|cdn|none] [--woff2 파일] [--out 폴더]'); process.exit(2); }
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const mode = opt('--font', 'inline');
const outDir = opt('--out', path.dirname(path.resolve(src)));
let html = fs.readFileSync(src, 'utf8');
const re = /\/\*FONT-FACE\*\/[\s\S]*?\/\*END-FONT-FACE\*\//;
if (!re.test(html)) console.warn('경고: /*FONT-FACE*/ 블록이 없어 폰트 처리를 건너뜀');

function findWoff2() {
  const given = opt('--woff2');
  if (given) return given;
  const cache = path.join(os.tmpdir(), 'pretendard-pkg');
  const cand = path.join(cache, 'package/dist/web/variable/woff2/PretendardVariable.woff2');
  if (fs.existsSync(cand)) return cand;
  fs.mkdirSync(cache, { recursive: true });
  execSync('npm pack pretendard@1.3.9 --silent', { cwd: cache, stdio: 'pipe' });
  execSync('tar xzf pretendard-1.3.9.tgz', { cwd: cache });
  return cand;
}
if (mode === 'inline') {
  const b64 = fs.readFileSync(findWoff2()).toString('base64');
  html = html.replace(re, `/*FONT-FACE*/@font-face{font-family:"Pretendard";src:url(data:font/woff2;base64,${b64}) format("woff2");font-weight:45 920;font-style:normal;font-display:swap}/*END-FONT-FACE*/`);
} else if (mode === 'cdn') {
  html = html.replace(re, '@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css");');
} else {
  // 외부 요청 0건: Pretendard 블록과 JetBrains Mono(Google Fonts) 링크를 모두 뺌. 고정폭은 시스템 폰트로 대체됨
  html = html.replace(re, '').replace(/<link[^>]+fonts\.(googleapis|gstatic)\.com[^>]*>\s*/g, '');
}
const base = path.basename(src).replace(/\.src\.html$|\.html$/, '');
const titleM = /<title>([^<]*)<\/title>/.exec(html);
const frag = path.join(outDir, `${base}.artifact.html`);
const full = path.join(outDir, `${base}.html`);
fs.writeFileSync(frag, html);
fs.writeFileSync(full, `<!doctype html>\n<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">${titleM ? '' : '<title>발표자료</title>'}\n<style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}body{margin:0}</style>\n</head><body>\n${html}\n</body></html>\n`);
console.log(`게시용 조각: ${frag}\n단독 파일:   ${full}\n크기: ${(html.length / 1048576).toFixed(2)} MB (font=${mode})`);
