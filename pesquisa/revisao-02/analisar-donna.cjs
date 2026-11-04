const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
const fs=require('node:fs/promises'),path=require('node:path'),{pathToFileURL}=require('node:url');
(async()=>{
 const dir=__dirname;await fs.mkdir(dir,{recursive:true});
 const b=await chromium.launch({channel:'chrome',headless:true});const context=await b.newContext({viewport:{width:1440,height:1050},locale:'pt-BR'});
 let cards=[];
 for(const [name,url]of [['instagram','https://www.instagram.com/donna.oficial/'],['loja','https://www.lojadonnaoficial.com.br/']]){
  const p=await context.newPage();const response=await p.goto(url,{waitUntil:'domcontentloaded',timeout:45000});await p.waitForTimeout(5000);await p.keyboard.press('Escape');
  if(name==='loja'){await p.evaluate(()=>window.scrollTo(0,1800));await p.waitForTimeout(1200);}
  const data=await p.evaluate(()=>({title:document.title,text:document.body.innerText,images:[...document.images].filter(i=>i.naturalWidth>=300&&i.naturalHeight>=350).map(i=>({src:i.currentSrc,alt:i.alt,w:i.naturalWidth,h:i.naturalHeight}))}));
  data.url=url;data.status=response?.status();await fs.writeFile(path.join(dir,name+'.json'),JSON.stringify(data,null,2));await p.screenshot({path:path.join(dir,name+'.png'),fullPage:true});
  const unique=[...new Map(data.images.map(x=>[x.src,x])).values()].slice(0,name==='instagram'?12:16);
  for(let i=0;i<unique.length;i++){
   try{const im=unique[i];const r=await context.request.get(im.src);if(!r.ok())continue;const filename=name+'-'+String(i+1).padStart(2,'0')+'.jpg';await fs.writeFile(path.join(dir,filename),await r.body());cards.push({filename,label:im.alt||name+' / '+(i+1),source:url});}catch(e){console.log('image',name,i,e.message.slice(0,90));}
  }
  console.log(JSON.stringify({name,status:data.status,images:unique.length,text:data.text.slice(0,1300)}));await p.close();
 }
 const html='<meta charset="utf-8"><style>body{margin:0;padding:20px;background:#ece7df;display:grid;grid-template-columns:repeat(5,1fr);gap:20px;font:15px Arial;color:#202020}figure{margin:0}img{width:100%;height:330px;object-fit:cover;object-position:top}figcaption{font-size:12px;padding:8px 0}</style>'+cards.map(c=>`<figure><img src="${c.filename}"><figcaption>${c.filename}<br>${c.label.replaceAll('<','&lt;')}</figcaption></figure>`).join('');
 await fs.writeFile(path.join(dir,'contato.html'),html);await fs.writeFile(path.join(dir,'imagens.json'),JSON.stringify(cards,null,2));const p=await context.newPage();await p.setViewportSize({width:1600,height:1000});await p.goto(pathToFileURL(path.join(dir,'contato.html')).href);await p.screenshot({path:path.join(dir,'contato.png'),fullPage:true});await b.close();
})();
