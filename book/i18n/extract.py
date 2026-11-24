import re,json,sys
from bs4 import BeautifulSoup, NavigableString, Comment
src=sys.argv[1]
S=open(src,encoding='utf-8').read()
soup=BeautifulSoup(S,'lxml')
INL={'b','i','em','strong','code','span','a','br','sup','sub','kbd','small','u','mark','s'}
H=re.compile('[가-힣]')
segs=[]
def allinline(el):
    for d in el.descendants:
        if getattr(d,'name',None) and d.name not in INL: return False
    return True
def walk(el):
    for c in list(el.children):
        if isinstance(c,Comment): continue
        if isinstance(c,NavigableString):
            if H.search(str(c)):
                segs.append(c)
            continue
        if c.name in ('style','script'): continue
        if c.name in INL and not allinline(c):
            walk(c); continue
        if allinline(c) and H.search(c.get_text()):
            segs.append(c)
        else: walk(c)
walk(soup.body)
# also attributes
out=[]
for i,s in enumerate(segs):
    if isinstance(s,NavigableString): out.append({'id':i,'t':'text','src':str(s)})
    else: out.append({'id':i,'t':'html','src':s.decode_contents()})
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
print(len(out),sum(len(o['src']) for o in out), sum(len(H.findall(o['src'])) for o in out))
