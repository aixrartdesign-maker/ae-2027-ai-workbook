import re,json,sys
from bs4 import BeautifulSoup, NavigableString, Comment
lang=sys.argv[1]; src='/tmp/b13_c.html'
sys.path.insert(0,'/home/claude/tr')
U=json.load(open('/home/claude/tr/uniq.json'));idx={s:i for i,s in enumerate(U)}
T={}
import glob
for f in sorted(glob.glob(f'/home/claude/tr/{lang}/c*.txt')):
    cur=None
    for line in open(f,encoding='utf-8'):
        m=re.match(r'\[(\d+)\] ?(.*)',line.rstrip('\n'))
        if m: cur=int(m.group(1)); T[cur]=m.group(2)
        elif cur is not None and line.strip(): T[cur]+=' '+line.strip()
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
            if H.search(str(c)): segs.append(c)
            continue
        if c.name in ('style','script'): continue
        if c.name in INL and not allinline(c): walk(c); continue
        if allinline(c) and H.search(c.get_text()): segs.append(c)
        else: walk(c)
walk(soup.body)
miss=0
for s in segs:
    key=str(s) if isinstance(s,NavigableString) else s.decode_contents()
    i=idx.get(key)
    if i is None or i not in T: miss+=1; continue
    tr=T[i]
    if isinstance(s,NavigableString):
        lead=re.match(r'\s*',key).group(0); tail=re.search(r'\s*$',key).group(0)
        s.replace_with(NavigableString(lead+BeautifulSoup(tr,'html.parser').get_text()+tail))
    else:
        s.clear()
        frag=BeautifulSoup(tr,'html.parser')
        for n in list(frag.contents): s.append(n)
out=str(soup)
out=out.replace('<html lang="ko"','<html lang="'+lang+'"')
lv={'en':'Level ','ru':'Уровень ','es':'Nivel '}[lang]
out=out.replace('content:"난이도 "','content:"'+lv+'"')
out=out.replace('</style></head>','.pg-body, .cover { hyphens:auto; word-break:normal; overflow-wrap:break-word; }\n</style></head>',1)
open(f'/tmp/b13_{lang}.html','w',encoding='utf-8').write(out)
print(lang,'segs',len(segs),'missing',miss,'translated ids',len(T))
