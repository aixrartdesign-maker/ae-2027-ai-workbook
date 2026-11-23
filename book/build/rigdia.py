s=0.36
def X(x): return (x-820)*s+24
def Y(y): return (y-235)*s+22
def rect(cx,top,w,h,fill,r=8):
    return f'<rect x="{X(cx-w/2):.1f}" y="{Y(top):.1f}" width="{w*s:.1f}" height="{h*s:.1f}" rx="{r}" fill="{fill}"/>'
skin='#f7d2b0'; top='#2a8c96'; arm='#21737c'; pant='#3a4458'; shoe='#26262c'
P=[]
for cx in (925,995):
    P.append(rect(cx,615,54,150,pant)); P.append(rect(cx,760,48,140,pant))
P.append(rect(925-12,880,84,30,shoe,5)); P.append(rect(995+12,880,84,30,shoe,5))
P.append(rect(960,575,130,50,pant,6)); P.append(rect(960,360,150,240,top,14))
P.append(f'<ellipse cx="{X(960)}" cy="{Y(295)}" rx="{65*s}" ry="{70*s}" fill="{skin}"/>')
for cx in (870,1050):
    P.append(rect(cx,380,44,130,arm)); P.append(rect(cx,505,40,120,skin))
    P.append(f'<circle cx="{X(cx)}" cy="{Y(643)}" r="{23*s}" fill="{skin}"/>')
J=[(960,600,'골반·허리'),(960,365,'목'),(870,380,'어깨'),(1050,380,''),(870,505,'팔꿈치'),(1050,505,''),(870,620,'손목'),(1050,620,''),(925,615,''),(995,615,'엉덩이'),(925,760,''),(995,760,'무릎'),(925,895,''),(995,895,'발목')]
for x,y,l in J:
    P.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4.2" fill="#ff5a36" stroke="#fff" stroke-width="1.4"/>')
    if l:
        side = 1 if x>=960 else -1
        tx = X(1075) if side>0 else X(845)
        anchor='start' if side>0 else 'end'
        if l in ('골반·허리','목'): tx=X(1075); anchor='start'
        P.append(f'<line x1="{X(x):.1f}" y1="{Y(y):.1f}" x2="{tx - (4 if anchor=="end" else -0) :.1f}" y2="{Y(y):.1f}" stroke="#ff5a36" stroke-width=".7" stroke-dasharray="2 2"/>')
        dyl={'골반·허리':-5,'엉덩이':9}.get(l,0)
        P.append(f'<text x="{tx+(3 if anchor=="start" else -3):.1f}" y="{Y(y)+3.5+dyl:.1f}" text-anchor="{anchor}" font-size="10" fill="#14143a" font-weight="700">{l}</text>')
# tree
T=[(0,'전체_조종','널 · 골반 가운데'),(1,'골반','기준점 골반 가운데'),(2,'몸통','기준점 허리'),(3,'머리','기준점 목'),(4,'눈_왼 · 눈_오 · 입','각자 가운데'),
(3,'위팔_왼 / 위팔_오','기준점 어깨'),(4,'아래팔','기준점 팔꿈치'),(5,'손','기준점 손목'),
(2,'허벅지_왼 / 허벅지_오','기준점 엉덩이'),(3,'정강이','기준점 무릎'),(4,'발','기준점 발목')]
x0=235; y0=34; dy=23.5; ind=20
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
svg=f'<svg viewBox="0 0 560 296" xmlns="http://www.w3.org/2000/svg" style="width:100%;font-family:\'Noto Sans KR\',\'Noto Sans CJK KR\',\'NanumGothic\',sans-serif">'+''.join(P)+'</svg>'
open('/home/claude/book/img/R_rig.svg','w',encoding='utf-8').write(svg)
print(len(svg))
