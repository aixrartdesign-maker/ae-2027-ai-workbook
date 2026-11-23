# -*- coding: utf-8 -*-
# 4-3 관절 리그 / 13-9 카메라+널 삽입 (mk13c.py 맨 앞에서 실행)
RIG_SVG=open('/home/claude/book/img/R_rig.svg',encoding='utf-8').read()
TREE=open('/home/claude/book/img/R_tree.svg',encoding='utf-8').read()
SEC4="""
<h2><span class="tag t1">따라 하기</span> 4-3 사람 몸 움직이기 — 관절에 부모 걸기</h2>
<p>종이 인형처럼 몸을 마디별 레이어로 나누고, 마디마다 <b>기준점(Anchor Point)</b>을 관절로 옮긴 뒤, <b>몸에 가까운 쪽을 부모</b>로 잇습니다. 그러면 어깨만 돌려도 팔 전체가, 허리만 움직여도 윗몸 전체가 따라옵니다. 이렇게 짠 뼈대를 <b>리그(rig)</b>라고 합니다. 실습 파일 <span class="mono">04-3_캐릭터리그</span>의 캐릭터는 힉스필드 GPT Image로 그린 <b>부품 시트</b> 한 장을 잘라 만들었습니다.</p>
<div class="why"><b>세 가지 규칙</b>① <b>나누기</b> — 레이어 하나는 관절과 관절 사이 한 마디입니다. 위팔과 아래팔을 한 장에 그리면 팔꿈치가 굽혀지지 않습니다. ② <b>기준점</b> — 기준점은 그 마디의 <b>몸 쪽 관절</b>에 둡니다. 위팔은 어깨, 아래팔은 팔꿈치, 손은 손목입니다. ③ <b>부모</b> — 몸 쪽 마디가 부모입니다. 손 → 아래팔 → 위팔 → 몸통 → 전체_조종(널) 순서로 겁니다.</div>
<figure class="shot wide"><img src="img/R_rigfig.jpg"><figcaption><b>그림 4-91</b>왼쪽: 힉스필드 GPT Image로 만든 정면 부품 시트(배경 제거). 빨간 점이 각 부품의 기준점입니다. 오른쪽: 부모 관계. 들여 쓴 레이어가 바로 위 레이어의 자식입니다.</figcaption></figure>
<table><tr><th>레이어</th><th>기준점 위치</th><th>부모</th><th>주로 움직이는 속성</th></tr>
<tr><td>전체_조종 (널)</td><td>골반 높이 가운데</td><td>없음</td><td>Position — 화면 이동, 걸을 때 위아래</td></tr>
<tr><td>몸통 (상의·치마)</td><td>허리(벨트 가운데)</td><td>전체_조종</td><td>Rotation — 숙이기 · Scale Y — 숨쉬기</td></tr>
<tr><td>머리 (머리카락·목 포함)</td><td>목 아래</td><td>몸통</td><td>Rotation — 끄덕임, 갸웃</td></tr>
<tr><td>위팔 (좌우)</td><td>어깨</td><td>몸통</td><td>Rotation</td></tr>
<tr><td>아래팔 (좌우)</td><td>팔꿈치</td><td>위팔</td><td>Rotation</td></tr>
<tr><td>손 (좌우)</td><td>손목</td><td>아래팔</td><td>Rotation</td></tr>
<tr><td>허벅지 (좌우)</td><td>엉덩이 관절</td><td>전체_조종</td><td>Rotation</td></tr>
<tr><td>정강이 (좌우)</td><td>무릎</td><td>허벅지</td><td>Rotation</td></tr>
<tr><td>발 (좌우)</td><td>발목</td><td>정강이</td><td>Rotation</td></tr>
<tr><td>그림자</td><td>가운데</td><td>없음</td><td>몸이 뛰어도 땅에 남도록 부모를 걸지 않습니다</td></tr>
</table>
<div class="step"><div class="n">1</div><div class="b"><b>부품 시트 만들기.</b> 힉스필드에서 캐릭터 정면·옆모습을 한 장 만든 뒤, 그 그림을 참조로 넣고 아래처럼 <b>부품 시트</b>를 요청합니다. 결과는 Remove Background로 배경을 지워 PNG로 받습니다. 직접 그린다면 일러스트레이터·포토샵에서 부품마다 레이어를 나눠 저장합니다.</div></div>
<div class="prompt"><span class="lbl">PROMPT · 힉스필드 GPT Image (참조 이미지 1장)</span>2D cut-out animation puppet parts sheet of the same character in the reference. Flat even colors on limbs. Plain light gray background, every piece separated by wide gaps, no text. Each limb piece straight and vertical with a round ball-joint circle at both ends: head with neck, upper body, separate skirt, upper arm, forearm, hand, thigh, lower leg, boot.</div>
<div class="step"><div class="n">2</div><div class="b"><b>한 장을 부품 수만큼 자르기.</b> 같은 PNG를 부품 수만큼 컴포지션에 놓고, 레이어마다 사각형 마스크로 부품 하나만 남깁니다. 레이어 이름은 <span class="mono">위팔_왼</span>처럼 부위와 방향을 함께 씁니다.</div></div>
<div class="step"><div class="n">3</div><div class="b"><b>기준점을 관절로.</b> <b>Pan Behind(Anchor Point) 도구</b>(<span class="k">Y</span>)로 기준점을 관절, 즉 둥근 끝의 중심까지 끕니다. 이 도구는 그림은 그대로 두고 기준점만 옮깁니다. 그다음 Position을 움직여 각 부품을 몸에 맞게 조립합니다.</div></div>
<div class="step"><div class="n">4</div><div class="b"><b>부모 걸기와 쌓는 순서.</b> 끝에서 몸 쪽으로 Pick Whip을 끌어 겁니다(손 → 아래팔 → 위팔 → 몸통). 부모와 쌓는 순서는 따로입니다. 관절에서는 <b>몸 쪽 마디를 위에</b> 쌓아 둥근 끝이 아래 마디를 덮게 합니다. 정면에서는 팔을 몸통 위에, 다리는 몸통 아래에 둡니다.</div></div>
<div class="step"><div class="n">5</div><div class="b"><b>Rotation만 움직이기.</b> 이제 각 마디는 Rotation 하나면 됩니다. 어깨를 먼저 돌리고, 팔꿈치·손목은 2~4프레임 늦게 따라가게 하면 채찍처럼 자연스럽습니다. 이것을 <b>오버랩(follow-through)</b>이라고 합니다.</div></div>
<figure class="shot"><img src="img/R_parent.jpg"><figcaption><b>그림 4-92</b>실제 Parent &amp; Link 칸. 손_오 → 3번 아래팔_오 → 4번 위팔_오 → 8번 몸통 → 1번 널(전체_조종)로 이어집니다. 머리는 8번 몸통, 허벅지는 1번 널에 걸려 있고, 16번 그림자만 부모가 없습니다.</figcaption></figure>
<figure class="shot wide"><img src="img/R_poses.jpg"><figcaption><b>그림 4-93</b>Rotation만 바꾼 손 흔들기. 어깨가 먼저 올라가고, 팔꿈치와 손목이 조금씩 늦게 따라옵니다.</figcaption></figure>
<div class="prompt"><span class="lbl">EXPRESSION · 실습 파일의 반복 동작</span>// 위팔_오 Rotation — 팔을 들고 작게 흔들기<br>-140 + Math.sin(time*Math.PI*4)*6;<br>// 아래팔_오 Rotation — 0.5만큼 늦게 따라감 = 오버랩<br>-30 + Math.sin(time*Math.PI*4 - 0.5)*25;<br>// 머리 Rotation — 고개를 살짝 갸웃<br>Math.sin(time*Math.PI*2 + 1)*5;</div>
<table><tr><th>동작</th><th>어디에 무엇을 거나</th></tr>
<tr><td>걷기</td><td>전체_조종 Position X로 앞으로, Y로 한 걸음마다 위아래. 허벅지·정강이 Rotation은 좌우 반대로, 팔은 같은 쪽 다리와 반대로 흔듭니다. 옆모습 걷기는 4-4에서 자세히 다룹니다.</td></tr>
<tr><td>손 흔들기</td><td>위팔 Rotation으로 팔을 든 채 고정, 아래팔과 손 Rotation만 반복합니다.</td></tr>
<tr><td>고개 끄덕 · 갸웃</td><td>머리 Rotation. 기준점이 목에 있어야 목을 축으로 움직입니다.</td></tr>
<tr><td>숨쉬기</td><td>몸통 Scale Y 100 → 102%. 기준점이 허리라서 위로만 부풉니다.</td></tr>
<tr><td>점프</td><td>전체_조종 Position Y로 뛰고, 착지 순간 몸통 Scale Y를 98%로 살짝 눌러 줍니다.</td></tr>
</table>
<div class="why"><b>애니메이션 전문가 체크 — 이음매가 보이지 않게</b>① 관절 끝은 <b>둥근 원(볼 조인트)</b>으로 그립니다. 원의 중심이 기준점이면 몇 도를 굽혀도 두 부품이 겹쳐 틈이 생기지 않습니다. ② 3D 렌더처럼 명암이 강하면 겹친 자리에 경계선이 드러납니다. 팔다리는 <b>평평한 채색</b>이 이음매를 감춥니다. ③ 치마·소매처럼 관절을 덮는 옷은 <b>따로 한 장</b>으로 만들어, 다리가 움직여도 옷이 자연스럽게 가려 줍니다. ④ 부품을 처음부터 곧게 펴진 자세(차렷)로 그려야 회전값 0이 기본자세가 됩니다.</div>
<div class="stuck"><b>막혔을 때</b>엉뚱한 곳을 중심으로 돈다 → 기준점이 가운데 있습니다. <span class="k">Y</span> 도구로 관절에 옮기세요. 부모를 걸자 부위가 튀어 간다 → <span class="k">Shift</span>를 누른 채 Pick Whip하면 자식이 부모 위치로 옮겨집니다. 그냥 끌면 제자리에 있습니다. 자식 크기가 같이 변한다 → 부모의 Scale을 바꾼 탓입니다. 크기는 전체_조종에서만 바꿉니다. 관절에 틈이 벌어진다 → 기준점이 둥근 끝의 중심에서 벗어났습니다.</div>
<div class="tip"><b>더 나아가기</b>관절이 많은 캐릭터는 무료 스크립트 <b>Duik</b>이 IK(손끝을 끌면 팔 전체가 따라 굽는 방식)를 만들어 줍니다. 팔다리를 고무처럼 휘게 하려면 한 장짜리 팔에 5-6의 퍼펫 핀을 꽂습니다.</div>
"""
SEC4B="""
<h2><span class="tag t1">따라 하기</span> 4-4 옆에서 본 걷기 — 네 자세로 만드는 한 사이클</h2>
<p>걷기는 <b>네 자세의 반복</b>입니다. 발이 땅에 닿고(닿기), 무게를 받아 내려앉고(내려앉기), 다른 발이 몸 옆을 지나가고(지나가기), 발끝으로 밀어 올라섭니다(올라서기). 30fps에서 한 걸음은 15프레임, 왼발·오른발 두 걸음 30프레임(1초)이 한 사이클입니다. 네 자세만 키프레임으로 주면 사이는 애펙이 채우고, 끝에 <span class="mono">loopOut()</span>을 걸면 계속 걷습니다. 컴포지션 <span class="mono">04-4_옆모습걷기</span>.</p>
<figure class="shot dia-fig"><img src="img/P_sheet_side.jpg"><figcaption><b>그림 4-94</b>옆모습 걷기용 부품 시트. 팔다리 양 끝이 둥근 원(볼 조인트)이고, 빨간 점이 기준점입니다. 위 마디의 아래 원과 아래 마디의 위 원이 같은 자리에 겹치도록 조립합니다. 치마는 다리와 따로 한 장입니다.</figcaption></figure>
<figure class="shot wide"><img src="img/W_poses.jpg"><figcaption><b>그림 4-95</b>실습 파일의 네 자세. 캐릭터는 왼쪽을 봅니다. 밝은 쪽이 보는 쪽(앞) 팔다리, 어두운 쪽이 먼 쪽(뒤) 팔다리입니다. 15프레임부터는 앞뒤 다리가 바뀌어 같은 네 자세를 한 번 더 합니다.</figcaption></figure>
<div class="why"><b>옆모습 리그가 다른 점</b>① 팔다리를 <b>앞(보는 쪽)·뒤(먼 쪽) 두 벌</b> 만들고 이름 끝에 _앞, _뒤를 붙입니다. 같은 부품을 두 번 불러오면 됩니다. ② 뒤쪽은 Exposure 효과를 −0.7 정도 넣어 어둡게 하고 레이어를 몸통 아래로 내립니다. 쌓는 순서는 위에서부터 앞팔 → 몸통 → 머리 → 치마 → 앞다리 → 뒷다리 → 뒷팔입니다. ③ 한 팔·한 다리 안에서는 위 마디(위팔, 허벅지)를 위에 쌓아 둥근 끝이 아래 마디를 덮게 합니다. ④ 왼쪽을 보는 캐릭터에서 Rotation <b>+</b> 값은 다리를 앞(왼쪽)으로, <b>−</b> 값은 뒤로 보냅니다.</div>
<table><tr><th>자세</th><th>앞다리 허벅지 / 정강이 / 발</th><th>뒷다리 허벅지 / 정강이 / 발</th><th>몸 높이 (전체_조종 Y)</th><th>앞팔 위팔</th></tr>
<tr><td>① 닿기 0f</td><td>20 / −2 / −6 — 뒤꿈치로 착지</td><td>−18 / −18 / 18 — 발끝으로 밂</td><td>485 (보폭이 가장 넓어 낮음)</td><td>−18 (뒤로)</td></tr>
<tr><td>② 내려앉기 4f</td><td>13 / −15 / 0 — 무릎 굽혀 무게 받음</td><td>−11 / −40 / 8 — 발을 뗌</td><td>471</td><td>−9</td></tr>
<tr><td>③ 지나가기 8f</td><td>0 / −4 / 3 — 곧게 서서 몸 받침</td><td>7 / −55 / 20 — 무릎 들고 앞으로</td><td>469</td><td>0 (몸 옆)</td></tr>
<tr><td>④ 올라서기 11f</td><td>−9 / −6 / −6 — 뒤꿈치 듦</td><td>22 / −20 / 10 — 앞으로 뻗음</td><td>452 (가장 높음)</td><td>8</td></tr>
<tr><td>⑤ 닿기 15f</td><td colspan="2">①의 값을 앞다리 ↔ 뒷다리 바꿔 넣음. 19f·23f·26f도 ②~④를 바꿔 넣음</td><td>485</td><td>18 (앞으로)</td></tr>
<tr><td>30f</td><td colspan="4">0f와 같은 값. 이 키가 있어야 반복이 끊기지 않습니다</td></tr>
</table>
<div class="step"><div class="n">1</div><div class="b"><b>앞다리부터.</b> 허벅지_앞, 정강이_앞, 발_앞의 Rotation에 0·4·8·11·15·19·23·26·30프레임 키를 표대로 넣습니다. 15f 이후 값은 표의 ①~④에서 뒷다리 쪽 값을 씁니다.</div></div>
<div class="step"><div class="n">2</div><div class="b"><b>뒷다리는 반 박자 늦게.</b> 앞다리 키를 모두 골라 복사(<span class="k">Ctrl</span>+<span class="k">C</span>)하고, 뒷다리 레이어를 고른 뒤 15f에서 붙여 넣습니다(<span class="k">Ctrl</span>+<span class="k">V</span>). 30f를 넘어간 키는 30프레임 앞으로 옮겨 0~30f 안에 둡니다.</div></div>
<div class="step"><div class="n">3</div><div class="b"><b>팔은 다리와 반대로.</b> 앞다리가 앞으로 나갈 때 앞팔은 뒤로 갑니다. 위팔 −18 → 0 → 18 → 0 → −18. 아래팔은 2프레임, 손은 3프레임 늦게 따라가게 하면(오버랩) 팔이 막대기처럼 보이지 않습니다.</div></div>
<div class="step"><div class="n">4</div><div class="b"><b>몸 높이 맞추기.</b> 전체_조종 Position Y를 자세마다 바꿔 <b>바닥에 닿은 발이 땅선에 딱 붙게</b> 합니다. 발이 땅을 뚫으면 Y를 줄이고, 뜨면 늘립니다. 몸통은 −2 ~ −5°로 살짝 앞으로 기울이고, 머리는 반대로 1 ~ 3° 들어 시선을 앞에 둡니다.</div></div>
<div class="step"><div class="n">5</div><div class="b"><b>치마는 따라오게.</b> 치마는 전체_조종의 자식으로 두고, 두 허벅지 각도를 조금 늦게 받아 반대로 흔들리게 합니다(아래 익스프레션). 이렇게 '따라 움직이는 부분'을 <b>2차 동작</b>이라고 합니다.</div></div>
<div class="step"><div class="n">6</div><div class="b"><b>반복과 이동.</b> 키가 있는 모든 속성에 <span class="mono">loopOut("cycle")</span>을 넣습니다. 제자리걸음을 앞으로 걸어가게 하려면 전체_조종 Position X를 1초에 보폭 두 배만큼 옮깁니다. 땅에 닿은 발이 화면에서 멈춰 보이는 속도가 맞는 값입니다.</div></div>
<div class="prompt"><span class="lbl">EXPRESSION · 걷기 반복, 치마, 이동</span>// 키가 있는 Rotation, Position 모두 — 0~1초를 계속 반복<br>loopOut("cycle");<br>// 치마 Rotation — 두 다리를 0.06초 늦게 따라 반대로 흔들림<br>-(thisComp.layer("허벅지_앞").transform.rotation.valueAtTime(time-0.06)<br>&nbsp;&nbsp;+ thisComp.layer("허벅지_뒤").transform.rotation.valueAtTime(time-0.06)) * 0.15;<br>// 전체_조종 Position — 반복하면서 왼쪽으로 걸어감 (숫자는 보폭에 맞게)<br>loopOut("cycle") + [-time*400, 0];</div>
<div class="stuck"><b>막혔을 때</b>발이 미끄러지듯 보인다 → 이동 속도가 보폭과 안 맞습니다. 400을 조금씩 바꿔 땅에 닿은 발이 멈춰 보이는 값을 찾습니다. 반복할 때 툭 끊긴다 → 0f와 30f 키 값이 다릅니다. 다리가 꼬여 보인다 → 뒷다리가 앞다리와 같은 밝기이거나 레이어 순서가 바뀌었습니다. 무릎에 틈이 보인다 → 허벅지를 정강이 위에 쌓았는지, 두 원의 중심이 기준점에 맞는지 봅니다. 걸음이 로봇 같다 → 키를 모두 골라 <span class="k">F9</span>(Easy Ease)를 주고, 아래팔·손의 오버랩을 늘립니다.</div>
<div class="tip"><b>프레임 수 바꾸기</b>24fps라면 한 걸음 12프레임으로 0·3·6·9·12f에 같은 네 자세를 둡니다. 느긋한 걸음은 한 걸음 18~20프레임, 뛰기는 8프레임 안팎이며 두 발이 모두 뜨는 순간이 생깁니다.</div>
"""
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
