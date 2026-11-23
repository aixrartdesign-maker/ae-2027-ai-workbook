# -*- coding: utf-8 -*-
# 4-3 관절 리그 / 13-9 카메라+널 삽입 (mk13c.py 맨 앞에서 실행)
RIG_SVG=open('/home/claude/book/img/R_rig.svg',encoding='utf-8').read()
SEC4='''
<h2><span class="tag t1">따라 하기</span> 4-3 사람 몸 움직이기 — 관절에 부모 걸기</h2>
<p>종이 인형처럼 몸을 마디별 레이어로 나누고, 마디마다 <b>기준점(Anchor Point)</b>을 관절로 옮긴 뒤, <b>몸에 가까운 쪽을 부모</b>로 잇습니다. 그러면 어깨만 돌려도 팔 전체가, 골반만 움직여도 온몸이 따라옵니다. 이렇게 짠 뼈대를 <b>리그(rig)</b>라고 합니다. 실습 파일의 컴포지션 <span class="mono">04-3_캐릭터리그</span>에 레이어 30개짜리 리그가 들어 있습니다. 손에는 엄지, 발에는 신발 밑창, 얼굴에는 귀·볼·머리카락이 따로 붙어 있습니다.</p>
<div class="why"><b>세 가지 규칙</b>① <b>나누기</b> — 레이어 하나는 관절과 관절 사이 한 마디입니다. 위팔과 아래팔을 한 장에 그리면 팔꿈치가 굽혀지지 않습니다. ② <b>기준점</b> — 기준점은 그 마디의 <b>몸 쪽 관절</b>에 둡니다. 위팔은 어깨, 아래팔은 팔꿈치, 손은 손목입니다. ③ <b>부모</b> — 몸 쪽 마디가 부모입니다. 손 → 아래팔 → 위팔 → 몸통 → 골반 → 전체_조종(널) 순서로 겁니다.</div>
<figure class="shot dia-fig">'''+RIG_SVG+'''<figcaption><b>그림 4-91</b>왼쪽: 빨간 점이 각 마디의 기준점(관절) 위치입니다. 오른쪽: 부모 관계. 들여 쓴 레이어가 바로 위 레이어의 자식입니다.</figcaption></figure>
<table><tr><th>레이어</th><th>기준점 위치</th><th>부모</th><th>주로 움직이는 속성</th></tr>
<tr><td>전체_조종 (널)</td><td>골반 가운데</td><td>없음</td><td>Position — 화면 이동, 걸을 때 위아래 통통</td></tr>
<tr><td>골반</td><td>골반 가운데</td><td>전체_조종</td><td>Rotation — 엉덩이 흔들기</td></tr>
<tr><td>몸통</td><td>허리(아래 끝 가운데)</td><td>골반</td><td>Rotation — 숙이기 · Scale Y — 숨쉬기</td></tr>
<tr><td>목</td><td>목 아래 끝</td><td>몸통</td><td>보통 고정 (머리와 몸 사이 틈 가리기)</td></tr>
<tr><td>머리</td><td>목(턱 아래 가운데)</td><td>목</td><td>Rotation — 끄덕임, 갸웃</td></tr>
<tr><td>눈 · 입 · 귀 · 볼 · 머리카락</td><td>각자 가운데</td><td>머리</td><td>Scale — 깜빡임, 입 벌림 · Position — 눈동자 방향</td></tr>
<tr><td>위팔 (좌우)</td><td>어깨</td><td>몸통</td><td>Rotation</td></tr>
<tr><td>아래팔 (좌우)</td><td>팔꿈치</td><td>위팔</td><td>Rotation</td></tr>
<tr><td>손 (좌우)</td><td>손목</td><td>아래팔</td><td>Rotation</td></tr>
<tr><td>엄지 (좌우)</td><td>가운데</td><td>손</td><td>보통 고정 (주먹 쥘 때 Rotation)</td></tr>
<tr><td>허벅지 (좌우)</td><td>엉덩이 관절</td><td>골반</td><td>Rotation</td></tr>
<tr><td>정강이 (좌우)</td><td>무릎</td><td>허벅지</td><td>Rotation</td></tr>
<tr><td>발 (좌우)</td><td>발목</td><td>정강이</td><td>Rotation</td></tr>
<tr><td>밑창 (좌우)</td><td>가운데</td><td>발</td><td>고정 (발과 함께 돎)</td></tr>
<tr><td>그림자</td><td>가운데</td><td>없음</td><td>몸이 뛰어도 땅에 남도록 부모를 걸지 않습니다</td></tr>
</table>
<div class="step"><div class="n">1</div><div class="b"><b>마디 그리기.</b> 셰이프, 일러스트레이터, 포토샵 레이어 무엇이든 좋습니다. 팔다리는 <b>양 끝이 둥근 캡슐</b>(사각형 Roundness = 폭의 절반)로 그리고, 기준점을 둥근 끝의 중심에 두면 굽혀도 관절이 매끈하게 겹칩니다. 손은 타원에 엄지 타원 하나, 발은 둥근 사각형 신발에 밑창 한 줄이면 충분합니다. 레이어 이름은 <span class="mono">위팔_왼</span>처럼 부위와 방향을 함께 씁니다.</div></div>
<div class="step"><div class="n">2</div><div class="b"><b>기준점을 관절로.</b> 레이어를 고르고 <b>Pan Behind(Anchor Point) 도구</b>(<span class="k">Y</span>)로 기준점을 관절까지 끕니다. 이 도구는 그림은 그대로 두고 기준점만 옮깁니다. 숫자로 하려면 <span class="k">A</span>를 눌러 Anchor Point를 바꾸고 Position도 같은 만큼 맞춥니다. 예: 높이 130px인 위팔은 Anchor <span class="mono">0, −65</span>가 위쪽 끝(어깨)입니다.</div></div>
<div class="step"><div class="n">3</div><div class="b"><b>부모 걸기.</b> 끝에서 몸 쪽으로 차례로 겁니다. 손의 소용돌이 아이콘(Pick Whip)을 아래팔로, 아래팔은 위팔로, 위팔은 몸통으로 끕니다. 눈·입처럼 같은 부모를 가질 레이어는 여러 개를 함께 고른 뒤 한 레이어의 Parent 칸만 바꾸면 한꺼번에 걸립니다.</div></div>
<div class="step"><div class="n">4</div><div class="b"><b>앞뒤 순서 정하기.</b> 부모와 쌓는 순서는 따로입니다. 레이어 패널에서 위에 있을수록 화면 앞이므로 팔은 몸통 위, 다리는 골반 아래에 둡니다. 몸 뒤로 가는 팔은 몸통 아래로 내립니다.</div></div>
<div class="step"><div class="n">5</div><div class="b"><b>Rotation만 움직이기.</b> 이제 각 마디는 Rotation 하나면 됩니다. 어깨를 먼저 돌리고, 팔꿈치·손목은 2~4프레임 늦게 따라가게 하면 채찍처럼 자연스럽습니다. 이것을 <b>오버랩(follow-through)</b>이라고 합니다.</div></div>
<figure class="shot"><img src="img/R_parent.jpg"><figcaption><b>그림 4-92</b>실제 Parent &amp; Link 칸(레이어 30개). 엄지_오 → 3번 손_오 → 4번 아래팔_오 → 5번 위팔_오 → 20번 몸통 → 21번 골반 → 1번 전체_조종으로 이어집니다. 머리는 19번 목에, 밑창은 발에 걸려 있고, 30번 그림자만 부모가 없습니다.</figcaption></figure>
<figure class="shot wide"><img src="img/R_poses.jpg"><figcaption><b>그림 4-93</b>Rotation만 바꾼 세 자세. 오른팔은 들어서 흔들고, 다리는 제자리걸음, 눈은 2.2초마다 깜빡이고, 입은 말하듯 벌어집니다. 골반 옆 빨간 네모는 렌더에 나오지 않는 널(전체_조종)입니다.</figcaption></figure>
<div class="prompt"><span class="lbl">EXPRESSION · 실습 파일의 반복 동작</span>// 위팔_오 Rotation — 팔을 들고 작게 흔들기<br>-130 + Math.sin(time*Math.PI*4)*8;<br>// 아래팔_오 Rotation — 0.5만큼 늦게 따라감 = 오버랩<br>-35 + Math.sin(time*Math.PI*4 - 0.5)*28;<br>// 허벅지_왼 Rotation — 한쪽 다리만 들기 (오른쪽은 부호 반대)<br>Math.max(0, Math.sin(time*Math.PI*2))*14;<br>// 눈 Scale — 깜빡임<br>(time % 2.2 &lt; 0.12) ? [100, 12] : [100, 100];<br>// 입 Scale — 말하는 입<br>[100, 100 + Math.abs(Math.sin(time*9))*220];</div>
<table><tr><th>동작</th><th>어디에 무엇을 거나</th></tr>
<tr><td>걷기</td><td>전체_조종 Position X로 앞으로, Y로 한 걸음마다 위아래. 허벅지·정강이 Rotation은 좌우 반대로, 팔은 같은 쪽 다리와 반대로 흔듭니다. 옆모습 걷기는 4-4에서 자세히 다룹니다.</td></tr>
<tr><td>손 흔들기</td><td>위팔 Rotation으로 팔을 든 채 고정, 아래팔과 손 Rotation만 반복합니다.</td></tr>
<tr><td>고개 끄덕 · 갸웃</td><td>머리 Rotation. 기준점이 목에 있어야 목을 축으로 움직입니다.</td></tr>
<tr><td>숨쉬기</td><td>몸통 Scale Y 100 → 102%. 기준점이 허리라서 위로만 부풉니다.</td></tr>
<tr><td>표정</td><td>눈 Scale Y(깜빡임), 눈동자 Position(보는 방향), 입 Scale이나 Path(말하기). 얼굴 부품은 모두 머리의 자식입니다.</td></tr>
<tr><td>점프</td><td>전체_조종 Position Y로 뛰고, 착지 순간 골반을 몇 픽셀 내려 무릎이 눌리는 느낌을 줍니다.</td></tr>
</table>
<div class="stuck"><b>막혔을 때</b>엉뚱한 곳을 중심으로 돈다 → 기준점이 가운데 있습니다. <span class="k">Y</span> 도구로 관절에 옮기세요. 부모를 걸자 부위가 튀어 간다 → <span class="k">Shift</span>를 누른 채 Pick Whip하면 자식이 부모 위치로 옮겨집니다. 그냥 끌면 제자리에 있습니다. 자식 크기가 같이 변한다 → 부모의 Scale을 바꾼 탓입니다. 크기는 전체_조종에서만 바꿉니다. 팔이 몸 뒤로 숨는다 → 부모가 아니라 레이어 순서 문제입니다.</div>
<div class="tip"><b>더 나아가기</b>관절이 많은 캐릭터는 무료 스크립트 <b>Duik</b>이 IK(손끝을 끌면 팔 전체가 따라 굽는 방식)를 만들어 줍니다. 몸 전체를 고무처럼 휘게 하려면 5-6의 퍼펫 핀을 함께 씁니다.</div>
'''
SEC4B='\n<h2><span class="tag t1">따라 하기</span> 4-4 옆에서 본 걷기 — 네 자세로 만드는 한 사이클</h2>\n<p>걷기는 <b>네 자세의 반복</b>입니다. 발이 땅에 닿고(닿기), 무게를 받아 내려앉고(내려앉기), 다른 발이 몸 옆을 지나가고(지나가기), 발끝으로 밀어 올라섭니다(올라서기). 30fps에서 한 걸음은 15프레임, 왼발·오른발 두 걸음 30프레임(1초)이 한 사이클입니다. 네 자세만 키프레임으로 주면 사이는 애펙이 채우고, 끝에 <span class="mono">loopOut()</span>을 걸면 계속 걷습니다. 컴포지션 <span class="mono">04-4_옆모습걷기</span>.</p>\n<figure class="shot wide"><img src="img/W_poses.jpg"><figcaption><b>그림 4-94</b>실습 파일의 네 자세. 캐릭터는 왼쪽을 봅니다. 밝은 색이 보는 쪽(앞) 다리, 어두운 색이 먼 쪽(뒤) 다리입니다. 15프레임부터는 앞뒤 다리가 바뀌어 같은 네 자세를 한 번 더 합니다.</figcaption></figure>\n<div class="why"><b>옆모습 리그가 다른 점</b>① 팔다리를 <b>앞(보는 쪽)·뒤(먼 쪽) 두 벌</b> 만들고 이름 끝에 _앞, _뒤를 붙입니다. ② 뒤쪽은 색을 한 단계 어둡게 하고 레이어를 몸통 아래로 내립니다. 쌓는 순서는 위에서부터 앞팔 → 머리 → 몸통 → 골반 → 앞다리 → 뒷다리 → 뒷팔입니다. ③ 왼쪽을 보는 캐릭터에서 Rotation <b>+</b> 값은 다리를 앞(왼쪽)으로, <b>−</b> 값은 뒤로 보냅니다. 오른쪽을 보게 하려면 부호를 모두 바꿉니다.</div>\n<table><tr><th>자세</th><th>앞다리 허벅지 / 정강이 / 발</th><th>뒷다리 허벅지 / 정강이 / 발</th><th>몸 높이 (전체_조종 Y)</th><th>앞팔 위팔</th></tr>\n<tr><td>① 닿기 0f</td><td>28 / −2 / −8 — 뒤꿈치로 착지</td><td>−25 / −22 / 22 — 발끝으로 밂</td><td>589 (보폭이 가장 넓음)</td><td>−24 (뒤로)</td></tr>\n<tr><td>② 내려앉기 4f</td><td>18 / −18 / 0 — 무릎 굽혀 무게 받음</td><td>−15 / −50 / 10 — 발을 뗌</td><td>581</td><td>−12</td></tr>\n<tr><td>③ 지나가기 8f</td><td>0 / −4 / 4 — 곧게 서서 몸 받침</td><td>10 / −75 / 25 — 무릎 들고 앞으로</td><td>575</td><td>0 (몸 옆)</td></tr>\n<tr><td>④ 올라서기 11f</td><td>−12 / −6 / −8 — 뒤꿈치 듦</td><td>30 / −25 / 12 — 앞으로 뻗음</td><td>546 (가장 높음)</td><td>10</td></tr>\n<tr><td>⑤ 닿기 15f</td><td colspan="2">①의 값을 앞다리 ↔ 뒷다리 바꿔 넣음. 19f·23f·26f도 ②~④를 바꿔 넣음</td><td>589</td><td>24 (앞으로)</td></tr>\n<tr><td>30f</td><td colspan="4">0f와 같은 값. 이 키가 있어야 반복이 끊기지 않습니다</td></tr>\n</table>\n<div class="step"><div class="n">1</div><div class="b"><b>앞다리부터.</b> 허벅지_앞, 정강이_앞, 발_앞의 Rotation에 0·4·8·11·15·19·23·26·30프레임 키를 표대로 넣습니다. 15f 이후 값은 표의 ①~④에서 뒷다리 쪽 값을 씁니다.</div></div>\n<div class="step"><div class="n">2</div><div class="b"><b>뒷다리는 반 박자 늦게.</b> 앞다리 키를 모두 골라 복사(<span class="k">Ctrl</span>+<span class="k">C</span>)하고, 뒷다리 레이어를 고른 뒤 15f에서 붙여 넣습니다(<span class="k">Ctrl</span>+<span class="k">V</span>). 30f를 넘어간 키는 30프레임 앞으로 옮겨 0~30f 안에 둡니다.</div></div>\n<div class="step"><div class="n">3</div><div class="b"><b>팔은 다리와 반대로.</b> 앞다리가 앞으로 나갈 때 앞팔은 뒤로 갑니다. 위팔 −24 → 0 → 24 → 0 → −24. 아래팔은 2프레임, 손은 3프레임 늦게 따라가게 하면(오버랩) 팔이 막대기처럼 보이지 않습니다.</div></div>\n<div class="step"><div class="n">4</div><div class="b"><b>몸 높이 맞추기.</b> 전체_조종 Position Y를 자세마다 바꿔 <b>바닥에 닿은 발이 땅선에 딱 붙게</b> 합니다. 발이 땅을 뚫으면 Y를 줄이고, 뜨면 늘립니다. 몸통은 −4 ~ −7°로 살짝 앞으로 기울이고, 머리는 반대로 2 ~ 5° 들어 시선을 앞에 둡니다.</div></div>\n<div class="step"><div class="n">5</div><div class="b"><b>반복과 이동.</b> 키가 있는 모든 속성에 <span class="mono">loopOut("cycle")</span>을 넣습니다. 제자리걸음을 앞으로 걸어가게 하려면 전체_조종 Position X를 1초에 보폭 두 배만큼 옮깁니다. 이 캐릭터는 닿기 자세에서 두 발목 사이가 약 250px이라 1초에 500px입니다.</div></div>\n<div class="prompt"><span class="lbl">EXPRESSION · 걷기 반복과 이동</span>// 키가 있는 Rotation, Position 모두 — 0~1초를 계속 반복<br>loopOut("cycle");<br>// 전체_조종 Position — 반복하면서 왼쪽으로 걸어감<br>loopOut("cycle") + [-time*500, 0];</div>\n<div class="stuck"><b>막혔을 때</b>발이 미끄러지듯 보인다 → 이동 속도가 보폭과 안 맞습니다. 500을 조금씩 바꿔 땅에 닿은 발이 화면에서 멈춰 보이는 값을 찾습니다. 반복할 때 툭 끊긴다 → 0f와 30f 키 값이 다릅니다. 다리가 꼬여 보인다 → 뒷다리 색이 앞다리와 같거나 레이어 순서가 바뀌었습니다. 걸음이 로봇 같다 → 키를 모두 골라 <span class="k">F9</span>(Easy Ease)를 주고, 아래팔·손의 오버랩을 늘립니다.</div>\n<div class="tip"><b>프레임 수 바꾸기</b>24fps라면 한 걸음 12프레임으로 0·3·6·9·12f에 같은 네 자세를 둡니다. 느긋한 걸음은 한 걸음 18~20프레임, 뛰기는 8프레임 안팎이며 두 발이 모두 뜨는 순간이 생깁니다.</div>\n'
SEC13='''
<h2><span class="tag t1">따라 하기</span> 13-9 카메라를 널에 걸어 돌리기</h2>
<p>카메라에 직접 키프레임을 주면 원을 그리며 도는 움직임을 만들기 어렵습니다. 대신 피사체 가운데에 널을 두고 카메라를 그 널의 자식으로 걸면, <b>널을 돌리는 것만으로 카메라가 원을 그리며</b> 돕니다. 사람 몸에서 어깨를 돌리면 손이 원을 그리는 것(4-3)과 같은 원리입니다. 컴포지션 <span class="mono">13-4_카메라널궤도</span>.</p>
<table><tr><th>레이어</th><th>역할</th><th>부모</th><th>움직이는 속성</th></tr>
<tr><td>Camera 1</td><td>눈</td><td>궤도_널</td><td>보통 고정. Position <span class="mono">0, 0, −2667</span>, Point of Interest <span class="mono">0, 0, 0</span></td></tr>
<tr><td>궤도_널 (3D)</td><td>회전축</td><td>크레인_널</td><td>Y Rotation = 좌우로 돌기, X Rotation = 위에서 넘겨보기</td></tr>
<tr><td>크레인_널 (3D)</td><td>높이와 위치</td><td>없음</td><td>Position Y = 크레인 상승, Position X = 옆으로 이동(트럭)</td></tr>
</table>
<div class="step"><div class="n">1</div><div class="b"><b>Layer → New → Null Object</b>를 두 번 만들고 이름을 <span class="mono">궤도_널</span>, <span class="mono">크레인_널</span>로 바꿉니다. 두 널 모두 <b>3D 스위치</b>(정육면체 칸)를 켭니다. 꺼져 있으면 Rotation 하나만 보이고 Y Rotation이 없습니다.</div></div>
<div class="step"><div class="n">2</div><div class="b">두 널의 Position을 돌고 싶은 중심, 보통 피사체 가운데(예: <span class="mono">960, 540, 0</span>)에 둡니다. 궤도_널의 Parent를 크레인_널로 겁니다.</div></div>
<div class="step"><div class="n">3</div><div class="b">카메라의 Parent를 궤도_널로 겁니다. 그다음 카메라를 고르고 <span class="k">A</span>(Point of Interest)를 <span class="mono">0, 0, 0</span>, <span class="k">P</span>(Position)를 <span class="mono">0, 0, −2667</span>로 바꿉니다. 자식의 값은 부모 기준이므로, 카메라는 널 앞 2667px에서 널을 바라봅니다. 2667은 이 카메라의 Zoom 값이며, 이 거리에서 z=0 레이어가 원래 크기로 보입니다.</div></div>
<div class="step"><div class="n">4</div><div class="b">궤도_널을 고르고 <span class="k">R</span>을 눌러 <b>Y Rotation</b>에 키프레임(0초 0°, 4초 0x+360°)을 주거나 아래 익스프레션을 넣습니다.</div></div>
<div class="step"><div class="n">5</div><div class="b">크레인_널의 Position Y를 줄이면(위로) 카메라가 올라가며 내려다봅니다. 돌기와 오르기를 다른 널에 나눠 두었기 때문에 서로 따로 고칠 수 있습니다.</div></div>
<figure class="shot wide"><img src="img/C_timeline_a.jpg"><figcaption><b>그림 13-91</b>실습 파일의 타임라인. ① 궤도_널의 부모는 2번 크레인_널, Y Rotation에 익스프레션 ② 크레인_널 Position에 위아래 익스프레션 ③ Camera 1의 부모는 1번 궤도_널.</figcaption></figure>
<figure class="shot wide"><img src="img/C_orbits.jpg"><figcaption><b>그림 13-92</b>카메라는 그대로 두고 널만 돌린 결과. 같은 장면을 정면, 오른쪽 위, 왼쪽에서 봅니다. 카드 두 장의 깊이 차이가 보입니다.</figcaption></figure>
<div class="prompt"><span class="lbl">EXPRESSION · 널로 카메라 움직이기</span>// 궤도_널 Y Rotation — 4초에 한 바퀴<br>time * 90;<br>// 궤도_널 Y Rotation — 좌우 35°를 왕복 (실습 파일)<br>Math.sin(time*Math.PI/2) * 35;<br>// 크레인_널 Position — 2초에 300px 올라갔다 내려옴<br>value + [0, -Math.sin(time*Math.PI/4)*300, 0];</div>
<table><tr><th>카메라 움직임</th><th>거는 곳</th></tr>
<tr><td>궤도 (Orbit, Arc)</td><td>궤도_널 Y Rotation</td></tr>
<tr><td>위에서 넘겨보기 (Tilt over)</td><td>궤도_널 X Rotation</td></tr>
<tr><td>크레인 (Crane)</td><td>크레인_널 Position Y</td></tr>
<tr><td>트럭 (Truck)</td><td>크레인_널 Position X</td></tr>
<tr><td>돌리 (Dolly, 다가가기)</td><td>카메라 Position Z (부모 기준이라 숫자 하나로 거리 조절)</td></tr>
<tr><td>롤 (Roll)</td><td>카메라 Z Rotation</td></tr>
<tr><td>줌</td><td>카메라 Zoom. 화각이 바뀌어 원근감이 달라지므로 돌리와 다릅니다.</td></tr>
</table>
<div class="stuck"><b>막혔을 때</b>부모를 걸자 화면이 크게 바뀐다 → 카메라 Position이 이제 부모 기준으로 읽힙니다. 3단계처럼 <span class="mono">0, 0, −거리</span>로 다시 넣으세요. 카메라가 엉뚱한 곳을 본다 → Point of Interest가 <span class="mono">0, 0, 0</span>인지 확인합니다. 한 바퀴 돌면 배경 끝이나 카드 뒷면이 보인다 → 배경이 평면 한 장이라서입니다. 실습 파일처럼 좌우 왕복으로 두거나, 3D 모델과 Environment Light로 사방을 채웁니다.</div>
'''
import re
def apply(S):
    a='<h2><span class="tag t1">따라 하기</span> 4-3 묶기(프리컴포즈)</h2>'
    assert a in S
    for old,new in [('4-6 블렌딩','4-8 블렌딩'),('4-5 트랙 매트','4-7 트랙 매트'),('4-4 마스크','4-6 마스크'),('4-3 묶기','4-5 묶기')]:
        assert S.count(old)>=1,old; S=S.replace(old,new)
    S=S.replace('<h2><span class="tag t1">따라 하기</span> 4-5 묶기(프리컴포즈)</h2>',SEC4.strip()+'\n\n'+SEC4B.strip()+'\n\n<h2><span class="tag t1">따라 하기</span> 4-5 묶기(프리컴포즈)</h2>',1)
    i=S.find('<div class="ch-no">CHAPTER 13'); j=S.find('<h2>이 장 점검</h2>',i)
    S=S[:j]+SEC13.strip()+'\n'+S[j:]
    S=S.replace('카메라를 널에 페어런팅하면, 널을 돌리는 것만으로 부드러운 궤도 촬영이 됩니다.','카메라를 널에 페어런팅하면, 널을 돌리는 것만으로 부드러운 궤도 촬영이 됩니다(13-9).',1)
    S=S.replace('빛만 남습니다(4-6)','빛만 남습니다(4-8)')
    return S
