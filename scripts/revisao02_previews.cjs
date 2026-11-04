const fs=require('node:fs/promises'),path=require('node:path'),{pathToFileURL}=require('node:url');
const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
(async()=>{
const dir=path.resolve('pesquisa/revisao-02');let cards=[];
for(const file of ['revision_templates_1.json','revision_templates_2.json']){const d=JSON.parse(await fs.readFile(path.join(dir,file)));for(const t of d.templates){const r=await fetch(t.previewUrl);if(r.ok){const name='template-'+t.id+'.webp';await fs.writeFile(path.join(dir,name),Buffer.from(await r.arrayBuffer()));cards.push(`<figure><img src="${name}"><figcaption>${t.id} · ${t.premium?'Premium':'Livre'} · ${t.name}</figcaption></figure>`);}}}
await fs.writeFile(path.join(dir,'templates.html'),'<meta charset="utf-8"><style>body{margin:0;padding:20px;background:#eee;display:grid;grid-template-columns:repeat(6,1fr);gap:20px;font:13px Arial}figure{margin:0}img{width:100%}figcaption{padding:8px 0}</style>'+cards.join(''));
const b=await chromium.launch({channel:'chrome',headless:true});const p=await b.newPage({viewport:{width:1800,height:1000}});await p.goto(pathToFileURL(path.join(dir,'templates.html')).href);await p.screenshot({path:path.join(dir,'templates.png'),fullPage:true});await b.close();})();
