# -*- coding: utf-8 -*-
import re, sys, html as H
S=open('/tmp/b13_b.html',encoding='utf-8').read()
sys.path.insert(0,'/home/claude/book/tools'); import ins_rig; S=ins_rig.apply(S)
import ins_extra; S=ins_extra.apply(S)

# ---- stray challenge boxes on the TOC page -> move into chapters 06, 07, 12
m=re.search(r'<section class="chapter toc-page">.*?</section>',S,flags=re.S)
toc_sec=m.group(0)
strays=re.findall(r'<div class="layer3"><div class="lh"><span class="tag t5">도전 과제</span></div>.*?</div>\n',toc_sec,flags=re.S)
assert len(strays)==3, len(strays)
def add_to_chapter(no,box):
    global S
    box=box.strip().replace('<span class="tag t5">도전 과제</span>','<span class="tag t5">도전 과제</span> 심화')
    pat=r'(<div class="ch-no">CHAPTER '+no+r'</div>.*?)(</section>)'
    S,k=re.subn(pat,lambda mm:mm.group(1)+box+'\n'+mm.group(2),S,count=1,flags=re.S)
    assert k==1
add_to_chapter('06',strays[0]); add_to_chapter('07',strays[1]); add_to_chapter('12',strays[2])

# ---- chapter ids + collect titles
parts=[]; cur=None
def clean(t): return re.sub(r'\s+',' ',re.sub(r'<span class="lv">.*?</span>','',t)).strip()
out=[]; pos=0
secs=list(re.finditer(r'<section class="(part|chapter)[^"]*"[^>]*>.*?</section>',S,flags=re.S))
toc=[]  # (kind, id, label, title)
pi=-1
for sm in secs:
    sec=sm.group(0)
    if sm.group(1)=='part':
        no=re.search(r'<div class="no">(.*?)</div>',sec).group(1); t=re.search(r'<h1>(.*?)</h1>',sec).group(1)
        pid='part-'+no.split()[-1]
        toc.append(('part',pid,no,t))
        new=sec.replace('<section class="part"','<section class="part" id="'+pid+'"',1)
    else:
        mm=re.search(r'<div class="ch-no">(.*?)</div>',sec); hh=re.search(r'<h1 class="ch">(.*?)</h1>',sec,flags=re.S)
        label=mm.group(1) if mm else ''
        title=clean(hh.group(1))
        if label.startswith('CHAPTER'):
            num=label.replace('CHAPTER ','')
            cid='ch-'+re.sub(r'[^0-9①②③]','',num).replace('①','a').replace('②','b').replace('③','c')
            toc.append(('ch',cid,num,title))
            new=sec.replace('<div class="ch-no">','<div class="ch-no" id="'+cid+'">',1)
        elif label=='APPENDIX':
            toc.append(('ch','ch-app','부록','단축키 · 이펙트 30선 · 용어 · 문제 해결 · 참고 자료'))
            new=sec.replace('<div class="ch-no">','<div class="ch-no" id="ch-app">',1)
        elif not mm and '지은이' in title:
            toc.append(('ch','ch-bio','','지은이'))
            new=sec.replace('<section class="chapter" style="break-before:page">','<section class="chapter" id="sec-bio">').replace('<h1 class="ch">지은이</h1>','<div class="ch-no" id="ch-bio">AUTHOR</div>\n<h1 class="ch">지은이</h1>')
        else:
            new=sec
    out.append(S[pos:sm.start()]); out.append(new); pos=sm.end()
out.append(S[pos:]); S=''.join(out)

# ---- new TOC (two columns, page numbers filled by paginator)
def entry(kind,cid,label,title):
    if kind=='part':
        no=label.replace('PART ','')
        return f'<div class="tp"><span class="tpn">PART {no}</span><span class="tpt">{title}</span><span class="pn" data-target="{cid}"></span></div>'
    lab=label.replace(' · ①','-1').replace(' · ②','-2').replace(' · ③','-3')
    t=title.strip()
    if ' — ' in t:
        a,b=t.split(' — ',1); t=a+'<em> — '+b+'</em>'
    return f'<div class="te"><span class="tn">{lab}</span><span class="tt">{t}</span><span class="pn" data-target="{cid}"></span></div>'
idx=[i for i,t in enumerate(toc) if t[0]=='part' and t[2]=='PART 4'][0]
colA=''.join(entry(*t) for t in toc[:idx]); colB=''.join(entry(*t) for t in toc[idx:])
newtoc=('<section class="chapter toc-page" data-break="1">\n<div class="ch-no">CONTENTS</div>\n<h1 class="ch">차례</h1>\n'
        '<div class="toc1">'+colA+'</div>\n</section>\n'
        '<section class="chapter toc-page toc-cont" data-break="1">\n<div class="toc1">'+colB+'</div>\n</section>')
S=S.replace(toc_sec,newtoc)
# PART 0 starts a new page
S=S.replace('<section class="part" id="part-0" style="break-before:page;margin-top:0">','<section class="part" id="part-0" data-break="1">')
assert 'data-break="1"><div class="no">PART 0' in S

# ---- shortcuts: 8 small tables -> one 4-column table (splittable by rows)
gm=re.search(r'<div class="sc-grid">(.*?)</div>\n<div class="warn"><b>한글 입력 상태 주의</b>',S,flags=re.S)
assert gm
groups=[]
for g in re.finditer(r'<div class="sc"><div class="sh">(.*?)</div><table>(.*?)</table></div>',gm.group(1),flags=re.S):
    rows=re.findall(r'<tr><td class="mono">(.*?)</td><td>(.*?)</td></tr>',g.group(2),flags=re.S)
    groups.append((g.group(1),rows))
assert len(groups)==8,len(groups)
tb='<table class="sct"><colgroup><col style="width:22%"><col style="width:28%"><col style="width:22%"><col style="width:28%"></colgroup>'
for i in range(0,8,2):
    (ta,ra),(tb2,rb)=groups[i],groups[i+1]
    tb+=f'<tr class="cat"><th colspan="2">{ta}</th><th colspan="2">{tb2}</th></tr>'
    for k in range(max(len(ra),len(rb))):
        a=ra[k] if k<len(ra) else ('','')
        b=rb[k] if k<len(rb) else ('','')
        tb+=f'<tr><td class="mono">{a[0]}</td><td>{a[1]}</td><td class="mono">{b[0]}</td><td>{b[1]}</td></tr>'
tb+='</table>'
S=S[:gm.start()]+tb+'\n<div class="warn"><b>한글 입력 상태 주의</b>'+S[gm.end():]

# ---- making-of after bio text
nfig=len(re.findall(r'<figure',S))
mk=('<h2>이 책을 만든 과정</h2>\n<p>이 책의 실습과 화면은 2026년 11월 22일과 23일 이틀 동안, 저자의 지시에 따라 Claude가 Windows PC의 애프터이펙트를 직접 조작해 만들었습니다. 컴포지션과 레이어는 힉스필드 브리지로, 메뉴 선택과 화면 캡처는 Claude의 컴퓨터 사용 기능으로, 실습 영상과 도판 사진은 힉스필드의 생성 모델로 만들었습니다. 로그인과 결제, 무엇을 넣고 뺄지의 판단, 마지막 검수는 사람이 했습니다.</p>\n'
    '<table><tr><th style="width:36%">항목</th><th>기록</th></tr>'
    f'<tr><td>화면 캡처와 도판</td><td>{nfig}점 (실제 캡처, 직접 그린 도식, 생성 이미지에 표기를 더한 사진)</td></tr>'
    '<tr><td>애펙 프로젝트</td><td>컴포지션 34개 — 저장소 project 폴더의 .aep 한 파일</td></tr>'
    '<tr><td>힉스필드 크레딧</td><td>약 238 (25장의 기록표)</td></tr>'
    '<tr><td>조판</td><td>HTML과 CSS로 짜고 PDF로 출력 (182 × 257mm)</td></tr></table>\n'
    '<h2>책 정보</h2>\n<table><tr><th style="width:36%">항목</th><th>내용</th></tr>'
    '<tr><td>책 이름</td><td>애프터이펙트 2027 완전 실습 — 기본기부터 AI 협업까지</td></tr>'
    '<tr><td>지은이 · 펴낸 날</td><td>안지아 · 2026년 11월 23일 (2027 EDITION, 1판)</td></tr>'
    '<tr><td>기준 버전</td><td>Adobe After Effects 27.0 · Higgsfield Plugin v1.0.64</td></tr>'
    '<tr><td>실습 자료</td><td>깃허브 저장소 (주소는 뒤표지)</td></tr>'
    '<tr><td>글꼴</td><td>본문 Noto Sans CJK KR, 도판 나눔고딕 (SIL Open Font License)</td></tr></table>\n'
    '<p class="src">화면 캡처와 도판은 저자가 직접 만들었습니다. Adobe, After Effects, Premiere는 Adobe Inc.의, Higgsfield는 Higgsfield AI의, Claude는 Anthropic의 상표입니다. 이 책은 각 회사의 공식 출판물이 아닙니다.</p>\n')
assert '지은 책으로 『UX란 무엇인가?』' in S
S=re.sub(r'(지은 책으로 『UX란 무엇인가\?』.*?</p>\n)(</section>)',lambda m:m.group(1)+mk+m.group(2),S,count=1,flags=re.S)
assert '이 책을 만든 과정' in S

# ---- colophon after bio
pass

# ---- figure renumber + reference mapping
mapping={}
def renum(sec_m):
    sec=sec_m.group(0)
    mm=re.search(r'<div class="ch-no"[^>]*>CHAPTER (\d+)',sec)
    if not mm: return sec
    n=int(mm.group(1)); k=[0]
    def f(c):
        k[0]+=1; old=c.group(1); new=f'{n}-{k[0]}'
        if old!='0-0' and old!=new: mapping[old]=new
        return f'<figcaption><b>그림 {new}</b>'
    return re.sub(r'<figcaption><b>그림 ([0-9]+-[0-9]+[a-z]?)</b>',f,sec)
S=re.sub(r'<section class="chapter[^>]*>.*?</section>',renum,S,flags=re.S)
print('renumber map:',mapping)
# update in-text references (not captions)
def refs(m):
    old=m.group(2)
    return m.group(1)+'그림 '+mapping.get(old,old)
S2=re.sub(r'(?<!<b>)()그림 ([0-9]+-[0-9]+)(?!</b>)',refs,S)
changed=[(a,b) for a,b in zip(re.findall(r'(?<!<b>)그림 ([0-9]+-[0-9]+)(?!</b>)',S),re.findall(r'(?<!<b>)그림 ([0-9]+-[0-9]+)(?!</b>)',S2)) if a!=b]
print('ref updates:',changed)
S=S2
print('in-text figure refs:',sorted(set(re.findall(r'(?<!<b>)그림 ([0-9]+-[0-9]+)(?!</b>)',S))))
open('/tmp/b13_c.html','w',encoding='utf-8').write(S)
print('TOC entries',len(toc)); 
for t in toc: print(t[0],t[1],t[2],'|',t[3][:40])

# ---- comp names -> book-order names (2026.11.23 rename in project)
REN=[('E_샘플_텍스트애니','06_텍스트애니메이터'),('E_파티클_불꽃 · 눈 · 연기 · 깨짐 · 흩어짐','05-4~05-8_파티클_…'),
 ('E_샘플_효과','05-1_글로우·잔상'),('E_샘플_퍼펫','05-2_퍼펫핀'),('E_샘플_파티클','05-3_파티클_입자'),('E_샘플_오디오','05-9_소리반응'),
 ('E_샘플_움직임','07-1_익스프레션_움직임'),('E_샘플_값','07-2_익스프레션_값'),('E_샘플_글자','07-3_익스프레션_글자'),('E_샘플_마커','07-4_익스프레션_마커'),
 ('C9_3D트래커','10-1_3D트래커'),('C10_물체지우기','11_물체지우기'),('C11_색보정','12_색보정'),('C7_키잉','08-1_크로마키'),('C8_트래킹','09_트래킹'),
 ('G_3D_4뷰','13-1_3D_4뷰'),('P1_FirstMove','01_처음움직임'),('B1_통통공','03_통통공'),('18장 실습_걷는 인물','18_패널_걷는인물'),('20장 실습_말하는 인물','20_패널_말하는인물')]
for a,b in REN: S=S.replace(a,b)
note=('<div class="note"><b>컴포지션 이름</b>저장소의 프로젝트 파일은 컴포지션 이름 앞에 책의 장·절 번호를 붙여, 프로젝트 패널에서 이름순으로 정렬하면 책 순서대로 보입니다(01_처음움직임, 05-1_글로우·잔상 … 24-2_스토리보드_v2). '
      '일부 캡처 속 탭에는 집필 중에 쓴 이전 이름(E_샘플_…, C7~C11, 3장·6장·8장 등)이 보이지만 같은 컴포지션입니다.</div>')
S=re.sub(r'<div class="note"><b>컴포지션 이름</b>.*?</div>',lambda m:note,S,count=1,flags=re.S)
open('/tmp/b13_c.html','w',encoding='utf-8').write(S)

S=S.replace('이 책의 실습 자료는 깃허브 저장소 <span class="mono">github.com/aixrartdesign-maker/ae-2027-ai-workbook</span>에 정리되어 있습니다.','이 책의 실습 자료는 깃허브 저장소에 정리되어 있습니다. 주소는 뒤표지에 있습니다.')
assert 'github.com/aixrartdesign' not in S, 'url left'
back='''<section class="cover back" id="backcover">
  <div class="bband"></div>
  <div class="bq">애펙 한 가지 프로그램을 처음부터 끝까지.<br>손으로 먼저 익히고, AI와 함께 완성합니다.</div>
  <ul class="bl"><li>기본기 · 모션그래픽 · 익스프레션 · 합성 · 3D</li><li>힉스필드 플러그인 패널 · Claude 브리지 · 애펙 AI Assistant</li><li>실제 화면 캡처와 실제 크레딧 기록</li></ul>
  <div class="bgh"><img class="bqr" src="img/qr_github.svg"><span>실습 자료 · 프로젝트 파일</span>github.com/aixrartdesign-maker/ae-2027-ai-workbook<em>QR을 찍으면 저장소로 바로 갑니다.</em></div>
  <div class="author">안지아 지음</div>
  <div class="draft">2027 EDITION · 2026.11</div>
</section>'''
S=S.replace('</body></html>',back+'\n</body></html>',1)
open('/tmp/b13_c.html','w',encoding='utf-8').write(S)
