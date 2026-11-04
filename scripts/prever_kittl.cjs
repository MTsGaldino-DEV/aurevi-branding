const fs=require('node:fs/promises'),path=require('node:path');const {pathToFileURL}=require('node:url');
const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
(async()=>{
let cards=[];
for(const f of ['templates-sacolas.json','templates-tags.json','templates-cartoes.json']){
 const raw=JSON.parse(await fs.readFile('.tools/kittl/'+f));const data=JSON.parse(raw.content.find(x=>x.type==='text').text);
 for(const t of data.templates){const r=await fetch(t.previewUrl);if(r.ok)await fs.writeFile('.tools/kittl/template-'+t.id+'.webp',Buffer.from(await r.arrayBuffer()));cards.push(`<figure><img src="template-${t.id}.webp"><figcaption>${t.id} · ${t.premium?'Premium':'Livre'}<br>${t.name}</figcaption></figure>`);}
}
await fs.writeFile('.tools/kittl/previews.html',`<meta charset="utf-8"><style>body{margin:0;background:#f4efe6;display:grid;grid-template-columns:repeat(4,1fr);font:14px Arial}figure{margin:14px}img{width:100%}figcaption{padding:8px}</style>${cards.join('')}`);
const b=await chromium.launch({channel:'chrome',headless:true});const p=await b.newPage({viewport:{width:1400,height:1000}});await p.goto(pathToFileURL(path.resolve('.tools/kittl/previews.html')).href);await p.screenshot({path:'.tools/kittl/previews.png',fullPage:true});await b.close();})();
