const fs=require('node:fs/promises'),path=require('node:path'),{pathToFileURL}=require('node:url');
const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
(async()=>{
const b=await chromium.launch({channel:'chrome',headless:true});const c=await b.newContext({offline:true,viewport:{width:1440,height:1000}});const p=await c.newPage();
const net=[];p.on('request',r=>{if(/^https?:/.test(r.url()))net.push(r.url())});
await p.goto(pathToFileURL(path.resolve('ENTREGA/COMECE-AQUI.html')).href,{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);
const desktop=await p.evaluate(()=>({pages:document.querySelectorAll('.page').length,failedImages:[...document.images].filter(i=>!i.naturalWidth).length,fonts:[document.fonts.check('400 24px Fraunces'),document.fonts.check('400 24px Manrope')],overflow:document.documentElement.scrollWidth>innerWidth}));
await p.getByRole('button',{name:'Tamanho real',exact:true}).click();const zoom=await p.evaluate(()=>document.body.classList.contains('real'));
await p.getByRole('button',{name:'Ajustar à tela',exact:true}).click();
await p.setViewportSize({width:390,height:844});await p.waitForTimeout(200);
const mobile=await p.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,firstPageWidth:document.querySelector('.sheet').getBoundingClientRect().width,viewport:innerWidth}));
await p.screenshot({path:'.tools/previews/manual-mobile.png'});
// The editable SVGs retain real text and render their embedded fonts offline.
const editPath='ENTREGA/02-redes/feed/editaveis/02-manifesto.svg';await p.goto(pathToFileURL(path.resolve(editPath)).href);await p.evaluate(()=>document.fonts.ready);await p.setViewportSize({width:1080,height:1350});
const editable=await p.evaluate(()=>({textNodes:document.querySelectorAll('text').length,fontLoaded:document.fonts.check('450 128px Fraunces')}));
await p.screenshot({path:'.tools/previews/editavel-manifesto.png',omitBackground:true});
const summary={desktop,mobile,zoomWorks:zoom,externalResourceRequests:net,editable};await fs.writeFile('.tools/browser-check.json',JSON.stringify(summary,null,2));console.log(JSON.stringify(summary));
await b.close();if(desktop.failedImages||desktop.overflow||mobile.overflow||!zoom||net.length||!editable.textNodes||!editable.fontLoaded)process.exitCode=1;
})();
