const fs=require('node:fs/promises'),path=require('node:path'),{pathToFileURL}=require('node:url');
const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
const root=path.resolve('IDENTIDADE-ELEGANTE-OUSADA');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const context=await browser.newContext({offline:true,viewport:{width:1800,height:1200},deviceScaleFactor:1});
 const p=await context.newPage();const errors=[];p.on('pageerror',e=>errors.push(e.message));
 const items=JSON.parse(await fs.readFile(path.join(root,'inventario.json'),'utf8'));
 const svgCheck=[];
 for(const item of items){
  const src=path.join(root,item.file);
  await p.setViewportSize({width:Math.ceil(item.width),height:Math.ceil(item.height)});
  const svg=await fs.readFile(src,'utf8');
  await p.setContent('<!doctype html><html><head><meta charset="utf-8"></head><body>'+svg+'</body></html>');await p.evaluate(()=>document.fonts.ready);
  await p.addStyleTag({content:'html,body{margin:0;padding:0;background:transparent}svg{display:block}'});
  // Physical SVGs are displayed at native viewport size for pixel exports.
  await p.locator('svg').first().evaluate((e,v)=>{e.style.width=v.w+'px';e.style.height=v.h+'px'}, {w:item.width,h:item.height});
  await p.screenshot({path:src.replace(/\.svg$/,'.png'),omitBackground:true});
  svgCheck.push({file:item.file,images:await p.evaluate(()=>[...document.querySelectorAll('image')].length)});
  if(item.physical_mm){
   const [w,h]=item.physical_mm;
   await p.addStyleTag({content:`@page{size:${w}mm ${h}mm;margin:0}@media print{svg{width:${w}mm!important;height:${h}mm!important}html,body{width:${w}mm;height:${h}mm;margin:0}}`});
   await p.pdf({path:src.replace(/\.svg$/,'.pdf'),preferCSSPageSize:true,printBackground:true});
  }
 }
 await p.setViewportSize({width:1800,height:1200});
 await p.goto(pathToFileURL(path.join(root,'APRESENTACAO.html')).href);await p.evaluate(()=>document.fonts.ready);
 const missing=await p.evaluate(()=>[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.getAttribute('src')));
 const fonts=await p.evaluate(()=>({display:document.fonts.check('500 76px Cormorant'),body:document.fonts.check('400 24px Manrope')}));
 const outside=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((e,i)=>{
  const box=e.getBoundingClientRect();
  const bad=[...e.querySelectorAll('p,h1,h2,h3,blockquote,img,.eyebrow,.small,.cards,.three,.swatches,.story-grid,.highlight-grid')].filter(n=>{
   if(e.classList.contains('cover'))return false;
   const r=n.getBoundingClientRect();return r.bottom>box.bottom-52||r.right>box.right-35||r.left<box.left;
  }).map(n=>({tag:n.tagName,text:n.textContent.slice(0,70),bottom:Math.round(n.getBoundingClientRect().bottom-box.top)}));return {page:i+1,bad};
 }).filter(v=>v.bad.length));
 await p.pdf({path:path.join(root,'Manual-Aurevi-Elegante-Ousada.pdf'),preferCSSPageSize:true,printBackground:true,tagged:true});
 await fs.mkdir(path.join(root,'paginas'),{recursive:true});
 await p.addStyleTag({content:'nav{display:none!important}'});
 for(let i=0;i<18;i++) await p.locator('.page').nth(i).screenshot({path:path.join(root,'paginas',String(i+1).padStart(2,'0')+'.png')});
 await p.setViewportSize({width:390,height:844});await p.waitForTimeout(100);
 const mobile=await p.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,width:innerWidth}));
 await p.setViewportSize({width:1800,height:1200});
 await p.goto(pathToFileURL(path.join(root,'VISAO-GERAL.html')).href);await p.evaluate(()=>document.fonts.ready);
 await p.screenshot({path:path.join(root,'Visao-geral.png'),fullPage:true});
 // Guide PDF is a readable text document separate from the visual presentation.
 const md=await fs.readFile(path.join(root,'07-guias','Guia-de-uso-conteudo-e-loja.md'),'utf8');
 const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
 const body=md.split(/\r?\n\r?\n/).map(t=>t.startsWith('### ')?'<h3>'+esc(t.slice(4))+'</h3>':t.startsWith('## ')?'<h2>'+esc(t.slice(3))+'</h2>':t.startsWith('# ')?'<h1>'+esc(t.slice(2))+'</h1>':'<p>'+esc(t).replaceAll('\n','<br>')+'</p>').join('');
 const guide=`<!doctype html><html lang="pt-BR"><meta charset="utf-8"><style>@font-face{font-family:M;src:url('../06-fontes/Manrope.ttf')}@font-face{font-family:C;src:url('../06-fontes/CormorantGaramond.ttf')}body{font:12pt/1.65 M;color:#242424;margin:30px}h1,h2,h3{color:#450A10;break-after:avoid}h1,h2{font-family:C}h1{font-size:34pt}h2{font-size:26pt;margin-top:30px}h3{font-size:14pt}p{orphans:3;widows:3}@page{size:A4;margin:18mm}</style>${body}</html>`;
 await fs.writeFile(path.join(root,'07-guias','Guia-de-uso-conteudo-e-loja.html'),guide);
 await p.goto(pathToFileURL(path.join(root,'07-guias','Guia-de-uso-conteudo-e-loja.html')).href);await p.evaluate(()=>document.fonts.ready);
 await p.pdf({path:path.join(root,'07-guias','Guia-de-uso-conteudo-e-loja.pdf'),preferCSSPageSize:true,printBackground:true});
 const result={artes:items.length,pages:18,missing,fonts,outside,mobile,errors};
 await fs.writeFile(path.join(root,'verificacao-playwright.json'),JSON.stringify(result,null,2));
 console.log(JSON.stringify(result));await browser.close();
 if(missing.length||outside.length||mobile.overflow||errors.length||!fonts.display||!fonts.body)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1});
