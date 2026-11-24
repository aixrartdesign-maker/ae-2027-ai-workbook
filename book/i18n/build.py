import sys,subprocess
l=sys.argv[1]
T={'en':'After Effects 2027 Complete Hands-On','ru':'After Effects 2027: полный практикум','es':'After Effects 2027: práctica completa'}[l]
S=open(f'/tmp/b13_{l}.html',encoding='utf-8').read()
css=open('/home/claude/book/tools/page.css',encoding='utf-8').read()
js=open('/home/claude/book/tools/paginate.js',encoding='utf-8').read().replace("'애프터이펙트 2027 완전 실습'","'"+T+"'")
S=S.replace('</style></head>','\n'+css+'\n.pg-body, .cover { hyphens:auto; word-break:normal; overflow-wrap:break-word; }\n</style></head>',1)
S=S.replace('</body></html>','<script>\n'+js+'\n</script>\n</body></html>')
open(f'/home/claude/book/book_{l}.html','w',encoding='utf-8').write(S)
