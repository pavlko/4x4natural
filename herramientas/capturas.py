"""Capturas de la interfaz de Safari Gaucho en distintas pantallas.
Uso:  python3 herramientas/capturas.py ruta/al/juego.html salida.png
Necesita: pip install playwright pillow && playwright install chromium
Recorre los estados del juego (entrada, manejando, caminando, foto, cuaderno, mapa, personalizar)
en varias pantallas (PC 4:3, PC ancha, celular vertical tipo S25, celular horizontal, tablet) y arma una hoja.
"""
import asyncio,sys
from playwright.async_api import async_playwright
from PIL import Image,ImageDraw
SCREENS=[('PC 4:3',1024,768,False),('PC ancha',1600,900,False),('Celular vertical (S25)',384,832,True),('Celular horizontal',832,384,True),('Tablet',800,1180,True)]
CLEAN="document.querySelectorAll('#announce').forEach(e=>e.classList.remove('show','sticky'));document.querySelectorAll('.toast').forEach(e=>e.remove());"
STATES=[('Entrada',""),
 ('Manejando',"SAVE.nbTip0=1;document.querySelector('#go').click();SAVE.mask=true;SAVE.micro=true;SAVE.mapOk=true;"),
 ('Foto',"togglePhoto(true)"),
 ('Caminando',"togglePhoto(false);startWalk()"),
 ('Cuaderno',"toggleBook(true)"),
 ('Mapa',"toggleBook(false);toggleMap(true)"),
 ('Personalizar',"toggleMap(false);openCustom()")]
async def main(src,out,only=None):
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader"])
        rows=[]
        for (sn,w,h,touch) in SCREENS:
            if only and sn not in only:continue
            ctx=await b.new_context(viewport={'width':w,'height':h},has_touch=touch,is_mobile=touch)
            pg=await ctx.new_page();await pg.goto('file://'+src,timeout=120000);await pg.wait_for_timeout(7000);row=[]
            for (st,js) in STATES:
                try:await pg.evaluate("(()=>{try{"+js+"}catch(e){console.log(e)};"+CLEAN+"})()")
                except Exception:pass
                await pg.wait_for_timeout(900);await pg.evaluate("(()=>{"+CLEAN+"})()")
                f=f'/tmp/cap_{len(rows)}_{len(row)}.png';await pg.screenshot(path=f,timeout=90000);row.append((st,f))
            await ctx.close();rows.append((sn,w,h,row))
        TH=300;pad=12;W=0
        for sn,w,h,row in rows:W=max(W,len(row)*(int(TH*w/h)+pad)+pad)
        sheet=Image.new('RGB',(W,len(rows)*(TH+44)+pad),(243,235,221));d=ImageDraw.Draw(sheet);y=pad
        for sn,w,h,row in rows:
            tw=int(TH*w/h);d.text((pad,y),sn,fill=(35,64,47));y+=16
            for i,(st,f) in enumerate(row):
                im=Image.open(f).convert('RGB').resize((tw,TH));x=pad+i*(tw+pad);sheet.paste(im,(x,y));d.text((x,y+TH+4),st,fill=(35,64,47))
            y+=TH+28
        sheet.save(out);print('listo',out)
        await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2],sys.argv[3:] or None))
