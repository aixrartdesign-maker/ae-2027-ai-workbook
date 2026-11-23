T=[(0,'전체_조종','널 · 골반 높이'),(1,'몸통','기준점 허리(벨트)'),(2,'머리','기준점 목 아래'),
(2,'위팔_왼 / 위팔_오','기준점 어깨'),(3,'아래팔','기준점 팔꿈치'),(4,'손','기준점 손목'),
(1,'허벅지_왼 / 허벅지_오','기준점 엉덩이'),(2,'정강이','기준점 무릎'),(3,'발','기준점 발목')]
x0=14; y0=40; dy=26; ind=24; P=[]
P.append(f'<text x="{x0}" y="18" font-size="12" font-weight="800" fill="#00005B">부모 → 자식 (들여 쓴 것이 자식)</text>')
prev={}
for i,(lv,name,note) in enumerate(T):
    y=y0+i*dy; x=x0+lv*ind
    if lv>0:
        py=prev[lv-1]; px=x0+(lv-1)*ind+7
        P.append(f'<path d="M{px} {py+6} V{y-4} H{x-3}" fill="none" stroke="#b9b6f0" stroke-width="1.2"/>')
    prev[lv]=y
    w=sum(11.5 if ord(c)>0x3000 else 4.6 for c in name)+16
    P.append(f'<rect x="{x}" y="{y-13}" width="{w:.0f}" height="19" rx="4" fill="{"#00005B" if lv==0 else "#f1f0ff"}"/>')
    P.append(f'<text x="{x+8}" y="{y+1.5}" font-size="11.5" font-weight="700" fill="{"#fff" if lv==0 else "#14143a"}">{name}</text>')
    P.append(f'<text x="{x+w+7:.0f}" y="{y+1.5}" font-size="10.5" fill="#5a5f70">{note}</text>')
svg='<svg viewBox="0 0 330 270" xmlns="http://www.w3.org/2000/svg" style="width:100%;font-family:\'Noto Sans KR\',\'Noto Sans CJK KR\',\'NanumGothic\',sans-serif">'+''.join(P)+'</svg>'
open('/home/claude/book/img/R_tree.svg','w',encoding='utf-8').write(svg)
