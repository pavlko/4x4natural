# Repone en index.html los enlaces de app instalable (manifiesto e íconos) y arma la edición aula.
import re,sys
idx='/home/claude/g/idx.html'
s=open(idx).read()
HEAD=('<link rel="manifest" href="manifest.webmanifest">\n<meta name="theme-color" content="#23402F">\n'
 '<link rel="icon" type="image/png" href="icons/icon-192-v4.png">\n<link rel="apple-touch-icon" href="icons/apple-touch-icon-v4.png">\n'
 '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n'
 '<meta name="apple-mobile-web-app-title" content="Safari Gaucho">\n')
if 'rel="manifest"' not in s:
    m=re.search(r'<meta charset="[^"]*">\s*',s,re.I);assert m
    s=s[:m.end()]+HEAD+s[m.end():]
open(idx,'w').write(s)
if len(sys.argv)>1 and sys.argv[1]=='aula':
    a=s.replace('href="icons/','href="../icons/')
    a=a.replace('content="https://pavlko.github.io/4x4natural/"','content="https://pavlko.github.io/4x4natural/aula/"')
    a=a.replace('<meta name="apple-mobile-web-app-title" content="Safari Gaucho">','<meta name="apple-mobile-web-app-title" content="Safari Gaucho Aula">')
    a=a.replace(HEAD.split('\n')[0],HEAD.split('\n')[0]+"\n<script>window.SG_ED='aula';</script>",1)
    assert "SG_ED='aula'" in a
    open('/home/claude/g/aula.html','w').write(a)
print('ok')
