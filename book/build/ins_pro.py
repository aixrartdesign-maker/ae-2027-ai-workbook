# -*- coding: utf-8 -*-
# 2026-11-26 (2): rendering formats/alpha/sequences, .aep import, templates, layer hiding,
# 3D axes & PBR maps, Element 3D, plugin map, pro pipeline, cinematic title project.
from ins_more import st, steps, K, M, P


# ---------------------------------------------------------------- ch.2 layer hiding
HIDE = '''
<h2><span class="tag t1">따라 하기</span> 2-6 레이어 숨기기와 정리 — Shy, Solo, Lock, Guide</h2>
<p>레이어가 수십 개가 되면 “보이지 않게 하기”에도 종류가 있다는 것을 알아야 합니다. <b>화면에서 숨기기</b>, <b>렌더에서 빼기</b>, <b>타임라인 목록에서만 숨기기</b>는 서로 다른 스위치입니다.</p>
<table>
<tr><th style="width:24%">스위치·기능</th><th style="width:16%">화면</th><th style="width:16%">렌더</th><th>쓰는 때</th></tr>
<tr><td>눈(Video)</td><td>숨김</td><td>빠짐</td><td>잠깐 꺼 두고 비교할 때. 꺼 둔 채 잊고 렌더하는 실수가 가장 흔합니다</td></tr>
<tr><td>Solo</td><td>이 레이어만</td><td>솔로 상태 그대로</td><td>한 레이어만 보며 고칠 때. 솔로를 켠 채 렌더하면 그 레이어만 나옵니다</td></tr>
<tr><td>Lock(자물쇠)</td><td>보임</td><td>나옴</td><td>다 만든 레이어를 실수로 움직이지 않게</td></tr>
<tr><td>Shy(수줍은 사람)</td><td>보임</td><td>나옴</td><td>타임라인 목록에서만 숨겨 작업 중인 레이어만 보기</td></tr>
<tr><td>Guide Layer</td><td>보임</td><td>기본은 빠짐</td><td>참고 이미지, 안내 격자, 콘티 그림</td></tr>
<tr><td>fx 스위치</td><td>효과만 끔</td><td>효과 빠짐</td><td>무거운 효과를 끄고 가볍게 작업할 때</td></tr>
</table>
''' + steps(
    '타임라인 아래 <b>Toggle Switches / Modes</b>(%s)로 스위치 칸을 엽니다. 레이어 줄의 작은 사람 모양 칸이 <b>Shy</b>입니다.' % K('F4'),
    '숨길 레이어들(완성된 배경, 조명 널 등)의 Shy 칸을 클릭합니다. 아이콘이 납작하게 바뀝니다.',
    '타임라인 맨 위 오른쪽의 <b>Hide All Shy Layers</b> 버튼(같은 사람 모양)을 누릅니다. 표시한 레이어가 목록에서 사라집니다. 화면과 렌더에는 그대로 나옵니다.',
    '다시 보려면 같은 버튼을 한 번 더 누릅니다.',
    '참고 이미지 레이어는 고른 뒤 <b>Layer → Guide Layer</b>를 누릅니다. 이름 앞에 파란 표시가 붙고, 렌더하면 나오지 않습니다(Render Settings의 Guide Layers 항목으로 켤 수도 있습니다).',
) + '''
<table>
<tr><th style="width:26%">단축키·기능</th><th>하는 일</th></tr>
<tr><td><span class="k">U</span> / <span class="k">U</span><span class="k">U</span></td><td>키프레임이 있는 속성만 / 기본값에서 바꾼 속성만 펼치기. 남의 프로젝트 읽을 때 첫 동작</td></tr>
<tr><td><span class="k">E</span><span class="k">E</span></td><td>익스프레션이 들어간 속성만 펼치기</td></tr>
<tr><td><span class="k">Ctrl+Shift+H</span></td><td>컴포지션 창의 레이어 테두리·핸들·경로·카메라 선을 숨겼다 보이기. 화면을 깨끗하게 보며 판단할 때</td></tr>
<tr><td>라벨 색 → Select Label Group</td><td>레이어 왼쪽 색 칸을 클릭해 <b>Select Label Group</b>을 고르면 같은 색 레이어가 한꺼번에 선택됩니다. 자막은 노랑, 효과는 보라처럼 정해 두면 여러 개를 한 번에 숨기거나 옮깁니다</td></tr>
<tr><td>타임라인 검색칸</td><td>타임라인 위 돋보기 칸에 “Opacity”나 레이어 이름을 치면 그것만 남깁니다</td></tr>
</table>
<div class="warn"><b>렌더 전 점검</b>꺼 둔 눈, 켜 둔 Solo, 꺼 둔 fx는 렌더 결과를 바꿉니다. 렌더 직전에 타임라인 맨 위 스위치 줄을 한 번 훑어보는 습관을 들이세요. 23장의 AI Assistant에게 “꺼진 레이어와 솔로 상태를 찾아 줘”라고 시켜도 됩니다.</div>
'''

# ---------------------------------------------------------------- ch.13 3D axes, PBR, Element 3D
AXES = '''
<h2>13-10 축과 회전 완전 정리 — X·Y·Z, Orientation, 단축키</h2>
<p>3D가 어렵게 느껴지는 이유의 대부분은 축입니다. 애펙의 축은 세 개이고, 화면에 보이는 색 화살표와 같습니다.</p>
<table>
<tr><th style="width:14%">축</th><th style="width:16%">화살표 색</th><th style="width:28%">Position에서</th><th>Rotation에서 (그 축을 꼬챙이로 삼아 돎)</th></tr>
<tr><td>X</td><td>빨강</td><td>좌우. 오른쪽이 +</td><td>앞뒤로 끄덕이기. 바닥에 눕히기, 문이 위로 열리기</td></tr>
<tr><td>Y</td><td>초록</td><td>위아래. <b>아래쪽이 +</b>(수학과 반대)</td><td>좌우로 도리도리. 카드 뒤집기, 회전문</td></tr>
<tr><td>Z</td><td>파랑</td><td>깊이. 멀어질수록 +</td><td>시계바늘처럼 기울이기(2D 회전과 같음)</td></tr>
</table>
<p><b>Orientation과 X·Y·Z Rotation의 차이</b>: 3D 레이어에는 회전 값이 두 벌 있습니다. <b>Orientation</b>은 “어느 방향을 보고 있나”를 정하는 값으로, 키프레임을 걸면 가장 짧은 길로만 돌아 360°를 넘는 회전이 안 됩니다. <b>X·Y·Z Rotation</b>은 축마다 따로 키프레임을 걸 수 있고 “2x+30°”처럼 여러 바퀴도 됩니다. 처음 놓는 각도는 Orientation, 움직임은 Rotation으로 나누면 꼬이지 않습니다.</p>
<table>
<tr><th style="width:30%">단축키·도구</th><th>하는 일</th></tr>
<tr><td><span class="k">P</span> <span class="k">A</span> <span class="k">S</span> <span class="k">R</span></td><td>Position, Anchor Point, Scale, Rotation 펼치기. 3D 레이어에서 <span class="k">R</span>은 Orientation과 X·Y·Z Rotation을 함께 엽니다</td></tr>
<tr><td><span class="k">Shift</span>+속성 키</td><td>지금 열린 속성에 더해 펼치기(예: <span class="k">P</span> 다음 <span class="k">Shift+R</span>)</td></tr>
<tr><td><span class="k">V</span> / <span class="k">W</span></td><td>선택 도구 / 회전 도구. 회전 도구로 축 고리를 끌면 그 축으로만 돕니다</td></tr>
<tr><td><span class="k">C</span></td><td>카메라 도구(궤도·이동·돌리). 누를 때마다 다음 도구로</td></tr>
<tr><td>도구 막대의 축 모드</td><td><b>Local Axis</b>(레이어 자기 기준), <b>World Axis</b>(공간 기준), <b>View Axis</b>(지금 보는 화면 기준). 기울어진 레이어를 “공간의 위쪽”으로 올리려면 World</td></tr>
<tr><td><span class="k">F10</span> <span class="k">F11</span> <span class="k">F12</span></td><td>등록된 3D 보기로 전환(13-5)</td></tr>
<tr><td><span class="k">Ctrl+Alt+O</span></td><td>Auto-Orient. <b>Orient Towards Camera</b>를 고르면 레이어가 늘 카메라를 바라봄(나뭇잎·입자 카드)</td></tr>
<tr><td>Layer → Transform → Center Anchor Point in Layer Content</td><td>축의 중심(Anchor Point)을 물체 가운데로. 이상하게 돌면 먼저 이것부터</td></tr>
</table>
<div class="tip"><b>문이 열리듯 돌리려면</b>회전은 Anchor Point를 중심으로 일어납니다. 카드가 왼쪽 모서리를 축으로 열리게 하려면 <b>Pan Behind Tool</b>(%s)로 Anchor Point를 왼쪽 모서리로 옮긴 뒤 Y Rotation에 키프레임을 겁니다.</div>
'''.replace('%s', K('Y'))

PBR = '''
<h2>13-11 텍스처 맵 이해하기 — PBR 재질의 일곱 장</h2>
<p>3D 모델의 겉모습은 숫자 몇 개가 아니라 <b>이미지 여러 장(맵)</b>으로 정해집니다. 요즘 3D 프로그램·애펙 Advanced 3D·Substance는 모두 <b>PBR</b>(물리 기반 렌더링, Metal-Roughness 방식)을 씁니다. 맵 이름만 알아도 다운로드한 모델과 재질을 이해할 수 있습니다.</p>
<table>
<tr><th style="width:24%">맵</th><th style="width:20%">생김새</th><th>하는 일</th></tr>
<tr><td>Base Color (Albedo, Diffuse)</td><td>컬러 사진</td><td>표면 본래의 색. 그림자와 반짝임이 들어가 있지 않아야 합니다</td></tr>
<tr><td>Roughness</td><td>흑백</td><td>검정은 매끈(거울), 흰색은 거침(무광). 손때·긁힘이 여기 들어갑니다</td></tr>
<tr><td>Metallic</td><td>흑백(대개 0 또는 1)</td><td>흰색 부분만 금속처럼 반사합니다. 녹슨 쇠는 녹 부분만 검정</td></tr>
<tr><td>Normal</td><td>보라·파랑 이미지</td><td>모양은 그대로 두고 빛이 닿는 방향만 바꿔 요철이 있는 것처럼 보이게</td></tr>
<tr><td>Height (Displacement)</td><td>흑백</td><td>표면을 실제로 밀어 올림. 무거우니 가까이 찍을 때만</td></tr>
<tr><td>Emissive (Emission)</td><td>컬러, 대부분 검정</td><td>스스로 빛나는 부분. 화면, 네온, 계기판</td></tr>
<tr><td>Ambient Occlusion</td><td>흑백</td><td>틈과 구석의 어두움. 맵이 없을 때보다 입체감이 깊어짐</td></tr>
</table>
<p><b>애펙에서 맵을 쓰는 세 가지 길</b></p>
<ul>
<li><b>모델 파일에 맵을 넣어 가져오기</b>: 블렌더나 Substance Painter에서 맵을 입힌 뒤 <b>GLB</b>로 내보내면 맵이 파일 안에 함께 들어가, 애펙에 불러오는 순간 그대로 보입니다. 가장 확실한 방법입니다.</li>
<li><b>Substance 재질(.sbsar)</b>: Adobe Substance 3D Assets에서 받은 재질을 프로젝트에 불러와 Material 드롭다운에서 고릅니다. 맵이 재질 안에 들어 있고 색·거칠기를 슬라이더로 바꿉니다(23-7).</li>
<li><b>레이어를 재질로(27.0)</b>: 컴포지션·영상·이미지를 Base Color로 씁니다. 움직이는 화면, 간판에 좋습니다(23-7).</li>
</ul>
''' + '''<p><b>따라 하기 — HDRI로 금속을 금속답게</b></p>
''' + steps(
    '금속 재질 모델(또는 Extrude한 3D 글자, Metallic 1, Roughness 0.2)을 Advanced 3D 컴포지션에 놓습니다. 처음엔 회색 덩어리처럼 보입니다. 금속은 <b>주변을 비추는</b> 물체라 비출 것이 없으면 칙칙합니다.',
    'HDRI 파일(.hdr 또는 .exr, 2K~4K)을 불러와 컴포지션 맨 아래에 놓습니다. Poly Haven 같은 곳에서 무료 HDRI를 받을 수 있습니다.',
    '<b>Layer → New → Light</b>에서 Light Type을 <b>Environment</b>로 고르고 OK. Light Options의 <b>Source</b>를 방금 놓은 HDRI 레이어로 지정합니다.',
    'HDRI 레이어의 눈을 끕니다. 배경으로는 안 보이고 반사와 빛으로만 쓰입니다.',
    '환경 라이트의 Intensity(100%에서 시작)와 Y Rotation을 바꿔 가며 반사가 글자 면을 훑고 지나가는 각도를 찾습니다. 이 각도에 키프레임을 걸면 빛이 흐르는 고급 로고가 됩니다.',
)

E3D = '''
<h2>13-12 Element 3D — 3D 플러그인의 대표</h2>
<p>Video Copilot의 <b>Element 3D</b>는 애펙 안에서 3D 모델을 GPU로 빠르게 그리는 유료 플러그인입니다. Advanced 3D가 생기기 전부터 3D 로고·글자·우주선 장면을 만드는 표준처럼 쓰였고, 지금도 마켓 템플릿 상당수가 Element 3D를 요구합니다. 특징은 <b>OBJ·C4D 모델 불러오기</b>, 글자 <b>돌출(Extrude)</b>, 풍부한 재질 프리셋, 하나의 모델을 수백 개로 복제하는 <b>Particle Replicator</b>, 애펙 카메라·라이트와의 연동입니다.</p>
''' + steps(
    '검은 솔리드(%s)를 만들고 <b>Effect → Video Copilot → Element</b>를 넣습니다. 컴포지션에 카메라가 없으면 먼저 <b>Layer → New → Camera</b>로 카메라를 만듭니다. Element는 애펙 카메라로 장면을 찍습니다.' % K('Ctrl+Y'),
    '글자를 돌출하려면 텍스트 레이어를 하나 만들고 눈을 끈 뒤, Element의 <b>Custom Layers → Custom Text and Masks → Path Layer 1</b>에서 그 텍스트 레이어를 고릅니다.',
    'Effect Controls 맨 위의 <b>Scene Setup</b>을 누르면 Element 전용 창이 열립니다. 위쪽 <b>EXTRUDE</b> 버튼을 누르면 글자가 3D로 솟습니다. 모델을 쓰려면 <b>IMPORT</b>로 OBJ 파일을 불러오거나 왼쪽 <b>Model Browser</b>에서 고릅니다.',
    '아래쪽 <b>Presets</b>의 재질(금속, 유리, 크롬 등)을 모델 위로 끌어다 놓습니다. 오른쪽 <b>Edit</b> 패널에서 Diffuse·Specularity·Reflectivity·Normal Bump·Illumination 텍스처를 바꿉니다. 13-11의 맵이 여기서 그대로 쓰입니다.',
    '<b>OK</b>를 눌러 애펙으로 돌아옵니다. Effect Controls의 <b>Group 1 → Particle Replicator</b>에서 Particle Count와 Replicator Shape(Plane, Ring, Sphere 등)를 바꾸면 모델이 여러 개로 늘어 배열됩니다.',
    '<b>Render Settings</b>에서 Ambient Occlusion과 Motion Blur를 켜고, <b>Lighting</b>에서 애펙 라이트를 쓰게 합니다. 무거우면 작업 중엔 Render Mode를 Preview로 둡니다.',
) + '''
<table>
<tr><th style="width:26%">비교</th><th style="width:37%">애펙 Advanced 3D (기본 기능)</th><th>Element 3D (플러그인)</th></tr>
<tr><td>값</td><td>애펙에 포함</td><td>따로 구입</td></tr>
<tr><td>모델 형식</td><td>GLB·GLTF·OBJ·FBX</td><td>OBJ·C4D</td></tr>
<tr><td>복제·배열</td><td>직접 레이어를 복제</td><td>Particle Replicator로 수백 개를 한 번에</td></tr>
<tr><td>템플릿 호환</td><td>새 템플릿 위주</td><td>기존 마켓 템플릿 다수가 요구</td></tr>
<tr><td>주의</td><td>버전마다 기능이 늘어남</td><td>애펙 새 버전이 나오면 호환 업데이트를 기다려야 할 때가 있음</td></tr>
</table>
<div class="warn"><b>설치 전 확인</b>Element 3D는 그래픽 카드(GPU) 성능에 크게 기대고, 애펙의 큰 버전이 바뀐 직후에는 호환 업데이트가 나올 때까지 충돌이 날 수 있습니다. Video Copilot 사이트에서 지원 버전을 확인한 뒤 설치하고, 템플릿을 살 때도 “Element 3D 필요” 표시를 먼저 봅니다.</div>
'''

# ---------------------------------------------------------------- ch.14 rendering, import, templates
RENDER = '''
<h2><span class="tag t1">따라 하기</span> 14-8 Render Queue 한 바퀴 — 설정 칸 전부 읽기</h2>
''' + steps(
    '렌더할 컴포지션을 프로젝트 패널에서 고르고 <b>Composition → Add to Render Queue</b>(%s). 아래쪽에 Render Queue 패널이 열리고 한 줄이 생깁니다.' % K('Ctrl+M'),
    '<b>Render Settings</b> 옆 파란 글씨(기본 Best Settings)를 누릅니다. Quality <b>Best</b>, Resolution <b>Full</b>을 확인하고, 아래 <b>Time Span</b>을 봅니다. <b>Work Area Only</b>면 작업 영역만, <b>Length of Comp</b>면 전체가 렌더됩니다. 잘린 영상이 나오는 가장 흔한 이유가 여기입니다.',
    '<b>Output Module</b> 옆 파란 글씨(기본 H.264 또는 High Quality)를 누릅니다. 아래 표의 칸을 정하고 OK.',
    '<b>Output To</b> 옆 파란 글씨를 눌러 저장 폴더와 이름을 정합니다. 프로젝트 폴더의 %s 폴더를 씁니다.' % M('render'),
    '오른쪽 위 <b>Render</b>. 끝나면 소리가 나고 줄이 초록으로 바뀝니다. 같은 컴포지션을 여러 형식으로 내려면 Output Module 줄 왼쪽의 <b>+</b>를 눌러 출력을 하나 더 붙입니다(MP4와 ProRes 동시에).',
) + '''
<table>
<tr><th style="width:26%">Output Module 칸</th><th>고르는 법</th></tr>
<tr><td>Format</td><td>H.264(MP4), QuickTime(MOV), AVI, PNG Sequence, JPEG Sequence, TIFF Sequence, OpenEXR Sequence, WAV 등</td></tr>
<tr><td>Format Options…</td><td>코덱과 화질. QuickTime이면 Video Codec(ProRes 422 HQ, ProRes 4444 등), H.264면 비트레이트, JPEG면 Quality</td></tr>
<tr><td>Channels</td><td><b>RGB</b>(보통) / <b>RGB + Alpha</b>(투명 배경) / Alpha(흑백 매트만)</td></tr>
<tr><td>Depth</td><td>Millions of Colors / <b>Millions of Colors+</b>(알파 포함일 때 자동). 고급 납품은 Trillions(16bit)</td></tr>
<tr><td>Color</td><td>Premultiplied(Matted, 기본) / Straight(Unmatted). 받는 쪽 규격을 따릅니다</td></tr>
<tr><td>Resize · Crop</td><td>4K로 만든 것을 1080p로 줄여 함께 낼 때 Resize</td></tr>
<tr><td>Post-Render Action</td><td><b>Import &amp; Replace Usage</b>를 고르면 렌더 결과가 프로젝트로 들어와 원래 컴포지션 자리를 대신합니다(프리렌더)</td></tr>
<tr><td>Audio Output</td><td>Auto / On / Off, 48kHz. 소리가 안 나오면 여기가 Off인지 확인</td></tr>
</table>
<div class="tip"><b>자주 쓰는 설정을 기본으로</b><b>Edit → Templates → Output Module</b>에서 “ProRes 4444 알파”, “유튜브 4K” 같은 설정을 이름 붙여 저장하고 Default로 정해 두면, 매번 칸을 고르지 않습니다. 현업에서는 팀이 같은 템플릿을 나눠 씁니다.</div>

<h2>14-9 형식별 정리 — MP4(H.264), MOV, AVI, 4K</h2>
<table>
<tr><th style="width:16%">형식</th><th style="width:22%">고르는 곳</th><th style="width:16%">투명 배경</th><th>쓰는 곳과 요령</th></tr>
<tr><td>MP4 (H.264)</td><td>Format: H.264</td><td>안 됨</td><td>유튜브·SNS·휴대폰·발표. 1080p 10~20Mbps, 4K 35~45Mbps. 편집에 다시 쓰면 화질이 떨어지므로 최종 배포용</td></tr>
<tr><td>MP4 (H.265/HEVC)</td><td>Media Encoder</td><td>안 됨</td><td>같은 화질에 파일이 더 작음. 4K 이상·저장 공간이 빠듯할 때. 오래된 기기는 재생이 안 될 수 있음</td></tr>
<tr><td>MOV (ProRes 422 HQ)</td><td>QuickTime → Apple ProRes 422 HQ</td><td>안 됨</td><td>편집용 마스터. 파일이 크지만 여러 번 다시 써도 깨끗함</td></tr>
<tr><td>MOV (ProRes 4444)</td><td>QuickTime → Apple ProRes 4444</td><td><b>됨</b></td><td>자막·로고·이펙트처럼 다른 영상 위에 얹을 소스. 방송 송출 서버 납품</td></tr>
<tr><td>AVI</td><td>Format: AVI</td><td>설정에 따라</td><td>윈도우의 오래된 형식. 무압축이라 파일이 매우 큼. 전광판 플레이어 등 현장 장비가 AVI만 읽을 때만</td></tr>
<tr><td>PNG 시퀀스</td><td>PNG Sequence</td><td><b>됨</b></td><td>프레임마다 한 장. 무손실, 렌더가 중간에 멈춰도 이어서 가능</td></tr>
<tr><td>JPG 시퀀스</td><td>JPEG Sequence</td><td>안 됨</td><td>가벼운 미리보기, 웹·게임 엔진용 프레임, 썸네일 뽑기</td></tr>
<tr><td>EXR 시퀀스</td><td>OpenEXR Sequence</td><td>됨</td><td>VFX 납품, 32bit 색. 다른 합성 프로그램으로 넘길 때</td></tr>
</table>
<p><b>4K로 렌더하려면</b>: 출력에서 키우는 것이 아니라 <b>처음부터 컴포지션을 4K로</b> 만듭니다. <b>Composition → Composition Settings</b>(%s)에서 Preset을 <b>UHD 4K 29.97</b>(3840×2160)로, 영화관용 DCI 4K는 4096×2160입니다. 1080p로 만든 컴포지션을 Output Module에서 4K로 Resize하면 흐릿하게 늘어날 뿐입니다. 작업 중에는 미리보기 해상도를 Half로 두면 가볍습니다.</p>
<div class="note"><b>무엇을 고를지 모르겠다면</b>마스터는 ProRes 422 HQ(투명이 필요하면 4444)로 한 번 렌더하고, 그 파일을 Media Encoder에 넣어 MP4를 만듭니다. 고칠 일이 생겨도 마스터에서 다시 만들면 되므로 애펙 렌더를 반복하지 않습니다.</div>
'''.replace('%s', K('Ctrl+K')) + '''
<h2><span class="tag t1">따라 하기</span> 14-10 투명 배경(알파)으로 렌더하기</h2>
<p>자막·로고 애니메이션을 프리미어나 다른 영상 위에 얹으려면 배경이 투명한 파일이 필요합니다. 애펙에서는 <b>아무것도 없는 곳</b>이 곧 투명입니다.</p>
''' + steps(
    '컴포지션에서 배경 솔리드를 끄거나 지웁니다. Composition Settings의 Background Color는 렌더에 들어가지 않으니 신경 쓰지 않아도 됩니다.',
    '컴포지션 패널 아래 <b>Toggle Transparency Grid</b>(바둑판 아이콘)를 누릅니다. 바둑판이 보이는 곳이 투명하게 나올 곳입니다.',
    '%s로 Render Queue에 넣고 Output Module에서 Format <b>QuickTime</b>, Format Options의 Video Codec을 <b>Apple ProRes 4444</b>로 고릅니다.' % K('Ctrl+M'),
    '<b>Channels</b>를 <b>RGB + Alpha</b>로 바꿉니다. 이 칸을 RGB로 두면 투명한 곳이 검정으로 채워집니다.',
    'Color는 기본 <b>Premultiplied (Matted)</b>로 둡니다. 렌더한 파일을 프리미어 타임라인의 영상 위 트랙에 올려 배경이 비쳐 보이면 성공입니다.',
    '프레임 단위 이미지가 필요하면 Format을 <b>PNG Sequence</b>로, Channels를 <b>RGB + Alpha</b>로 같은 방법으로 냅니다.',
) + '''
<div class="stuck"><b>알파가 안 빠질 때</b>① MP4(H.264)와 JPG는 투명을 담지 못합니다. ② Channels가 RGB인지 확인합니다. ③ 맨 아래에 꺼지지 않은 솔리드나 조정 레이어 위의 효과(예: 배경을 채우는 Fill)가 없는지 봅니다. ④ 글자 가장자리에 검은 테가 생기면 받는 쪽에서 알파를 Straight로 해석했기 때문이니, Premultiplied로 바꾸거나 렌더를 Straight로 다시 냅니다.</div>

<h2><span class="tag t1">따라 하기</span> 14-11 이미지 시퀀스 — JPG·PNG로 렌더하고 다시 불러오기</h2>
<p><b>A. 시퀀스로 렌더하기</b></p>
''' + steps(
    'Render Queue의 Output Module에서 Format을 <b>JPEG Sequence</b>(또는 PNG Sequence)로 고릅니다.',
    'JPEG이면 <b>Format Options</b>에서 Quality를 <b>10</b>(최대)으로 올립니다.',
    'Output To에서 <b>새 폴더</b>를 지정합니다. 파일 이름은 %s처럼 끝에 %s가 붙어 있어야 합니다. 애펙이 그 자리에 00000, 00001… 프레임 번호를 넣습니다.' % (M('title_[#####].jpg'), M('[#####]')),
    'Render. 30fps 10초면 300장이 폴더에 생깁니다.',
) + '''
<p><b>B. 시퀀스 불러오기</b></p>
''' + steps(
    '<b>File → Import → File</b>(%s)을 누르고 시퀀스 폴더에서 <b>첫 번째 파일</b>만 고릅니다.' % K('Ctrl+I'),
    '창 아래의 <b>JPEG Sequence</b>(PNG면 PNG Sequence) 체크를 켜고 Import. 수백 장이 영상 한 개로 들어옵니다. 체크를 끄면 사진 한 장만 들어옵니다.',
    '들어온 시퀀스의 속도를 맞춥니다. 프로젝트 패널에서 고르고 <b>File → Interpret Footage → Main</b>(%s) → <b>Frame Rate</b>에서 <b>Assume this frame rate</b>에 24 또는 30을 넣습니다.' % K('Ctrl+Alt+G'),
    'PNG처럼 투명이 있는 시퀀스는 같은 창의 <b>Alpha</b>에서 Premultiplied·Straight를 고르거나 <b>Guess</b>를 누릅니다.',
) + '''
<div class="tip"><b>시퀀스를 쓰는 이유</b>렌더가 3시간 걸리는데 중간에 꺼져도 이미 만든 프레임은 남아 그다음부터 이어서 렌더할 수 있습니다. 블렌더·C4D·AI 영상 툴에서 프레임으로 받은 결과물도 같은 방법으로 불러옵니다. 기본 프레임레이트는 <b>Edit → Preferences → Import → Sequence Footage</b>에서 바꿉니다.</div>
'''

AEP = '''
<h2>14-12 다른 프로젝트(.aep) 통째로 가져오기</h2>
<p>다른 사람이 만든 장면, 예전 작업의 로고 애니메이션, 내려받은 템플릿을 지금 프로젝트에 합칠 때 <b>.aep 파일을 그대로 불러옵니다</b>. 열고 복사·붙여넣기 할 필요가 없습니다.</p>
''' + steps(
    '가져올 프로젝트를 먼저 원래 컴퓨터에서 <b>File → Dependencies → Collect Files</b>로 소스와 함께 한 폴더에 모아 받습니다(14-6). 이 폴더를 내 프로젝트 폴더 안으로 옮깁니다.',
    '내 프로젝트에서 <b>File → Import → File</b>(%s)을 누르고 .aep 파일을 고릅니다. 탐색기에서 .aep를 프로젝트 패널로 끌어다 놓아도 됩니다.' % K('Ctrl+I'),
    '프로젝트 패널에 그 파일 이름의 <b>폴더</b>가 생기고, 안에 컴포지션·소스·폴더 구조가 그대로 들어옵니다.',
    '빠진 파일(기울어진 이름)이 있으면 2-4의 Replace Footage로 다시 연결합니다. 같은 폴더에 있던 나머지 파일은 한 번에 따라 연결됩니다.',
    '필요한 컴포지션만 남기려면 그것을 고르고 <b>File → Dependencies → Reduce Project</b>. 쓰이지 않는 항목이 정리됩니다.',
) + '''
<table>
<tr><th style="width:30%">가져올 것</th><th>방법</th></tr>
<tr><td>다른 .aep의 컴포지션</td><td>위 방법. 한 프로젝트 안에서 같은 이름 소스가 겹치면 <b>File → Dependencies → Consolidate All Footage</b>로 중복을 합칩니다</td></tr>
<tr><td>프리미어 시퀀스</td><td><b>File → Import → Import Adobe Premiere Pro Project</b>, 또는 프리미어에서 Dynamic Link(14-3)</td></tr>
<tr><td>포토샵·일러스트레이터</td><td>Composition - Retain Layer Sizes로(14-5). 일러스트 글자를 편집하려면 SVG로(23-7)</td></tr>
<tr><td>애니메이션 프리셋(.ffx)</td><td>Effects &amp; Presets 패널에서 적용하거나 <b>Animation → Apply Animation Preset</b></td></tr>
<tr><td>MOGRT</td><td>프리미어의 Essential Graphics에서 사용. 애펙에서 고치려면 원본 .aep가 필요합니다</td></tr>
</table>
<div class="warn"><b>버전 주의</b>새 버전 애펙에서 저장한 .aep는 옛 버전에서 열리지 않습니다. 옛 버전 사용자에게 넘길 때는 <b>File → Save As → Save a Copy As</b>(바로 앞 버전용)으로 저장합니다. 옛 프로젝트를 새 버전에서 열면 “변환되었다”는 안내가 뜨고, 원본을 덮어쓰지 않게 새 이름으로 저장하는 것이 안전합니다.</div>
'''

TEMPLATE = '''
<h2>14-13 템플릿이라는 개념 — 다섯 가지 모양</h2>
<p>템플릿은 “잘 만든 구조를 다시 쓰는 것”입니다. 애펙에서는 같은 말이 다섯 가지 다른 파일을 가리키므로 구분해 두면 현업에서 덜 헤맵니다.</p>
<table>
<tr><th style="width:22%">종류</th><th style="width:16%">파일</th><th>만드는 법과 쓰는 법</th></tr>
<tr><td>프로젝트 템플릿</td><td>.aet</td><td><b>File → Save As → Save As</b>에서 파일 형식을 <b>After Effects Project Template</b>으로 저장. 열면 이름 없는 사본이 열려 원본이 덮어써지지 않습니다. 매주 쓰는 방송 CG, 수업 과제 틀</td></tr>
<tr><td>애니메이션 프리셋</td><td>.ffx</td><td>효과와 키프레임이 든 속성을 고르고 <b>Animation → Save Animation Preset</b>. Effects &amp; Presets 패널의 User Presets에서 끌어다 씁니다. 자주 쓰는 글자 등장, 흔들림, 색 보정 묶음</td></tr>
<tr><td>모션 그래픽 템플릿</td><td>.mogrt</td><td>Essential Graphics로 내보내 프리미어에서 글자·색만 바꿔 씀(14-4)</td></tr>
<tr><td>Essential Properties</td><td>(프로젝트 안)</td><td>프리컴포즈 안의 속성을 Essential Graphics에 올려 두면, 바깥에서 그 프리컴포즈를 여러 번 놓고 <b>각각 다른 글자·색</b>을 줄 수 있습니다. 하단 자막 하나로 출연자 10명을 만듭니다</td></tr>
<tr><td>마켓 템플릿</td><td>.aep 묶음</td><td>Adobe Stock, Envato, Motion Array 등에서 사는 완성 프로젝트. 아래 순서로 고칩니다</td></tr>
</table>
''' + '''<p><b>따라 하기 — 마켓 템플릿 고치는 순서</b></p>
''' + steps(
    '사기 전에 설명에서 <b>필요한 애펙 버전</b>, <b>필요한 플러그인</b>(Element 3D, Optical Flares, Trapcode 등), <b>글꼴</b>, <b>해상도</b>를 확인합니다. 플러그인이 없으면 열어도 빨간 경고만 보입니다.',
    '내려받은 압축을 프로젝트 폴더에 풀고 함께 든 <b>Help</b>·<b>Read Me</b> 파일이나 안내 영상을 먼저 봅니다.',
    '.aep를 열면 보통 <b>01_Edit</b>(고칠 곳)·<b>02_Final</b>(렌더할 곳)·<b>03_Elements</b>(건드리지 않을 곳)처럼 나뉘어 있습니다. Edit 폴더의 컴포지션만 엽니다.',
    '글자는 Edit 컴포지션 안의 텍스트를 바꾸고, 사진·영상 자리는 그 자리 레이어를 고른 뒤 프로젝트 패널의 내 파일을 %s를 누른 채 끌어다 놓아 바꿉니다. 크기가 안 맞으면 %s(Fit to Comp)로 맞춥니다.' % (K('Alt'), K('Ctrl+Alt+F')),
    '색은 템플릿에 보통 있는 <b>Controller</b>·<b>Color Control</b> 레이어에서 한 번에 바꿉니다(7-16 리그와 같은 원리).',
    'Final 컴포지션을 Render Queue로 보냅니다. 남에게 넘길 때는 Collect Files로 모읍니다.',
) + '''
<div class="note"><b>템플릿과 실력</b>템플릿은 마감을 지키게 해 주지만, 고칠 수 있는 만큼만 내 것이 됩니다. 이 책의 리그(7-16)·Essential Graphics(14-4)·프리컴포즈(4-5)를 알면 템플릿을 뜯어 원하는 대로 바꾸고, 결국 내 템플릿을 만들어 팔거나 팀에 나눌 수 있습니다.</div>
'''

# ---------------------------------------------------------------- ch.16 pro pipeline
PIPE = '''
<h2>16-1 숙련자의 작업 순서 — 현업 파이프라인</h2>
<p>기능을 많이 아는 것과 일을 잘하는 것은 다릅니다. 현업 숙련자는 같은 기능을 <b>정해진 순서</b>로 씁니다. 순서를 지키면 수정 요청이 와도 무너지지 않습니다.</p>
<table>
<tr><th style="width:6%">#</th><th style="width:24%">단계</th><th>하는 일</th></tr>
<tr><td>1</td><td>레퍼런스·스타일프레임</td><td>참고 영상 3~5개, 멈춘 화면 한 장(스타일프레임)을 먼저 승인받습니다. 움직이기 전에 “한 장의 그림”을 합의</td></tr>
<tr><td>2</td><td>애니매틱</td><td>박스와 임시 글자로 타이밍만 맞춘 거친 영상. 음악·내레이션에 맞춰 컷 길이 확정</td></tr>
<tr><td>3</td><td>프로젝트 구조</td><td>폴더(00_Comps, 01_Footage, 02_Precomps, 03_Render, 99_Guide), 이름 규칙(SH010_title_v003), 마스터 컴포지션 하나에 샷별 프리컴포즈</td></tr>
<tr><td>4</td><td>리그 먼저</td><td>색·글자·속도를 바꿀 컨트롤 레이어(7-16)를 만든 뒤 애니메이션. 수정이 오면 컨트롤 값만 바꿉니다</td></tr>
<tr><td>5</td><td>블로킹 → 다듬기</td><td>Linear 키로 위치·타이밍만(블로킹) → 그래프 에디터로 속도(3-4) → 겹침·잔동작(Polish)</td></tr>
<tr><td>6</td><td>합성·룩</td><td>조정 레이어 묶음: 색 보정 → 글로우 → 그레인 → 비네트 순서를 고정</td></tr>
<tr><td>7</td><td>사운드</td><td>효과음은 마지막이 아니라 다듬기 단계에서 함께. 소리에 맞춰 키프레임을 한두 프레임 당기면 체감 품질이 크게 올라갑니다</td></tr>
<tr><td>8</td><td>검수·납품</td><td>세이프 영역, 오탈자, 꺼진 레이어, 음량, 규격별 렌더(14-8), Collect Files로 백업</td></tr>
</table>

<h2>16-2 무거운 프로젝트 다루기 — 숙련자의 기술</h2>
<table>
<tr><th style="width:24%">기술</th><th>방법</th></tr>
<tr><td>프록시</td><td>4K·8K 소스를 우클릭 → <b>Create Proxy → Movie</b>로 가벼운 사본을 만들어 작업하고, 렌더할 때는 Render Settings의 <b>Proxy Use: Use No Proxies</b>로 원본을 씁니다</td></tr>
<tr><td>프리렌더</td><td>끝난 무거운 프리컴포즈를 Post-Render Action: <b>Import &amp; Replace Usage</b>로 렌더해 영상으로 바꿔 끼웁니다(14-8). 고칠 일이 생기면 원래 컴포지션으로 되돌립니다</td></tr>
<tr><td>디스크 캐시</td><td><b>Preferences → Media &amp; Disk Cache</b>를 빠른 SSD로, 크기는 100GB 이상. 프로젝트가 크면 체감 속도가 달라집니다</td></tr>
<tr><td>32bpc·선형 작업</td><td><b>File → Project Settings → Color</b>에서 Bit Depth 32 bpc. 빛을 더하는 글로우·모션 블러·렌즈 효과가 실제 빛처럼 자연스럽게 섞입니다. 영화·광고 VFX는 OCIO/ACES 색 관리로 통일합니다</td></tr>
<tr><td>3D 멀티패스</td><td>블렌더·C4D에서 EXR 멀티채널(빛·반사·그림자·깊이 분리)로 받아 <b>Effect → 3D Channel → EXtractoR</b>로 패스를 꺼내 따로 색을 고칩니다. 3D를 다시 렌더하지 않고 반사만 줄이는 식입니다</td></tr>
<tr><td>여러 규격 동시 납품</td><td>16:9 마스터 컴포지션을 9:16·1:1 컴포지션에 프리컴포즈로 넣고 위치만 다시 잡습니다. 원본을 고치면 모든 규격에 반영됩니다</td></tr>
<tr><td>스크립트·자동화</td><td><b>File → Scripts → Run Script File</b>로 .jsx를 실행하고, 자주 쓰는 스크립트는 Scripts 폴더에 넣어 Window 메뉴에서 패널로 씁니다. 이름 일괄 변경, 레이어 정렬처럼 반복 작업에 씁니다. 지금은 AI Assistant(23장)와 Claude 브리지(21장)가 이 역할을 상당 부분 대신합니다</td></tr>
<tr><td>명령줄 렌더</td><td>애펙 설치 폴더의 <b>aerender</b>로 창을 열지 않고 렌더합니다. 예: <span class="mono">aerender -project "D:\\job\\title.aep" -comp "Final" -output "D:\\job\\render\\title.mov"</span>. 밤새 여러 프로젝트를 순서대로 렌더할 때</td></tr>
<tr><td>버전 관리</td><td>File → Increment and Save로 v001, v002…를 남기고, 클라이언트에 보낸 버전은 이름 끝에 _sent를 붙입니다. 무엇을 보냈는지 늘 되짚을 수 있어야 합니다</td></tr>
</table>
'''

# ---------------------------------------------------------------- appendix C plugins
PLUGINS = '''<h2>C. 플러그인 생태계 — 현업에서 자주 쓰는 것</h2>
<p>플러그인은 애펙에 없는 기능을 채우거나, 있는 기능을 훨씬 빠르게 해 줍니다. 아래는 현업과 마켓 템플릿에서 자주 만나는 것들입니다. 값과 지원 버전은 바뀌므로 설치 전 각 회사 사이트에서 애펙 2027 지원 여부를 확인하세요.</p>
<table>
<tr><th style="width:15%">분야</th><th style="width:31%">플러그인 (회사)</th><th>하는 일</th></tr>
<tr><td>파티클</td><td>Trapcode Particular · Form (Maxon Red Giant)</td><td>3D 입자의 표준. 연기·불꽃·마법 효과, 글자가 입자로 흩어지기. Form은 격자 모양 입자로 추상 그래픽</td></tr>
<tr><td>파티클</td><td>Stardust (Superluminal)</td><td>노드 방식 3D 입자, 모델 복제</td></tr>
<tr><td>3D</td><td>Element 3D (Video Copilot)</td><td>3D 모델·글자 돌출·복제(13-12)</td></tr>
<tr><td>3D</td><td>Cinema 4D · Cineware (Maxon, 애펙에 Lite 포함)</td><td>3D 장면을 레이어처럼 연결</td></tr>
<tr><td>빛</td><td>Optical Flares (Video Copilot)</td><td>렌즈 플레어. 영화 타이틀의 단골</td></tr>
<tr><td>빛</td><td>Deep Glow (Plugin Everything)</td><td>실제 빛처럼 퍼지는 고급 글로우</td></tr>
<tr><td>빛</td><td>Saber (Video Copilot, 무료)</td><td>광선검·네온·전기 테두리</td></tr>
<tr><td>효과 종합</td><td>Sapphire (Boris FX) · Red Giant Universe (Maxon) · BCC (Boris FX)</td><td>글리치, 렌즈 효과, 전환, 빛 번짐 등 수백 가지. 방송·광고 현장 표준</td></tr>
<tr><td>추적·로토</td><td>Mocha Pro (Boris FX)</td><td>Mocha AE(내장, 9-6)의 상위판. 제거·안정화·렌즈 보정까지</td></tr>
<tr><td>색</td><td>Magic Bullet Looks (Maxon Red Giant)</td><td>영화 같은 룩을 미리보기 보며 쌓기</td></tr>
<tr><td>속도·블러</td><td>Twixtor · ReelSmart Motion Blur (RE:Vision Effects)</td><td>프레임을 만들어 내는 슬로모션, 사후 모션 블러</td></tr>
<tr><td>잡음</td><td>Neat Video (ABSoft)</td><td>어두운 장면의 노이즈 제거</td></tr>
<tr><td>선·연결</td><td>Plexus (Rowbyte)</td><td>점과 선이 이어지는 데이터·네트워크 그래픽</td></tr>
<tr><td>리깅</td><td>Duik (RxLab, 무료) · RubberHose · Joysticks 'n Sliders (Battle Axe)</td><td>캐릭터 관절·팔다리·표정 리그</td></tr>
<tr><td>작업 효율</td><td>Motion Tools Pro (무료) · Flow · Overlord (Battle Axe) · Animation Composer (Mister Horse)</td><td>정렬·이징·일러스트 레이어 옮기기·프리셋 라이브러리. 하루에 수십 번 하는 클릭을 줄임</td></tr>
<tr><td>웹 내보내기</td><td>Bodymovin / LottieFiles</td><td>웹·앱용 Lottie(JSON)</td></tr>
<tr><td>AI</td><td>Higgsfield 플러그인</td><td>AI 생성·편집 패널과 Claude 브리지(17~22장)</td></tr>
</table>
<div class="tip"><b>처음 살 플러그인을 고른다면</b>무료인 Saber·Duik·Motion Tools Pro로 시작하고, 일이 생기는 분야에 맞춰 하나씩 더합니다. 영상 효과·광고 쪽이면 Trapcode Particular와 Optical Flares, 방송이면 Sapphire, 3D 로고가 많으면 Element 3D를 먼저 봅니다. 템플릿을 많이 쓴다면 그 템플릿이 요구하는 플러그인이 곧 첫 구매 목록입니다.</div>
'''

# ---------------------------------------------------------------- ch.24 cinematic title
CINE = '''
<h2><span class="tag t3">한 걸음 더</span> 24-4 고급 실전 — 영화 같은 오프닝 타이틀 30초</h2>
<p>지금까지 배운 기능을 한 장면에 모으면 영화 예고편 같은 타이틀이 됩니다. 고급스러움은 특별한 버튼이 아니라 <b>깊이(3D·피사계 심도) + 빛(반사·플레어·글로우) + 공기(안개·먼지) + 필름 질감(그레인·모션 블러) + 소리</b>를 겹치는 데서 나옵니다. 아래는 현업 타이틀 디자이너가 쓰는 순서를 그대로 따른 과제입니다.</p>
<div class="mission"><div class="lbl">목표</div><p>어두운 공간에서 금속 질감의 3D 제목이 안개 속에서 천천히 드러나고, 빛이 글자 면을 훑고 지나간 뒤 렌즈 플레어와 함께 멈추는 30초 오프닝. 4K, 2.39:1 화면비, 23.976fps.</p></div>
<p><b>1. 판 짜기</b></p>
''' + steps(
    '새 컴포지션 %s, 3840×2160, 23.976fps, 30초. <b>Advanced 3D</b> 렌더러를 고릅니다. <b>Advanced</b> 탭에서 Motion Blur의 Shutter Angle을 180°로 둡니다(영화 카메라와 같은 잔상).' % M('MAIN_title'),
    '<b>File → Project Settings → Color</b>에서 Bit Depth를 <b>32 bpc</b>로. 빛이 겹치는 장면이라 색 띠(밴딩) 없이 부드럽게 섞입니다.',
    '맨 위에 2.39:1 레터박스를 만듭니다. 검은 솔리드에 사각형 마스크를 그려 가운데 3840×1607 영역을 비우고(마스크 Inverted), Guide Layer가 아닌 일반 레이어로 둡니다. 이름은 %s.' % M('LETTERBOX'),
) + '''<p><b>2. 제목 만들기</b></p>
''' + steps(
    '제목 글자를 쓰고(굵은 세리프나 넓은 산세리프, 자간 넓게) 3D 스위치를 켭니다. <b>Geometry Options</b>에서 Extrusion Depth 60, Bevel Style <b>Angular</b>, Bevel Depth 4.',
    'Material Assignment에서 Metallic 1, Roughness 0.25. Substance 금속 재질(.sbsar)이 있으면 앞면에 붓으로 쓸린 금속, 옆면에 어두운 금속을 따로 입힙니다(23-7).',
    '13-11처럼 HDRI를 Environment Light의 Source로 지정하고 HDRI 레이어의 눈을 끕니다. 글자에 주변 빛이 비치기 시작합니다.',
) + '''<p><b>3. 카메라와 깊이</b></p>
''' + steps(
    '카메라(50mm)를 만들고 널에 부모로 겁니다(13-9). 널의 Z Position을 30초 동안 −400만큼 천천히 앞으로 밀고(돌리 인), 끝 키프레임은 <b>Easy Ease In</b>(%s)으로 부드럽게 멈춥니다.' % K('Shift+F9'),
    '카메라의 <b>Depth of Field</b>를 켜고 글자를 고른 채 카메라에서 <b>Layer → Camera → Link Focus Distance to Layer</b>. 카메라가 움직여도 초점이 글자에 붙어 있습니다. Aperture를 올려 앞뒤 흐림을 키웁니다.',
    '빛이 흐르게 합니다. Environment Light의 Y Rotation에 키프레임을 걸어 8초에서 14초 사이에 60° 돌리면 반사가 글자 면을 왼쪽에서 오른쪽으로 훑습니다. 이 순간이 타이틀의 “주인공 장면”입니다.',
) + '''<p><b>4. 공기 — 안개와 먼지</b></p>
''' + steps(
    '5-7의 B 방법으로 Fractal Noise 안개를 두 장 만들고 3D 스위치를 켜서 하나는 글자 앞(Z −300), 하나는 뒤(Z 600)에 둡니다. 카메라가 지나가며 안개 사이로 시차가 생깁니다.',
    '5-7의 ① 방법으로 아주 작은 먼지 입자(Faded Sphere, Birth Size 0.02, Velocity 0.02, Gravity 0)를 만들고 Opacity 40%, Mode Add. 빛 속에 떠다니는 먼지가 공간감을 줍니다.',
    '먼지 레이어에 Fast Box Blur 2를 줘서 초점 밖처럼 만듭니다.',
) + '''<p><b>5. 빛 — 플레어와 글로우</b></p>
''' + steps(
    '검은 솔리드에 <b>Effect → Generate → Lens Flare</b>(또는 Optical Flares)를 넣고 Mode <b>Screen</b>. 반사가 지나가는 14초 부근에 Flare Brightness를 0 → 120 → 60으로 키프레임합니다.',
    '%s 조정 레이어를 맨 위(레터박스 아래)에 만들고 <b>Glow</b>(또는 Deep Glow)를 넣어 Glow Threshold 80%%, Radius 60, Intensity 0.6. 밝은 반사만 은은하게 번집니다.' % M('ADJ_glow'),
    '빛이 글자 뒤에서 새어 나오는 느낌을 원하면 글자 복제본에 <b>CC Light Rays</b>를 넣고 Center를 글자 뒤 광원 위치로, Mode Add.',
) + '''<p><b>6. 색과 필름 질감</b></p>
''' + steps(
    '%s 조정 레이어에 Lumetri Color. Color Wheels에서 Shadows를 청록, Highlights를 주황 쪽으로 조금씩 밀고(틸·오렌지), Curves로 검정을 살짝 들어 올려 필름처럼 바닥이 뜬 검정을 만듭니다. Creative 탭에서 LUT를 써도 됩니다.' % M('ADJ_grade'),
    '%s 조정 레이어에 <b>Noise &amp; Grain → Add Grain</b>(Intensity 0.3, Size 1.2). 디지털의 매끈함이 사라지고 필름 질감이 생깁니다.' % M('ADJ_grain'),
    '비네트: 검은 솔리드에 타원 마스크를 Inverted, Feather 1200, Opacity 50%. 시선이 가운데 글자로 모입니다.',
    '조정 레이어 순서는 위에서부터 레터박스 → 그레인 → 비네트 → 그레이드 → 글로우 → 장면입니다. 그레인은 항상 가장 마지막(맨 위 근처)에 둡니다.',
) + '''<p><b>7. 소리와 렌더</b></p>
''' + steps(
    '저음이 길게 깔리는 드론, 반사가 지나갈 때의 휙 소리(whoosh), 제목이 완성되는 순간의 묵직한 타격음(impact)을 넣습니다. 타격음 프레임에 맞춰 플레어 최고점 키프레임을 1~2프레임 앞당깁니다.',
    '모든 레이어의 모션 블러 스위치와 타임라인 위 Enable Motion Blur 버튼을 켭니다.',
    '마스터는 ProRes 422 HQ 4K로, 배포용은 그 파일을 Media Encoder에서 H.264 4K 40Mbps로 냅니다(14-9).',
) + '''
<table>
<tr><th style="width:30%">“싸 보이는” 원인</th><th>고치는 곳</th></tr>
<tr><td>모든 것이 선명하고 깨끗함</td><td>피사계 심도, 그레인, 모션 블러가 빠짐</td></tr>
<tr><td>빛이 평평함</td><td>Environment Light와 반사가 없음. 금속은 비출 것이 있어야 함</td></tr>
<tr><td>움직임이 기계적임</td><td>Linear 키, 모든 것이 동시에 움직임. 이징과 0.1~0.3초 시차(7-8)</td></tr>
<tr><td>색이 너무 쨍함</td><td>채도를 낮추고 그림자·하이라이트에 서로 다른 색을 줌</td></tr>
<tr><td>소리가 없음</td><td>타이틀 품질의 절반은 소리. 효과음에 맞춰 키프레임을 다시 맞춤</td></tr>
<tr><td>너무 많은 효과</td><td>주인공 장면(빛이 훑는 순간) 하나에 집중하고 나머지는 덜어냄</td></tr>
</table>
<div class="why"><b>AI와 함께 하면</b>안개·먼지·빛 소스나 배경 장면은 힉스필드에서 검은 배경으로 생성해 Screen 모드로 얹을 수 있고(18~20장), 반복적인 조정 레이어 구성·이름 정리·익스프레션은 Claude 브리지(21장)나 AI Assistant(23장)에 맡길 수 있습니다. 판단은 사람이 합니다. “어디가 주인공 장면인가”를 정하는 것이 디렉터의 일입니다.</div>
'''


def apply4(S):
    def rep(old, new):
        nonlocal S
        assert old in S, old[:80]
        S = S.replace(old, new, 1)

    def before_check(ch_id, html):
        nonlocal S
        i = S.find('<h1 class="ch">' + ch_id)
        assert i > 0, ch_id
        j = S.find('<h2>이 장 점검</h2>', i)
        S = S[:j] + html + S[j:]

    before_check('화면, 시간, 아이콘 읽기', HIDE)
    before_check('3D 레이어, 카메라, 라이트', AXES + PBR + E3D)
    before_check('렌더링, 출력, 다른 프로그램과 연결', RENDER + AEP + TEMPLATE)
    # ch.16 has no check section: append before its </section>
    i = S.find('<h1 class="ch">직업별 실전 팁'); j = S.find('</section>', i)
    S = S[:j] + PIPE + S[j:]
    # ch.24 cinematic before 평가 기준
    i = S.find('<h1 class="ch">통합 프로젝트'); j = S.find('<h2>평가 기준', i)
    S = S[:j] + CINE + S[j:]
    # appendix C
    i = S.find('<h2>C. 플러그인 생태계</h2>'); j = S.find('<h2>D. 용어', i)
    S = S[:i] + PLUGINS + '\n' + S[j:]
    return S
