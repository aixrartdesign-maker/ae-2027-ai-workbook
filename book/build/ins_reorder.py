# -*- coding: utf-8 -*-
# 2026-11-26: move AE's own AI chapter (old 23) to the front of the AI part and renumber 17..23.
import re, os

MAP = {23: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23}
RENUM = os.environ.get('RENUM', '1') == '1'

# contexts where "N장" means sheets/images or a composition name, not a chapter
PROTECT = ['Z Image 21장', 'Banana 2 21장', '스틸 21장', '21장에 7.5', 'GPT Image 19장', '이미지 19장 생성', '22장_로고리빌']


def m(n):
    return str(MAP[int(n)]) if int(n) in MAP else n


def renum_text(t):
    t = re.sub(r'(?<![\d.\w])(1[7-9]|2[0-3])-(\d+)(?!\d|\.\d)', lambda g: m(g.group(1)) + '-' + g.group(2), t)
    t = re.sub(r'((?:\d+\s*(?:~|·|→|,)\s*)*\d+)(\s*장)(?! ?실습_|_)',
               lambda g: re.sub(r'\d+', lambda x: m(x.group(0)), g.group(1)) + g.group(2), t)
    t = re.sub(r'CHAPTER (1[7-9]|2[0-3])\b', lambda g: 'CHAPTER ' + m(g.group(1)), t)
    return t


def apply6(S):
    # 1. move chapter 23 right after the PART 5 section
    k = S.find('<div class="ch-no">CHAPTER 23</div>')
    a = S.rfind('<section', 0, k); b = S.find('</section>', k) + len('</section>')
    ch23 = S[a:b]
    S = S[:a] + S[b:]
    p5 = S.find('<section class="part"', S.find('<div class="no">PART 4</div>'))
    p5 = S.find('<div class="no">PART 5</div>')
    e5 = S.find('</section>', p5) + len('</section>')
    S = S[:e5] + '\n' + ch23 + '\n' + S[e5:]

    if not RENUM:
        return S

    # 2. renumber in text nodes of the body
    for i, s in enumerate(PROTECT):
        S = S.replace(s, '\x00%d\x00' % i)
    head, body = S.split('<body', 1)
    parts = re.split(r'(<[^>]+>)', body)
    parts = [p if p.startswith('<') else renum_text(p) for p in parts]
    S = head + '<body' + ''.join(parts)
    for i, s in enumerate(PROTECT):
        S = S.replace('\x00%d\x00' % i, s)

    # 3. part titles, overview cards, syllabus
    def rep(old, new, cnt=1):
        nonlocal S
        assert S.count(old) >= cnt, old
        S = S.replace(old, new)
    rep('<h1>AI 연결 준비</h1><p>애펙을 영문판으로 바꾸고, 힉스필드 플러그인을 깔고, Claude와 애펙 사이에 다리를 놓습니다. 처음 한 번만 하면 됩니다.</p>',
        '<h1>애펙 자체 AI와 연결 준비</h1><p>먼저 설치 없이 바로 쓰는 애펙 2027의 AI Assistant부터 익힙니다. 그다음 애펙을 영문판으로 바꾸고, 힉스필드 플러그인을 깔고, Claude와 애펙 사이에 다리를 놓습니다. 연결은 처음 한 번만 하면 됩니다.</p>')
    rep('<h1>Claude와 애펙 자체 AI</h1>', '<h1>Claude와 함께 만들기</h1>')
    rep('>AI 연결 준비</text>', '>애펙 AI · 연결 준비</text>')
    rep('>Claude · 자체 AI</text>', '>Claude 브리지</text>')
    rep('>18장</text>', '>17~18장</text>')
    rep('>22~17장</text>', '>22~23장</text>')
    rep('AI 연결, 패널 ① 편집 (17~18)', '애펙 자체 AI, 연결, 패널 ① (17~19)')
    rep('패널 ②③, Claude 타이틀 (19~22)', '패널 ②③, Claude 타이틀 (20~23)')
    rep('자체 AI, 통합 기획, 검수 (23~25)', '통합 기획, 검수 (24~25)')
    return S
