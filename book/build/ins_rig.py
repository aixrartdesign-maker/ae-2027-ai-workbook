# -*- coding: utf-8 -*-
# 4-3 관절 리그 / 13-9 카메라+널 삽입 (mk13c.py 맨 앞에서 실행)
RIG_SVG=open('/home/claude/book/img/R_rig.svg',encoding='utf-8').read()
SEC4='''
<h2><span class="tag t1">따라 하기</span> 4-3 사람 몸 움직이기 — 관절에 부모 걸기</h2>
<p>종이 인형처럼 몸을 마디별 레이어로 나누고, 마디마다 <b>기준점(Anchor Point)</b>을 관절로 옮긴 뒤, <b>몸에 가까운 쪽을 부모</b>로 잇습니다. 그러면 어깨만 돌려도 팔 전체가, 골반만 움직여도 온몸이 따라옵니다. 이렇게 짠 뼈대를 <b>리그(rig)</b>라고 합니다. 실습 파일의 컴포지션 <span class="mono">04-3_캐릭터리그</span>에 레이어 19개짜리 리그가 들어 있습니다.</p>
<div class="why"><b>세 가지 규칙</b>① <b>나누기</b> — 레이어 하나는 관절과 관절 사이 한 마디입니다. 위팔과 아래팔을 한 장에 그리면 팔꿈치가 굽혀지지 않습니다. ② <b>기준점</b> — 기준점은 그 마디의 <b>몸 쪽 관절</b>에 둡니다. 위팔은 어깨, 아래팔은 팔꿈치, 손은 손목입니다. ③ <b>부모</b> — 몸 쪽 마디가 부모입니다. 손 → 아래팔 → 위팔 → 몸통 → 골반 → 전체_조종(널) 순서로 겁니다.</div>
<figure class="shot dia-fig">'''+RIG_SVG+'''<figcaption><b>그림 4-91</b>왼쪽: 빨간 점이 각 마디의 기준점(관절) 위치입니다. 오른쪽: 부모 관계. 들여 쓴 레이어가 바로 위 레이어의 자식입니다.</figcaption></figure>
<table><tr><th>레이어</th><th>기준점 위치</th><th>부모</th><th>주로 움직이는 속성</th></tr>
<tr><td>전체_조종 (널)</td><td>골반 가운데</td><td>없음</td><td>Position — 화면 이동, 걸을 때 위아래 통통</td></tr>
<tr><td>골반</td><td>골반 가운데</td><td>전체_조종</td><td>Rotation — 엉덩이 흔들기</td></tr>
<tr><td>몸통</td><td>허리(아래 끝 가운데)</td><td>골반</td><td>Rotation — 숙이기 · Scale Y — 숨쉬기</td></tr>
<tr><td>머리</td><td>목(아래 끝 가운데)</td><td>몸통</td><td>Rotation — 끄덕임, 갸웃</td></tr>
<tr><td>눈 · 입 · 눈썹</td><td>각자 가운데</td><td>머리</td><td>Scale — 깜빡임, 입 벌림 · Position — 눈동자 방향</td></tr>
<tr><td>위팔 (좌우)</td><td>어깨</td><td>몸통</td><td>Rotation</td></tr>
<tr><td>아래팔 (좌우)</td><td>팔꿈치</td><td>위팔</td><td>Rotation</td></tr>
<tr><td>손 (좌우)</td><td>손목</td><td>아래팔</td><td>Rotation</td></tr>
<tr><td>허벅지 (좌우)</td><td>엉덩이 관절</td><td>골반</td><td>Rotation</td></tr>
<tr><td>정강이 (좌우)</td><td>무릎</td><td>허벅지</td><td>Rotation</td></tr>
<tr><td>발 (좌우)</td><td>발목</td><td>정강이</td><td>Rotation</td></tr>
</table>
<div class="step"><div class="n">1</div><div class="b"><b>마디 그리기.</b> 셰이프, 일러스트레이터, 포토샵 레이어 무엇이든 좋습니다. 관절 쪽 끝을 둥글게, 조금 길게 그리면 굽혀도 틈이 보이지 않습니다. 레이어 이름은 <span class="mono">위팔_왼</span>처럼 부위와 방향을 함께 씁니다.</div></div>
<div class="step"><div class="n">2</div><div class="b"><b>기준점을 관절로.</b> 레이어를 고르고 <b>Pan Behind(Anchor Point) 도구</b>(<span class="k">Y</span>)로 기준점을 관절까지 끕니다. 이 도구는 그림은 그대로 두고 기준점만 옮깁니다. 숫자로 하려면 <span class="k">A</span>를 눌러 Anchor Point를 바꾸고 Position도 같은 만큼 맞춥니다. 예: 높이 130px인 위팔은 Anchor <span class="mono">0, −65</span>가 위쪽 끝(어깨)입니다.</div></div>
<div class="step"><div class="n">3</div><div class="b"><b>부모 걸기.</b> 끝에서 몸 쪽으로 차례로 겁니다. 손의 소용돌이 아이콘(Pick Whip)을 아래팔로, 아래팔은 위팔로, 위팔은 몸통으로 끕니다. 눈·입처럼 같은 부모를 가질 레이어는 여러 개를 함께 고른 뒤 한 레이어의 Parent 칸만 바꾸면 한꺼번에 걸립니다.</div></div>
<div class="step"><div class="n">4</div><div class="b"><b>앞뒤 순서 정하기.</b> 부모와 쌓는 순서는 따로입니다. 레이어 패널에서 위에 있을수록 화면 앞이므로 팔은 몸통 위, 다리는 골반 아래에 둡니다. 몸 뒤로 가는 팔은 몸통 아래로 내립니다.</div></div>
<div class="step"><div class="n">5</div><div class="b"><b>Rotation만 움직이기.</b> 이제 각 마디는 Rotation 하나면 됩니다. 어깨를 먼저 돌리고, 팔꿈치·손목은 2~4프레임 늦게 따라가게 하면 채찍처럼 자연스럽습니다. 이것을 <b>오버랩(follow-through)</b>이라고 합니다.</div></div>
<figure class="shot"><img src="img/R_parent.jpg"><figcaption><b>그림 4-92</b>실제 Parent &amp; Link 칸. 손_오의 부모는 4번 아래팔_오, 아래팔_오는 6번 위팔_오, 위팔은 12번 몸통, 몸통은 13번 골반, 골반은 1번 전체_조종입니다. 다리는 허벅지 → 골반으로 이어집니다.</figcaption></figure>
<figure class="shot wide"><img src="img/R_poses.jpg"><figcaption><b>그림 4-93</b>Rotation만 바꾼 세 자세. 오른팔은 들어서 흔들고, 다리는 제자리걸음, 눈은 2.2초마다 깜빡이고, 입은 말하듯 벌어집니다. 골반 옆 빨간 네모는 렌더에 나오지 않는 널(전체_조종)입니다.</figcaption></figure>
<div class="prompt"><span class="lbl">EXPRESSION · 실습 파일의 반복 동작</span>// 위팔_오 Rotation — 팔을 들고 작게 흔들기<br>-130 + Math.sin(time*Math.PI*4)*8;<br>// 아래팔_오 Rotation — 0.5만큼 늦게 따라감 = 오버랩<br>-35 + Math.sin(time*Math.PI*4 - 0.5)*28;<br>// 허벅지_왼 Rotation — 한쪽 다리만 들기 (오른쪽은 부호 반대)<br>Math.max(0, Math.sin(time*Math.PI*2))*14;<br>// 눈 Scale — 깜빡임<br>(time % 2.2 &lt; 0.12) ? [100, 12] : [100, 100];<br>// 입 Scale — 말하는 입<br>[100, 100 + Math.abs(Math.sin(time*9))*220];</div>
<table><tr><th>동작</th><th>어디에 무엇을 거나</th></tr>
<tr><td>걷기</td><td>전체_조종 Position X로 앞으로, Y로 한 걸음마다 위아래. 허벅지·정강이 Rotation은 좌우 반대로, 팔은 같은 쪽 다리와 반대로 흔듭니다.</td></tr>
<tr><td>손 흔들기</td><td>위팔 Rotation으로 팔을 든 채 고정, 아래팔과 손 Rotation만 반복합니다.</td></tr>
<tr><td>고개 끄덕 · 갸웃</td><td>머리 Rotation. 기준점이 목에 있어야 목을 축으로 움직입니다.</td></tr>
<tr><td>숨쉬기</td><td>몸통 Scale Y 100 → 102%. 기준점이 허리라서 위로만 부풉니다.</td></tr>
<tr><td>표정</td><td>눈 Scale Y(깜빡임), 눈동자 Position(보는 방향), 입 Scale이나 Path(말하기). 얼굴 부품은 모두 머리의 자식입니다.</td></tr>
<tr><td>점프</td><td>전체_조종 Position Y로 뛰고, 착지 순간 골반을 몇 픽셀 내려 무릎이 눌리는 느낌을 줍니다.</td></tr>
</table>
<div class="stuck"><b>막혔을 때</b>엉뚱한 곳을 중심으로 돈다 → 기준점이 가운데 있습니다. <span class="k">Y</span> 도구로 관절에 옮기세요. 부모를 걸자 부위가 튀어 간다 → <span class="k">Shift</span>를 누른 채 Pick Whip하면 자식이 부모 위치로 옮겨집니다. 그냥 끌면 제자리에 있습니다. 자식 크기가 같이 변한다 → 부모의 Scale을 바꾼 탓입니다. 크기는 전체_조종에서만 바꿉니다. 팔이 몸 뒤로 숨는다 → 부모가 아니라 레이어 순서 문제입니다.</div>
<div class="tip"><b>더 나아가기</b>관절이 많은 캐릭터는 무료 스크립트 <b>Duik</b>이 IK(손끝을 끌면 팔 전체가 따라 굽는 방식)를 만들어 줍니다. 몸 전체를 고무처럼 휘게 하려면 5-6의 퍼펫 핀을 함께 씁니다.</div>
'''
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
    for old,new in [('4-6 블렌딩','4-7 블렌딩'),('4-5 트랙 매트','4-6 트랙 매트'),('4-4 마스크','4-5 마스크'),('4-3 묶기','4-4 묶기')]:
        assert S.count(old)>=1,old; S=S.replace(old,new)
    S=S.replace('<h2><span class="tag t1">따라 하기</span> 4-4 묶기(프리컴포즈)</h2>',SEC4.strip()+'\n\n<h2><span class="tag t1">따라 하기</span> 4-4 묶기(프리컴포즈)</h2>',1)
    i=S.find('<div class="ch-no">CHAPTER 13'); j=S.find('<h2>이 장 점검</h2>',i)
    S=S[:j]+SEC13.strip()+'\n'+S[j:]
    S=S.replace('카메라를 널에 페어런팅하면, 널을 돌리는 것만으로 부드러운 궤도 촬영이 됩니다.','카메라를 널에 페어런팅하면, 널을 돌리는 것만으로 부드러운 궤도 촬영이 됩니다(13-9).',1)
    S=S.replace('빛만 남습니다(4-6)','빛만 남습니다(4-7)')
    return S
