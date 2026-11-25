# -*- coding: utf-8 -*-
# 2026-11-26 (3): NEW part first (AI basics, install, AE AI) → Connect part (connect, other AIs) → Higgsfield → Claude
# → fundamentals (with a new Character chapter before Structure) ...
import re, os
from ins_more import st, steps, K, M, P
from ins_reorder import walk_text

RENUM3 = os.environ.get('RENUM3', '1') == '1'

# chapter map (current -> new); 8, 9, 10 are dissolved (sections mapped below)
CMAP = {1: 3, 2: 4, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 2, 9: 1, 10: 2, 11: 11, 12: 12, 13: 13}
for _i in range(14, 30):
    CMAP[_i] = _i + 1
SMAP = {(9, 1): (1, 5), (9, 2): (1, 6), (9, 3): (1, 7), (9, 4): (1, 8),
        (10, 1): (2, 1), (10, 2): (2, 2), (8, 3): (2, 4), (2, 2): (2, 5),
        (8, 1): (2, 6), (8, 2): (2, 7), (8, 4): (2, 8),
        (10, 3): (4, 2), (10, 4): (4, 3), (2, 1): (4, 1)}
for _k in range(3, 10):
    SMAP[(2, _k)] = (4, _k + 1)

PROTECT = ['58장의', '1초에 30장', '이미지 1장)', '300장이', '21장에 7.5', '스틸 21장', 'Z Image 21장', 'Banana 2 21장',
           '이미지 3장', 'GPT Image 19장', '이미지 19장 생성', '3장·4장·6장·8장', '3장·6장·8장']


def cm(n):
    k = int(n)
    if k not in CMAP:
        return n
    v = CMAP[k]
    return ('%02d' % v) if (len(n) == 2 and n.startswith('0')) else str(v)


def rn_text(t):
    t = re.sub(r'그림 (\d{1,2})-(\d{1,2})', lambda g: '그림\x03%s\x04%s' % (CMAP.get(int(g.group(1)), int(g.group(1))), g.group(2)), t)
    def nm(g):
        a, b = int(g.group(1)), int(g.group(2))
        if (a, b) in SMAP:
            return '%d-%d' % SMAP[(a, b)]
        if a in CMAP and a not in (8, 9, 10):
            return '%d-%d' % (CMAP[a], b)
        return g.group(0)
    t = re.sub(r'(?<![\d.\w:/+−*)-])(\d{1,2})-(\d{1,2})(?!\d|\.\d|_)', nm, t)
    t = re.sub(r'((?:\d+\s*(?:~|·|→|,)\s*)*\d+)(\s*장)(?! ?실습_|_)',
               lambda g: re.sub(r'\d+', lambda x: cm(x.group(0)), g.group(1)) + g.group(2), t)
    t = re.sub(r'CHAPTER (\d\d)\b', lambda g: 'CHAPTER %02d' % CMAP.get(int(g.group(1)), int(g.group(1))), t)
    t = t.replace('그림\x03', '그림 ').replace('\x04', '-')
    return t


def renum(S):
    if not RENUM3:
        return S
    for i, s in enumerate(PROTECT):
        S = S.replace(s, '\x02%d\x02' % i)
    S = walk_text('<body' + S, rn_text)[len('<body'):] if '<body' not in S else walk_text(S, rn_text)
    for i, s in enumerate(PROTECT):
        S = S.replace('\x02%d\x02' % i, s)
    return S


def chap(S, no):
    k = S.find('<div class="ch-no">CHAPTER %02d</div>' % no)
    assert k > 0, no
    a = S.rfind('<section', 0, k); b = S.find('</section>', k) + len('</section>')
    return a, b


def h2blocks(sec):
    """return (head, [h2 block html...], tail) where tail starts at </section>"""
    body = sec[:sec.rfind('</section>')]
    parts = re.split(r'(?=<h2[ >])', body)
    return parts[0], parts[1:], '</section>'


def blk(blocks, label):
    for b in blocks:
        if re.match(r'<h2[^>]*>(?:<span class="tag[^"]*">[^<]*</span> )?' + re.escape(label) + r' ', b):
            return b
    raise KeyError(label)


def part(no, title, desc):
    return '<section class="part"><div class="no">PART %d</div><h1>%s</h1><p>%s</p></section>\n' % (no, title, desc)


def chead(no, title, lv, lead, mission=None):
    s = '<section class="chapter">\n<div class="ch-no">CHAPTER %02d</div>\n<h1 class="ch">%s <span class="lv">%s</span></h1>\n<p class="lead">%s</p>\n' % (no, title, lv, lead)
    if mission:
        s += '<div class="mission"><div class="lbl">오늘의 미션</div>%s</div>\n' % mission
    return s


# ======================================================================== new content (final numbering)
CH1_HEAD = chead(1, 'AI란 무엇인가 — 역사와 최근 생성형 AI', '●○○',
                 'AI는 2022년에 갑자기 나타난 기술이 아닙니다. 70년 넘게 쌓인 연구가 “말로 시키면 그림과 영상을 만들어 주는” 단계에 이른 것입니다. 이 장에서는 AI가 무엇인지, 어떻게 여기까지 왔는지, 그리고 지금 애펙 작업에 어떤 AI들이 들어와 있는지를 한 번에 정리합니다.')

CH1_NEW = '''
<h2>1-1 AI는 무엇인가 — 규칙에서 학습으로</h2>
<p><b>인공지능(AI, Artificial Intelligence)</b>은 사람이 지능을 써서 하던 일을 컴퓨터가 하게 만드는 기술 전체를 말합니다. 처음에는 사람이 규칙을 하나하나 적어 넣었습니다. “빨간 픽셀이 많고 둥글면 사과”처럼요. 하지만 세상의 사과는 너무 다양해서 규칙으로는 끝이 없었습니다.</p>
<p>그래서 방법이 바뀌었습니다. 규칙을 적는 대신 <b>예시를 아주 많이 보여 주고</b> 컴퓨터가 스스로 공통점을 찾게 하는 것, 이것이 <b>머신러닝(기계 학습)</b>입니다. 그중 사람 뇌의 신경망을 흉내 낸 여러 겹의 계산 구조를 쓰는 방식을 <b>딥러닝</b>이라고 하고, 지금 우리가 쓰는 AI는 거의 모두 딥러닝입니다.</p>
<table>
<tr><th style="width:24%">용어</th><th>뜻</th></tr>
<tr><td>모델(Model)</td><td>학습이 끝난 AI 자체. “Seedance 2.0”, “Claude”, “Firefly Image 5”가 모두 모델 이름입니다</td></tr>
<tr><td>학습 데이터</td><td>모델이 보고 배운 글·이미지·영상. 무엇을 배웠는지가 결과의 품질과 저작권 문제를 좌우합니다</td></tr>
<tr><td>프롬프트(Prompt)</td><td>모델에게 주는 지시문. 이 책의 PROMPT 상자가 모두 프롬프트입니다</td></tr>
<tr><td>생성형 AI</td><td>분류·판단을 넘어 새 글·그림·소리·영상을 만들어 내는 AI</td></tr>
<tr><td>에이전트(Agent)</td><td>대답만 하지 않고 도구를 직접 써서 일을 끝내는 AI. Claude가 브리지로 애펙을 조작하는 것이 에이전트의 예입니다</td></tr>
<tr><td>크레딧</td><td>생성할 때마다 빠지는 사용료 단위. 모델·해상도·길이에 따라 다릅니다(4-2, 3-8)</td></tr>
</table>

<h2>1-2 AI의 짧은 역사 — 70년을 한 표로</h2>
<table>
<tr><th style="width:12%">해</th><th>일어난 일</th></tr>
<tr><td>1950</td><td>앨런 튜링이 “기계가 생각할 수 있는가”를 묻는 논문에서 튜링 테스트를 제안</td></tr>
<tr><td>1956</td><td>미국 다트머스 회의에서 “인공지능”이라는 말이 처음 쓰임</td></tr>
<tr><td>1970~80년대</td><td>사람이 규칙을 적어 넣는 전문가 시스템의 시대. 기대만큼 성과가 나지 않아 연구비가 끊긴 “AI 겨울”을 두 번 겪음</td></tr>
<tr><td>1997</td><td>IBM 딥 블루가 체스 세계 챔피언을 이김</td></tr>
<tr><td>2012</td><td>딥러닝 모델 AlexNet이 이미지 인식 대회에서 압도적으로 우승. 그래픽카드(GPU)로 신경망을 학습시키는 시대가 열림</td></tr>
<tr><td>2014</td><td>두 신경망이 서로 겨루며 그림을 만드는 GAN 발표. “AI가 그림을 그린다”의 시작</td></tr>
<tr><td>2016</td><td>알파고가 이세돌 9단을 이김</td></tr>
<tr><td>2017</td><td>구글 연구진이 트랜스포머(Transformer) 구조를 발표. 오늘날 대화형 AI와 영상 AI의 뼈대</td></tr>
<tr><td>2020</td><td>GPT-3. 글을 이어 쓰는 능력이 사람 수준에 가까워짐</td></tr>
<tr><td>2022</td><td>이미지 생성 대중화(DALL·E 2, Midjourney, Stable Diffusion). 11월 ChatGPT 공개</td></tr>
<tr><td>2023</td><td>어도비 Firefly 공개, 포토샵 생성형 채우기. 대화형 AI가 업무 도구로 퍼짐</td></tr>
<tr><td>2024</td><td>OpenAI Sora 공개로 영상 생성 경쟁 본격화(Kling, Runway, Veo 등). 11월 Anthropic이 MCP 공개</td></tr>
<tr><td>2025</td><td>소리까지 함께 만드는 영상 모델 등장. AI가 앱을 직접 조작하는 에이전트가 확산, ChatGPT 안에 포토샵 등 어도비 앱이 들어감</td></tr>
<tr><td>2026</td><td>힉스필드 애펙 플러그인(5월), 브리지 MCP(7월), 애펙 27.0 AI Assistant(11월). 애펙 안에서 AI와 함께 일하는 시대</td></tr>
</table>

<h2>1-3 생성형 AI는 어떻게 만들어 내나</h2>
<p>생성형 AI는 종류마다 만드는 방식이 다릅니다. 원리를 대강 알면 “왜 손가락이 이상하게 나오는지”, “왜 같은 프롬프트에도 결과가 다른지”를 이해할 수 있습니다.</p>
<table>
<tr><th style="width:18%">종류</th><th style="width:36%">원리 (아주 짧게)</th><th>애펙 작업에서의 쓰임 · 대표 모델</th></tr>
<tr><td>글 (LLM)</td><td>앞 글자를 보고 다음에 올 말을 확률로 하나씩 고름</td><td>기획·자막·익스프레션 작성, 애펙 조작 · Claude, ChatGPT, Gemini</td></tr>
<tr><td>이미지</td><td>잡음(노이즈)에서 시작해 프롬프트에 맞게 조금씩 잡음을 걷어 냄(디퓨전)</td><td>배경·소품·스타일 프레임 · Firefly, GPT Image, Nano Banana, FLUX</td></tr>
<tr><td>영상</td><td>이미지 생성을 시간 축으로 넓혀, 프레임 사이가 이어지도록 함께 만듦</td><td>B롤, 장면 바꾸기, 이미지를 움직이기 · Seedance, Kling, Veo, Runway</td></tr>
<tr><td>소리</td><td>목소리·음악의 파형이나 그 특징을 생성</td><td>내레이션, 더빙, 효과음 · ElevenLabs 등</td></tr>
<tr><td>분할·추적</td><td>화면 속 물체의 경계를 찾아 프레임마다 따라감</td><td>배경 제거, 로토스코핑 · 애펙 Object Matte, Roto Brush</td></tr>
</table>
<div class="why"><b>결과가 매번 다른 이유</b>생성형 AI는 매번 다른 잡음과 확률에서 출발합니다. 그래서 같은 프롬프트도 결과가 달라지고, 마음에 드는 결과를 얻으려면 여러 번 뽑거나(크레딧) 참조 이미지·시드(seed)로 범위를 좁힙니다. 반대로 애펙의 키프레임은 몇 번을 렌더해도 똑같습니다. 이 책이 “AI로 빨리 만들고, 애펙으로 정확히 고친다”를 기본 흐름으로 삼는 이유입니다.</div>

<h2>1-4 2026년 지금의 생성형 AI 지도</h2>
<table>
<tr><th style="width:22%">분야</th><th>대표 서비스</th></tr>
<tr><td>대화·에이전트</td><td>Claude(Anthropic), ChatGPT(OpenAI), Gemini(Google), Copilot(Microsoft)</td></tr>
<tr><td>통합 생성 플랫폼</td><td>Higgsfield(여러 회사 모델을 한 크레딧으로), Adobe Firefly 앱, Runway</td></tr>
<tr><td>애펙 안의 AI</td><td>AI Assistant(27.0), Object Matte(26.2), Roto Brush, Content-Aware Fill, 힉스필드 패널</td></tr>
<tr><td>연결 규격</td><td>MCP — AI와 앱을 잇는 공통 포트(1-8, 5장)</td></tr>
</table>
<div class="warn"><b>AI가 아직 못하는 것</b>① 그럴듯하게 틀린 말을 하기도 합니다(환각). 메뉴 이름·수치는 직접 확인합니다. ② 같은 인물·로고를 장면마다 똑같이 지키기 어렵습니다(14-6). ③ 학습 데이터와 결과물의 저작권·초상권 문제는 쓰는 사람이 책임집니다(29장). ④ 생성할 때마다 비용이 듭니다.</div>
'''

CH2_HEAD = chead(2, '애펙 설치와 준비 — 비용, 설치, 업데이트 내역, 언어', '●○○',
                 '애펙을 사고, 설치하고, 최신 버전으로 올리고, 영문 메뉴로 바꾸는 데까지 한 장에서 끝냅니다. 뒤쪽에는 지금까지 어떤 업데이트가 있었는지와 애펙 30년의 흐름을 정리했습니다.')

CH2_INSTALL = '''
<h2><span class="tag t1">따라 하기</span> 2-3 애펙 설치하고 최신 버전으로 올리기</h2>
''' + steps(
    '<b>Creative Cloud 데스크톱 앱</b>을 엽니다(2-2에서 설치). 왼쪽 위 프로필이 내 어도비 계정인지 확인합니다.',
    '<b>앱</b> 탭에서 <b>After Effects</b>를 찾아 <b>설치</b>를 누릅니다. 수 GB를 내려받으니 전원과 인터넷을 연결해 둡니다.',
    '설치가 끝나면 <b>열기</b>. 첫 실행 때 홈 화면이 뜨면 <b>New Project</b>를 눌러 빈 프로젝트가 열리는지 봅니다.',
    '버전 확인: 애펙 메뉴 <b>Help → About After Effects</b>. 이 책은 <b>27.0</b> 기준입니다. 26.x 이하라면 다음 단계로 올립니다.',
    '업데이트: Creative Cloud 앱의 <b>업데이트</b> 항목에서 After Effects 옆 <b>업데이트</b>. 앱 목록의 <b>⋯ → 다른 버전</b>에서는 예전 버전을 함께 설치할 수도 있습니다(학교 컴퓨터가 옛 버전일 때 대비).',
    '새 기능을 미리 써 보고 싶다면 <b>베타 앱</b> 항목의 After Effects (Beta)를 따로 설치합니다. 정식판과 따로 깔리며 기능이 불안정할 수 있습니다.',
) + '''
<table>
<tr><th style="width:24%">컴퓨터 사양 (참고)</th><th>이 책 실습에 무리 없는 수준</th></tr>
<tr><td>운영체제</td><td>Windows 10/11 64비트, 또는 최신 macOS</td></tr>
<tr><td>메모리(RAM)</td><td>최소 16GB, 4K·3D 작업은 32GB 이상 권장</td></tr>
<tr><td>그래픽카드</td><td>VRAM 4GB 이상, Advanced 3D와 Object Matte는 GPU 성능에 크게 좌우</td></tr>
<tr><td>저장 공간</td><td>설치용 여유 공간 + 디스크 캐시용 SSD(27-2)</td></tr>
</table>
<p class="src">정확한 최소 사양은 버전마다 바뀌므로 adobe.com의 After Effects 시스템 요구 사항 페이지에서 확인하세요.</p>
'''

PART_NEW = part(1, 'NEW — AI와 함께 시작하는 애펙 2027',
                'AI가 무엇이고 어떻게 여기까지 왔는지, 애펙을 설치하고 무엇이 새로워졌는지, 그리고 애펙 안에 들어온 AI Assistant부터 만납니다. 이 책을 처음 펼쳤다면 여기서 시작하세요.')
PART_CONNECT = part(2, '연결',
                    '힉스필드 플러그인과 Claude 브리지를 애펙에 잇고, ChatGPT·Gemini 같은 다른 AI로 연결하는 방법까지 봅니다. 연결은 처음 한 번만 하면 됩니다.')

CH5 = chead(5, 'Claude 말고도 — ChatGPT·Gemini·Copilot·Cursor 연결하기', '●○○',
            '이 책의 실습은 Claude로 했지만, 연결의 바탕인 MCP는 여러 AI가 함께 쓰는 공통 규격입니다. 같은 힉스필드 계정과 크레딧을 ChatGPT, Cursor 같은 다른 AI에서도 쓸 수 있습니다. 내가 이미 쓰고 있는 AI부터 연결해 보세요.',
            '내가 쓰는 AI(ChatGPT 등)에 힉스필드를 연결하고, 대화창에서 짧은 이미지 하나를 만들면 성공입니다.') + '''
<h2>5-1 한눈에 보기 — 어떤 AI를 어떻게 잇나</h2>
<table class="big">
<tr><th style="width:17%">AI</th><th style="width:33%">힉스필드 연결 방법</th><th style="width:22%">애펙 조작(브리지)</th><th>함께 알아 둘 것</th></tr>
<tr><td><b>Claude</b></td><td>설정 → 커넥터 → 커스텀 커넥터에 <span class="mono">mcp.higgsfield.ai/mcp</span></td><td><b>이 책에서 직접 확인</b>(6~10장)</td><td>데스크톱 앱·웹 모두 가능</td></tr>
<tr><td><b>ChatGPT</b></td><td>플러그인(Plugins) 목록에서 공식 <b>Higgsfield</b> 플러그인 추가 → 로그인</td><td>커스텀 MCP 서버로 브리지 주소 추가 가능(요금제에 따라). 이 책에서는 시험하지 않음</td><td>어도비 커넥터로 포토샵·프리미어·Firefly 일부 기능을 ChatGPT 안에서 사용(5-4)</td></tr>
<tr><td><b>Cursor</b></td><td>Customize → Marketplace에서 Higgsfield 추가</td><td>MCP 설정에 주소를 넣는 방식</td><td>코드·스크립트 작업과 함께 쓸 때</td></tr>
<tr><td><b>Codex · Claude Code</b></td><td>힉스필드 CLI + 스킬 설치</td><td>MCP 설정</td><td>터미널에서 일하는 코딩 에이전트</td></tr>
<tr><td><b>Gemini</b></td><td>Gemini CLI 같은 MCP 지원 도구의 설정 파일에 서버 주소 추가</td><td>같은 방식</td><td>구글 계정 중심으로 일할 때</td></tr>
<tr><td><b>Copilot</b></td><td>VS Code의 Copilot 에이전트 모드 등 MCP 지원 환경에서 서버 추가</td><td>같은 방식</td><td>마이크로소프트 업무 환경</td></tr>
</table>
<div class="note"><b>같은 계정, 같은 크레딧</b>힉스필드 계정 하나를 Claude, ChatGPT, Cursor에 동시에 연결할 수 있고, 어디서 만들든 같은 크레딧에서 빠집니다. 연결할 때 API 키는 필요 없고, 힉스필드 로그인 창에서 허용만 누르면 됩니다.</div>

<h2><span class="tag t1">따라 하기</span> 5-2 ChatGPT에 힉스필드 연결하기</h2>
''' + steps(
    'ChatGPT(웹 또는 데스크톱 앱)에 로그인합니다. 힉스필드는 유료 구독이 있어야 생성할 수 있습니다(4-2).',
    '왼쪽 메뉴나 설정에서 <b>플러그인(Plugins)</b> 목록을 엽니다. 검색칸에 <b>Higgsfield</b>를 입력합니다.',
    '<b>Higgsfield</b>를 누르고 <b>추가(Add)</b>. 힉스필드 로그인 창이 열리면 <b>직접</b> 로그인하고 허용합니다. 비밀번호를 ChatGPT 대화창에 쓰지 않습니다.',
    '새 대화를 열고 힉스필드를 이름으로 불러 시험합니다.',
) + P('PROMPT · ChatGPT에게', 'Higgsfield로 16:9 이미지 한 장을 가장 싼 모델로 만들어 줘. 비 오는 밤 네온 간판이 있는 골목, 사람 없음. 만들기 전에 크레딧이 얼마나 드는지 먼저 알려 줘.') + '''
<div class="ok"><b>성공하면</b>대화창에 생성 결과가 나오고, higgsfield.ai의 내 생성 목록에도 같은 이미지가 보입니다.</div>
<div class="warn"><b>되지 않는 기능도 있습니다</b>힉스필드 안내에 따르면 웹사이트 만들기 같은 일부 스킬은 ChatGPT 플러그인에서 쓸 수 없고 Claude·Cursor·CLI 에이전트에서만 됩니다. 메뉴 이름과 위치는 ChatGPT 업데이트에 따라 바뀔 수 있습니다.</div>

<h2>5-3 ChatGPT에 다른 MCP 서버 넣기 — 브리지를 쓰고 싶을 때</h2>
<p>ChatGPT는 원격 MCP 서버를 직접 추가할 수 있습니다. 힉스필드 브리지(<span class="mono">bridge.higgsfield.ai/mcp</span>)처럼 플러그인 목록에 없는 서버를 넣을 때 씁니다.</p>
''' + steps(
    'ChatGPT의 플러그인 화면에서 <b>추가(Add)</b> → <b>커스텀 MCP 서버 만들기(Create custom MCP server)</b>를 고릅니다. 예전 화면에서는 <b>설정 → 앱 → 고급 설정 → 개발자 모드</b>를 먼저 켜야 했습니다.',
    '이름(예: Higgsfield Bridge)과 서버 주소를 넣고 만듭니다.',
    '로그인 창이 열리면 힉스필드로 직접 로그인합니다.',
    '애펙에서 힉스필드 패널을 열고 Bridge MCP의 <b>Connect</b>를 누른 상태에서, 대화창에 “지금 열린 애펙의 컴포지션 목록을 보여 줘”라고 시험합니다.',
) + '''
<div class="note"><b>요금제와 권한</b>커스텀 MCP 서버를 쓸 수 있는 요금제와 쓰기(조작) 권한 범위는 ChatGPT 요금제와 시기에 따라 달랐습니다. 이 책은 브리지 조작을 Claude에서만 확인했으므로, 다른 AI에서는 같은 결과가 나오는지 짧은 작업으로 먼저 시험하세요.</div>

<h2>5-4 ChatGPT 안의 어도비 — Adobe for ChatGPT</h2>
<p>어도비는 2025년 12월 포토샵·Adobe Express·Acrobat을 ChatGPT 안에서 쓸 수 있게 했고, 지금은 하나의 <b>Adobe 커넥터</b>로 포토샵, 프리미어, Firefly, Express, Acrobat 등의 기능을 대화로 부를 수 있습니다. 애펙 자체가 들어간 것은 아니지만, 소스를 다듬는 데 유용합니다.</p>
<table>
<tr><th style="width:30%">이렇게 시키면</th><th>쓰는 곳</th></tr>
<tr><td>“Adobe Photoshop, 이 사진 배경을 흐리게 해 줘”</td><td>애펙에 넣을 배경 사진 손질</td></tr>
<tr><td>“Adobe Express로 행사 포스터 만들어 줘”</td><td>영상과 함께 쓸 홍보물</td></tr>
<tr><td>“Adobe Acrobat, 이 PDF에서 표만 뽑아 줘”</td><td>자막·데이터 그래픽용 자료 정리</td></tr>
</table>
<p>더 세밀하게 고치려면 대화 안의 버튼으로 웹·데스크톱 앱으로 넘어가 이어서 작업합니다.</p>

<h2>5-5 어떤 AI를 고를까</h2>
<table>
<tr><th style="width:28%">이럴 때</th><th>추천</th></tr>
<tr><td>애펙을 말로 조작하고 싶다</td><td>Claude + 브리지(이 책의 기준 환경)</td></tr>
<tr><td>이미 ChatGPT를 매일 쓴다</td><td>ChatGPT + 힉스필드 플러그인으로 생성부터. 사진·문서 손질은 Adobe 커넥터</td></tr>
<tr><td>스크립트·자동화를 함께 한다</td><td>Cursor·Codex·Claude Code + 힉스필드 CLI</td></tr>
<tr><td>회사가 마이크로소프트·구글 환경이다</td><td>Copilot·Gemini의 MCP 지원 도구. 회사 보안 정책을 먼저 확인</td></tr>
</table>
<div class="warn"><b>어떤 AI든 지킬 것</b>로그인과 결제는 본인이 직접 합니다. 연결은 공식 목록(플러그인·마켓플레이스)이나 공식 주소로만 합니다. 처음 연결한 AI에는 크레딧이 적게 드는 작업부터 시킵니다.</div>
<p class="src">출처: Higgsfield 도움말 “How do I connect Higgsfield to Claude, ChatGPT, or another AI agent?”, OpenAI 개발자 문서·커뮤니티 공지(ChatGPT 개발자 모드와 커스텀 MCP), Adobe 뉴스룸(2025.12.10), Adobe 도움말 “Adobe for ChatGPT”. 2026년 11월 확인.</p>
<h2>이 장 점검</h2>
<div class="stuck"><b>막혔을 때</b>플러그인이 보이지 않으면 요금제와 지역을 확인하고, 새 대화에서 힉스필드를 이름으로 불러 봅니다. 대화마다 커넥터를 켜는 스위치가 있는 경우도 있습니다. 연결 오류가 나면 커넥터를 지우고 다시 추가한 뒤 도구 목록을 새로 고칩니다.</div>
</section>
'''

CH14 = chead(14, '캐릭터란 무엇인가 — 설계, 리그, AI로 같은 인물 지키기', '●○○ ~ ●●○',
             '다음 장에서 로봇을 관절째 움직이기 전에, 움직일 “캐릭터”가 무엇이고 어떻게 준비하는지부터 봅니다. 손으로 움직일 때도, AI로 만들 때도 좋은 캐릭터는 같은 조건을 갖습니다.',
             '내 캐릭터 하나를 정하고, 정면·옆면 두 장짜리 간단한 캐릭터 시트를 만들면 성공입니다.') + '''
<h2>14-1 캐릭터란 무엇인가</h2>
<p><b>캐릭터(character)</b>는 영상 속에서 생각하고 움직이며 이야기를 끌고 가는 존재입니다. 사람만이 아닙니다. 동물, 로봇, 학교 마스코트, 말하는 로고, 눈과 입을 붙인 우유팩도 성격과 행동이 있으면 캐릭터입니다.</p>
<table>
<tr><th style="width:26%">모션그래픽에서의 캐릭터</th><th>예</th></tr>
<tr><td>브랜드 마스코트</td><td>기업·학교 홍보 영상의 안내자, SNS 스티커</td></tr>
<tr><td>설명 영상의 진행자</td><td>앱 사용법·공공 캠페인을 대신 설명하는 인물</td></tr>
<tr><td>의인화된 사물</td><td>그래프 막대가 웃으며 자라는 데이터 영상</td></tr>
<tr><td>AI 인물</td><td>AI로 만든 가상 모델·인플루언서. 장면마다 같은 얼굴을 지키는 것이 과제(14-6)</td></tr>
</table>

<h2>14-2 좋은 캐릭터의 조건</h2>
<table>
<tr><th style="width:22%">조건</th><th>확인하는 법</th></tr>
<tr><td>실루엣</td><td>검은색으로 칠해도 누군지 알아볼 수 있는가. 머리 모양·귀·소품이 실루엣을 만듭니다</td></tr>
<tr><td>비율</td><td>머리와 몸의 비율(2~3등신은 귀엽고, 6~8등신은 사실적). 움직일 관절이 분명한가</td></tr>
<tr><td>색</td><td>주된 색 2~3개. 배경 위에서도 묻히지 않는가</td></tr>
<tr><td>성격</td><td>서 있는 자세와 표정만 봐도 성격이 보이는가. 성격이 정해져야 걷는 속도·몸짓이 정해집니다</td></tr>
<tr><td>단순함</td><td>선과 부품이 적을수록 움직이기 쉽고, AI도 같은 모습을 잘 유지합니다</td></tr>
</table>

<h2><span class="tag t1">따라 하기</span> 14-3 캐릭터 시트 만들기</h2>
<p><b>캐릭터 시트</b>는 한 캐릭터를 여러 각도와 표정으로 정리한 설계도입니다. 애니메이터가 바뀌어도, AI에게 여러 장면을 시켜도 같은 모습을 지키게 해 줍니다.</p>
''' + steps(
    '종이나 일러스트레이터에서 <b>정면</b> 전신을 그립니다. 키를 같은 높이 선에 맞춥니다.',
    '같은 높이로 <b>옆면</b>(필요하면 3/4면, 뒷면)을 그립니다. 이 네 방향 묶음을 <b>턴어라운드</b>라고 합니다.',
    '아래에 <b>표정</b> 4~6개(기본, 웃음, 놀람, 화남, 슬픔)를 얼굴만 그립니다.',
    '옆에 <b>색 견본</b>(HEX 값)과 키·비율 메모를 적습니다. 애펙에서는 이 색을 컨트롤 레이어(18-16)에 넣어 둡니다.',
    '완성한 시트를 PNG로 저장해 프로젝트의 %s 폴더에 둡니다. 14-6에서 AI 참조 이미지로도 씁니다.' % M('99_Guide'),
) + '''
<h2>14-4 애펙에서 캐릭터를 움직이는 세 가지 방법</h2>
<table>
<tr><th style="width:24%">방법</th><th style="width:38%">어떻게</th><th>잘 맞는 캐릭터</th></tr>
<tr><td>부위 레이어 + 부모</td><td>머리·몸통·팔·다리를 레이어로 나누고 관절마다 부모를 겁니다(15-3, 15-4)</td><td>로봇, 종이 인형, 플랫 일러스트</td></tr>
<tr><td>퍼펫 핀</td><td>한 장의 그림에 핀을 꽂아 고무처럼 구부립니다(16-6)</td><td>꼬리, 머리카락, 흔들리는 마스코트</td></tr>
<tr><td>리깅 플러그인</td><td>Duik, RubberHose 같은 도구로 팔다리 IK·표정 컨트롤을 만듭니다(부록 C)</td><td>대사·걷기가 많은 본격 캐릭터 애니메이션</td></tr>
</table>

<h2><span class="tag t1">따라 하기</span> 14-5 일러스트레이터·포토샵에서 캐릭터 준비하기</h2>
''' + steps(
    '그림을 <b>움직일 부위마다 다른 레이어</b>로 나눕니다: 머리, 몸통, 윗팔, 아래팔, 손, 허벅지, 정강이, 발(좌우 각각).',
    '관절이 꺾여도 틈이 보이지 않도록, 이어지는 부위 끝을 <b>둥글게 겹쳐</b> 그립니다(팔꿈치·무릎에 원).',
    '레이어 이름을 영어로 짧게 정합니다(%s, %s…). 익스프레션과 AI 지시에서 이 이름을 그대로 부릅니다.' % (M('Head'), M('Arm_Upper_L')),
    '애펙에서 <b>File → Import → File</b>로 불러올 때 Import As를 <b>Composition - Retain Layer Sizes</b>로 고릅니다(25-5). 부위마다 레이어가 따로 들어옵니다.',
    '각 부위의 Anchor Point를 <b>관절 위치</b>로 옮깁니다. 도구 막대의 <b>Pan Behind Tool</b>(%s)로 팔은 어깨, 아래팔은 팔꿈치로 끌어다 놓습니다. 이제 다음 장의 부모 걸기를 할 준비가 끝났습니다.' % K('Y'),
) + '''
<h2>14-6 AI 캐릭터 — 장면마다 같은 인물 지키기</h2>
<p>AI로 캐릭터 영상을 만들 때 가장 어려운 일은 <b>일관성</b>입니다. 장면마다 얼굴, 옷, 비율이 조금씩 달라지기 때문입니다. 다음 방법을 겹쳐 쓰면 크게 줄어듭니다.</p>
<table>
<tr><th style="width:26%">방법</th><th>하는 일</th></tr>
<tr><td>참조 이미지</td><td>14-3의 캐릭터 시트를 매번 함께 넣습니다. 정면과 옆면을 같이 주면 돌아서는 장면도 덜 무너집니다</td></tr>
<tr><td>고정 설명문</td><td>“노란 우비, 둥근 안경, 2.5등신 로봇”처럼 바꾸지 않을 특징을 한 문단으로 정해 매번 같은 문장으로 씁니다</td></tr>
<tr><td>캐릭터 저장 기능</td><td>힉스필드의 캐릭터(인물 참조) 기능이나 Kling의 Elements처럼 인물을 저장해 두고 이름으로 불러 씁니다</td></tr>
<tr><td>시드·같은 모델</td><td>마음에 든 결과의 시드(seed)와 모델을 기록해 두고 바꾸지 않습니다</td></tr>
<tr><td>애펙에서 마무리</td><td>AI로 만든 동작 위에 애펙에서 로고·의상 색·자막을 얹으면, 브랜드 요소는 장면마다 정확히 같아집니다</td></tr>
</table>
<div class="warn"><b>실제 사람을 캐릭터로 쓸 때</b>실제 인물의 얼굴·목소리로 AI 캐릭터를 만들려면 본인의 동의가 필요합니다. 유명인·타인의 사진을 참조로 넣지 않고, 학교·기업 마스코트도 사용 권한을 확인합니다(29장).</div>
<h2>이 장 점검</h2>
<div class="ok"><b>성공하면</b>캐릭터 시트 한 장이 99_Guide 폴더에 있고, 부위별로 나뉜 캐릭터 파일이 애펙에 레이어로 들어와 있습니다.</div>
<div class="stuck"><b>막혔을 때</b>부위가 한 장으로 합쳐져 들어오면 Import As가 Footage로 되어 있는 것입니다. Composition - Retain Layer Sizes로 다시 불러옵니다.</div>
</section>
'''


def apply8(S):
    # ---------- cut pieces (current numbering)
    pieces = {}
    for no in (1, 2, 8, 9, 10, 14):
        a, b = chap(S, no)
        pieces[no] = S[a:b]
    h8, b8, _ = h2blocks(pieces[8])
    h9, b9, _ = h2blocks(pieces[9])
    h10, b10, _ = h2blocks(pieces[10])
    h2_, b2, _ = h2blocks(pieces[2])
    lang = blk(b2, '2-2')
    ch2_rest = pieces[2].replace(lang, '')
    # Higgsfield plans/sign-up go into the connect chapter, before plugin install (2-3)
    hig = blk(b10, '10-3') + blk(b10, '10-4')
    k = ch2_rest.find('<h2>2-3 ')
    ch2_rest = ch2_rest[:k] + hig + ch2_rest[k:]

    new1 = CH1_HEAD + CH1_NEW + renum(''.join(b9)) + '</section>\n'
    new2 = (CH2_HEAD + renum(blk(b10, '10-1') + blk(b10, '10-2')) + CH2_INSTALL
            + renum(blk(b8, '8-3') + lang + blk(b8, '8-1') + blk(b8, '8-2') + blk(b8, '8-4')) + '</section>\n')
    new3 = renum(pieces[1])
    new4 = renum(ch2_rest)

    # ---------- remove old pieces and old parts 1 & 4, then insert new front
    def cut(s, frag):
        assert frag in s, frag[:60]
        return s.replace(frag, '', 1)
    p1 = re.search(r'<section class="part"[^>]*><div class="no">PART 1</div>.*?</section>\n?', S, re.S).group(0)
    p4 = re.search(r'<section class="part"[^>]*><div class="no">PART 4</div>.*?</section>\n?', S, re.S).group(0)
    p2pos_marker = re.search(r'<section class="part"[^>]*><div class="no">PART 2</div>', S).group(0)
    for frag in (pieces[1], pieces[2], pieces[8], pieces[9], pieces[10], p1, p4):
        S = cut(S, frag)
    # renumber everything that remains (chapters 3..29)
    S = renum(S)
    # character chapter right before (new) chapter 15 "구조 만들기"
    k = S.find('<div class="ch-no">CHAPTER 15</div>')
    a = S.rfind('<section', 0, k)
    S = S[:a] + CH14 + '\n' + S[a:]
    # front block before the Higgsfield part (old PART 2)
    k = S.find(p2pos_marker)
    front = PART_NEW + new1 + new2 + new3 + PART_CONNECT + new4 + CH5
    S = S[:k] + front + '\n' + S[k:]
    # relabel parts in order
    order = list(re.finditer(r'<div class="no">PART \d</div>', S))
    pos = {mo.start(): i + 1 for i, mo in enumerate(order)}
    S = re.sub(r'<div class="no">PART \d</div>', lambda mo: '<div class="no">PART %d</div>' % pos[mo.start()], S)

    # ---------- front matter: overview cards, syllabus, notes
    cards = [('PART 1', '●○○', 'NEW · AI와 시작', '1~3장'),
             ('PART 2', '●○○', '연결', '4~5장 · GPT 등'),
             ('PART 3', '●○○', '힉스필드 패널', '6~8장'),
             ('PART 4', '●○○ ~ ●●○', 'Claude 브리지', '9~10장'),
             ('PART 5', '●○○ ~ ●●○', '애펙 기본기', '11~15장 · 캐릭터'),
             ('PART 6', '●●○ ~ ●●●', '모션그래픽', '16~18장'),
             ('PART 7', '●●○ ~ ●●●', '합성과 VFX', '19~23장'),
             ('PART 8', '●○○ ~ ●●●', '3D와 실무', '24~27장'),
             ('PART 9', '●○○ ~ ●●○', '완성과 정리', '28~30장 · 부록')]
    flat = [x for c in cards for x in c]
    i = S.find('>PART 1</text>')
    a = S.rfind('<svg', 0, i); b = S.find('</svg>', i)
    svg = S[a:b]
    cnt = [0]
    def tf(mo):
        j = cnt[0]; cnt[0] += 1
        if j < len(flat):
            return mo.group(1) + flat[j] + mo.group(3)
        if mo.group(2).startswith('AI부터 하려면'):
            return mo.group(1) + '처음이라면 PART 1부터, 애펙을 이미 안다면 PART 2부터 읽어도 됩니다.' + mo.group(3)
        return mo.group(0)
    svg = re.sub(r'(<text[^>]*>)([^<]*)(</text>)', tf, svg)
    S = S[:a] + svg + S[b:]

    def rep(old, new):
        nonlocal S
        if not RENUM3 and old not in S:
            print('pre-skip', old[:40]); return
        assert old in S, old
        S = S.replace(old, new)
    rep('<h1 class="ch">연결하기 — 영문 전환, 플러그인, 브리지', '<h1 class="ch">연결하기 — 힉스필드 가입, 플러그인, 브리지')
    rep('(PART 1~3, 9 실습용)', '(PART 1~4, 9 실습용)')
    rep('앞부분(PART 1~3)에서는 AI를 얹는 세 가지 길, 곧 애펙 자체 AI, 힉스필드 플러그인 패널, Claude 브리지로 먼저 결과를 만들어 보고, 뒷부분(PART 4~9)에서는',
        '앞부분(PART 1~4)에서는 AI가 무엇인지 짚고, AI를 얹는 세 가지 길, 곧 애펙 자체 AI, 힉스필드 플러그인 패널, Claude 브리지로 먼저 결과를 만들어 보고, 뒷부분(PART 5~9)에서는')
    rows = [('역사와 AI 지도, 설치 (8~10, 2-5)', '역사와 AI 지도, 설치 (1~2)'),
            ('부모, 마스크, 매트 (14)', '캐릭터, 부모, 마스크, 매트 (14~15)'),
            ('셰이프와 모션그래픽 기법 (15)', '셰이프와 모션그래픽 기법 (16)'),
            ('텍스트 애니메이션 (16)', '텍스트 애니메이션 (17)'),
            ('익스프레션 ① 기본 어휘 (17)', '익스프레션 ① 기본 어휘 (18)'),
            ('익스프레션 ②, 중간 과제 (17)', '익스프레션 ②, 중간 과제 (18)'),
            ('크로마키, 색 보정 (18, 22)', '크로마키, 색 보정 (19, 23)'),
            ('트래킹, 3D 트래커, 지우기 (19~21)', '트래킹, 3D 트래커, 지우기 (20~22)'),
            ('3D, 렌더와 출력, 직업별 팁 (23~26)', '3D, 렌더와 출력, 직업별 팁 (24~27)'),
            ('애펙 자체 AI, 연결, 패널 ① (1~3)', '애펙 자체 AI, 연결, 패널 ① (3~6)'),
            ('패널 ②③, Claude 타이틀 (4~7)', '패널 ②③, Claude 타이틀 (7~10)'),
            ('통합 기획, 검수 (27~28)', '통합 기획, 검수 (28~29)'),
            ('기말 발표: 30초 홍보영상 (27, 29)', '기말 발표: 30초 홍보영상 (28, 30)')]
    for o, n in rows:
        rep(o, n)
    return S
