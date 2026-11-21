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
ed=sys.argv[1] if len(sys.argv)>1 else ''
if ed in ('aula','prueba'):
    T={'aula':'Safari Gaucho Aula','prueba':'Safari Gaucho Prueba'}[ed]
    a=s.replace('href="icons/','href="../icons/')
    a=a.replace('content="https://pavlko.github.io/4x4natural/"','content="https://pavlko.github.io/4x4natural/%s/"'%ed)
    a=a.replace('<meta name="apple-mobile-web-app-title" content="Safari Gaucho">','<meta name="apple-mobile-web-app-title" content="%s">'%T)
    a=a.replace(HEAD.split('\n')[0],HEAD.split('\n')[0]+"\n<script>window.SG_ED='%s';</script>"%ed,1)
    assert "SG_ED='%s'"%ed in a
    open('/home/claude/g/%s.html'%ed,'w').write(a)
print('ok')
