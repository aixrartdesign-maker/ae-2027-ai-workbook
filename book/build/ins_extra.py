# -*- coding: utf-8 -*-
# Extra content (2026-11-24): relinking missing footage (ch.2), timeline modes and blending modes (ch.4), troubleshooting rows.

RELINK = '''
<h3>원본 파일 이름을 바꾸거나 옮겼을 때 — 다시 연결하기</h3>
<p>애펙 프로젝트(.aep)는 영상·이미지를 파일 안에 담지 않고 <b>원본 파일이 있는 자리(경로)</b>만 기억합니다. 그래서 작업 중에 소스 파일의 이름을 바꾸거나, 다른 폴더로 옮기거나, 지우면 다음에 프로젝트를 열 때 “files are missing” 경고가 뜹니다. 그 레이어는 화면에 <b>컬러 바(색 막대)</b>로 나오고, 프로젝트 패널의 이름은 기울어진 글자로 바뀝니다.</p>
<div class="step"><div class="n">1</div><div class="b">프로젝트 패널에서 기울어진 이름의 항목을 우클릭 → <b>Replace Footage → File</b>(<span class="k">Ctrl+H</span>).</div></div>
<div class="step"><div class="n">2</div><div class="b">옮긴 곳의 파일, 또는 이름을 바꾼 파일을 골라 <b>Import</b>합니다. 같은 폴더에 빠진 파일이 더 있으면 애펙이 나머지도 한꺼번에 찾아 연결합니다.</div></div>
<div class="step"><div class="n">3</div><div class="b">이미지 시퀀스(001.png, 002.png …)라면 첫 파일을 고르고 <b>Sequence</b> 체크를 켭니다.</div></div>
<div class="step"><div class="n">4</div><div class="b">빠진 파일이 많으면 <b>File → Dependencies → Find Missing Footage</b>로 빠진 항목만 모아 보고 하나씩 연결합니다.</div></div>
<div class="tip"><b>Replace Footage의 다른 쓰임</b>효과·키프레임·마스크는 그대로 두고 원본만 바꿉니다. 480p 연습 영상으로 작업한 뒤 업스케일한 최종본(18-5)으로 바꿔 끼울 때도 같은 방법을 씁니다. 지운 파일은 다시 연결할 수 없으니 휴지통에서 되살리거나 같은 내용의 파일로 바꿔 끼웁니다.</div>
<div class="layer3"><div class="lh"><span class="tag t4">현장의 기준</span> 경로가 깨지지 않게</div><ul><li>프로젝트 폴더 안에 <span class="mono">footage</span>·<span class="mono">render</span> 폴더를 먼저 만들고, 소스를 넣은 뒤 불러옵니다. 바탕화면·다운로드 폴더에서 바로 불러오지 않습니다.</li><li>불러온 뒤에는 파일 이름을 바꾸지 않습니다. 바꿔야 한다면 애펙을 닫기 전에 Replace Footage까지 끝냅니다.</li><li>다른 컴퓨터로 옮기거나 제출할 때는 <b>File → Dependencies → Collect Files</b>(14-6)로 소스까지 한 폴더에 모읍니다.</li></ul></div>
'''

MODES = '''
<table>
<tr><th style="width:22%">모드 묶음</th><th style="width:34%">대표 모드</th><th>이렇게 섞입니다</th></tr>
<tr><td>기본</td><td>Normal, Dissolve</td><td>위 레이어가 그대로 덮음. Dissolve는 불투명도를 점으로 흩뿌림</td></tr>
<tr><td>어둡게</td><td>Darken, Multiply, Color Burn, Linear Burn</td><td>흰색은 사라지고 어두운 곳만 남음 — 종이 질감, 그림자, 잉크</td></tr>
<tr><td>밝게</td><td>Lighten, Screen, Add, Color Dodge</td><td>검은색은 사라지고 밝은 곳만 남음 — 빛, 불꽃, 렌즈 플레어</td></tr>
<tr><td>대비</td><td>Overlay, Soft Light, Hard Light, Vivid Light</td><td>중간 회색은 사라지고 대비가 커짐 — 질감 입히기, 색 보정</td></tr>
<tr><td>차이</td><td>Difference, Exclusion, Subtract</td><td>두 레이어의 차이를 보여 줌 — 정렬 확인, 반전 효과</td></tr>
<tr><td>색</td><td>Hue, Saturation, Color, Luminosity</td><td>색상·채도·밝기 중 하나만 가져옴 — 흑백 영상에 색 입히기</td></tr>
<tr><td>투명</td><td>Stencil Alpha, Silhouette Alpha</td><td>이 레이어 모양으로 아래 레이어 전체를 뚫거나 남김</td></tr>
</table>
<h3>타임라인에서 모드 칸 쓰기</h3>
<div class="step"><div class="n">1</div><div class="b">타임라인 아래 <b>Toggle Switches / Modes</b> 버튼(<span class="k">F4</span>)을 누르면 스위치 칸과 <b>Mode</b> 칸이 번갈아 나옵니다(그림 2-4).</div></div>
<div class="step"><div class="n">2</div><div class="b">레이어 줄의 Mode 칸(처음엔 Normal)을 눌러 모드를 고릅니다. 레이어를 고른 채 <span class="k">Shift</span>+<span class="k">=</span> / <span class="k">Shift</span>+<span class="k">-</span>를 누르면 모드를 하나씩 넘겨 보며 바로 비교할 수 있습니다.</div></div>
<div class="step"><div class="n">3</div><div class="b">칸 제목 줄을 우클릭 → <b>Columns</b>에서 Modes, Parent &amp; Link, Stretch(속도) 같은 칸을 늘 보이게 켤 수 있습니다. 스위치와 모드를 동시에 보고 싶을 때 씁니다.</div></div>
<div class="tip"><b>모드가 안 먹는 것 같을 때</b>블렌딩 모드는 바로 <b>아래 레이어들</b>과 섞입니다. 맨 아래 레이어에 모드를 주면 섞을 대상이 없어 변화가 없습니다. 프리컴포즈 안에서 준 모드는 그 컴포지션 안에서만 섞이니, 바깥과 섞으려면 프리컴포즈 레이어에 모드를 줍니다.</div>
'''

def apply(S):
    a = '<tr><td>이름이 기울어진 글자</td><td>Missing</td><td>원본을 찾지 못함 — 우클릭 → Replace Footage</td></tr>\n</table>'
    assert a in S, 'missing row'
    S = S.replace(a, a.replace('원본을 찾지 못함 — 우클릭 → Replace Footage', '원본을 찾지 못함 — 아래 “다시 연결하기”') + RELINK, 1)
    h = '<h2><span class="tag t2">왜 그럴까</span> 4-8 블렌딩 모드</h2>'
    i = S.index(h); j = S.index('</table>', i) + len('</table>')
    S = S[:i] + h + '\n<p>블렌딩 모드는 위 레이어의 색을 아래 레이어들과 <b>어떤 계산으로 섞을지</b> 정합니다. 30개 가까이 되지만 일곱 묶음으로 나누면 쉽습니다. 묶음 안의 모드는 세기만 다릅니다.</p>' + MODES + S[j:]
    # troubleshooting rows
    t = '<tr><td>생성이 오래 걸림</td>'
    if t in S:
        S = S.replace(t, '<tr><td>화면이 컬러 바, 이름이 기울어짐</td><td>원본 파일 이름이 바뀌거나 옮겨짐. 우클릭 → Replace Footage → File(2-4)</td></tr>\n<tr><td>블렌딩 모드가 안 먹음</td><td>맨 아래 레이어이거나 프리컴포즈 안쪽에 준 경우(4-8)</td></tr>\n' + t, 1)
    return S

CREDITS = '''
<h2><span class="tag t2">왜 그럴까</span> 23-3 어도비 생성 크레딧 — 얼마나, 어떻게 쓰이나</h2>
<p>AI Assistant, Generative Fill, 영상 생성처럼 어도비의 생성형 AI 기능은 <b>생성 크레딧(generative credits)</b>으로 값을 치릅니다. 크레딧은 <b>어도비 계정(Adobe ID)</b>에 붙어 있어서 포토샵·프리미어·애펙·Firefly 어디서 쓰든 같은 통에서 빠집니다. 힉스필드 크레딧과는 전혀 별개입니다.</p>
<table>
<tr><th style="width:26%">항목</th><th>내용 (2026년 11월 기준)</th></tr>
<tr><td>지급 방식</td><td>플랜마다 매달 정해진 양을 받습니다. 결제를 시작한 날을 기준으로 매달 다시 채워지고, <b>남은 크레딧은 다음 달로 넘어가지 않습니다</b>. 플랜이 둘이면 각 플랜의 결제일에 따로 채워집니다.</td></tr>
<tr><td>플랜별 양</td><td>애펙 단일 앱(2025년 6월 17일 이후 가입) 월 25 · Creative Cloud Standard 월 25 · Creative Cloud Pro 월 4,000(표준 기능은 무제한)</td></tr>
<tr><td>표준 기능</td><td>Generative Fill 같은 이미지 기능. 보통 한 번에 1크레딧이고, Creative Cloud Pro·Firefly 플랜은 무제한입니다.</td></tr>
<tr><td>프리미엄 기능</td><td>영상·소리 생성과 파트너 모델. Firefly 영상 생성은 720p 초당 50, 1080p 초당 100크레딧입니다. 파트너 모델은 모델마다 다릅니다(예: Veo 3.1 초당 50, GPT Image 2 고해상도 한 장 80, Nano Banana 2 1K 한 장 20 — 일부는 한시 요율).</td></tr>
<tr><td>모자랄 때</td><td>다음 달까지 기다리거나 Firefly 플랜을 더합니다. 미국 기준 Standard 월 $9.99(2,000) · Pro $19.99(4,000) · Pro Plus $49.99(10,000) · Premium $199.99(50,000). 2,000크레딧은 5초 영상 약 20편 분량입니다.</td></tr>
</table>
<h3>AI Assistant 베타의 크레딧 정책</h3>
<ul>
<li>공개 베타 초기에는 Firefly 생성까지 무료였고, 2026년 11월 6일부터 After Effects (beta)에서 크레딧 차감이 시작되었습니다.</li>
<li>어도비는 지금 요율이 <b>“도입 요율이며 바뀔 수 있다”</b>고 밝힙니다. 동작마다 드는 양이 다르고, 동작이 끝난 뒤 크레딧 아이콘에 마우스를 올리면 실제로 쓴 양이 보입니다.</li>
<li>애펙 단일 앱의 월 25크레딧은 생성 동작 한두 번이면 끝납니다. 이미지·영상 생성까지 자주 쓰려면 Creative Cloud Pro나 Firefly 플랜이 필요합니다.</li>
</ul>
<h3>어떤 엔진으로 돌아가나</h3>
<p>AI Assistant는 어도비의 크리에이티브 에이전트가 요청을 해석해 애펙 안의 동작으로 바꾸고, 이미지·영상은 <b>Firefly 모델</b>과 <b>파트너 모델</b>(Google Gemini·Nano Banana·Veo, OpenAI GPT Image, FLUX, Runway, Luma, ElevenLabs 등)로 만듭니다. 모델을 지정하지 않으면 Assistant가 고릅니다. 대화를 맡는 언어 모델의 회사는 공개되지 않았습니다. Firefly 결과물은 상업적 사용에 안전하다고 어도비가 밝히지만 파트너 모델 결과물은 사용자가 판단해야 하고, 생성물은 레이어가 아닌 파일로 들어옵니다. 사용자 콘텐츠는 모델 학습에 쓰이지 않습니다.</p>

<p class="src">출처: Adobe 도움말 「Generative credits FAQ」「Partner models in Adobe products」「After Effects AI Assistant (beta) FAQ」, Adobe 커뮤니티 공지(2026.11), adobe.com Firefly 요금 페이지. 2026년 11월 24일 확인. 요금과 요율은 자주 바뀌므로 쓰기 전에 다시 확인하세요.</p>
'''

def apply2(S):
    a = '<div class="note"><b>어도비 생성 크레딧</b>AI Assistant의 AI 동작 대부분은 어도비 계정의 생성 크레딧(generative credits)을 씁니다. 남은 양은 어도비 계정 페이지에서 확인하세요. 힉스필드 크레딧과는 별개입니다.</div>'
    assert a in S
    S = S.replace(a, a.replace('힉스필드 크레딧과는 별개입니다.', '힉스필드 크레딧과는 별개입니다. 자세한 정책은 23-3에 정리했습니다.'), 1)
    i = S.index('<h2>23-2 Object Matte')
    j = S.index('<h2>이 장 점검</h2>', i)
    return S[:j] + CREDITS.strip() + '\n\n' + S[j:]
