const fs=require('node:fs/promises');const path=require('node:path');const {pathToFileURL}=require('node:url');
const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
(async()=>{
 const b=await chromium.launch({channel:'chrome',headless:true});
 const p=await b.newPage({viewport:{width:1664,height:1100}});
 const logs=[];p.on('pageerror',e=>logs.push(e.message));
 await p.goto(pathToFileURL(path.resolve('ENTREGA/COMECE-AQUI.html')).href,{waitUntil:'load'});
 await p.evaluate(()=>document.fonts.ready);
 const errors=await p.evaluate(()=>[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.getAttribute('src')));
 if(errors.length)throw Error('Missing images: '+errors.join(', '));
 await p.pdf({path:'ENTREGA/Manual-Aurevi.pdf',printBackground:true,preferCSSPageSize:true,tagged:true,displayHeaderFooter:false});
 await fs.mkdir('.tools/previews/manual',{recursive:true});
 const sheets=p.locator('.sheet');const n=await sheets.count();
 for(let i=0;i<n;i++){await sheets.nth(i).screenshot({path:'.tools/previews/manual/'+String(i+1).padStart(2,'0')+'.png'});}
 const bounds=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((s,i)=>{
   const rect=s.getBoundingClientRect();
   const outside=[...s.querySelectorAll('h1,h2,h3,p,figcaption,.bio,.file-list')].filter(e=>{const r=e.getBoundingClientRect();return r.right>rect.right+.5||r.bottom>rect.bottom-35||r.left<rect.left-.5;}).map(e=>e.textContent.slice(0,90));
   return {page:i+1,outside};
 }).filter(x=>x.outside.length));
 // Four print documents retain their physical size and bleed, plus the sticker.
 const printables=[['tag-frente',61,101],['tag-verso',61,101],['cartao-frente',96,61],['cartao-verso',96,61],['adesivo-lacre',56,56]];
 for(const [name,w,h]of printables){
  const f=path.resolve('ENTREGA/03-embalagens/'+name+'.svg');
  const html=`<!doctype html><html><head><style>@page{size:${w}mm ${h}mm;margin:0}html,body{margin:0;width:${w}mm;height:${h}mm}img{width:${w}mm;height:${h}mm;display:block}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}</style></head><body><img src="${pathToFileURL(f).href}"></body></html>`;
  const tmp=path.resolve('.tools/previews/'+name+'-print.html');await fs.writeFile(tmp,html);await p.goto(pathToFileURL(tmp).href,{waitUntil:'load'});
  await p.pdf({path:f.replace(/\.svg$/,'.pdf'),preferCSSPageSize:true,printBackground:true,displayHeaderFooter:false});
 }
 // Contact sheet to inspect all pages together, using screenshots created above.
 const contact='<meta charset="utf-8"><style>body{margin:0;padding:20px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;background:#ded6c9;font:15px Arial;color:#203c32}figure{margin:0}img{width:100%}figcaption{margin:6px 0}</style>'+Array.from({length:n},(_,i)=>`<figure><img src="manual/${String(i+1).padStart(2,'0')}.png"><figcaption>${i+1}</figcaption></figure>`).join('');
 await fs.writeFile('.tools/previews/manual-contato.html',contact);await p.setViewportSize({width:1800,height:1000});await p.goto(pathToFileURL(path.resolve('.tools/previews/manual-contato.html')).href);await p.screenshot({path:'.tools/previews/manual-contato.png',fullPage:true});
 await fs.writeFile('.tools/manual-check.json',JSON.stringify({pages:n,missingImages:errors,jsErrors:logs,outsideBounds:bounds},null,2));
 console.log(JSON.stringify({pages:n,missingImages:errors,jsErrors:logs,outsideBounds:bounds}));await b.close();
})();
