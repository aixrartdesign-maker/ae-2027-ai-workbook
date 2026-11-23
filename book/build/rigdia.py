s=0.36
def X(x): return (x-820)*s+46
def Y(y): return (y-185)*s+12
def rect(cx,top,w,h,fill,r=8):
    return f'<rect x="{X(cx-w/2):.1f}" y="{Y(top):.1f}" width="{w*s:.1f}" height="{h*s:.1f}" rx="{r}" fill="{fill}"/>'
skin='#f9d1ad'; skinD='#e6b794'; top='#2b99a8'; arm='#24858f'; pant='#3d4c6b'; shoe='#f2734d'; hair='#3b2921'
P=[]
def cap(cx,top_,w,h,fill): return rect(cx,top_-w/2,w,h,fill,w*s/2)
P.append(f'<ellipse cx="{X(960)}" cy="{Y(884)}" rx="{150*s}" ry="{13*s}" fill="#dcdcd8"/>')
for cx,dx in ((928,-8),(992,8)):
    P.append(cap(cx,615,58,170,pant)); P.append(cap(cx,727,52,165,pant))
    P.append(rect(cx+dx,837,84,42,shoe,7)); P.append(rect(cx+dx,872,88,10,'#fbf6ec',3))
P.append(rect(960,576,140,60,pant,9)); P.append(rect(960,350,164,256,top,20))
P.append(rect(960,324,40,46,skin,5))
for ex in (888,1032): P.append(f'<ellipse cx="{X(ex)}" cy="{Y(282)}" rx="{13*s}" ry="{18*s}" fill="{skinD}"/>')
P.append(f'<ellipse cx="{X(960)}" cy="{Y(276)}" rx="{72*s}" ry="{76*s}" fill="{skin}"/>')
P.append(f'<ellipse cx="{X(960)}" cy="{Y(226)}" rx="{78*s}" ry="{48*s}" fill="{hair}"/>')
for ex in (933,987): P.append(f'<ellipse cx="{X(ex)}" cy="{Y(282)}" rx="{7*s}" ry="{9.5*s}" fill="#222"/>')
for cx in (866,1054):
    P.append(cap(cx,384,46,132,arm)); P.append(cap(cx,470,40,122,skin))
    P.append(f'<ellipse cx="{X(cx)}" cy="{Y(574)}" rx="{23*s}" ry="{28*s}" fill="{skin}"/>')
J=[(960,600,'골반·허리'),(960,365,'목'),(866,384,'어깨'),(1054,384,''),(866,470,'팔꿈치'),(1054,470,''),(866,552,'손목'),(1054,552,''),(928,615,''),(992,615,'엉덩이'),(928,727,''),(992,727,'무릎'),(928,840,''),(992,840,'발목')]
for x,y,l in J:
    P.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4.2" fill="#ff5a36" stroke="#fff" stroke-width="1.4"/>')
    if l:
        side = 1 if x>=960 else -1
        tx = X(1085) if side>0 else X(835)
        anchor='start' if side>0 else 'end'
        if l in ('골반·허리','목'): tx=X(1085); anchor='start'
        P.append(f'<line x1="{X(x):.1f}" y1="{Y(y):.1f}" x2="{tx - (4 if anchor=="end" else -0) :.1f}" y2="{Y(y):.1f}" stroke="#ff5a36" stroke-width=".7" stroke-dasharray="2 2"/>')
        dyl={'골반·허리':-5,'엉덩이':9}.get(l,0)
        P.append(f'<text x="{tx+(3 if anchor=="start" else -3):.1f}" y="{Y(y)+3.5+dyl:.1f}" text-anchor="{anchor}" font-size="10" fill="#14143a" font-weight="700">{l}</text>')
# tree
T=[(0,'전체_조종','널 · 골반 가운데'),(1,'골반','기준점 골반 가운데'),(2,'몸통','기준점 허리'),(3,'목 → 머리','기준점 목 아래'),(4,'눈 · 입 · 귀 · 볼 · 머리카락','각자 가운데'),
(3,'위팔_왼 / 위팔_오','기준점 어깨'),(4,'아래팔','기준점 팔꿈치'),(5,'손 → 엄지','기준점 손목'),
(2,'허벅지_왼 / 허벅지_오','기준점 엉덩이'),(3,'정강이','기준점 무릎'),(4,'발 → 밑창','기준점 발목')]
x0=250; y0=34; dy=23.5; ind=20
P.append(f'<text x="{x0}" y="18" font-size="11" font-weight="800" fill="#00005B">부모 → 자식 (위가 부모)</text>')
prev={}
for i,(lv,name,note) in enumerate(T):
    y=y0+i*dy; x=x0+lv*ind
    if lv>0:
        py=prev[lv-1]; px=x0+(lv-1)*ind+6
        P.append(f'<path d="M{px} {py+5} V{y-4} H{x-3}" fill="none" stroke="#b9b6f0" stroke-width="1.1"/>')
    prev[lv]=y
    w=sum(10.6 if ord(c)>0x3000 else 4.2 for c in name)+14
    P.append(f'<rect x="{x}" y="{y-12}" width="{w:.0f}" height="17" rx="4" fill="{"#00005B" if lv==0 else "#f1f0ff"}"/>')
    P.append(f'<text x="{x+7}" y="{y+1}" font-size="10.5" font-weight="700" fill="{"#fff" if lv==0 else "#14143a"}">{name}</text>')
    P.append(f'<text x="{x+w+6:.0f}" y="{y+1}" font-size="9.5" fill="#5a5f70">{note}</text>')
svg=f'<svg viewBox="0 0 570 300" xmlns="http://www.w3.org/2000/svg" style="width:100%;font-family:\'Noto Sans KR\',\'Noto Sans CJK KR\',\'NanumGothic\',sans-serif">'+''.join(P)+'</svg>'
open('/home/claude/book/img/R_rig.svg','w',encoding='utf-8').write(svg)
print(len(svg))
