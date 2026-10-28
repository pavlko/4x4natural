// Safari Gaucho: guarda el juego para que abra rápido y funcione sin conexión
const CACHE='natural4x4-v89';
const SHELL=['./','./index.html','./manifest.webmanifest','./icons/icon-192.png','./icons/icon-512.png','./icons/icon-maskable-512.png','./icons/apple-touch-icon.png',
  'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>Promise.allSettled(SHELL.map(u=>c.add(u)))).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;
  const url=new URL(r.url);
  // la página: primero la red (para recibir actualizaciones), si no hay conexión, la copia guardada
  if(r.mode==='navigate'){e.respondWith(fetch(r,{cache:'reload'}).then(res=>{const cp=res.clone();caches.open(CACHE).then(c=>c.put('./index.html',cp));return res;}).catch(()=>caches.match('./index.html')));return;}
  // el resto: lo guardado primero, y se actualiza en segundo plano (incluye las tipografías)
  if(url.pathname.endsWith('version.json')){e.respondWith(fetch(r,{cache:'no-store'}));return;}
  e.respondWith(caches.match(r).then(hit=>{const net=fetch(r).then(res=>{if(res&&(res.ok||res.type==='opaque')){const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp));}return res;}).catch(()=>hit);return hit||net;}));});
