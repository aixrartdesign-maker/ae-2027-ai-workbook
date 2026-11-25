# -*- coding: utf-8 -*-
# 2026-11-26: deeper tracking (ch.9, ch.10), particles (5-7: snow/rain/smoke), AE 27.0 AI features (ch.23)

def st(n, b):
    return '<div class="step"><div class="n">%d</div><div class="b">%s</div></div>\n' % (n, b)

def steps(*bs):
    return ''.join(st(i + 1, b) for i, b in enumerate(bs))

K = lambda s: '<span class="k">%s</span>' % s
M = lambda s: '<span class="mono">%s</span>' % s

# ---------------------------------------------------------------- particles
PART_SNOW = '''
<h3>눈 내리기 — CC Snowfall 한 단계씩</h3>
<p>눈은 CC Particle World보다 <b>CC Snowfall</b>이 빠릅니다. 화면 전체에 깊이감 있는 눈송이를 한 번에 깔아 주고, 바람과 흔들림이 처음부터 들어 있습니다.</p>
''' + steps(
    '눈을 얹을 영상이 있는 컴포지션을 엽니다. 메뉴 <b>Layer → New → Solid</b>(%s)를 누르고, 창에서 <b>Make Comp Size</b>를 누른 뒤 색은 검정, 이름은 %s로 적고 <b>OK</b>.' % (K('Ctrl+Y'), M('눈_가까이')),
    '솔리드를 고른 채 메뉴 <b>Effect → Simulation → CC Snowfall</b>을 누릅니다. 왼쪽 위 Effect Controls 패널에 CC Snowfall이 열리고, 검은 화면에 흰 점이 떨어집니다.',
    'Effect Controls 맨 아래 <b>Composite With Original</b> 체크를 끕니다. 검은 바탕이 사라지지는 않으니, 타임라인에서 솔리드의 Mode 칸(%s로 표시)을 <b>Screen</b>으로 바꿉니다. 이제 눈만 영상 위에 남습니다.' % K('F4'),
    '아래 표의 “가까운 눈” 값으로 바꿉니다. 숫자 칸은 클릭해 직접 입력하거나, 숫자 위에서 좌우로 드래그해 바꿉니다.',
    '솔리드를 %s로 복제하고 이름을 %s로 바꿉니다. 표의 “먼 눈” 값으로 바꾸고, <b>Effect → Blur &amp; Sharpen → Fast Box Blur</b>를 넣어 Blur Radius 2를 줍니다. 먼 눈은 작고 느리고 흐릿해야 깊이가 생깁니다.' % (K('Ctrl+D'), M('눈_멀리')),
    '가까운 눈 레이어에도 Fast Box Blur 1.5를 줍니다. 카메라 가까이 지나가는 눈은 초점이 맞지 않아 살짝 흐려야 자연스럽습니다.',
    '<span class="k">Space</span>로 재생해 보며 Wind 값을 조절합니다. 사람이 걸어가는 방향과 반대로 살짝 기울이면 바람 부는 날이 됩니다.',
) + '''
<table>
<tr><th style="width:30%">항목</th><th style="width:17%">가까운 눈</th><th style="width:17%">먼 눈</th><th>하는 일</th></tr>
<tr><td>Flakes</td><td>3000</td><td>9000</td><td>눈송이 수. 먼 눈을 많게, 가까운 눈을 적게</td></tr>
<tr><td>Size</td><td>6</td><td>2</td><td>눈송이 크기</td></tr>
<tr><td>Variation % (Size)</td><td>80</td><td>60</td><td>크기의 들쭉날쭉한 정도</td></tr>
<tr><td>Speed</td><td>220</td><td>90</td><td>떨어지는 속도. 함박눈은 느리게</td></tr>
<tr><td>Wind</td><td>40</td><td>40</td><td>옆으로 밀리는 힘. 두 레이어를 같게</td></tr>
<tr><td>Spread</td><td>15</td><td>15</td><td>눈송이마다 방향이 흩어지는 정도</td></tr>
<tr><td>Wiggle → Amount</td><td>4</td><td>2</td><td>좌우로 하늘거리는 폭</td></tr>
<tr><td>Opacity</td><td>100</td><td>70</td><td>먼 눈은 조금 옅게</td></tr>
</table>
<div class="tip"><b>더 그럴듯하게</b>눈 오는 날은 대비가 낮고 차갑습니다. 영상 위에 조정 레이어(<b>Layer → New → Adjustment Layer</b>)를 두고 Lumetri Color에서 Temperature −15, Contrast −20, Highlights +15를 주면 눈과 배경이 같은 날씨로 보입니다. 바닥에 쌓이는 눈은 Extras → <b>Ground Level</b>과 <b>Embed Depth</b>로 눈이 사라지는 높이를 정합니다.</div>
'''

PART_RAIN = '''
<h3>비 내리기 — CC Rainfall 한 단계씩</h3>
<p>비는 <b>CC Rainfall</b>을 씁니다. 빗줄기 자체는 거의 투명해서, 효과만으로는 비가 “보이지” 않습니다. 빗줄기 + 젖은 화면 색 + 깊이, 세 가지를 함께 만들어야 비 오는 날이 됩니다.</p>
''' + steps(
    '검은 솔리드(%s)를 만들고 이름을 %s로 적습니다. <b>Effect → Simulation → CC Rainfall</b>을 넣습니다.' % (K('Ctrl+Y'), M('비_가까이')),
    'Effect Controls에서 <b>Composite With Original</b>을 끄고, 레이어 Mode를 <b>Screen</b>으로 바꿉니다(눈과 같은 원리입니다).',
    '아래 표의 값으로 바꿉니다. <b>Wind</b>를 주면 빗줄기가 비스듬해지고, <b>Spread</b>를 줄이면 빗줄기가 한 방향으로 가지런해집니다.',
    '%s로 복제해 %s를 만들고 Drops를 늘리고 Size와 Opacity를 낮춥니다. 먼 비는 가늘고 촘촘해야 공기 속의 비처럼 보입니다.' % (K('Ctrl+D'), M('비_멀리')),
    '영상 바로 위에 조정 레이어를 두고 <b>Effect → Color Correction → Lumetri Color</b>를 넣습니다. Basic Correction에서 Exposure −0.6, Contrast −15, Saturation 75, Temperature −20. 비 오는 날의 어둡고 차가운 빛이 됩니다.',
    '번개를 넣고 싶으면 조정 레이어를 하나 더 만들어 <b>Exposure</b> 효과를 넣고, 두세 프레임만 Exposure를 +1.5로 올렸다 내리는 키프레임을 겁니다. 번갯불 모양까지 원하면 <b>Effect → Generate → Advanced Lightning</b>을 씁니다.',
) + '''
<table>
<tr><th style="width:30%">항목</th><th style="width:17%">가까운 비</th><th style="width:17%">먼 비</th><th>하는 일</th></tr>
<tr><td>Drops</td><td>4000</td><td>12000</td><td>빗방울 수</td></tr>
<tr><td>Size</td><td>4</td><td>2</td><td>빗줄기 굵기·길이</td></tr>
<tr><td>Speed</td><td>5000</td><td>4000</td><td>떨어지는 속도. 빠를수록 빗줄기가 길어짐</td></tr>
<tr><td>Wind</td><td>600</td><td>600</td><td>기울기. 두 레이어를 같게</td></tr>
<tr><td>Variation % (Wind)</td><td>20</td><td>20</td><td>빗줄기마다 기울기가 조금씩 다르게</td></tr>
<tr><td>Spread</td><td>4</td><td>4</td><td>방향 흩어짐. 소나기는 작게</td></tr>
<tr><td>Opacity</td><td>45</td><td>25</td><td>빗줄기 진하기</td></tr>
<tr><td>Extras → Appearance</td><td>Soft Solid</td><td>Refracting</td><td>Soft Solid는 하얀 줄, Refracting은 뒤 배경을 굴절시킨 투명 줄</td></tr>
</table>
<div class="note"><b>힉스필드와 비교</b>19-1의 Change Weather는 땅이 젖고 빛이 바뀌는 것까지 한 번에 만들어 줍니다. CC Rainfall은 빗줄기만 만들지만 굵기·양·방향을 프레임 단위로 고칠 수 있고 크레딧이 들지 않습니다. 둘을 겹쳐 AI 결과 위에 앞쪽 빗줄기만 더하는 방법도 좋습니다.</div>
'''

PART_SMOKE = '''
<h3>연기 — 피어오르는 연기 기둥과 깔리는 연기</h3>
<p>연기는 두 가지로 나눠 만듭니다. 굴뚝·향·찻잔처럼 <b>한 곳에서 피어오르는 연기</b>는 CC Particle World로, 바닥에 깔리거나 화면을 지나가는 <b>넓은 연기</b>는 Fractal Noise로 만듭니다.</p>
<p><b>A. 피어오르는 연기 기둥</b></p>
''' + steps(
    '검은 솔리드(%s)를 만들고 이름을 %s로 적은 뒤 <b>Effect → Simulation → CC Particle World</b>를 넣습니다.' % (K('Ctrl+Y'), M('연기_기둥')),
    'Effect Controls에서 <b>Producer</b>를 펼쳐 Position X·Y를 연기가 나올 자리(예: 찻잔 위)로 옮기고, Radius X 0.02, Radius Y 0.02, Radius Z 0.02로 아주 좁힙니다. 한 점에서 나와야 기둥이 됩니다.',
    '<b>Birth Rate</b> 0.6, <b>Longevity (sec)</b> 3. <b>Physics</b>를 펼쳐 Velocity 0.15, <b>Gravity −0.08</b>(음수라 위로 올라갑니다), Extra 0.4(흔들리는 정도)로 바꿉니다.',
    '<b>Particle</b>을 펼쳐 Particle Type <b>Faded Sphere</b>, Birth Size 0.25, Death Size 1.4(올라가며 퍼지게), Max Opacity 20%. Birth Color는 밝은 회색, Death Color는 어두운 회색으로 둡니다.',
    '<b>Effect → Blur &amp; Sharpen → Fast Box Blur</b>를 넣고 Blur Radius 25. 알갱이가 뭉개지며 하나의 연기 덩어리가 됩니다.',
    '<b>Effect → Distort → Turbulent Displace</b>를 넣고 Amount 40, Size 60. Evolution의 스톱워치를 %s+클릭해 익스프레션 %s를 넣으면 연기가 계속 일렁입니다.' % (K('Alt'), M('time*120')),
    '레이어 Mode를 <b>Screen</b>으로 바꿔 배경 영상 위에 얹습니다. 너무 진하면 레이어 Opacity를 60% 정도로 낮춥니다.',
) + '''
<p><b>B. 화면에 깔리는 연기·안개</b></p>
''' + steps(
    '검은 솔리드를 만들고 이름을 %s로 적은 뒤 <b>Effect → Noise &amp; Grain → Fractal Noise</b>를 넣습니다. 화면이 회색 구름 무늬로 바뀝니다.' % M('연기_바닥'),
    'Noise Type <b>Soft Linear</b>, Contrast 160, Brightness −45. 어두운 부분이 투명해질 곳, 밝은 부분이 연기가 될 곳입니다.',
    '<b>Transform</b>을 펼쳐 Uniform Scaling 체크를 끄고 Scale Width 400, Scale Height 160. 연기가 옆으로 길게 퍼집니다. Complexity는 5.',
    '움직임을 넣습니다. <b>Offset Turbulence</b>의 스톱워치를 %s+클릭하고 %s를 입력하면 연기가 오른쪽으로 흘러갑니다. <b>Evolution</b>에도 %s를 넣어 모양이 계속 바뀌게 합니다.' % (K('Alt'), M('value + [time*60, 0]'), M('time*40')),
    '타임라인에서 레이어를 고른 채 도구 막대의 <b>Rectangle Tool</b>(%s)을 더블클릭하면 레이어 크기의 마스크가 생깁니다. %s를 두 번 눌러 Mask Feather를 열고 200으로 올린 뒤, 마스크 윗변을 화면 아래쪽 1/3까지 끌어내립니다. 연기가 바닥에만 깔립니다.' % (K('Q'), K('F')),
    'Mode를 <b>Screen</b>으로 바꾸고 Opacity 50%. 앞쪽에 하나, 뒤쪽에 Scale을 다르게 한 것 하나를 더 두면 겹겹의 연기가 됩니다.',
) + '''
<div class="tip"><b>색 있는 연기</b>연막탄처럼 색이 있는 연기는 마지막에 <b>Effect → Color Correction → Tint</b>로 Map White To를 원하는 색으로 바꿉니다. 불에서 나는 연기는 아래쪽이 주황, 위쪽이 회색이므로 CC Particle World의 Birth Color를 주황, Death Color를 회색으로 두면 됩니다.</div>
'''

# ---------------------------------------------------------------- tracking ch.9
TRK_PANEL = '''
<h2>9-2 Tracker 패널 한눈에 보기</h2>
<p>모든 2D 트래킹은 <b>Window → Tracker</b> 패널에서 시작합니다. 버튼과 칸이 많아 보이지만, 위에서 아래로 “무엇을 추적할지 → 어떤 방식으로 → 결과를 어디에 붙일지” 순서로 놓여 있습니다.</p>
<table>
<tr><th style="width:28%">자리</th><th>하는 일</th></tr>
<tr><td>Track Camera</td><td>3D 카메라 트래커를 넣습니다(10장)</td></tr>
<tr><td>Warp Stabilize</td><td>흔들림을 자동으로 잡는 Warp Stabilizer를 넣습니다(9-8)</td></tr>
<tr><td>Track Motion</td><td>점을 따라가 그 움직임을 다른 레이어에 붙입니다</td></tr>
<tr><td>Stabilize Motion</td><td>점을 따라가 그 반대로 영상을 움직여 흔들림을 없앱니다</td></tr>
<tr><td>Motion Source</td><td>추적할 영상 레이어. 영상 레이어를 고른 뒤 Track Motion을 누르면 자동으로 들어갑니다</td></tr>
<tr><td>Current Track</td><td>한 레이어에 트래커를 여러 개 만들었을 때 지금 고친 트래커</td></tr>
<tr><td>Track Type</td><td>Transform(위치·회전·크기), Parallel corner pin(평행 4점), Perspective corner pin(원근 4점), Stabilize, Raw(데이터만)</td></tr>
<tr><td>Position · Rotation · Scale</td><td>Transform일 때 무엇을 따라갈지. Position만 켜면 점 1개, Rotation이나 Scale을 켜면 점 2개가 생깁니다</td></tr>
<tr><td>Motion Target / Edit Target…</td><td>추적 결과를 붙일 대상. 레이어 또는 <b>Effect point control</b>(렌즈 플레어 중심 같은 효과의 점)을 고를 수 있습니다</td></tr>
<tr><td>Options…</td><td>Channel(RGB·Luminance·Saturation), 추적 전 흐림·선명하게, Adapt Feature On Every Frame, 신뢰도가 낮을 때 할 일</td></tr>
<tr><td>Analyze ◀| ◀ ▶ |▶</td><td>한 프레임 뒤로, 뒤로 끝까지, 앞으로 끝까지, 한 프레임 앞으로 분석</td></tr>
<tr><td>Reset · Apply</td><td>트래커 위치를 처음으로 되돌림 · 결과를 대상에 붙임</td></tr>
</table>
<p>Layer 패널에 나타나는 <b>트랙 포인트</b>는 세 부분입니다. 안쪽 상자(Feature Region)는 따라갈 무늬, 바깥 상자(Search Region)는 다음 프레임에서 그 무늬를 찾는 범위, 가운데 십자(Attach Point)는 결과가 붙는 자리입니다. 상자 안쪽 빈 곳을 드래그하면 세 부분이 함께 움직이고, 상자 모서리를 드래그하면 크기만 바뀝니다.</p>
'''

TRK_ONE = '''
<h2><span class="tag t1">따라 하기</span> 9-3 1점 트래킹 — 널에 붙이고 글자를 따라가게</h2>
<p>움직이는 사람 옆에 이름표를, 달리는 차 위에 화살표를 붙이는 가장 기본적인 방법입니다. 결과를 글자에 바로 붙이지 않고 <b>널(Null)</b>에 먼저 붙이는 것이 핵심입니다. 널은 화면에 보이지 않는 빈 손잡이라서, 글자·셰이프·이미지를 몇 개든 거기에 걸 수 있고, 글자 자체의 애니메이션도 망가지지 않습니다.</p>
''' + steps(
    '영상을 컴포지션에 놓고 그 레이어를 클릭해 고릅니다. 메뉴 <b>Animation → Track Motion</b>을 누릅니다(또는 Tracker 패널의 <b>Track Motion</b>). 화면이 Layer 패널로 바뀌고 <b>Track Point 1</b>이 생깁니다.',
    'Tracker 패널에서 Track Type이 <b>Transform</b>, <b>Position</b>만 체크되어 있는지 확인합니다.',
    '타임 인디케이터를 0초로 옮깁니다(%s). 트랙 포인트의 안쪽 상자 빈 곳을 드래그해, 따라갈 대상에서 <b>대비가 강하고 모양이 뚜렷한 곳</b>(어깨의 단추, 차 번호판의 모서리)에 얹습니다. 드래그하는 동안 상자 안이 확대되어 보입니다.' % K('Home'),
    '대상이 빨리 움직이면 바깥 상자를 넓히고, 무늬가 크면 안쪽 상자도 조금 키웁니다. 상자가 클수록 정확하지만 분석이 느립니다.',
    'Tracker 패널의 <b>Analyze forward</b>(▶)를 누릅니다. 프레임마다 상자가 따라가며 경로에 작은 점(키프레임)이 찍힙니다.',
    '중간에 상자가 미끄러지면 바로 <b>Stop</b>을 누르고, 어긋난 첫 프레임으로 가서 상자를 제자리로 옮긴 뒤 다시 Analyze forward를 누릅니다. 그 뒤 프레임만 다시 분석됩니다.',
    '이제 붙일 대상을 만듭니다. 메뉴 <b>Layer → New → Null Object</b>(%s). 타임라인에 %s이 생깁니다.' % (K('Ctrl+Alt+Shift+Y'), M('Null 1')),
    'Tracker 패널의 <b>Edit Target…</b>을 누르고, Motion Target 창에서 Layer를 <b>Null 1</b>로 고른 뒤 <b>OK</b>.',
    '<b>Apply</b>를 누르면 Motion Tracker Apply Options 창이 뜹니다. Apply Dimensions를 <b>X and Y</b>로 두고 <b>OK</b>. 널의 Position에 프레임마다 키프레임이 들어갑니다.',
    '화면을 Composition 패널로 돌아가 텍스트를 씁니다(%s로 Type Tool, 화면 클릭 후 입력). 글자를 대상 옆 원하는 자리에 놓습니다.' % K('Ctrl+T'),
    '타임라인에서 텍스트 레이어의 <b>Parent &amp; Link</b> 칸의 소용돌이 아이콘(픽윕)을 끌어 <b>Null 1</b> 위에 놓습니다. 재생하면 글자가 지금 자리를 유지한 채 대상을 따라갑니다.',
)

TRK_ONE_TAIL = '''
<table>
<tr><th style="width:24%">붙일 것</th><th>방법과 요령</th></tr>
<tr><td>텍스트</td><td>널에 부모로 겁니다. 글자 등장 애니메이션(6장)은 텍스트 레이어에 따로 넣으면 따라가면서 움직입니다</td></tr>
<tr><td>셰이프(화살표·원)</td><td>텍스트와 같습니다. 여러 개를 한 널에 걸면 한꺼번에 따라갑니다</td></tr>
<tr><td>이미지·영상·프리컴포즈</td><td>같은 방법. 대상이 가까워지거나 멀어지면 9-4의 2점 트래킹으로 크기까지 따라가게 합니다</td></tr>
<tr><td>조정 레이어</td><td>조정 레이어에 마스크를 그리고 널에 걸면, 그 부분만 색을 바꾸거나 흐리게 할 수 있습니다. 모양이 바뀌는 대상은 9-7의 마스크 트래킹이 낫습니다</td></tr>
<tr><td>효과의 점</td><td>Edit Target에서 <b>Effect point control</b>을 고르면 Lens Flare의 Flare Center 같은 점이 직접 따라갑니다. 햇빛 반사가 움직이는 차를 따라가게 할 때 씁니다</td></tr>
</table>
<div class="why"><b>왜 글자에 바로 붙이지 않을까</b>Apply로 글자에 바로 붙이면 글자의 Position이 트래킹 키프레임으로 덮여, 글자를 옮기거나 등장 애니메이션을 넣을 수 없습니다. 널에 붙여 두면 트래킹은 널이, 디자인은 글자가 맡아 서로 방해하지 않습니다. 트래킹을 다시 하더라도 널만 바꾸면 됩니다.</div>
'''

TRK_TWO = '''
<h2><span class="tag t1">따라 하기</span> 9-4 2점 트래킹 — 돌고 커지는 대상까지</h2>
<p>대상이 기울어지거나 카메라에 다가오면 위치만으로는 부족합니다. 점 두 개의 거리와 각도를 재서 <b>회전과 크기</b>까지 따라가게 합니다. 돌아가는 자동차 바퀴의 로고, 다가오는 상자 위 스티커가 이런 경우입니다.</p>
''' + steps(
    '영상 레이어를 고르고 <b>Animation → Track Motion</b>. Tracker 패널에서 <b>Position, Rotation, Scale</b>을 모두 체크합니다. Layer 패널에 Track Point 1과 2가 생깁니다.',
    '두 점을 대상 위에서 <b>되도록 멀리 떨어진</b> 두 곳에 놓습니다(상자 왼쪽 위 모서리와 오른쪽 아래 모서리). 두 점이 가까우면 작은 오차에도 회전이 크게 흔들립니다.',
    'Analyze forward(▶). 두 점이 모두 끝까지 따라갔는지 확인합니다.',
    '널(%s)을 만들고 Edit Target에서 널을 고른 뒤 Apply → X and Y → OK. 널에 Position, Rotation, Scale 키프레임이 모두 들어갑니다.' % K('Ctrl+Alt+Shift+Y'),
    '붙일 이미지(로고·스티커)를 널에 부모로 겁니다. 이미지가 대상과 함께 돌고 커집니다.',
) + '''
<div class="tip"><b>점이 화면 밖으로 나갈 때</b>대상의 한쪽이 화면 밖으로 나가는 순간 분석이 무너집니다. 그 프레임에서 멈추고, 그 점을 아직 보이는 다른 무늬로 옮긴 뒤 이어서 분석합니다. Attach Point는 그대로 두고 Feature Region만 옮기려면 %s 키를 누른 채 상자를 드래그합니다.</div>
''' % K('Alt')

TRK_MOCHA = '''
<h2>9-6 Mocha AE — 점 대신 면으로 추적하기</h2>
<p>점 트래커는 작은 무늬 하나를 따라가므로, 그 무늬가 손가락에 가려지거나 흐려지면 무너집니다. 애펙에 함께 들어 있는 <b>Mocha AE</b>는 <b>평평한 면 전체</b>를 따라가므로 일부가 가려져도 버팁니다. 9-5의 화면 바꾸기가 자꾸 미끄러질 때 씁니다.</p>
''' + steps(
    '영상 레이어를 고르고 메뉴 <b>Animation → Track in Boris FX Mocha</b>를 누릅니다. 레이어에 <b>Mocha AE</b> 효과가 들어갑니다.',
    'Effect Controls 맨 위의 큰 <b>Mocha</b> 로고 버튼을 누르면 Mocha 창이 따로 열립니다.',
    '왼쪽 위 도구 중 <b>X-Spline</b> 펜 도구를 고르고, 따라갈 평평한 면(휴대폰 화면, 벽의 간판) 바로 안쪽을 클릭해 점을 찍어 둘러쌉니다. 마지막에 우클릭하면 모양이 닫힙니다.',
    '아래쪽 재생 버튼 줄의 <b>Track Forwards</b>(오른쪽 화살표에 T가 붙은 버튼)를 누릅니다. 면이 프레임마다 따라가며 파란 모양이 같이 움직입니다.',
    '위쪽 도구 막대의 <b>Show planar surface</b>(S 모양 버튼)를 켜면 파란 사각형이 나타납니다. 그 네 모서리를 화면의 네 귀퉁이에 정확히 끌어다 맞춥니다.',
    '<b>File → Save Project</b>(%s)로 저장하고 Mocha 창을 닫습니다.' % K('Ctrl+S'),
    '애펙으로 돌아와 Effect Controls의 <b>Tracking Data</b>를 펼치고 <b>Create Track Data</b>를 누른 뒤, 창에서 방금 만든 레이어 이름을 확인하고 <b>OK</b>.',
    '<b>Export Option</b>을 <b>Corner Pin (Supports Motion Blur)</b>로, <b>Layer Export To</b>를 바꿔 끼울 이미지 레이어로 고르고 <b>Apply Export</b>. 이미지 네 귀퉁이가 화면에 붙어 움직입니다.',
) + '''
<div class="note"><b>Mocha가 강한 곳</b>손가락이 화면을 지나가는 장면, 초점이 잠깐 나가는 장면, 화면에 반사가 비치는 장면. 모양을 그릴 때 손가락이 지나갈 부분은 빼고 그리면 더 안정적입니다.</div>
'''

TRK_MASK = '''
<h2><span class="tag t1">따라 하기</span> 9-7 마스크 트래킹 — 얼굴·번호판 가리기</h2>
<p>얼굴이나 자동차 번호판을 모자이크로 가리는 일은 마스크가 대상을 따라가게 하는 <b>마스크 트래커</b>로 합니다. 널이 필요 없고, 마스크 자체가 움직입니다.</p>
''' + steps(
    '영상 레이어를 %s로 복제합니다. 위쪽 레이어에 가림 효과를, 아래쪽은 원본으로 둡니다.' % K('Ctrl+D'),
    '위쪽 레이어를 고르고 도구 막대에서 <b>Ellipse Tool</b>(%s를 눌러 바꿈)로 얼굴을 둘러싸는 마스크를 그립니다. 번호판이면 Rectangle Tool을 씁니다.' % K('Q'),
    '타임라인에서 레이어를 펼쳐 <b>Masks → Mask 1</b>을 클릭해 고릅니다. 마스크 이름에서 우클릭 → <b>Track Mask</b>. Tracker 패널이 마스크용으로 바뀝니다.',
    'Tracker 패널의 <b>Method</b>를 고릅니다. 얼굴은 <b>Face Tracking (Outline Only)</b>, 번호판은 <b>Perspective</b>, 그 밖에는 <b>Position, Scale &amp; Rotation</b>.',
    '<b>Track selected masks forward</b>(▶)를 누릅니다. 마스크 모양에 프레임마다 키프레임이 생깁니다.',
    '위쪽 레이어에 <b>Effect → Stylize → Mosaic</b>를 넣고 Horizontal Blocks·Vertical Blocks를 40쯤으로. 흐림으로 가리려면 <b>Gaussian Blur</b>를 넣고 Blurriness 40, <b>Repeat Edge Pixels</b> 체크.',
    '%s를 두 번 눌러 Mask Feather를 15 정도로 올리면 가림 경계가 부드러워집니다. 대상이 마스크 밖으로 벗어나면 Mask Expansion을 10~20 늘립니다.' % K('F'),
)

TRK_STAB = '''
<h2>9-8 흔들림 잡기 — Warp Stabilizer와 Stabilize Motion</h2>
<p>트래킹은 무언가를 “붙이는” 데도 쓰지만 흔들린 영상을 “잡는” 데도 씁니다. 손으로 들고 찍은 영상은 Warp Stabilizer부터 써 보고, 결과가 출렁이면 Stabilize Motion으로 직접 잡습니다.</p>
<p><b>A. Warp Stabilizer — 자동</b></p>
''' + steps(
    '영상 레이어를 고르고 <b>Animation → Warp Stabilizer VFX</b>(또는 Tracker 패널의 Warp Stabilize).',
    '화면에 파란 띠로 “Analyzing in background”가 뜨고, 이어서 주황 띠로 “Stabilizing”이 뜹니다. 띠가 사라질 때까지 기다립니다. 그동안 다른 작업을 해도 됩니다.',
    'Effect Controls에서 <b>Result</b>를 고릅니다. <b>Smooth Motion</b>은 카메라 움직임은 살리고 떨림만, <b>No Motion</b>은 삼각대에 세운 것처럼 완전히 고정합니다.',
    '<b>Smoothness</b>(기본 50%)를 올릴수록 부드러워지지만 가장자리가 더 많이 잘립니다. <b>Framing</b>은 기본 Stabilize, Crop, Auto-scale(잘린 만큼 확대)을 그대로 둡니다.',
    '건물 같은 직선이 휘어 보이면 <b>Method</b>를 Subspace Warp에서 <b>Position, Scale, Rotation</b>으로 바꿉니다. 화면이 일그러지지 않고 통째로만 움직입니다.',
) + '''
<p><b>B. Stabilize Motion — 직접</b></p>
''' + steps(
    '영상 레이어를 고르고 Tracker 패널의 <b>Stabilize Motion</b>. Position과 Rotation을 체크합니다.',
    '두 점을 움직이지 않는 배경(건물 모서리, 표지판)에 놓고 Analyze forward.',
    '<b>Apply</b> → X and Y → OK. 영상이 흔들림의 반대로 움직여 배경이 고정됩니다.',
    '가장자리에 검은 빈 곳이 보이므로 영상을 프리컴포즈(%s)한 뒤 Scale을 110%% 정도로 키웁니다.' % K('Ctrl+Shift+C'),
) + '''
<div class="stuck"><b>“다른 효과와 함께 쓰려면 프리컴포즈하라”는 경고</b>Warp Stabilizer는 레이어에 다른 효과가 먼저 있거나 레이어 크기가 컴포지션과 다르면 동작하지 않습니다. 영상을 프리컴포즈(Move all attributes)하고 프리컴포즈 레이어에 다시 넣습니다.</div>
'''

# ---------------------------------------------------------------- 3D camera tracker ch.10
CAM_MORE = '''
<h2>10-2 3D Camera Tracker 효과 컨트롤 읽기</h2>
<p>분석이 끝나면 영상 레이어의 Effect Controls에 <b>3D Camera Tracker</b>가 남습니다. 결과가 나쁠 때 고칠 곳이 여기 모여 있습니다.</p>
<table>
<tr><th style="width:30%">항목</th><th>하는 일과 고르는 법</th></tr>
<tr><td>Analyze / Cancel</td><td>다시 분석 · 분석 중단</td></tr>
<tr><td>Shot Type</td><td><b>Fixed Angle of View</b>(줌 없음, 기본) · <b>Variable Zoom</b>(촬영 중 줌을 당긴 영상) · <b>Specify Angle of View</b>(렌즈 화각을 알 때 직접 입력)</td></tr>
<tr><td>Show Track Points</td><td>3D Solved(계산된 공간의 점) · 2D Source(원본 영상에서 찾은 점)</td></tr>
<tr><td>Render Track Points</td><td>점을 렌더에도 그립니다. 확인용이며 보통 끕니다</td></tr>
<tr><td>Track Point Size</td><td>화면의 점 크기. 점이 너무 작아 고르기 힘들 때 키웁니다</td></tr>
<tr><td>Target Size</td><td>빨간 과녁의 크기. 만들 글자·솔리드의 처음 크기도 이 값을 따릅니다</td></tr>
<tr><td>Create Camera</td><td>점을 고르지 않고 카메라만 만듭니다</td></tr>
<tr><td>Advanced → Solve Method</td><td>Auto Detect · Typical · <b>Mostly Flat Scene</b>(바닥·벽 하나만 보이는 영상) · <b>Tripod Pan</b>(삼각대에서 돌리기만 한 영상)</td></tr>
<tr><td>Advanced → Average Error</td><td>계산의 평균 오차(픽셀). 작을수록 좋고, 1을 넘으면 결과가 미끄러질 수 있습니다</td></tr>
<tr><td>Advanced → Detailed Analysis</td><td>체크하면 더 오래 걸리지만 질감이 적은 영상에서 점을 더 찾습니다</td></tr>
<tr><td>Advanced → Auto-delete Points Across Time</td><td>지운 점과 같은 점을 다른 프레임에서도 자동으로 지웁니다. 움직이는 사람·차 위의 점을 지울 때 켭니다</td></tr>
</table>

<h2>10-3 과녁 메뉴 — 무엇을 만들 수 있나</h2>
<p>점들을 고르고 과녁 위에서 우클릭하면 아래 메뉴가 나옵니다. 어떤 것을 고르든 <b>3D 카메라 + 그 자리에 놓인 레이어</b>가 함께 만들어지고, 카메라는 한 번만 만들어집니다.</p>
<table>
<tr><th style="width:36%">메뉴</th><th>만들어지는 것과 쓰임</th></tr>
<tr><td>Create Text and Camera</td><td>과녁 면에 누운 3D 텍스트. 바닥 글자, 벽 글자</td></tr>
<tr><td>Create Solid and Camera</td><td>과녁 면에 붙은 3D 솔리드. 이미지로 바꿔 끼워 간판·포스터·화면 교체(10-5)</td></tr>
<tr><td>Create Null and Camera</td><td>그 자리의 3D 널. 로고·프리컴포즈·3D 모델을 걸어 놓는 손잡이(10-4)</td></tr>
<tr><td>Create Shadow Catcher, Camera and Light</td><td>그림자만 받는 바닥, 라이트. 세운 글자의 그림자가 실제 바닥에 떨어지게(10-6)</td></tr>
<tr><td>Create Multiple Text / Solid / Null Layers</td><td>여러 점을 골랐을 때 점마다 하나씩 만듭니다. 바닥 위 여러 자리에 표시를 세울 때</td></tr>
<tr><td>Set Ground Plane and Origin</td><td>그 면을 “바닥”과 원점으로 정합니다. 이후 만드는 레이어가 이 면 기준으로 놓입니다</td></tr>
<tr><td>Delete Selected Points</td><td>고른 점을 지웁니다. 움직이는 사람·차·물결 위의 점은 지우는 것이 좋습니다</td></tr>
</table>
<div class="tip"><b>과녁 다루기</b>점 하나 위에 마우스를 올리면 근처 세 점으로 과녁이 그려집니다. 원하는 면이 아니면 빈 곳을 드래그해 점 여러 개를 둘러싸 고르거나, %s를 누른 채 점을 하나씩 클릭해 고릅니다. 과녁 가운데를 드래그하면 과녁만 면 위에서 옮길 수 있습니다.</div>
'''.replace('%s', K('Shift')) + '''
<h2><span class="tag t1">따라 하기</span> 10-4 널에 로고·이미지 세우기</h2>
<p>글자 말고 로고나 프리컴포즈를 공간에 세우려면 널을 만들고 거기에 거는 것이 가장 깔끔합니다.</p>
''' + steps(
    '10-1의 1단계처럼 분석을 마칩니다. 3D Camera Tracker 효과 이름을 클릭해 고른 상태로, 로고를 세울 바닥 위 점들을 드래그로 고릅니다.',
    '과녁에서 우클릭 → <b>Create Null and Camera</b>. 타임라인에 %s과 %s가 생깁니다.' % (M('Track Null 1'), M('3D Tracker Camera')),
    '프로젝트 패널에서 로고 이미지(또는 프리컴포즈)를 타임라인에 끌어다 놓고, 레이어의 <b>3D Layer</b> 스위치(정육면체 아이콘)를 켭니다.',
    '로고 레이어의 Parent &amp; Link 픽윕을 <b>Track Null 1</b>에 끌어 놓습니다.',
    '로고 레이어를 고르고 %s로 Position을 열어 <b>0, 0, 0</b>을 입력합니다. 부모에 건 뒤의 0은 “부모와 같은 자리”라는 뜻이라, 로고가 널 위치로 정확히 옮겨집니다.' % K('P'),
    '크기가 맞지 않으면 %s로 Scale을 열어 줄입니다(트래커가 만드는 공간은 단위가 커서 10~30%%로 시작합니다). 로고가 누워 있으면 %s로 Rotation을 열어 X Rotation −90°로 세웁니다.' % (K('S'), K('R')),
    '%s로 재생해 로고가 바닥에 붙어 있는지 봅니다. 떠 보이면 Position의 Z나 Y를 조금씩 바꿔 바닥에 닿게 합니다.' % K('Space'),
)
CAM_MORE += '''
<h2><span class="tag t1">따라 하기</span> 10-5 벽의 간판을 다른 그림으로 바꾸기</h2>
''' + steps(
    '분석을 마친 뒤 간판이 붙은 <b>벽 면</b> 위의 점들만 골라, 과녁이 벽과 나란히 서도록 맞춥니다.',
    '과녁 우클릭 → <b>Create Solid and Camera</b>. 벽에 붙은 %s가 생깁니다.' % M('Track Solid 1'),
    '솔리드를 고르고 %s(Position·Scale)와 %s(Rotation)로 간판 크기와 자리에 맞춥니다. 레이어 Opacity를 50%%로 내리면 뒤 간판을 보며 맞추기 쉽습니다.' % (K('P'), K('R')),
    '프로젝트 패널의 새 간판 이미지를 %s를 누른 채 타임라인의 솔리드 위로 끌어다 놓습니다. 위치·회전·크기는 그대로 두고 내용만 바뀝니다. Opacity를 100%%로 돌립니다.' % K('Alt'),
    '새 간판이 너무 깨끗해 떠 보이면 Lumetri로 밝기와 색을 벽에 맞추고, <b>Effect → Noise &amp; Grain → Add Grain</b>으로 영상의 입자를 더합니다.',
) + '''
<h2>10-6 그림자까지 — Shadow Catcher</h2>
''' + steps(
    '세운 글자 아래 바닥의 점들을 고르고, 과녁 우클릭 → <b>Create Shadow Catcher, Camera and Light</b>. %s 솔리드와 %s가 생깁니다.' % (M('Shadow Catcher 1'), M('Light 1')),
    '글자 레이어를 펼쳐 <b>Material Options → Casts Shadows</b>를 <b>On</b>으로 바꿉니다(%s 두 번으로 빠르게 열 수 있습니다).' % K('A'),
    '<b>Light 1</b>을 고르고 Position을 옮겨 실제 영상의 해·조명 방향과 맞춥니다. 그림자가 원본 그림자들과 같은 쪽으로 떨어져야 합니다.',
    'Light Options의 <b>Shadow Darkness</b>(어둡기)와 <b>Shadow Diffusion</b>(번짐)을 영상 속 그림자와 비교해 맞춥니다. 흐린 날은 Diffusion을 크게 합니다.',
) + '''
<h2>10-7 잘 풀리지 않을 때</h2>
<table>
<tr><th style="width:32%">증상</th><th>원인과 손볼 곳</th></tr>
<tr><td>“Analysis failed” 또는 점이 거의 없음</td><td>질감이 부족하거나 흔들림·흐림이 큼. Detailed Analysis를 켜고 다시 Analyze. 그래도 안 되면 Warp Stabilizer로 흔들림을 줄인 영상을 프리컴포즈해 분석합니다</td></tr>
<tr><td>글자가 바닥에서 미끄러짐</td><td>Average Error 확인. 사람·차·물결 위 점을 골라 Delete Selected Points(Auto-delete Points Across Time 켜기) 후 다시 분석</td></tr>
<tr><td>카메라가 제자리에서 돌기만 한 영상</td><td>Advanced → Solve Method를 <b>Tripod Pan</b>으로. 깊이는 없지만 방향은 맞습니다</td></tr>
<tr><td>바닥 하나만 보이는 영상</td><td>Solve Method를 <b>Mostly Flat Scene</b>으로</td></tr>
<tr><td>촬영 중 줌을 당긴 영상</td><td>Shot Type을 <b>Variable Zoom</b>으로</td></tr>
<tr><td>레이어 크기 경고</td><td>프리컴포즈(Move all attributes) 후 다시 분석(그림 10-1)</td></tr>
</table>
'''

# ---------------------------------------------------------------- AE 27 AI (ch.23)
P = lambda lbl, t: '<div class="prompt"><span class="lbl">%s</span>%s</div>\n' % (lbl, t)

AI_OPEN = '''
<h2>23-1 AI Assistant 열기와 화면 읽기</h2>
''' + steps(
    '애펙 27.0을 엽니다. 화면 맨 위 헤더 막대의 <b>AI Assistant</b> 아이콘을 누르거나, 메뉴 <b>Window → AI Assistant</b>를 누릅니다. Quick Apply 검색(타임라인에서 %s)에 “Assistant”를 쳐서 열 수도 있습니다.' % K('Ctrl+Space'),
    '패널은 다른 패널처럼 끌어서 붙일 수 있습니다. 오른쪽 Effects &amp; Presets 옆에 탭으로 붙여 두면 화면을 가리지 않습니다.',
    '아래쪽 <b>입력칸(prompt bar)</b>에 할 일을 문장으로 쓰고 %s. 무엇을 쓸지 모르겠으면 <b>Start with a sample prompt</b> 옆 아이콘을 눌러 예시를 고릅니다.' % K('Enter'),
    'Assistant가 프로젝트를 바꾸려 하면 <b>Deny / Always proceed / Proceed</b>를 묻습니다. 처음에는 매번 내용을 읽고 Proceed를 누르세요. Always proceed는 같은 종류의 동작을 다음부터 묻지 않습니다.',
    '대화가 길어져 엉키면 패널 왼쪽 위 <b>Add a new chat</b> 아이콘으로 새 대화를 엽니다. 이전 대화의 맥락은 넘어가지 않습니다.',
    '동작이 끝나면 크레딧 아이콘에 마우스를 올려 실제로 쓴 크레딧을 확인합니다(23-8).',
) + '''
<div class="warn"><b>되돌리기는 한 동작씩</b><span class="k">Ctrl+Z</span>는 Assistant가 한 동작을 하나씩 되돌립니다. 한 번의 요청이 열 가지를 바꿨다면 열 번 눌러야 합니다. 큰 정리를 시키기 전에는 <b>File → Save As</b>로 사본을 먼저 저장합니다.</div>
<p>Assistant는 프로젝트를 <b>읽고 고칠 수 있는</b> 도구라서, 어떤 일에 강하고 어떤 일에 약한지 알고 맡기는 것이 중요합니다. 어도비는 베타에서 <b>프로젝트 정리</b>와 <b>익스프레션</b>을 가장 다듬었다고 밝혔습니다.</p>
<table>
<tr><th style="width:24%">분야</th><th>시킬 수 있는 일</th></tr>
<tr><td>프로젝트 정리</td><td>항목 설명, 폴더로 나누기, 이름 바꾸기, 색 라벨 붙이기, 레이어·컴포지션 정리 제안</td></tr>
<tr><td>익스프레션</td><td>식을 쉬운 말로 풀어 주기, 말로 설명한 움직임을 식으로 쓰기, 오류 원인 찾아 고치기, 이름을 바꿀 때 그 이름을 참조하는 식까지 함께 고치기</td></tr>
<tr><td>텍스트·셰이프</td><td>글자 일부만 바꾸기, 특정 글자 범위 고치기, 셰이프의 Path Operations 더하기·빼기·순서 바꾸기, 점선(Dashes)</td></tr>
<tr><td>템플릿</td><td>Essential Graphics에 속성·미디어 내보내기, 컨트롤 이름 정리, MOGRT로 내보내기</td></tr>
<tr><td>키프레임</td><td>키프레임 보간(Linear, Ease, Hold 등) 바꾸기</td></tr>
<tr><td>생성</td><td>Firefly와 파트너 모델로 이미지·영상 만들기, 프로젝트로 불러오기, 컴포지션 렌더</td></tr>
<tr><td>스킬</td><td>자주 하는 일련의 작업을 <b>스킬</b>로 저장해 다음에 다시 쓰기</td></tr>
</table>
<p>할 수 없는 일을 시키면 Assistant는 손으로 하는 방법을 알려 줍니다. 그 안내도 메뉴 이름을 찾는 데 쓸모가 있습니다.</p>
'''

AI_EXPR = '''
<h2>23-3 사례 ② 익스프레션 — 풀어 주기, 써 주기, 고쳐 주기</h2>
<p>7장에서 익힌 익스프레션을 Assistant와 함께 다뤄 봅니다. 실습은 21장에서 만든 타이틀 컴포지션처럼 익스프레션이 들어 있는 프로젝트로 합니다. Assistant가 쓰는 식은 매번 조금씩 다를 수 있으므로, 결과 식을 7장의 어휘로 읽어 보고 확인하는 습관을 들이세요.</p>
<p><b>A. 남이 쓴 식 읽기</b></p>
''' + steps(
    '식이 들어 있는 속성(빨간 = 표시가 붙은 속성)을 타임라인에서 클릭해 고릅니다.',
    '입력칸에 아래처럼 씁니다. 레이어와 속성 이름을 정확히 적을수록 엉뚱한 곳을 읽지 않습니다.',
) + P('PROMPT · AI Assistant', 'Explain in plain language what the expression on the Position property of the layer "Caption" does. Do not change anything.') + '''
<p>Assistant는 식을 한 줄씩 풀어 줍니다. 예를 들어 <span class="mono">wiggle(2,30)</span>이면 “1초에 두 번, 최대 30픽셀만큼 무작위로 흔들린다”고 설명합니다.</p>
<p><b>B. 말로 설명해 식 만들기</b></p>
''' + P('PROMPT · AI Assistant', 'Add an expression to the layer "Logo" so it gently floats up and down by 20 pixels, one full cycle every 2 seconds, starting from its current position.') + '''
''' + steps(
    '보내면 승인 창이 뜹니다. Proceed를 누르면 Logo 레이어의 Position에 식이 들어갑니다.',
    '%s를 두 번 눌러 식이 들어간 속성만 펼쳐 봅니다. %s처럼 지금 값에 사인 곡선을 더하는 식이 들어 있으면 맞습니다.' % (K('E'), M('value + [0, Math.sin(time*Math.PI)*20]')),
    '재생해 보고 바꾸고 싶은 점을 이어서 말합니다. “Make it 10 pixels and a bit faster”처럼 앞의 요청을 고치는 말이면 처음부터 다시 쓸 필요가 없습니다.',
) + '''
<p><b>C. 오류 고치기</b></p>
<p>레이어 이름을 바꾸면 그 이름을 부르던 식이 깨져 주황 오류 띠가 뜹니다(7-17). 이때 이렇게 맡깁니다.</p>
''' + P('PROMPT · AI Assistant', 'There is an expression error in this comp. Find the cause, explain it, and fix it.') + '''
<p>Assistant는 “없는 레이어를 참조함”, “속성 이름 철자가 틀림”처럼 원인을 말해 주고 고칩니다. 처음부터 이런 일을 막으려면 이름을 바꿀 때 Assistant에게 맡깁니다.</p>
''' + P('PROMPT · AI Assistant', 'Rename the layer "Control" to "Rig_Control" and update every expression that references it.') + '''
<div class="tip"><b>체크박스로 켜고 끄기</b>“Add a Checkbox Control named Show to the layer Control, and make the layer Caption visible only when Show is checked”처럼 시키면 Opacity에 <span class="mono">…("Show")("Checkbox").value ? 100 : 0</span> 같은 식을 넣어 줍니다. 7-16의 리그 만들기를 말로 할 수 있습니다.</div>
'''

AI_TEXT = '''
<h2>23-4 사례 ③ 글자·셰이프·템플릿 손보기</h2>
<p>납품 직전 자잘한 수정이 여러 컴포지션에 흩어져 있을 때 특히 편합니다.</p>
<table>
<tr><th style="width:44%">이렇게 시키면 (예)</th><th>Assistant가 하는 일</th></tr>
<tr><td><span class="mono">In every comp, change “2026” to “2027” in the text layers, keep the styling.</span></td><td>글자 전체를 갈아 끼우지 않고 해당 부분만 바꿔, 글꼴·색·애니메이터가 그대로 남습니다</td></tr>
<tr><td><span class="mono">Make the second line of the title text bold and orange.</span></td><td>특정 글자 범위만 스타일을 바꿉니다</td></tr>
<tr><td><span class="mono">Add Trim Paths to the shape “Check” and reorder it above Stroke.</span></td><td>셰이프의 Path Operations를 더하고 순서를 바꿉니다(5-2)</td></tr>
<tr><td><span class="mono">Make the stroke of “Frame” a dashed line, 12 px dash, 8 px gap.</span></td><td>Stroke의 Dashes를 만들고 값을 넣습니다</td></tr>
<tr><td><span class="mono">Expose the title text, the color, and the logo image in Essential Graphics, name the controls clearly, and export a MOGRT.</span></td><td>Essential Graphics 패널에 속성·미디어를 올리고 이름을 정리한 뒤 MOGRT로 내보냅니다(14-4)</td></tr>
<tr><td><span class="mono">Set all keyframes on the layer “Ball” to Easy Ease.</span></td><td>키프레임 보간을 한꺼번에 바꿉니다(3-2)</td></tr>
</table>
<div class="why"><b>좋은 요청의 세 가지</b>① <b>어디</b>(컴포지션·레이어·속성 이름) ② <b>무엇을</b>(바꿀 값, 숫자) ③ <b>남길 것</b>(“keep the styling”, “do not change anything else”). 셋이 다 들어가면 승인 창의 내용도 짧고 분명해집니다.</div>
'''

AI_GEN = '''
<h2>23-5 사례 ④ 이미지·영상 생성</h2>
<p>Assistant 안에서 Firefly와 파트너 모델로 배경·참고 이미지·짧은 영상을 만들어 바로 프로젝트에 넣을 수 있습니다. 생성은 크레딧이 많이 드는 동작이므로 23-8의 요율을 먼저 확인합니다.</p>
''' + steps(
    '입력칸에 만들 것을 구체적으로 씁니다. 크기와 길이, 쓸 곳을 함께 적으면 다시 만드는 일이 줄어듭니다.',
) + P('PROMPT · AI Assistant', 'Generate a 1920×1080 background plate of a city skyline at night, soft bokeh lights, no people, no logos. Import it into a folder named "Generated".') + steps(
    '승인 창에서 쓸 모델과 예상 크레딧을 확인하고 Proceed. 모델을 말하지 않으면 Assistant가 고릅니다.',
    '결과는 프로젝트 패널에 <b>파일(푸티지)</b>로 들어옵니다. 레이어로 바로 쌓이지 않으니 타임라인에 끌어다 놓습니다.',
    '이미지를 움직이게 하려면 이어서 씁니다: “Use this image as a reference and generate a 5-second video with a slow camera push-in.” 영상은 초당 크레딧이 들기 때문에 처음에는 짧게, 낮은 해상도로 시험합니다.',
) + '''
<div class="note"><b>어떤 생성을 어디서 할까</b>배경 한 장, 질감 하나처럼 애펙 안에서 바로 쓸 소스는 Assistant가 편합니다. 여러 모델을 비교하거나 같은 인물을 여러 컷에 이어야 하는 일은 힉스필드(18~20장)가 낫습니다. 어느 쪽이든 결과물의 상업적 사용 조건(23-8)과 사람·상표가 나오지 않는지 확인합니다.</div>
'''

AE27_OTHERS = '''
<h2>23-7 27.0의 다른 새 기능 — 직접 해 보기</h2>
<p>AI Assistant 말고도 27.0에는 손으로 쓰는 새 기능이 여럿 들어왔습니다. 짧게 하나씩 해 봅니다.</p>
<h3>레이어를 3D 재질로 — 움직이는 화면을 3D 물체에</h3>
''' + steps(
    'Composition 패널 위쪽의 <b>3D Renderer</b> 메뉴에서 <b>Advanced 3D</b>를 고릅니다.',
    '3D 물체를 만듭니다. 글자를 쓰고 <b>3D Layer</b> 스위치를 켠 뒤 Geometry Options에서 Extrusion Depth 40을 주거나, 3D 모델(13-4)을 불러옵니다.',
    '재질로 쓸 프리컴포즈·솔리드·이미지·영상을 <b>같은 컴포지션 안</b>에 끌어다 놓습니다. 다른 컴포지션에 있으면 목록에 나오지 않습니다.',
    '3D 레이어를 고르고 타임라인에서 <b>Material Assignment</b>를 펼칩니다. <b>Material</b> 드롭다운에서 방금 넣은 레이어를 고릅니다. Properties 패널의 검색칸에서 Compositions·Footage·Substance 3D Materials(.sbsar)로 걸러 볼 수 있습니다.',
    '<b>Offset, Rotation, Scale</b>로 재질이 면에 놓이는 자리를 맞추고, <b>Roughness, Metallic, Opacity, Emission Color, Emission Intensity, Ambient Response</b>로 질감을 다듬습니다. 화면처럼 빛나게 하려면 Emission Intensity를 올립니다.',
    '재질로 쓴 프리컴포즈 안의 애니메이션은 3D 물체 표면에서 그대로 움직입니다. 다시 내보내거나 불러올 필요가 없습니다.',
) + '''
<p>같은 방법으로 <b>Substance 3D 재질(.sbsar)</b>을 프로젝트에 불러와 3D 텍스트·셰이프의 앞면·옆면·뒷면·베벨에 따로 입힐 수 있습니다. 앞면은 금속, 옆면은 나무처럼 면마다 다르게 줍니다. 렌더러를 Classic 3D나 Cinema 4D로 바꾸면 기본 재질로 돌아가고, Advanced 3D로 돌아오면 다시 살아납니다.</p>
<h3>Contour Paint — 영상을 그림처럼</h3>
''' + steps(
    '영상 레이어를 고르고 <b>Effect → Stylize → Contour Paint</b>.',
    'Effect Controls 맨 위 <b>View</b>를 <b>Edge Map</b>으로 바꿉니다. 애펙이 찾은 경계와 그 방향(하늘색 화살표)이 보입니다.',
    'Edge Map을 보면서 <b>Contour Smearing → Stylization</b>을 올립니다. 클수록 작은 부분은 사라지고 큰 윤곽을 따라 물감이 번집니다. <b>Cleanliness</b>로 잔무늬를 얼마나 지울지 정합니다.',
    'View를 <b>Final Result</b>로 돌립니다. 더 추상적으로 하려면 <b>Smear Iterations</b>를 올립니다(최대 100, 렌더가 느려집니다).',
    '<b>Color Reduction → Draw Color Fills</b>를 <b>Over Smeared Image</b>나 <b>Only</b>로 바꾸면 색이 몇 가지로 줄어 판화·포스터 같은 느낌이 됩니다. <b>Posterization Level</b>로 색 수를 정하거나, <b>Match to Nearest Custom Color</b>로 직접 고른 팔레트만 쓰게 합니다.',
) + '''
<div class="tip"><b>Contour Paint를 더 잘 먹이려면</b>앞에 <b>Unsharp Mask</b>를 넣으면 윤곽이 강해져 모양이 또렷해지고, <b>Shadow/Highlight</b>를 넣으면 어두운 곳의 디테일이 살아납니다. 색이 프레임마다 바뀌어 깜빡이면 Custom Color 방식으로 바꿉니다.</div>
<h3>그 밖에 알아 둘 것</h3>
<table>
<tr><th style="width:28%">기능</th><th>쓰는 법</th></tr>
<tr><td>Adobe Stock 패널</td><td><b>Window → Adobe Stock</b>에서 검색하고 내려받으면 프로젝트 패널로 바로 들어옵니다. 라이선스 조건은 스톡 쪽을 따릅니다</td></tr>
<tr><td>일러스트레이터 글자를 편집 가능하게</td><td>일러스트레이터에서 SVG로 저장해 불러오면 글자가 애펙 텍스트 레이어로 바뀌고 글꼴·크기·색·위치·가변 글꼴 설정이 유지됩니다(14-5)</td></tr>
<tr><td>Auto-Save와 복구</td><td>애펙이 갑자기 꺼진 뒤 다시 열면 복구할 프로젝트를 고르게 합니다. 그래도 <span class="k">Ctrl+S</span>를 습관으로</td></tr>
<tr><td>Quick Apply 기록</td><td>Quick Apply가 최근에 쓴 효과·프리셋·메뉴 명령을 기억해 다시 검색하지 않아도 됩니다</td></tr>
<tr><td>Object Matte 디스크 캐시</td><td>Object Matte로 번진 결과를 디스크에 저장해, 프로젝트를 다시 열어도 다시 계산하지 않습니다. 긴 클립에서 메모리를 아낍니다</td></tr>
<tr><td>안내선(Guides)</td><td>퍼센트 위치, 가장자리 고정, 안내선 색을 정할 수 있습니다. 세로·가로 버전 레이아웃을 같이 만들 때 편합니다</td></tr>
<tr><td>PNG 시퀀스 압축</td><td>렌더 설정의 Compression 슬라이더로 렌더 시간과 파일 크기를 맞바꿉니다. 화질은 그대로(무손실)입니다</td></tr>
<tr><td>De-esser</td><td>목소리의 날카로운 ㅅ·ㅆ 소리를 줄이는 오디오 효과</td></tr>
</table>
'''

OM_MORE = '''
''' + steps(
    '걷는 사람 영상 레이어를 더블클릭해 <b>Layer 패널</b>로 엽니다.',
    '도구 막대에서 <b>Object Matte Tool</b>(%s)을 고르고, 인물 위를 한 번 클릭합니다. 보라색 테두리로 인물이 잡힙니다.' % K('Alt+W'),
    '빠진 부분은 <b>Quick Selection</b>이나 <b>Selection Brush</b>로 칠해 더하고, %s를 누른 채 칠하면 뺍니다.' % K('Alt'),
    '머리카락처럼 가는 경계는 <b>Refine Edge</b>로 칠해 다듬습니다.',
    'Layer 패널 아래쪽의 재생 버튼으로 앞뒤 프레임까지 번지게(propagate) 한 뒤, Composition 패널로 돌아가 배경이 빠졌는지 확인합니다. 27.0부터는 이 결과가 디스크에 저장되어 프로젝트를 다시 열어도 남습니다.',
)


def apply3(S):
    def rep(old, new, count=1):
        nonlocal S
        assert old in S, old[:80]
        S = S.replace(old, new, count)

    # --- particles: insert before the "더 필요해지면" note in 5-7
    anchor = '<div class="note"><b>더 필요해지면</b>CC Particle World는'
    rep(anchor, PART_SNOW + PART_RAIN + PART_SMOKE + anchor)

    # --- ch.9
    rep('<h2>9-2 실습 — 손에 든 화면 바꾸기</h2>', TRK_PANEL + TRK_ONE + TRK_ONE_TAIL + TRK_TWO + '<h2><span class="tag t1">따라 하기</span> 9-5 4점 트래킹 — 손에 든 화면 바꾸기</h2>')
    i = S.find('9-5 4점 트래킹'); j = S.find('<h2>이 장 점검</h2>', i)
    S = S[:j] + TRK_MOCHA + TRK_MASK + TRK_STAB + S[j:]

    # --- ch.10
    rep('<h2>10-2 하늘 바꾸기</h2>', CAM_MORE + '<h2>10-8 하늘 바꾸기</h2>')

    # --- ch.23
    rep('<h2>23-1 AI Assistant로 프로젝트 점검</h2>', AI_OPEN + '<h2>23-2 사례 ① 넘겨받은 프로젝트 점검과 정리</h2>')
    rep('<div class="tip"><b>Claude와 나눠 쓰기</b>', steps(
        '점검 보고서를 읽고 정리를 맡깁니다. 이번에는 바꾸는 요청이므로 승인 창마다 내용을 확인합니다.',
    ).replace('<div class="n">1</div>', '<div class="n">4</div>') + P('PROMPT · AI Assistant', 'Organize the project panel: put footage, images, precomps and final comps into clearly named folders, color-label the final comps green, and move unused items into an "_Archive" folder. Do not delete anything.') + st(5, '프로젝트 패널을 확인합니다. 폴더 이름이나 색이 마음에 들지 않으면 “Rename the folder Footage to 01_Footage”처럼 이어서 고칩니다. 정리 전·후를 캡처해 두면 팀원에게 무엇이 바뀌었는지 보여 주기 좋습니다.') + '<div class="tip"><b>Claude와 나눠 쓰기</b>')
    rep('<h2>23-2 Object Matte — 직접 해 보기</h2>', AI_EXPR + AI_TEXT + AI_GEN + '<h2>23-6 Object Matte — 직접 해 보기</h2>')
    rep('기기 안에서 처리되어 크레딧이 들지 않습니다.</p>', '기기 안에서 처리되어 크레딧이 들지 않습니다.</p>' + OM_MORE)
    i = S.find('23-6 Object Matte'); j = S.find('<h2><span class="tag t2">왜 그럴까</span> 23-3 어도비', i)
    S = S[:j] + AE27_OTHERS + S[j:]
    rep('<span class="tag t2">왜 그럴까</span> 23-3 어도비', '<span class="tag t2">왜 그럴까</span> 23-8 어도비')
    rep('자세한 정책은 23-3에 정리했습니다.', '자세한 정책은 23-8에 정리했습니다.')
    rep('AI Assistant로 빈 구간·꺼진 레이어 점검 (23-1)', 'AI Assistant로 빈 구간·꺼진 레이어 점검 (23-2)')
    return S
