# SVG diagrams for the book. Accent: After Effects purple.
P = "#9999FF"   # AE brand light purple
PD = "#5B54D6"  # darker purple for text/lines
N = "#00005B"   # AE navy
G = "#e6e7ee"; G2 = "#c9cbd6"; T = "#33363c"; M = "#7a7e88"

def svg(w, h, body):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" class="dia" '
            f'font-family="Noto Sans CJK KR, sans-serif">{body}</svg>')

def box(x, y, w, h, fill=G, stroke="none", r=6, sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def tx(x, y, s, size=13, fill=T, w="400", anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{w}" text-anchor="{anchor}">{s}</text>'

def arrow(x1, y1, x2, y2, c=PD, sw=2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}" marker-end="url(#ah)"/>')

DEFS = (f'<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
        f'<path d="M0,0 L8,4 L0,8 z" fill="{PD}"/></marker></defs>')

# 1. Interface map
def ui_map():
    b = DEFS
    b += box(0, 0, 640, 360, "#2b2d33", r=8)
    b += box(8, 8, 624, 22, "#3a3d45", r=3) + tx(16, 24, "메뉴 · 도구 막대 (Tools)", 11, "#ddd")
    b += box(8, 36, 150, 196, "#3a3d45", r=4) + tx(83, 120, "① Project", 13, "#fff", "700", "middle") + tx(83, 138, "재료 창고", 11, "#bbb", anchor="middle")
    b += box(164, 36, 330, 196, "#3a3d45", r=4) + box(190, 58, 278, 156, "#eeeeee", r=2) + tx(329, 130, "② Composition", 14, N, "700", "middle") + tx(329, 150, "무대 · 지금 시간의 화면", 11, M, anchor="middle")
    b += box(500, 36, 132, 196, "#3a3d45", r=4) + tx(566, 110, "④ Properties", 12, "#fff", "700", "middle") + tx(566, 128, "Effects &amp; Presets", 11, "#bbb", anchor="middle") + tx(566, 146, "Preview · 공구함", 11, "#bbb", anchor="middle")
    b += box(8, 238, 624, 114, "#3a3d45", r=4)
    b += tx(16, 256, "③ Timeline — 레이어(위가 앞) × 시간(왼쪽→오른쪽)", 12, "#fff", "700")
    for i, c in enumerate([P, "#7fd0a8", "#e0a46b"]):
        b += box(16, 266 + i * 24, 230, 18, "#4a4d57", r=2) + box(256, 266 + i * 24, 360 - i * 60, 18, c, r=2)
    b += f'<line x1="330" y1="262" x2="330" y2="346" stroke="#4aa3ff" stroke-width="2"/>' + tx(336, 344, "시간 표시기(CTI)", 10, "#9cc9ff")
    return svg(640, 360, b)

# 2. Frames & frame rate
def frames():
    b = DEFS + tx(0, 16, "1초 = 프레임 여러 장. 30fps는 1초에 30장", 13, T, "700")
    for i in range(10):
        x = 10 + i * 62
        b += box(x, 30, 54, 40, "#fff", G2, 3) + f'<circle cx="{x+12+i*3.2}" cy="50" r="8" fill="{P}"/>'
        b += tx(x + 27, 86, f"{i}f", 10, M, anchor="middle")
    b += tx(0, 112, "타임코드 읽는 법", 12, T, "700")
    b += box(0, 120, 260, 34, "#f4f4fb", r=4) + tx(12, 143, "0:00:01:15", 18, PD, "700")
    b += tx(280, 135, "시 : 분 : 초 : 프레임", 12, T) + tx(280, 152, "30fps에서 01:15 = 1.5초", 11, M)
    b += tx(0, 182, "자주 쓰는 프레임레이트", 12, T, "700")
    rows = [("23.976 / 24", "영화·뮤직비디오 느낌"), ("29.97 / 30", "방송·유튜브 표준(한국·미국)"), ("25", "유럽 방송(PAL)"), ("50 / 59.94 / 60", "스포츠·게임·전광판, 매끄러움")]
    for i, (a, d) in enumerate(rows):
        b += tx(10, 202 + i * 18, a, 11, PD, "700") + tx(150, 202 + i * 18, d, 11, T)
    return svg(640, 270, b)

# 3. Timeline switch icons legend
def switches():
    items = [
        ("eye", "Video", "보이기/숨기기"), ("spk", "Audio", "소리 켜기"), ("dot", "Solo", "이 레이어만 보기"),
        ("lock", "Lock", "잠그기"), ("shy", "Shy", "타임라인에서 숨기기"), ("star", "Collapse", "프리컴프 변형 펼치기"),
        ("q", "Quality", "화질(초안/최고)"), ("fx", "Effect", "효과 켜고 끄기"), ("fb", "Frame Blending", "프레임 섞기"),
        ("mb", "Motion Blur", "움직임 흐림"), ("adj", "Adjustment", "조정 레이어로"), ("cube", "3D Layer", "3D로 전환"),
        ("sw", "Stopwatch", "키프레임 시작"), ("kf", "Keyframe", "기록된 값(마름모)"), ("pw", "Pick Whip", "속성 연결"),
    ]
    def icon(k, x, y):
        c = PD
        if k == "eye": return f'<ellipse cx="{x}" cy="{y}" rx="10" ry="6" fill="none" stroke="{c}" stroke-width="2"/><circle cx="{x}" cy="{y}" r="3" fill="{c}"/>'
        if k == "spk": return f'<path d="M{x-8},{y-4} h5 l6,-5 v18 l-6,-5 h-5 z" fill="{c}"/>'
        if k == "dot": return f'<circle cx="{x}" cy="{y}" r="7" fill="{c}"/>'
        if k == "lock": return f'<rect x="{x-7}" y="{y-2}" width="14" height="10" fill="{c}" rx="2"/><path d="M{x-4},{y-2} v-4 a4,4 0 0 1 8,0 v4" stroke="{c}" stroke-width="2" fill="none"/>'
        if k == "shy": return f'<path d="M{x-9},{y+4} q9,-14 18,0" stroke="{c}" stroke-width="2" fill="none"/><circle cx="{x-3}" cy="{y}" r="1.6" fill="{c}"/><circle cx="{x+3}" cy="{y}" r="1.6" fill="{c}"/>'
        if k == "star": return f'<path d="M{x},{y-9} l3,6 7,1 -5,5 1,7 -6,-3 -6,3 1,-7 -5,-5 7,-1z" fill="{c}"/>'
        if k == "q": return f'<path d="M{x-8},{y+7} L{x+8},{y-7}" stroke="{c}" stroke-width="2.5"/>'
        if k == "fx": return f'<text x="{x}" y="{y+5}" font-size="15" font-style="italic" font-weight="700" fill="{c}" text-anchor="middle">fx</text>'
        if k == "fb": return f'<rect x="{x-9}" y="{y-6}" width="8" height="12" fill="none" stroke="{c}" stroke-width="2"/><rect x="{x+1}" y="{y-6}" width="8" height="12" fill="{c}"/>'
        if k == "mb": return f'<circle cx="{x+4}" cy="{y}" r="5" fill="{c}"/><circle cx="{x-2}" cy="{y}" r="5" fill="{c}" opacity=".5"/><circle cx="{x-7}" cy="{y}" r="5" fill="{c}" opacity=".25"/>'
        if k == "adj": return f'<circle cx="{x}" cy="{y}" r="8" fill="none" stroke="{c}" stroke-width="2"/><path d="M{x},{y-8} a8,8 0 0 1 0,16 z" fill="{c}"/>'
        if k == "cube": return f'<path d="M{x},{y-9} l8,4 v9 l-8,4 -8,-4 v-9z M{x},{y-1} l8,-4 M{x},{y-1} l-8,-4 M{x},{y-1} v9" stroke="{c}" stroke-width="1.6" fill="none"/>'
        if k == "sw": return f'<circle cx="{x}" cy="{y+1}" r="8" fill="none" stroke="{c}" stroke-width="2"/><path d="M{x},{y+1} l0,-5 M{x-2},{y-9} h4" stroke="{c}" stroke-width="2"/>'
        if k == "kf": return f'<path d="M{x},{y-8} l8,8 -8,8 -8,-8z" fill="{c}"/>'
        if k == "pw": return f'<path d="M{x-6},{y+6} q-4,-12 6,-12 q10,0 6,8 q-3,5 -8,2" stroke="{c}" stroke-width="2" fill="none"/>'
        return ""
    b = ""
    for i, (k, n, d) in enumerate(items):
        col, row = i % 3, i // 3
        x, y = 10 + col * 210, 12 + row * 46
        b += box(x, y, 200, 38, "#f6f6fd", r=5) + icon(k, x + 22, y + 19) + tx(x + 42, y + 17, n, 11.5, T, "700") + tx(x + 42, y + 31, d, 10.5, M)
    return svg(640, 12 + 5 * 46, b)

# 4. Interpolation
def interp():
    b = DEFS
    titles = [("Linear", "일정한 속도, 기계적"), ("Easy Ease (F9)", "천천히 출발·멈춤"), ("Hold", "값이 뚝 바뀜")]
    for i, (t, d) in enumerate(titles):
        x = 10 + i * 212
        b += box(x, 0, 200, 150, "#f6f6fd", r=6) + tx(x + 12, 20, t, 12, T, "700") + tx(x + 12, 36, d, 10.5, M)
        x0, y0, x1, y1 = x + 20, 130, x + 180, 50
        if i == 0: b += f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{PD}" stroke-width="3"/>'
        if i == 1: b += f'<path d="M{x0},{y0} C{x0+80},{y0} {x1-80},{y1} {x1},{y1}" stroke="{PD}" stroke-width="3" fill="none"/>'
        if i == 2: b += f'<path d="M{x0},{y0} H{x1-20} V{y1} H{x1}" stroke="{PD}" stroke-width="3" fill="none"/>'
        b += f'<path d="M{x0},{y0-6} l6,6 -6,6 -6,-6z" fill="{N}"/><path d="M{x1},{y1-6} l6,6 -6,6 -6,-6z" fill="{N}"/>'
    b += tx(10, 170, "가로축 = 시간, 세로축 = 값. 마름모가 키프레임입니다.", 11, M)
    return svg(640, 180, b)

# 5. Layer stack & parenting
def stack():
    b = DEFS + tx(0, 16, "레이어 순서 = 앞뒤", 13, T, "700")
    names = ["텍스트", "로고", "인물(키잉)", "배경 영상"]
    for i, n in enumerate(names):
        b += f'<g transform="translate({30+i*22},{40+i*26}) skewX(-20)">{box(0,0,160,60,["#e9e8ff","#d9d7ff","#c7c4ff","#b3afff"][i],PD,4,1)}</g>'
        b += tx(250, 70 + i * 26, f"{i+1}. {n}", 12, T)
    b += tx(250, 190, "위(1번) 레이어가 화면 앞에 보입니다", 11, M)
    b += tx(360, 16, "페어런팅 = 부모를 따라 움직임", 13, T, "700")
    b += box(420, 40, 120, 34, P, r=17) + tx(480, 62, "널(부모)", 12, "#fff", "700", "middle")
    for i, n in enumerate(["로고", "글자", "아이콘"]):
        x = 380 + i * 80
        b += arrow(480, 76, x + 30, 120) + box(x, 124, 60, 30, "#f0f0fb", PD, 15, 1) + tx(x + 30, 144, n, 11, T, "400", "middle")
    b += tx(370, 190, "널을 돌리면 자식이 함께 돕니다", 11, M)
    return svg(640, 200, b)

# 6. Track matte
def matte():
    b = DEFS
    b += box(0, 20, 170, 100, "#cfe7ff", r=4) + tx(85, 75, "영상(채울 것)", 12, T, "400", "middle")
    b += tx(200, 75, "+", 26, PD, "700", "middle")
    b += box(230, 20, 170, 100, "#fff", G2, 4) + tx(315, 85, "SEOUL", 38, N, "900", "middle")
    b += tx(430, 75, "=", 26, PD, "700", "middle")
    b += box(460, 20, 170, 100, "#fff", G2, 4)
    b += f'<defs><clipPath id="cl"><text x="545" y="85" font-size="38" font-weight="900" text-anchor="middle">SEOUL</text></clipPath></defs>'
    b += f'<rect x="460" y="20" width="170" height="100" fill="url(#gr)" clip-path="url(#cl)"/>'
    b += f'<defs><linearGradient id="gr" x1="0" x2="1"><stop offset="0" stop-color="#5aa9ff"/><stop offset="1" stop-color="{P}"/></linearGradient></defs>'
    b += tx(85, 14, "아래 레이어", 11, M, anchor="middle") + tx(315, 14, "매트 레이어(글자)", 11, M, anchor="middle") + tx(545, 14, "Alpha Matte 결과", 11, M, anchor="middle")
    return svg(640, 130, b)

# 7. 3D axes, camera, lights
def three_d():
    b = DEFS
    ox, oy = 120, 150
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox+120}" y2="{oy}" stroke="#e5534b" stroke-width="3"/>' + tx(ox + 126, oy + 4, "X (오른쪽 +)", 11, "#e5534b", "700")
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy+90}" stroke="#2da44e" stroke-width="3"/>' + tx(ox + 6, oy + 100, "Y (아래 +)", 11, "#2da44e", "700")
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox-70}" y2="{oy-70}" stroke="#3b82f6" stroke-width="3"/>' + tx(ox - 112, oy - 76, "Z (멀어질수록 +)", 11, "#3b82f6", "700")
    b += tx(0, 16, "애펙의 3D 좌표", 13, T, "700") + tx(0, 34, "포토샵처럼 왼쪽 위가 0,0 — Y는 아래로 갈수록 커집니다", 10.5, M)
    # camera scene
    b += tx(320, 16, "카메라와 3D 레이어", 13, T, "700")
    for i in range(3):
        x = 470 + i * 46; y = 50 + i * 14
        b += f'<g transform="translate({x},{y}) skewY(-18)">{box(0,0,40,90,["#d9d7ff","#c7c4ff","#b3afff"][i],PD,3,1)}</g>'
    b += f'<path d="M330,120 h44 v30 h-44z M374,128 l20,-10 v40 l-20,-10z" fill="{N}"/>' + tx(340, 175, "Camera", 11, T, "700")
    b += f'<path d="M394,135 L560,70 M394,135 L600,200" stroke="{P}" stroke-width="1.5" stroke-dasharray="5 4"/>'
    b += tx(470, 225, "Z 깊이가 다른 레이어 = 시차(패럴랙스)", 10.5, M)
    return svg(640, 240, b)

def lights():
    b = DEFS
    kinds = [("Point", "전구 — 사방으로"), ("Spot", "무대 조명 — 원뿔"), ("Parallel", "햇빛 — 한 방향"), ("Ambient", "전체 고르게, 그림자 없음"), ("Environment", "HDR 이미지로 주변광·반사")]
    for i, (k, d) in enumerate(kinds):
        x = 4 + i * 127
        b += box(x, 0, 120, 150, "#f6f6fd", r=6) + tx(x + 60, 20, k, 12, T, "700", "middle")
        cx = x + 60
        if k == "Point":
            b += f'<circle cx="{cx}" cy="70" r="9" fill="#ffd54d"/>' + "".join(f'<line x1="{cx}" y1="70" x2="{cx+30*__import__("math").cos(a)}" y2="{70+30*__import__("math").sin(a)}" stroke="#f0b400" stroke-width="2"/>' for a in [i*0.785 for i in range(8)])
        if k == "Spot":
            b += f'<path d="M{cx},44 L{cx-34},110 L{cx+34},110z" fill="#ffe89a" opacity=".8"/><circle cx="{cx}" cy="44" r="7" fill="#f0b400"/>'
        if k == "Parallel":
            b += "".join(f'<line x1="{x+20+j*20}" y1="40" x2="{x+10+j*20}" y2="105" stroke="#f0b400" stroke-width="2.5"/>' for j in range(5))
        if k == "Ambient":
            b += f'<rect x="{x+20}" y="44" width="80" height="62" fill="#fff3c4" rx="6"/>'
        if k == "Environment":
            b += f'<circle cx="{cx}" cy="76" r="32" fill="url(#env)"/><defs><radialGradient id="env"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#8fc3ff"/></radialGradient></defs>'
        b += tx(x + 60, 135, d, 9.5, M, anchor="middle")
    return svg(640, 155, b)

# 8. Green screen lighting top view
def greenscreen():
    b = DEFS
    b += box(40, 20, 560, 18, "#3fae5a", r=3) + tx(320, 33, "그린스크린", 11, "#fff", "700", "middle")
    for x in [70, 570]:
        b += box(x - 22, 60, 44, 24, "#ffe89a", "#d9a400", 4) + tx(x, 76, "스크린", 9, T, "400", "middle")
        b += arrow(x, 60, x + (60 if x < 300 else -60), 42)
    b += f'<circle cx="320" cy="170" r="22" fill="#f1d4c0" stroke="{T}" stroke-width="1.5"/>' + tx(320, 175, "배우", 11, T, "700", "middle")
    b += f'<line x1="320" y1="40" x2="320" y2="146" stroke="{M}" stroke-dasharray="4 4"/>' + tx(328, 100, "2~3m 떨어지기", 11, PD, "700")
    b += box(450, 150, 60, 26, "#ffe89a", "#d9a400", 4) + tx(480, 167, "키", 10, T, "700", "middle") + arrow(450, 165, 346, 170)
    b += box(130, 170, 60, 26, "#fff7d6", "#d9a400", 4) + tx(160, 187, "필", 10, T, "700", "middle") + arrow(190, 182, 296, 176)
    b += box(380, 110, 70, 24, "#ffd9e6", "#d65a8a", 4) + tx(415, 126, "역광(림)", 9.5, T, "700", "middle") + arrow(380, 124, 338, 155)
    b += f'<path d="M300,250 h40 v24 h-40z M320,250 l-10,-16 h20z" fill="{N}"/>' + tx(320, 292, "카메라", 11, T, "700", "middle")
    b += tx(10, 290, "위에서 본 배치도", 11, M)
    return svg(640, 300, b)

# 9. Expressions visualized
def expr_graphs():
    import math, random
    b = ""
    def panel(x, y, title, sub, pts, c=PD):
        s = box(x, y, 200, 120, "#f6f6fd", r=6) + tx(x + 10, y + 18, title, 11.5, T, "700") + tx(x + 10, y + 32, sub, 9.5, M)
        d = "M" + " L".join(f"{x+10+px:.1f},{y+80-py:.1f}" for px, py in pts)
        return s + f'<path d="{d}" stroke="{c}" stroke-width="2.2" fill="none"/>' + f'<line x1="{x+10}" y1="{y+80}" x2="{x+190}" y2="{y+80}" stroke="{G2}"/>'
    random.seed(3)
    w = []; v = 0
    for i in range(0, 181, 3):
        v += random.uniform(-6, 6); v *= .9; w.append((i, v))
    b += panel(10, 0, "wiggle(3, 30)", "무작위로 흔들림", w)
    b += panel(220, 0, "Math.sin(time*2)*6", "위아래 둥실 — 일정한 파도", [(i, 28*math.sin(i/14)) for i in range(0, 181, 3)])
    b += panel(430, 0, "inertial bounce", "멈춘 뒤 넘쳤다 돌아옴", [(i, 0 if i < 40 else 40*math.exp(-(i-40)/25)*math.cos((i-40)/7)) for i in range(0, 181, 3)])
    # loops
    def loop(kind):
        pts = []
        for i in range(0, 181, 3):
            t = i % 60 if kind != "pingpong" else (i % 60 if (i // 60) % 2 == 0 else 60 - i % 60)
            base = t * 0.6
            if kind == "offset": base += (i // 60) * 36 * 0.5
            pts.append((i, base - 10))
        return pts
    b += panel(10, 130, 'loopOut("cycle")', "처음부터 반복", loop("cycle"))
    b += panel(220, 130, 'loopOut("pingpong")', "갔다가 돌아오기", loop("pingpong"))
    b += panel(430, 130, 'loopOut("offset")', "이어서 쌓이기", loop("offset"))
    b += panel(10, 260, "linear(time,1,3,0,100)", "1~3초 동안 0→100", [(i, -30 if i < 60 else (30 if i > 120 else -30 + (i-60))) for i in range(0, 181, 3)])
    b += panel(220, 260, "ease(…)", "부드럽게 0→100", [(i, -30 if i < 60 else (30 if i > 120 else -30 + 60*(1-math.cos(math.pi*(i-60)/60))/2)) for i in range(0, 181, 3)])
    b += panel(430, 260, "valueAtTime(time-0.1*index)", "레이어마다 시간차", [(i, 25*math.sin((i-0)/18)) for i in range(0, 181, 3)], PD)
    b += f'<path d="M{440},{340} ' + " ".join(f"L{440+i},{340-25*math.sin((i-20)/18)}" for i in range(20, 181, 3)) + f'" stroke="{P}" stroke-width="2" fill="none"/>'
    return svg(640, 385, b)

# 10. Render pipeline
def pipeline():
    b = DEFS
    steps = [("기획·콘티", "Claude"), ("소스", "촬영·힉스필드"), ("애펙 작업", "레이어·키프레임"), ("검수", "AI Assistant"), ("출력", "Render Queue / AME"), ("납품", "방송·SNS·전광판")]
    for i, (a, d) in enumerate(steps):
        x = 4 + i * 106
        b += box(x, 10, 96, 56, "#f0efff" if i % 2 == 0 else "#e4e2ff", r=8) + tx(x + 48, 34, a, 12, N, "700", "middle") + tx(x + 48, 52, d, 9.5, M, anchor="middle")
        if i < 5: b += arrow(x + 96, 38, x + 106, 38)
    return svg(640, 76, b)

# 11. Keyframe on timeline anatomy
def timeline_anatomy():
    b = DEFS + box(0, 0, 640, 150, "#2b2d33", r=6)
    b += tx(12, 22, "▾ 공", 12, "#fff", "700")
    b += tx(28, 46, "◎ Position   300.0, 200.0", 11, "#9cc9ff")
    b += tx(28, 70, "◎ Scale        100.0, 100.0 %", 11, "#9cc9ff")
    b += f'<line x1="240" y1="8" x2="240" y2="140" stroke="#555"/>'
    for t in [260, 330, 390, 440, 480, 520, 600]:
        b += f'<path d="M{t},{40} l5,5 -5,5 -5,-5z" fill="{P}"/>'
    for t in [300, 330, 350, 380, 430, 440, 460]:
        b += f'<path d="M{t},{64} l5,5 -5,5 -5,-5z" fill="{P}"/>'
    b += f'<line x1="410" y1="8" x2="410" y2="140" stroke="#4aa3ff" stroke-width="2"/>'
    b += tx(16, 104, "◎ = 스톱워치(켜면 파랗게)", 10.5, "#ddd") + tx(16, 122, "◀ ◆ ▶ = 이전 키 · 키 추가 · 다음 키", 10.5, "#ddd")
    b += tx(420, 130, "◆ 키프레임   │ 시간 표시기", 10.5, "#ddd")
    return svg(640, 150, b)
