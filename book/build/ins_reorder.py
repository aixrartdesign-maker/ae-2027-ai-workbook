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


# ---------------------------------------------------------------- v2 (2026-11-26): AI parts to the very front
# intermediate chapter numbers (after apply6) -> final
MAP2 = {17: 1, 18: 2, 19: 3, 20: 4, 21: 5, 22: 6, 23: 7, 24: 27, 25: 28, 26: 29}
for _i in range(1, 17):
    MAP2[_i] = _i + 10
RENUM2 = os.environ.get('RENUM2', '1') == '1'
PROTECT2 = ['58장의', '1초에 30장', '이미지 1장)', '300장이', '21장에 7.5', '스틸 21장', 'Z Image 21장', 'Banana 2 21장',
            '이미지 3장', 'GPT Image 19장', '이미지 19장 생성', '3장·4장·6장·8장', '3장·6장·8장']


def m2(n):
    k = int(n)
    if k not in MAP2:
        return n
    v = MAP2[k]
    return ('%02d' % v) if (len(n) == 2 and n.startswith('0')) else str(v)


def sec0(k):
    k = int(k)
    if k <= 4: return '8-%d' % k
    if k <= 8: return '9-%d' % (k - 4)
    return '10-%d' % (k - 8)


def renum2_text(t):
    def nm(g):
        a, b = g.group(1), g.group(2)
        if int(a) == 0:
            return g.group(0) if int(b) == 0 else sec0(b)
        return m2(a) + '-' + b
    t = re.sub(r'(?<![\d.\w:/+−*)-])(\d{1,2})-(\d{1,2})(?!\d|\.\d|_)', nm, t)
    t = re.sub(r'((?:\d+\s*(?:~|·|→|,)\s*)*\d+)(\s*장)(?! ?실습_|_)',
               lambda g: re.sub(r'\d+', lambda x: m2(x.group(0)), g.group(1)) + g.group(2), t)
    t = re.sub(r'CHAPTER (\d\d)\b', lambda g: 'CHAPTER %02d' % MAP2.get(int(g.group(1)), int(g.group(1))), t)
    t = re.sub(r'CHAPTER 00 · ([①②③])', lambda g: 'CHAPTER %02d' % (8 + '①②③'.index(g.group(1))), t)
    return t


def walk_text(S, fn):
    head, body = S.split('<body', 1)
    toks = re.split(r'(<[^>]+>)', body)
    out = []; skip = None; depth = 0
    for p in toks:
        if p.startswith('<'):
            if skip is None:
                mo = re.match(r'<(\w+)[^>]*class="[^"]*\bmono\b[^"]*"', p)
                if mo and not p.endswith('/>'):
                    skip = mo.group(1); depth = 1
            else:
                if re.match(r'<%s\b' % skip, p): depth += 1
                elif p.startswith('</%s' % skip):
                    depth -= 1
                    if depth == 0: skip = None
            out.append(p)
        else:
            out.append(p if skip else fn(p))
    return head + '<body' + ''.join(out)


def apply7(S):
    # 1. move part blocks 5,6,7 in front of part 0
    def pstart(n):
        return S.find('<section class="part"', S.find('<div class="no">PART %d</div>' % n) - 200)
    starts = {n: S.find('<div class="no">PART %d</div>' % n) for n in range(9)}
    starts = {n: S.rfind('<section', 0, v) for n, v in starts.items()}
    blk = S[starts[5]:starts[8]]
    S = S[:starts[5]] + S[starts[8]:]
    S = S[:starts[0]] + blk + '\n' + S[starts[0]:]
    # relabel parts in new order
    order = []
    for mo in re.finditer(r'<div class="no">PART (\d)</div>', S):
        order.append(mo)
    newno = {}
    for i, mo in enumerate(order):
        newno[mo.start()] = i + 1
    S = re.sub(r'<div class="no">PART (\d)</div>', lambda mo: '<div class="no">PART %d</div>' % newno[mo.start()], S)
    if not RENUM2:
        return S
    for i, s in enumerate(PROTECT2):
        S = S.replace(s, '\x01%d\x01' % i)
    S = walk_text(S, renum2_text)
    for i, s in enumerate(PROTECT2):
        S = S.replace('\x01%d\x01' % i, s)

    # 2. overview cards (SVG): rewrite the 36 card texts in order
    cards = [('PART 1', '●○○ ~ ●●○', '애펙 AI · 연결 준비', '1~2장'),
             ('PART 2', '●○○', '힉스필드 패널', '3~5장'),
             ('PART 3', '●○○ ~ ●●○', 'Claude 브리지', '6~7장'),
             ('PART 4', '●○○', '이해하기', '8~10장 · 역사 · 비용'),
             ('PART 5', '●○○ ~ ●●○', '애펙 기본기', '11~14장'),
             ('PART 6', '●●○ ~ ●●●', '모션그래픽', '15~17장'),
             ('PART 7', '●●○ ~ ●●●', '합성과 VFX', '18~22장'),
             ('PART 8', '●○○ ~ ●●●', '3D와 실무', '23~26장'),
             ('PART 9', '●○○ ~ ●●○', '완성과 정리', '27~29장 · 부록')]
    flat = [x for c in cards for x in c]
    i = S.find('>이해하기</text>')
    a = S.rfind('<svg', 0, i); b = S.find('</svg>', i)
    svg = S[a:b]
    texts = list(re.finditer(r'(<text[^>]*>)([^<]*)(</text>)', svg))
    assert texts[0].group(2) == 'PART 0', texts[0].group(2)
    k = [0]
    def tf(mo):
        j = k[0]; k[0] += 1
        if j < len(flat):
            return mo.group(1) + flat[j] + mo.group(3)
        if mo.group(2).startswith('애펙만 배우려면'):
            return mo.group(1) + 'AI부터 하려면 PART 1~3, 애펙을 처음부터 배우려면 PART 4부터 읽어도 됩니다.' + mo.group(3)
        return mo.group(0)
    svg = re.sub(r'(<text[^>]*>)([^<]*)(</text>)', tf, svg)
    S = S[:a] + svg + S[b:]

    # 3. syllabus and other part references
    def rep(old, new):
        nonlocal S
        assert old in S, old
        S = S.replace(old, new)
    rep('(PART 5~8 실습용)', '(PART 1~3, 9 실습용)')
    rep('앞의 절반은 기본기·모션그래픽·합성·3D이고, 뒤의 절반은 그 위에 AI를 얹는 세 가지 길, 곧 힉스필드 플러그인 패널, Claude 브리지, 애펙 자체 AI입니다.',
        '앞부분(PART 1~3)에서는 AI를 얹는 세 가지 길, 곧 애펙 자체 AI, 힉스필드 플러그인 패널, Claude 브리지로 먼저 결과를 만들어 보고, 뒷부분(PART 4~9)에서는 그 결과를 직접 고치고 넓히는 기본기·모션그래픽·합성·3D를 다룹니다.')
    rows = {'역사와 AI 지도, 설치 (00, 2-2)': '역사와 AI 지도, 설치 (8~10, 2-2)',
            '처음 30분, 화면 읽기 (01~02)': '처음 30분, 화면 읽기 (11~12)',
            '키프레임과 그래프 (03)': '키프레임과 그래프 (13)',
            '부모, 마스크, 매트 (04)': '부모, 마스크, 매트 (14)',
            '셰이프와 모션그래픽 기법 (05)': '셰이프와 모션그래픽 기법 (15)',
            '텍스트 애니메이션 (06)': '텍스트 애니메이션 (16)',
            '익스프레션 ① 기본 어휘 (07)': '익스프레션 ① 기본 어휘 (17)',
            '익스프레션 ②, 중간 과제 (07)': '익스프레션 ②, 중간 과제 (17)',
            '크로마키, 색 보정 (08, 12)': '크로마키, 색 보정 (18, 22)',
            '트래킹, 3D 트래커, 지우기 (09~11)': '트래킹, 3D 트래커, 지우기 (19~21)',
            '3D, 렌더와 출력, 직업별 팁 (13~16)': '3D, 렌더와 출력, 직업별 팁 (23~26)',
            '애펙 자체 AI, 연결, 패널 ① (17~19)': '애펙 자체 AI, 연결, 패널 ① (1~3)',
            '패널 ②③, Claude 타이틀 (20~23)': '패널 ②③, Claude 타이틀 (4~7)',
            '통합 기획, 검수 (24~25)': '통합 기획, 검수 (27~28)',
            '기말 발표: 30초 홍보영상 (24, 26)': '기말 발표: 30초 홍보영상 (27, 29)'}
    for o, n in rows.items():
        rep(o, n)
    return S
