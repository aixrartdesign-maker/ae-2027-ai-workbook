import sys, json
from playwright.sync_api import sync_playwright
src=sys.argv[1]; out=sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')
    pg=b.new_page(viewport={'width':900,'height':1200})
    logs=[]
    pg.on('console',lambda m: logs.append(m.text)); pg.on('pageerror',lambda e: logs.append('ERR '+str(e)))
    pg.goto('file:///home/claude/book/'+src)
    try:
        pg.wait_for_function('window.__done===true',timeout=180000)
    except Exception as e:
        print('TIMEOUT',e); print('\n'.join(logs[-20:])); sys.exit(1)
    rep=pg.evaluate('window.__report')
    json.dump(rep,open('/tmp/report.json','w'),ensure_ascii=False)
    print('pages',rep['pages'],rep['stats'])
    bad=[r for r in rep['rows'] if r['left']>6 or r['over']>0]
    print('pages with leftover>6mm or overflow:',len(bad))
    for r in bad: print(r['no'],'left',r['left'],'raw',r['raw'],'over',r['over'],'|',(r.get('dbg') or {}).get('why'),'| next:',(r.get('dbg') or {}).get('next'),'/',(r.get('dbg') or {}).get('next2'),'| carry',(r.get('dbg') or {}).get('carry'),'| items',' '.join((r.get('dbg') or {}).get('items',[])))
    if logs: print('LOGS:',logs[:10])
    kw=dict(path='/home/claude/book/'+out,width='182mm',height='257mm',print_background=True,prefer_css_page_size=True)
    try:
        pg.pdf(outline=True,tagged=True,**kw)
    except TypeError:
        pg.pdf(**kw)
    b.close()
