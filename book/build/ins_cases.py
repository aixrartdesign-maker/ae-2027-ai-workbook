# -*- coding: utf-8 -*-
# 2026-11-26 (4): real Lighting / Motion Control results in ch7, five Claude build cases in ch10
import os

MC_DONE = os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'img', 'CAPTURE_7-6c_MotionControl_result.jpg'))

LIGHT_OLD_START = '<h2>7-3 Change Lighting — 조명만 바꾸기 (설정 화면)</h2>'
TIP_MARK = '<div class="tip"><b>순서 팁</b>날씨와 시간대를'

LIGHT = '''<h2><span class="tag t1">따라 하기</span> 7-3 Change Lighting — 조명만 바꾸기</h2>
<div class="why"><b>언제 쓰나</b>역광이나 얼굴 그늘을 고칠 때, 여러 컷의 빛 방향을 맞출 때. 날씨·시간은 그대로 두고 빛만 바꿉니다.</div>
<div class="step"><div class="n">1</div><div class="b">6장의 걷는 인물 컴포지션을 열고 타임라인에서 영상 레이어를 선택합니다. 패널 홈의 <b>Scene → Change Lighting</b>을 누르면 선택한 클립이 바로 들어옵니다. 다른 클립이 들어오면 원하는 컴포지션을 먼저 열고 다시 엽니다.</div></div>
<div class="step"><div class="n">2</div><div class="b">아래 막대에서 쓸 구간을 고릅니다(최대 14초). 이 클립은 5.1초 전체를 썼습니다.</div></div>
<div class="step"><div class="n">3</div><div class="b"><b>Presets</b>에서 빛을 고릅니다. Purple, Backlight, Rainbow, Golden Hour, Paparazzi Flash, Spotlight 여섯 가지입니다. 여기서는 해 질 녘 역광인 <b>Golden Hour</b>를 골랐습니다.</div></div>
<div class="step"><div class="n">4</div><div class="b"><b>Generate</b>. 약 3분 뒤 결과가 패널 생성 화면에 뜨고, 왼쪽 위 ↓로 내려받아 컴포지션에 넣습니다.</div></div>
<figure class="shot half"><img src="img/CAPTURE_7-5_Lighting_GoldenHour.jpg"><figcaption><b>그림 7-5</b> Video Lighting 설정. 구간 5.1초, 프리셋 Golden Hour. 버튼은 68크레딧으로 보였지만 실제 차감은 <b>22.5크레딧</b>이었습니다.</figcaption></figure>
<figure class="shot half"><img src="img/CAPTURE_7-5b_Lighting_result.jpg"><figcaption><b>그림 7-6</b> 결과 화면. 오른쪽 위에서 해가 비치고 벽돌과 머리카락 가장자리가 주황빛으로 바뀌었습니다.</figcaption></figure>
<figure class="shot"><img src="img/CAPTURE_7-5c_Lighting_before_after.jpg"><figcaption><b>그림 7-7</b> 원본(왼쪽)과 Golden Hour(오른쪽). 빛은 잘 바뀌었지만 결과가 <b>1:1로 다시 그려지면서 화면이 더 넓게 잡혔습니다</b>. 원본 구도를 지켜야 한다면 결과를 원본 크기에 맞춰 Scale을 키우거나, 6장의 Reframe으로 비율을 다시 맞춥니다.</figcaption></figure>
'''

MOTION_DONE = '''<div class="step"><div class="n">4</div><div class="b">다시 시도: 캐릭터를 사람 비율의 전신 이미지(노란 우비 캐릭터, 14장 14-6의 고정 설명문으로 생성)로 바꾸고, 동작은 6장의 걷는 인물 영상을 썼습니다. 패널에서 이미지 끌어 놓기가 되지 않아, 같은 기능을 Claude에서 힉스필드 MCP로 실행했습니다.</div></div>
<div class="prompt"><span class="lbl">PROMPT · Claude에게</span>힉스필드 Motion Control로 걷는 인물 영상의 동작을 노란 우비 캐릭터 이미지에 옮겨 줘. 720p, 만들기 전에 크레딧부터 알려 줘.</div>
<figure class="shot"><img src="img/CAPTURE_7-6c_MotionControl_result.jpg"><figcaption><b>그림 7-10</b> 1초와 4초 장면, 각각 원본(왼쪽)과 결과(오른쪽). 인물만 노란 우비 캐릭터로 바뀌고, 걷는 동작·카메라 움직임·배경 구도는 원본을 따랐습니다. 벽 질감은 새로 그려졌습니다. 1280×720 · <b>35크레딧</b>.</figcaption></figure>
'''
MOTION_PENDING = ''

MOTION = '''<h2><span class="tag t1">따라 하기</span> 7-4 Motion Control — 동작 옮기기</h2>
<div class="why"><b>언제 쓰나</b>춤·제스처를 그대로 다른 인물에게 입힐 때. 참고 동작 영상과 인물 이미지 두 가지만 있으면 됩니다. 실존 인물 사진은 동의 없이 쓰지 않습니다.</div>
<div class="step"><div class="n">1</div><div class="b">패널 홈 <b>Scene → Motion Control</b>. 왼쪽 <b>Motion</b> 칸을 눌러 프리셋 동작을 고르거나 <b>Custom motion</b>으로 내 영상을 올립니다.</div></div>
<div class="step"><div class="n">2</div><div class="b">캐릭터 이미지를 애펙에 먼저 불러온 뒤(Ctrl+I), Project 패널에서 오른쪽 <b>Character</b> 칸으로 끌어다 놓습니다. 끌어 놓기가 되지 않으면 칸을 눌러 파일을 직접 고릅니다.</div></div>
<div class="step"><div class="n">3</div><div class="b">Quality(720p/1080p)와 Background(Image: 캐릭터 이미지의 배경 / Video: 참고 영상의 배경)를 정하고 <b>Generate</b>. 모델은 Kling 3.0 Motion Control, 9:16으로 만들어집니다.</div></div>
<figure class="shot half"><img src="img/CAPTURE_7-6_MotionControl_dubu.jpg"><figcaption><b>그림 7-8</b> 프리셋 춤 동작 + 14장의 두부 로봇 캐릭터. 720p · Image 배경 · <b>25크레딧</b>.</figcaption></figure>
<figure class="shot half"><img src="img/CAPTURE_7-6b_MotionControl_blocked.jpg"><figcaption><b>그림 7-9</b> 결과는 “NSFW Content”로 막혔고 크레딧은 돌려받았습니다. 안전 필터나 처리 오류로 막힌 것으로, 팔다리가 막대인 로봇처럼 사람 몸과 구조가 다른 캐릭터는 동작을 옮기지 못하는 경우가 많습니다.</figcaption></figure>
''' + '%MOTION_RESULT%' + '''<div class="note"><b>실패도 기록합니다</b>막힌 생성은 크레딧이 환불되지만 시간은 듭니다. 동작 옮기기는 <b>머리·몸통·팔다리가 사람과 같은 비율</b>인 캐릭터, 전신이 잘 보이는 정면 이미지, 동작이 단순한 참고 영상일 때 잘 됩니다. 로봇처럼 구조가 다른 캐릭터는 14장처럼 애펙에서 부위별로 부모를 걸어 직접 움직이는 편이 확실합니다.</div>
'''

CASES = '''<h2>10-3 Claude 제작 사례 다섯 가지 — 말 한 번으로 시작하기</h2>
<p>아래 다섯 가지는 이 책을 쓰면서 Claude에게 브리지로 실제로 시킨 것입니다. 모두 크레딧이 들지 않았고, 결과는 이름 붙은 레이어와 키프레임으로 남아 손으로 고칠 수 있습니다. 각 사례 끝의 “고친 점”은 처음 결과에서 실제로 문제가 된 부분입니다. AI가 만든 첫 결과를 그대로 쓰지 말고 콘택트 시트로 한 번 확인하는 습관을 들이세요.</p>
<table>
<tr><th style="width:8%">#</th><th style="width:24%">사례</th><th style="width:14%">크기·길이</th><th>배울 점</th></tr>
<tr><td>1</td><td>막대그래프 인포그래픽</td><td>1920×1080 · 6초</td><td>Anchor Point를 막대 아래로 옮겨 아래에서 위로 자라게 하기</td></tr>
<tr><td>2</td><td>행사 카운트다운</td><td>1920×1080 · 6초</td><td>같은 동작을 1초 간격으로 반복하는 키프레임</td></tr>
<tr><td>3</td><td>쇼츠 세로 카드</td><td>1080×1920 · 6초</td><td>부모 레이어 하나로 카드 전체를 함께 움직이기</td></tr>
<tr><td>4</td><td>엔딩 크레딧</td><td>1920×1080 · 8초</td><td>일정한 속도(선형)로 올라가는 스크롤</td></tr>
<tr><td>5</td><td>구독 버튼 클릭</td><td>1920×1080 · 5초</td><td>눌림 → 색 바뀜 → 물결로 이어지는 짧은 상호작용</td></tr>
</table>

<h3>사례 1. 막대그래프 인포그래픽</h3>
<div class="prompt"><span class="lbl">PROMPT · Claude에게</span>/use-after-effects<br>
1920×1080, 6초 컴포지션 "Claude사례1_막대그래프"를 만들어 줘. 남색 배경에 제목 "월별 조회수", 부제 "단위: 만 회 · 예시 데이터". 9~12월 막대 네 개(26, 38, 50, 64)가 0.25초씩 차례로 아래에서 위로 자라고, 막대가 다 자라면 위에 숫자가 살짝 올라오며 나타나게. 마지막 달만 연두색으로 강조. 레이어 이름은 한글로.</div>
<figure class="shot wide"><img src="img/CLAUDE_CASE_1.jpg"><figcaption><b>그림 10-4</b> 0.4초 · 1.3초 · 1.8초 · 3초. 막대가 왼쪽부터 차례로 자라고, 숫자는 막대가 다 자란 뒤에 나타납니다.</figcaption></figure>
<div class="tip"><b>고친 점</b>막대가 가운데에서 위아래로 동시에 커지지 않게, Claude가 각 막대의 <b>Anchor Point를 아래 끝</b>(높이의 절반만큼 아래)으로 옮긴 뒤 Scale Y를 0→100으로 키웠습니다. 손으로 할 때는 Pan Behind Tool(Y)로 기준점을 막대 아래로 끌어 놓습니다. 처음 시도에서 글꼴 이름을 “Malgun Gothic”처럼 띄어 써서 오류가 났고, PostScript 이름 <span class="mono">MalgunGothic</span>, <span class="mono">MalgunGothicBold</span>로 고쳤습니다.</div>

<h3>사례 2. 행사 카운트다운</h3>
<div class="prompt"><span class="lbl">PROMPT · Claude에게</span>1920×1080, 6초 컴포지션 "Claude사례2_카운트다운". 보라색 원형 링 안에서 5, 4, 3, 2, 1이 1초마다 크게 나타났다 작아지며 바뀌고, 숫자가 바뀔 때마다 링이 살짝 튀게. 5초에 연두색 "START"가 톡 튀어나오며 끝나. 아래에 작은 글씨 "행사가 곧 시작됩니다".</div>
<figure class="shot wide"><img src="img/CLAUDE_CASE_2.jpg"><figcaption><b>그림 10-5</b> 0.5초 · 2.5초 · 4.5초 · 5.6초. 링은 바깥 원(보라)과 안쪽 원(배경색) 두 개를 겹쳐 만들었습니다.</figcaption></figure>
<div class="tip"><b>고친 점</b>처음 결과에서는 START 글자(150pt)가 링보다 넓어 테두리와 겹쳤습니다. “START 글자를 링 안에 들어가게 줄여 줘”라고 하자 100pt로 줄이고 위치를 다시 맞췄습니다. 숫자 하나는 0.12초에 나타나고 0.85~1초에 사라지는 같은 패턴이므로, 손으로 고칠 때도 숫자 레이어 하나의 키프레임을 복사해 1초씩 옮겨 붙이면 됩니다.</div>

<h3>사례 3. 쇼츠 세로 카드</h3>
<div class="prompt"><span class="lbl">PROMPT · Claude에게</span>1080×1920 쇼츠용 6초 컴포지션 "Claude사례3_쇼츠카드". 보라 배경 아래에서 흰 카드가 튀어 올라와 멈추고, 카드 안에 연두색 NEW 태그, 제목 "애펙 2027 / AI와 30초 만에", 본문 두 줄, 남색 "자세히 보기 →" 버튼이 차례로 나타나게. 버튼은 3.5초에 한 번 살짝 커졌다 돌아와. 카드 안 요소는 모두 카드에 부모로 걸어 줘.</div>
<figure class="shot wide"><img src="img/CLAUDE_CASE_3.jpg"><figcaption><b>그림 10-6</b> 0.35초 · 0.9초 · 1.6초 · 3초. 카드 위치 키는 3개뿐이고, 안의 글자와 버튼은 부모(카드)를 따라 함께 올라옵니다.</figcaption></figure>
<div class="tip"><b>고친 점</b>처음에는 제목과 본문을 왼쪽 정렬로 만들었더니 글자가 카드 왼쪽 밖으로 삐져나왔습니다(애펙 텍스트의 기준점 위치 문제). 가운데 정렬로 다시 만들고, 부모를 건 뒤에는 위치를 <b>카드 기준 좌표</b>(제목 0, −200 / 본문 0, 60)로 넣었습니다. 부모가 움직이는 중에 부모를 걸면 자식 위치가 엉뚱하게 바뀌므로, 부모는 애니메이션을 넣기 전에 거는 것이 안전합니다. 쇼츠는 위아래에 앱 버튼이 겹치므로 중요한 글자는 화면 가운데 70% 안에 둡니다.</div>

<h3>사례 4. 엔딩 크레딧</h3>
<div class="prompt"><span class="lbl">PROMPT · Claude에게</span>1920×1080, 8초 컴포지션 "Claude사례4_엔딩크레딧". 검은 배경에 "만든 사람들" 제목과 역할·이름 목록이 아래에서 위로 일정한 속도로 올라가게. 맨 끝 줄은 "이 영상의 일부 장면은 AI로 만들었습니다". 이름은 예시 이름으로, 줄 간격은 넉넉하게.</div>
<figure class="shot wide"><img src="img/CLAUDE_CASE_4.jpg"><figcaption><b>그림 10-7</b> 1.5초 · 3.2초 · 4.8초 · 6.4초. 본문 레이어 하나에 위치 키 두 개(0초, 8초)만 있고, 제목은 본문에 부모로 붙어 함께 올라갑니다.</figcaption></figure>
<div class="tip"><b>고친 점</b>크레딧은 속도가 일정해야 읽기 편하므로 위치 키에 <b>이징을 넣지 않았습니다</b>(선형). 처음엔 줄 간격이 좁아 “줄 간격 넓혀 줘”라고 했고, Leading 72px로 바뀌었습니다. 다른 사례처럼 마무리 도구(finalize)로 이징을 자동 보정하면 선형 키가 부드러운 키로 바뀌므로, 크레딧에는 쓰지 않습니다. AI로 만든 장면이 있으면 크레딧에 밝히는 습관도 함께 들이세요(29장).</div>

<h3>사례 5. 구독 버튼 클릭</h3>
<div class="prompt"><span class="lbl">PROMPT · Claude에게</span>1920×1080, 5초 컴포지션 "Claude사례5_구독버튼". 밝은 배경 가운데 빨간 둥근 "구독" 버튼이 톡 튀어나오고, 동그란 커서가 오른쪽 아래에서 다가와 1.5초에 누르면 버튼이 살짝 눌렸다가 회색 "구독중" 버튼으로 바뀌고 빨간 물결이 퍼지게. 커서는 3초쯤 빠져나가.</div>
<figure class="shot wide"><img src="img/CLAUDE_CASE_5.jpg"><figcaption><b>그림 10-8</b> 0.3초 · 1.2초 · 1.75초 · 2.8초. 빨강·회색 버튼 두 장을 겹쳐 두고 불투명도로 바꿉니다.</figcaption></figure>
<div class="tip"><b>고친 점</b>“구독중 ✓”의 체크 기호가 맑은 고딕에 없어 빈칸으로 나왔습니다. 기호를 빼고 “구독중”만 남겼습니다. 기호가 필요하면 셰이프로 체크 모양을 그리거나 기호가 있는 글꼴을 씁니다. 커서는 셰이프 원으로 대신했는데, 실제 마우스 모양이 필요하면 아이콘 이미지를 불러와 같은 위치 키를 붙입니다.</div>
<div class="note"><b>다섯 사례에서 공통으로 배운 것</b>① 레이어 이름을 한글로 정해 달라고 하면 나중에 “막대_12월만 초록으로”처럼 이름으로 고칠 수 있습니다. ② 결과는 반드시 콘택트 시트(여러 시점 한 장)로 확인합니다. ③ 글꼴은 PostScript 이름으로, 기호는 글꼴에 있는지 확인합니다. ④ 부모는 움직임을 넣기 전에 겁니다.</div>
'''


def apply9(S):
    a = S.find(LIGHT_OLD_START)
    b = S.find(TIP_MARK, a)
    assert a > 0 and b > a
    motion = MOTION.replace('%MOTION_RESULT%', MOTION_DONE if MC_DONE else MOTION_PENDING)
    S = S[:a] + LIGHT + motion + S[b:]
    k = S.find('<div class="ch-no" id="ch-10">')
    if k < 0:
        k = S.find('<div class="ch-no">CHAPTER 10</div>')
    assert k > 0
    j = S.find('<h2>이 장 점검</h2>', k)
    S = S[:j] + CASES + '\n' + S[j:]
    return S
