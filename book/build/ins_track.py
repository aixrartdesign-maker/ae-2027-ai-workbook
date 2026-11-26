# -*- coding: utf-8 -*-
# 2026-11-26 (5): tracking practice cases with real AE captures (ch20, ch21)

ROLE = '''<h2>20-9 같은 기능, 다른 역할 — 한 표로 보기</h2>
<p>트래킹 실습을 하다 보면 같은 기능이 사례마다 전혀 다른 일을 합니다. 기능 이름보다 <b>“이 장면에서 이 기능이 맡은 역할”</b>을 먼저 말할 수 있으면, 처음 보는 장면에서도 무엇을 꺼낼지 바로 정할 수 있습니다. 아래 사례 T1~T4는 이 장에서, T5~T8은 21장에서 직접 따라 합니다.</p>
<table>
<tr><th style="width:22%">기능</th><th style="width:26%">역할 ①</th><th style="width:26%">역할 ②</th><th>역할 ③</th></tr>
<tr><td>Perspective corner pin (4점)</td><td>T1 손에 든 폰 화면 교체</td><td>T2 벽걸이 TV 화면 교체</td><td>T3 거리 전광판 화면 교체</td></tr>
<tr><td>Keylight</td><td>T1 폰 화면의 초록을 지워 손가락을 앞에 남기기</td><td>19장 인물 뒤 그린스크린 지우기</td><td>T2 TV 화면에 초록 판을 띄워 찍었을 때 판만 지우기</td></tr>
<tr><td>Bezier Warp</td><td>T4 평면 그래프를 곡면 벽에 휘기</td><td>T3 전광판 화면을 물결처럼 휘는 연출</td><td>로고를 깃발처럼 살짝 휘기</td></tr>
<tr><td>3D Camera Tracker</td><td>T5 옥상 바닥에 글자 눕히기(Text)</td><td>T6 횡단보도에 영상 깔기(Solid)</td><td>T7·T8 벽·건물에 걸 손잡이(Null)</td></tr>
<tr><td>Blending Mode</td><td>T6 Overlay: 흰 줄무늬를 살린 채 색만 입히기</td><td>T2 Screen: 원본 반사를 화면 위에 다시 얹기</td><td>T7 Multiply: 벽 질감이 비치는 그래피티</td></tr>
<tr><td>Null</td><td>20-3 1점 트래킹 결과를 받아 글자를 따라가게</td><td>21-4 3D 공간의 고정점</td><td>T7 따라다니는 글자의 부모</td></tr>
<tr><td>Anchor Point</td><td>10장 막대가 아래에서 자라는 기준</td><td>T5 글자를 지붕 면 위에서 밀어 옮기기</td><td>T8 3D 글자가 도는 중심</td></tr>
<tr><td>Glow</td><td>T3 전광판이 빛나 보이게</td><td>16장 네온 글자</td><td>T6 바닥 영상의 번짐</td></tr>
</table>

<h2>20-10 기능별 사용 체크리스트</h2>
<p>실습 전에 한 번, 결과가 이상할 때 한 번 더 확인합니다. 칸을 채우듯 위에서 아래로 짚어 가면 대부분의 실수가 여기서 걸립니다.</p>
<p><b>A. Perspective corner pin (4점 트래킹)</b></p>
<ul class="check">
<li>영상 레이어를 먼저 고른 뒤 Tracker 패널의 <b>Track Motion</b>을 눌렀다(Current Track에 Tracker 이름이 보인다)</li>
<li>Track Type이 <b>Perspective corner pin</b>이다</li>
<li>Track Point 1~4를 <b>왼쪽 위 → 오른쪽 위 → 왼쪽 아래 → 오른쪽 아래</b> 순서로 놓았다</li>
<li>점이 대비가 강한 모서리(베젤 끝, 흰 점) 위에 있고, 끝까지 화면 안에 남는다</li>
<li>분석 후 경로가 매끄럽다. 튀는 프레임이 있으면 그 프레임부터 다시 분석했다</li>
<li>Edit Target에서 바꿔 끼울 레이어를 골랐고, Apply 후 그 레이어에 Corner Pin 효과와 Position 키가 생겼다</li>
<li>새 화면이 원래 화면보다 작으면 레이어 Scale을 키워 가장자리를 덮었다</li>
</ul>
<p><b>B. Keylight</b></p>
<ul class="check">
<li>키를 거는 레이어(원본)가 바꿔 끼운 화면 <b>위</b>에 있다</li>
<li>Screen Colour를 가장 넓고 고른 초록에서 찍었다</li>
<li>View를 Screen Matte로 바꿔 흰색(남길 곳)·검정(지울 곳)이 깨끗한지 봤다</li>
<li>가장자리에 초록이 남으면 Despill Bias, 구멍이 나면 Clip White를 조절했다</li>
</ul>
<p><b>C. Bezier Warp</b></p>
<ul class="check">
<li>휘기 전에 레이어 크기와 위치를 먼저 정했다(Vertex 값은 레이어 안 좌표)</li>
<li>꼭짓점 4개를 벽 모서리에, 접선 8개를 곡선 위 1/3·2/3 지점에 놓았다</li>
<li>Quality를 8 이상으로 두어 휜 글자가 계단처럼 보이지 않는다</li>
<li>카메라가 움직이는 장면이면 한 프레임만 맞는다는 것을 알고, 고정 장면에 쓰거나 띠로 나눴다</li>
</ul>
<p><b>D. 3D Camera Tracker</b></p>
<ul class="check">
<li>영상 레이어가 컴포지션 크기와 같고 Transform이 기본값이다(아니면 프리컴포즈)</li>
<li>분석이 끝나 Effect Controls에 프레임 수가 보이고 <b>Create Camera</b>가 활성화됐다</li>
<li>효과 이름을 클릭해 고른 상태에서 점이 보인다</li>
<li>과녁이 원하는 면(바닥·지붕·벽)에 <b>누워</b> 있다. 기울면 다른 점 3개를 골랐다</li>
<li>만들 것을 역할로 골랐다: 글자 = Text, 영상·그림 = Solid, 다른 레이어를 걸 손잡이 = Null</li>
<li>재생해서 처음·중간·끝 세 시점 모두 면에 붙어 있다</li>
</ul>
<p><b>E. 블렌딩과 마무리</b></p>
<ul class="check">
<li>바닥·벽처럼 무늬가 비쳐야 하면 Overlay·Multiply, 화면 반사를 얹으면 Screen을 썼다</li>
<li>합성한 것이 원본보다 선명하면 Opacity를 85~95%로 내리거나 Add Grain을 넣었다</li>
<li>빛나는 화면이면 Glow, 실제 물체면 그림자(21-6)를 더했다</li>
</ul>
'''

T1_4 = '''<h2><span class="tag t1">따라 하기</span> 20-11 실전 사례 T1~T4 — 화면 바꾸기 네 가지</h2>
<div class="mission"><div class="lbl">실습 소스</div><p>힉스필드 Seedance 2.0 Mini로 만든 5초 720p 클립(각 5크레딧): 초록 화면 폰을 든 손, 벽걸이 TV가 있는 거실, 밤 거리의 전광판, 곡면 미디어월이 있는 로비. 바꿔 끼울 화면은 10장 Claude 사례 1~3의 프레임입니다. 컴포지션은 1280×720, 5초, 24fps.</p></div>

<h3>T1. 폰 화면 교체 — 4점 트래킹 + Keylight</h3>
<p>역할: <b>Perspective corner pin</b>이 화면 네 귀퉁이를 따라가고, <b>Keylight</b>가 초록을 지워 손가락이 새 화면 앞에 오게 합니다.</p>
<div class="step"><div class="n">1</div><div class="b">컴포지션 <span class="mono">T1_폰크로마키</span>에 원본 영상(<span class="mono">원본_폰</span>)과 바꿔 끼울 세로 이미지(<span class="mono">넣을화면_쇼츠</span>)를 놓습니다. 원본 레이어를 클릭해 고르고 Tracker 패널의 <b>Track Motion</b>을 누릅니다. Layer 패널이 열립니다.</div></div>
<div class="step"><div class="n">2</div><div class="b">Track Type을 <b>Perspective corner pin</b>으로 바꾸면 점 4개가 생깁니다. 각 점의 안쪽 상자를 화면 귀퉁이의 흰 점 위로 옮깁니다. 마우스로 끌기 어려우면 점을 클릭해 고른 뒤 방향키(<span class="k">Shift</span>+방향키는 10픽셀씩)로 옮깁니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T1a_points.jpg"><figcaption><b>그림 20-91</b>네 점을 초록 화면 귀퉁이의 흰 점에 놓은 모습. 오른쪽 Tracker 패널에 Motion Source 원본_폰, Track Type Perspective corner pin이 보입니다.</figcaption></figure>
<div class="step"><div class="n">3</div><div class="b"><b>Analyze forward</b>(▶)를 누릅니다. 5초 클립은 몇 초면 끝납니다. 네 점이 귀퉁이를 따라가며 경로가 남습니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T1b_analyzed.jpg"><figcaption><b>그림 20-92</b>분석이 끝난 모습. 각 점 옆의 짧은 선이 프레임마다 움직인 경로입니다.</figcaption></figure>
<div class="step"><div class="n">4</div><div class="b"><b>Edit Target…</b>을 눌러 Layer를 <span class="mono">넣을화면_쇼츠</span>로 고르고 OK, 이어서 <b>Apply</b>. 이미지에 <b>Corner Pin</b> 효과가 생기고 네 귀퉁이와 Position에 프레임마다 키가 들어갑니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T1c_target.jpg"><figcaption><b>그림 20-93</b>Motion Target 창. “Apply Motion To: Layer”에서 바꿔 끼울 레이어를 고릅니다.</figcaption></figure>
<div class="step"><div class="n">5</div><div class="b">처음 결과를 보면 새 화면 둘레에 <b>초록 테두리</b>가 남습니다. 흰 점이 화면 끝이 아니라 조금 안쪽에 있었기 때문입니다. 바꿔 끼운 레이어의 Scale을 <b>133%, 122%</b>(가로·세로 따로)로 키워 초록을 덮었습니다.</div></div>
<div class="step"><div class="n">6</div><div class="b">원본 레이어를 바꿔 끼운 화면 <b>위</b>로 올리고(<b>Layer → Arrange → Bring Layer to Front</b>), <b>Effect → Keying → Keylight (1.2)</b>를 넣어 Screen Colour로 초록을 찍습니다. 손가락이 화면을 지나가도 손이 앞에 남습니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T1d_keylight.jpg"><figcaption><b>그림 20-94</b>왼쪽 Effect Controls에 Keylight(Screen Colour 초록), 아래 타임라인에 Corner Pin의 Upper Left~Lower Right 키가 프레임마다 찍혀 있습니다.</figcaption></figure>
<figure class="shot wide"><img src="img/TRK_T1e_before_after.jpg"><figcaption><b>그림 20-95</b>왼쪽: Apply 직후, 초록 테두리가 남았습니다. 오른쪽: Scale을 키우고 Keylight를 건 결과(2.5초).</figcaption></figure>

<h3>T2. 벽걸이 TV 화면 교체 — 같은 4점, 다른 결과</h3>
<p>역할: T1과 같은 <b>Perspective corner pin</b>이지만, 이번에는 흰 점 대신 <b>TV 베젤의 네 모서리</b>를 따라갑니다. 반사가 강한 검은 화면은 실제로 따라가기 어렵다는 것을 보여 주는 사례입니다.</p>
<div class="step"><div class="n">1</div><div class="b"><span class="mono">원본_TV</span>를 고르고 Track Motion → Perspective corner pin. 네 점을 베젤 바깥 모서리에 놓습니다. 안쪽 상자 절반은 TV, 절반은 벽이 들어가게 하면 모서리 모양이 뚜렷해집니다.</div></div>
<div class="step"><div class="n">2</div><div class="b">Analyze forward → Edit Target에서 <span class="mono">넣을화면_그래프</span> → Apply.</div></div>
<figure class="shot wide"><img src="img/TRK_T2a_analyzed.jpg"><figcaption><b>그림 20-96</b>분석 결과. 오른쪽 두 점은 베젤을 따라갔지만, 왼쪽 두 점(Track Point 1·3)은 경로가 화면 안쪽으로 휘었습니다.</figcaption></figure>
<figure class="shot wide"><img src="img/TRK_T2b_ok_drift.jpg"><figcaption><b>그림 20-97</b>왼쪽 0.5초는 정확합니다. 오른쪽 4.5초에는 카메라가 다가오며 왼쪽 모서리 뒤의 벽 밝기가 바뀌어 점이 미끄러졌고, 그래프가 TV 밖으로 삐져나왔습니다.</figcaption></figure>
<div class="stuck"><b>이렇게 고칩니다</b>① 점이 미끄러지기 시작한 프레임(이 영상은 약 1.2초)으로 가서 그 점만 모서리에 다시 놓고 그 프레임부터 다시 분석합니다. ② Options…에서 <b>Adapt Feature On Every Frame</b>을 켭니다. ③ 그래도 안 되면 점 대신 면을 따라가는 <b>Mocha AE</b>(20-6)로 TV 화면 전체를 추적합니다. 반사가 많은 화면은 Mocha가 훨씬 강합니다.</div>
<div class="tip"><b>반사 얹기</b>교체가 끝나면 원본 TV 레이어를 복제해 맨 위에 두고 블렌딩 모드를 <b>Screen</b>, Opacity 20~30%로 하면 원래 화면의 창문 반사가 새 화면 위에 얇게 비쳐 진짜처럼 보입니다.</div>

<h3>T3. 거리 전광판 — 4점 + Glow</h3>
<p>역할: 같은 4점 트래킹이 이번엔 <b>하늘을 배경으로 한 전광판 틀</b>을 따라갑니다. 대비가 강해 가장 잘 붙은 사례입니다.</p>
<div class="step"><div class="n">1</div><div class="b"><span class="mono">원본_전광판</span>을 고르고 Track Motion → Perspective corner pin. 네 점을 전광판 화면의 네 모서리에 놓습니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T3a_points.jpg"><figcaption><b>그림 20-98</b>네 점을 놓은 모습. 점 사이 흰 선이 바꿔 끼울 화면의 모양을 미리 보여 줍니다. 선이 전광판 테두리와 겹치면 제자리입니다.</figcaption></figure>
<div class="step"><div class="n">2</div><div class="b">Analyze forward. 카메라가 크게 돌아가지만 네 점 모두 끝까지 따라갑니다. Edit Target에서 <span class="mono">넣을화면_카운트</span> → Apply.</div></div>
<figure class="shot wide"><img src="img/TRK_T3b_analyzed.jpg"><figcaption><b>그림 20-99</b>5초 끝 프레임. 네 점의 경로(하늘색 띠)가 모두 전광판 모서리에 남아 있습니다.</figcaption></figure>
<div class="step"><div class="n">3</div><div class="b">바꿔 끼운 레이어에 <b>Effect → Stylize → Glow</b>를 넣고 Glow Radius 40, Glow Intensity 0.6. 밤거리에서 화면이 빛나 보입니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T3c_result.jpg"><figcaption><b>그림 20-100</b>0.5초(왼쪽)와 3.5초(오른쪽). 카메라가 돌아가며 전광판이 커져도 카운트다운 화면이 틀 안에 붙어 있습니다.</figcaption></figure>
<div class="tip"><b>웨이브 전광판</b>화면이 물결처럼 휘는 연출은 <b>Corner Pin보다 먼저</b> 휘어야 합니다. 바꿔 끼울 이미지를 프리컴포즈하고, 프리컴포즈 안에서 <b>Wave Warp</b>나 Bezier Warp를 건 뒤, 바깥의 프리컴포즈 레이어에 트래킹을 Apply합니다. 효과 순서가 바뀌면 물결이 전광판 밖으로 넘칩니다.</div>

<h3>T4. 곡면 미디어월 — Bezier Warp</h3>
<p>역할: 4점 트래킹은 평평한 면만 맞출 수 있습니다. 휘어진 벽에는 <b>Bezier Warp</b>로 이미지를 먼저 휘어 맞춥니다.</p>
<div class="step"><div class="n">1</div><div class="b"><span class="mono">넣을화면_그래프</span>를 고르고 <b>Effect → Distort → Bezier Warp</b>. 꼭짓점 4개(Top Left Vertex, Right Top Vertex, Bottom Right Vertex, Left Bottom Vertex)를 벽 화면의 네 모서리로 옮깁니다.</div></div>
<div class="step"><div class="n">2</div><div class="b">위쪽 곡선은 Top Left Tangent와 Top Right Tangent를 벽 윗선 위 1/3, 2/3 지점으로 옮겨 곡선을 만듭니다. 아래쪽도 같은 방법으로 맞춥니다. Effect Controls 이름 옆의 과녁 아이콘을 누르고 화면을 클릭해도 됩니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T4a_bezier.jpg"><figcaption><b>그림 20-101</b>Bezier Warp의 꼭짓점·접선 12개 값. 이 책에서 쓴 값이 그대로 보입니다(레이어 1920×1080 기준 좌표).</figcaption></figure>
<figure class="shot wide"><img src="img/TRK_T4b_result.jpg"><figcaption><b>그림 20-102</b>원본(왼쪽)과 결과(오른쪽), 0초. 그래프 위아래가 벽의 곡선과 원근을 따라 휘었습니다.</figcaption></figure>
<div class="note"><b>한계도 기억하세요</b>이 클립은 카메라가 크게 움직여 0초 한 프레임만 맞습니다. 곡면을 따라가는 트래킹은 애펙 기본 기능으로는 어렵습니다. 카메라가 고정된 장면에 쓰거나, 곡면을 평평한 <b>띠 3~4개</b>로 나눠 띠마다 4점 트래킹한 뒤 나란히 이어 붙입니다.</div>
'''

T5_8 = '''<h2><span class="tag t1">따라 하기</span> 21-9 실전 사례 T5~T8 — 공간에 붙이기</h2>
<div class="mission"><div class="lbl">실습 소스</div><p>Seedance 2.0 Mini 5초 720p 클립: 드론이 옥상을 돌아가는 장면, 횡단보도를 지나가는 장면(각 5크레딧). T7·T8은 6장의 걷는 인물 클립과 거리 클립으로 같은 순서를 응용합니다.</p></div>

<h3>T5. 옥상 바닥 글자 — Create Text and Camera</h3>
<p>역할: 3D Camera Tracker가 <b>지붕 면</b>을 찾고, Text가 그 면에 헬기장 표시처럼 누워 붙습니다.</p>
<div class="step"><div class="n">1</div><div class="b"><span class="mono">T5_옥상텍스트</span>에서 <span class="mono">원본_옥상</span>을 고르고 Tracker 패널의 <b>Track Camera</b>. 파란 띠로 “Analyzing in background (step 1 of 2)”가 뜹니다. 이 클립은 약 30초 만에 끝났습니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T5a_analyzing.jpg"><figcaption><b>그림 21-91</b>분석 중. 왼쪽 Effect Controls의 3D Camera Tracker에 Initializing…과 Cancel 버튼이 보입니다.</figcaption></figure>
<div class="step"><div class="n">2</div><div class="b">분석이 끝나면 효과 이름 <b>3D Camera Tracker</b>를 클릭해 고릅니다. 색 점이 나타나면 지붕 위 점들을 드래그로 둘러싸 고릅니다. 빨간 과녁이 지붕 면에 <b>누워</b> 있는지 확인합니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T5b_points.jpg"><figcaption><b>그림 21-92</b>지붕 앞쪽에 누운 빨간 과녁. Effect Controls에 “121 frames”가 보이면 분석 완료입니다.</figcaption></figure>
<div class="step"><div class="n">3</div><div class="b">과녁에서 우클릭 → <b>Create Text and Camera</b>. 타임라인에 <span class="mono">Text</span>와 <span class="mono">3D Tracker Camera</span>가 생깁니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T5c_menu.jpg"><figcaption><b>그림 21-93</b>과녁 우클릭 메뉴. 같은 과녁에서 Text, Solid, Null, Shadow Catcher를 역할에 따라 고릅니다(21-3 표).</figcaption></figure>
<div class="step"><div class="n">4</div><div class="b">도구 막대의 <b>Type Tool</b>을 고르고 화면의 글자를 클릭한 뒤 <span class="k">Ctrl+A</span>로 전체를 골라 <span class="mono">H  SKY 2027</span>을 입력합니다. Character 설정은 Malgun Gothic Bold, 30px, 자간 40, 연두색.</div></div>
<div class="step"><div class="n">5</div><div class="b">글자가 지붕 끝에 걸리면 Anchor Point를 바꿔 <b>면 위에서 밀어</b> 옮깁니다. 이 책에서는 Anchor Point에 익스프레션 <span class="mono">value + [-50, 130, 0]</span>을 넣어 지붕 가운데로 옮겼습니다. Position을 바꾸면 면에서 떠오르지만, 누운 레이어의 Anchor Point를 바꾸면 면을 따라 미끄러집니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T5d_props.jpg"><figcaption><b>그림 21-94</b>Properties 패널. 트래커가 만든 글자는 Scale 2000%, Orientation(274°, 357°, 321°)로 지붕 면에 맞춰져 있습니다. 이 값은 건드리지 않습니다.</figcaption></figure>
<figure class="shot wide"><img src="img/TRK_T5e_result.jpg"><figcaption><b>그림 21-95</b>0.5초(왼쪽)와 4.5초(오른쪽). 드론이 돌아가도 글자가 지붕 바닥에 칠해진 것처럼 붙어 있습니다.</figcaption></figure>
<div class="tip"><b>헬기처럼 떠서 도는 글자로</b>① Orientation의 X에 90을 더해 글자를 세우고 ② Anchor Point의 Y를 올려 지붕에서 띄운 뒤 ③ Y Rotation에 <span class="mono">time*90</span>을 넣으면 1초에 90°씩 돕니다. ④ 21-6의 Shadow Catcher로 바닥에 그림자를 떨어뜨리면 떠 있는 느낌이 납니다.</div>

<h3>T6. 횡단보도에 영상 깔기 — Create Solid and Camera</h3>
<p>역할: 같은 트래커가 이번엔 <b>도로 면</b>을 찾고, Solid가 그 위에 깔릴 화면이 됩니다. Overlay가 흰 줄무늬를 살립니다.</p>
<div class="step"><div class="n">1</div><div class="b"><span class="mono">원본_횡단보도</span>에 Track Camera. 분석이 끝나면 효과 이름을 클릭하고, 횡단보도 줄 위의 점 근처에 마우스를 올립니다. 근처 세 점이 이어진 삼각형과 과녁이 보이면 클릭해 고릅니다.</div></div>
<figure class="shot wide"><img src="img/TRK_T6a_target.jpg"><figcaption><b>그림 21-96</b>노란 점 세 개를 고르자 도로에 누운 과녁이 생겼습니다. 가까운 점과 먼 점을 섞어 고르면 면의 기울기가 정확해집니다.</figcaption></figure>
<div class="step"><div class="n">2</div><div class="b">과녁 우클릭 → <b>Create Solid and Camera</b>. <span class="mono">Track Solid 1</span>이 도로에 눕습니다. Scale을 550%로 키워 횡단보도를 덮습니다.</div></div>
<div class="step"><div class="n">3</div><div class="b">솔리드에 <b>Effect → Generate → 4-Color Gradient</b>를 넣고 블렌딩 모드를 <b>Overlay</b>, Opacity 85%. 영상을 깔려면 프로젝트 패널의 영상을 <span class="k">Alt</span>를 누른 채 솔리드 위로 끌어 놓아 바꿔 끼웁니다(21-5).</div></div>
<figure class="shot wide"><img src="img/TRK_T6b_result.jpg"><figcaption><b>그림 21-97</b>0.5초(왼쪽)와 4.5초(오른쪽). 카메라가 길을 건너며 방향이 바뀌어도 색이 도로에 붙어 있고, Overlay 덕분에 흰 줄무늬가 그대로 보입니다.</figcaption></figure>
<div class="note"><b>사람과 차가 지나가면</b>바닥 영상이 사람 발 위에 덮입니다. 지나가는 사람만 Roto Brush(22장 Object Matte)로 따서 맨 위에 다시 올립니다.</div>

<h3>T7. 벽 그래피티와 따라다니는 글자 — 응용</h3>
<p>역할: 3D 트래커는 벽을, 1점 트래킹은 사람을 맡습니다. 한 장면에서 두 트래커가 다른 일을 합니다.</p>
<div class="step"><div class="n">1</div><div class="b">6장의 걷는 인물 클립에 Track Camera. 사람 위의 점은 드래그로 골라 우클릭 → <b>Delete Selected Points</b>로 지웁니다(Advanced의 Auto-delete Points Across Time을 켜 두면 다른 프레임에서도 함께 지워집니다).</div></div>
<div class="step"><div class="n">2</div><div class="b">벽 면의 점을 골라 과녁이 벽과 나란히 <b>서도록</b> 맞추고 Create Solid and Camera. 솔리드를 그래피티 이미지(배경이 투명한 PNG)로 바꿔 끼우고 블렌딩 <b>Multiply</b>. 벽돌 질감이 그림 위로 비칩니다.</div></div>
<div class="step"><div class="n">3</div><div class="b">따라다니는 글자는 20-3의 1점 트래킹으로 만듭니다. 사람 어깨 같은 뚜렷한 곳을 Track Motion으로 따라가 <b>널</b>에 Apply하고, 글자를 널에 부모로 겁니다.</div></div>
<ul class="check">
<li>벽 과녁이 바닥처럼 눕지 않고 벽과 나란히 섰다</li>
<li>사람 위의 트랙 포인트를 지웠다</li>
<li>그래피티는 Multiply, 글자는 Normal로 구분했다</li>
</ul>

<h3>T8. 건물에 3D 글자 세우기 — 응용</h3>
<p>역할: Null이 건물 앞 바닥의 <b>손잡이</b>가 되고, 두께가 있는 3D 글자가 그 위에 섭니다.</p>
<div class="step"><div class="n">1</div><div class="b">거리 클립에 Track Camera → 건물 앞 바닥의 점을 골라 <b>Create Null and Camera</b>.</div></div>
<div class="step"><div class="n">2</div><div class="b"><b>Composition → Composition Settings → 3D Renderer</b>를 <b>Advanced 3D</b>로 바꿉니다. 글자를 입력하고 3D Layer 스위치를 켠 뒤 <b>Geometry Options → Extrusion Depth</b>를 40으로 올리면 두께가 생깁니다.</div></div>
<div class="step"><div class="n">3</div><div class="b">글자를 <span class="mono">Track Null 1</span>에 부모로 걸고 Position을 0, 0, 0으로. Orientation X에 90을 더해 세우고, 그림자는 21-6처럼 Shadow Catcher로 받습니다.</div></div>
<ul class="check">
<li>3D Renderer가 Advanced 3D이고 Extrusion Depth가 0보다 크다</li>
<li>글자의 바닥 선이 실제 바닥에 닿아 있다(Position Y 조절)</li>
<li>라이트 방향이 영상 속 해 방향과 같다</li>
</ul>
'''


def apply10(S):
    k = S.find('<div class="ch-no" id="ch-20">')
    if k < 0:
        k = S.find('<div class="ch-no">CHAPTER 20</div>')
    assert k > 0
    j = S.find('<h2>이 장 점검</h2>', k)
    S = S[:j] + ROLE + T1_4 + '\n' + S[j:]
    k = S.find('<div class="ch-no" id="ch-21">')
    if k < 0:
        k = S.find('<div class="ch-no">CHAPTER 21</div>')
    assert k > 0
    j = S.find('<h2>이 장 점검</h2>', k)
    S = S[:j] + T5_8 + '\n' + S[j:]
    return S
