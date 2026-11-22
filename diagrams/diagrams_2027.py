import sys
sys.path.insert(0,'/home/claude/book/v4')
from diagrams import svg, box, tx, arrow, DEFS, P, PD, N, G, G2, T, M

def stack():
    b = DEFS + tx(0, 16, "레이어 순서 = 앞뒤", 13, T, "700")
    names = ["텍스트", "로고", "인물(키잉)", "배경 영상"]
    cols = ["#e9e8ff", "#d9d7ff", "#c7c4ff", "#b3afff"]
    for i, n in enumerate(names):
        b += f'<g transform="translate({40+i*16},{38+i*26}) skewX(-20)">{box(0,0,120,48,cols[i],PD,4,1)}</g>'
    for i, n in enumerate(names):
        y = 66 + i * 26
        b += f'<line x1="{166+i*16}" y1="{y-4}" x2="226" y2="{y-4}" stroke="{G2}" stroke-width="1"/>'
        b += tx(232, y, f"{i+1}. {n}", 12, T)
    b += tx(0, 196, "위(1번) 레이어가 화면 앞에 보입니다", 11, M)
    b += f'<line x1="330" y1="6" x2="330" y2="200" stroke="{G}" stroke-width="1"/>'
    b += tx(350, 16, "페어런팅 = 부모를 따라 움직임", 13, T, "700")
    b += box(435, 42, 120, 34, P, r=17) + tx(495, 64, "널(부모)", 12, "#fff", "700", "middle")
    for i, n in enumerate(["로고", "글자", "아이콘"]):
        x = 385 + i * 80
        b += arrow(495, 78, x + 30, 122) + box(x, 126, 60, 30, "#f0f0fb", PD, 15, 1) + tx(x + 30, 146, n, 11, T, "400", "middle")
    b += tx(350, 196, "널을 돌리면 자식이 함께 돕니다", 11, M)
    return svg(640, 206, b)

def three_d():
    b = DEFS
    ox, oy = 120, 128
    b += tx(0, 16, "애펙의 3D 좌표", 13, T, "700") + tx(0, 34, "왼쪽 위가 0,0 — Y는 아래로 갈수록 커집니다", 10.5, M)
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox+110}" y2="{oy}" stroke="#e5534b" stroke-width="3"/>' + tx(ox + 116, oy + 4, "X (오른쪽 +)", 11, "#e5534b", "700")
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy+70}" stroke="#2da44e" stroke-width="3"/>' + tx(ox + 8, oy + 70, "Y (아래 +)", 11, "#2da44e", "700")
    b += f'<line x1="{ox}" y1="{oy}" x2="{ox-56}" y2="{oy-56}" stroke="#3b82f6" stroke-width="3"/>' + tx(ox - 50, oy - 62, "Z (멀어질수록 +)", 11, "#3b82f6", "700")
    b += f'<circle cx="{ox}" cy="{oy}" r="3.5" fill="{T}"/>'
    b += f'<line x1="318" y1="6" x2="318" y2="222" stroke="{G}" stroke-width="1"/>'
    b += tx(336, 16, "카메라와 3D 레이어", 13, T, "700")
    for i in range(3):
        x = 480 + i * 46; y = 62 + i * 14
        b += f'<g transform="translate({x},{y}) skewY(-18)">{box(0,0,40,84,["#d9d7ff","#c7c4ff","#b3afff"][i],PD,3,1)}</g>'
    b += f'<path d="M394,128 L566,66 M394,128 L612,196" stroke="{P}" stroke-width="1.5" stroke-dasharray="5 4" fill="none"/>'
    b += f'<path d="M340,112 h44 v30 h-44z M384,120 l18,-9 v38 l-18,-9z" fill="{N}"/>' + tx(340, 160, "Camera", 11, T, "700")
    b += tx(478, 218, "Z 깊이가 다른 레이어 = 시차(패럴랙스)", 10.5, M, anchor="middle")
    return svg(640, 228, b)

def pipeline():
    b = DEFS
    steps = [("기획·콘티", "Claude"), ("소스", "촬영·힉스필드"), ("애펙 작업", "레이어·키프레임"), ("검수", "AI Assistant"), ("출력", "렌더 큐·AME"), ("납품", "방송·SNS·전광판")]
    for i, (a, d) in enumerate(steps):
        x = 2 + i * 107
        b += box(x, 10, 94, 56, "#f0efff" if i % 2 == 0 else "#e4e2ff", r=8) + tx(x + 47, 34, a, 12, N, "700", "middle") + tx(x + 47, 52, d, 9.5, M, anchor="middle")
        if i < 5: b += arrow(x + 95, 38, x + 106, 38)
    return svg(640, 76, b)

def connect_map():
    b = DEFS
    def node(x, y, w, h, a, d, fill="#f0efff", fc=N):
        return box(x, y, w, h, fill, r=8) + tx(x + w/2, y + h/2 - 3, a, 12, fc, "700", "middle") + tx(x + w/2, y + h/2 + 13, d, 9.3, M if fc == N else "#d8d6ff", anchor="middle")
    b += node(4, 86, 96, 54, "Claude", "대화로 지시", N, "#fff")
    b += node(150, 16, 176, 54, "Higgsfield MCP", "mcp.higgsfield.ai/mcp")
    b += node(150, 156, 176, 54, "Higgsfield Bridge", "bridge.higgsfield.ai/mcp")
    b += node(376, 16, 124, 54, "힉스필드 클라우드", "영상·이미지·음성 생성", "#e4e2ff")
    b += node(376, 156, 124, 54, "애펙 속 패널", "Bridge MCP: Connect", "#e4e2ff")
    b += node(540, 156, 96, 54, "After Effects", "레이어·키프레임", N, "#fff")
    b += arrow(100, 104, 148, 50) + arrow(100, 122, 148, 176)
    b += arrow(326, 43, 374, 43) + arrow(326, 183, 374, 183) + arrow(500, 183, 538, 183)
    b += f'<line x1="438" y1="154" x2="438" y2="74" stroke="{PD}" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#ah)"/>'
    b += tx(446, 100, "길 ① 패널 버튼으로", 9.5, PD, "700") + tx(446, 114, "바로 생성", 9.5, PD, "700") + tx(446, 128, "(크레딧 사용)", 9.5, M)
    b += tx(238, 94, "Claude가 생성을 지시 (크레딧 사용)", 9.5, PD, "700", "middle")
    b += tx(238, 146, "길 ②  Claude가 애펙을 조작 (크레딧 없음)", 9.5, PD, "700", "middle")
    b += box(548, 88, 88, 44, "#fff", P, 8, 1.2) + tx(592, 106, "AI Assistant", 10.5, N, "700", "middle") + tx(592, 121, "길 ③ 자체 AI", 9, M, anchor="middle")
    b += f'<line x1="592" y1="132" x2="592" y2="154" stroke="{P}" stroke-width="1.5"/>'
    return svg(640, 222, b)

def create_path():
    b = DEFS
    b += tx(0, 16, "createPath(points, inTangents, outTangents, isClosed)", 12.5, T, "700")
    # left: two nulls and a line
    b += box(0, 30, 300, 150, "#fbfbff", "#e4e2ff", 6, 1)
    b += f'<line x1="60" y1="140" x2="230" y2="72" stroke="{N}" stroke-width="3" stroke-linecap="round"/>'
    for (x, y, n) in [(60, 140, "점A (널)"), (230, 72, "점B (널)")]:
        b += f'<rect x="{x-7}" y="{y-7}" width="14" height="14" fill="#fff" stroke="#e5534b" stroke-width="1.5"/>' + tx(x, y + 26 if n.startswith("점A") else y - 14, n, 10.5, T, "700", "middle")
    b += tx(14, 50, "points = [a, b] · 닫지 않음(false)", 10, M)
    # right: B moved
    b += box(340, 30, 300, 150, "#fbfbff", "#e4e2ff", 6, 1)
    b += f'<line x1="400" y1="140" x2="570" y2="72" stroke="{G2}" stroke-width="2" stroke-dasharray="5 4"/>'
    b += f'<line x1="400" y1="140" x2="590" y2="130" stroke="{N}" stroke-width="3" stroke-linecap="round"/>'
    b += f'<rect x="393" y="133" width="14" height="14" fill="#fff" stroke="#e5534b" stroke-width="1.5"/>' + tx(400, 166, "점A", 10.5, T, "700", "middle")
    b += f'<rect x="563" y="65" width="14" height="14" fill="#fff" stroke="{G2}" stroke-width="1.5"/>'
    b += f'<rect x="583" y="123" width="14" height="14" fill="#fff" stroke="#e5534b" stroke-width="1.5"/>' + tx(590, 156, "점B", 10.5, T, "700", "middle")
    b += f'<path d="M574,82 Q592,96 590,114" stroke="{PD}" stroke-width="1.5" fill="none" marker-end="url(#ah)"/>'
    b += tx(354, 50, "널을 옮기면 선이 스스로 따라옵니다", 10, M)
    b += arrow(304, 105, 336, 105)
    return svg(640, 186, b)

def book_map():
    b = DEFS
    parts = [("PART 0", "이해하기", "역사 · AI · 비용", "●○○"), ("PART 1", "애펙 기본기", "01~04장", "●○○ ~ ●●○"), ("PART 2", "모션그래픽", "05~07장", "●●○ ~ ●●●"),
             ("PART 3", "합성과 VFX", "08~12장", "●●○ ~ ●●●"), ("PART 4", "3D와 실무", "13~16장", "●○○ ~ ●●●"), ("PART 5", "AI 연결 준비", "17장", "●○○"),
             ("PART 6", "힉스필드 패널", "18~20장", "●○○"), ("PART 7", "Claude · 자체 AI", "21~23장", "●○○ ~ ●●○"), ("PART 8", "완성과 정리", "24~26장 · 부록", "●○○ ~ ●●○")]
    for i, (p, t, c, lv) in enumerate(parts):
        col = i % 3; row = i // 3
        x = 4 + col * 214; y = 6 + row * 78
        dark = row == 0 and col == 0
        fill = "#f0efff" if row < 2 else "#e4e2ff"
        b += box(x, y, 196, 62, fill, r=8)
        b += tx(x + 12, y + 20, p, 9, PD, "800") + tx(x + 184, y + 20, lv, 8.5, P, "700", "end")
        b += tx(x + 12, y + 40, t, 13.5, N, "700") + tx(x + 12, y + 55, c, 9.5, M)
        if col < 2: b += arrow(x + 197, y + 31, x + 213, y + 31)
    b += f'<path d="M620,37 h14 v39 h-630 v39" stroke="{PD}" stroke-width="1.6" fill="none" stroke-dasharray="4 3"/>'
    b += f'<path d="M620,115 h14 v39 h-630 v39" stroke="{PD}" stroke-width="1.6" fill="none" stroke-dasharray="4 3"/>'
    b += tx(4, 250, "애펙만 배우려면 PART 1~4, AI 실습만 하려면 PART 5~8부터 읽어도 됩니다.", 10.5, M)
    return svg(640, 256, b)

if __name__ == "__main__":
    import os
    os.makedirs('/tmp/dia2', exist_ok=True)
    for f in [stack, three_d, pipeline, connect_map, create_path, book_map]:
        open(f'/tmp/dia2/{f.__name__}.svg', 'w').write(f())
    html = '<html><body style="margin:20px;width:700px;font-family:Noto Sans CJK KR">' + ''.join(f'<div style="margin-bottom:24px;border:1px solid #ddd;padding:8px">{f()}</div>' for f in [stack, three_d, pipeline, connect_map, create_path, book_map]) + '</body></html>'
    open('/tmp/dia2/all.html', 'w').write(html)
