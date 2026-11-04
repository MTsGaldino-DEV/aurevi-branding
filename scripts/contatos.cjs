const fs=require('node:fs/promises'),path=require('node:path'),{pathToFileURL}=require('node:url');
const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
(async()=>{
 const out=path.resolve('ENTREGA');const pdir=path.resolve('.tools/previews');await fs.mkdir(pdir,{recursive:true});
 const b=await chromium.launch({channel:'chrome',headless:true});
 for(const [name,folder,cols]of [['feed','02-redes/feed',3],['stories','02-redes/stories',4],['embalagens','03-embalagens',4],['mockups','07-mockups-kittl',2]]){
  const files=(await fs.readdir(path.join(out,folder))).filter(f=>f.endsWith('.png')).sort();
  const html=`<meta charset="utf-8"><style>body{margin:0;padding:30px;background:#e0d9ce;display:grid;grid-template-columns:repeat(${cols},1fr);gap:22px;font:16px Arial;color:#203c32}figure{margin:0}img{width:100%;background:#f4efe6}figcaption{padding:10px 0}</style>`+files.map(f=>`<figure><img src="${pathToFileURL(path.join(out,folder,f)).href}"><figcaption>${f}</figcaption></figure>`).join('');
  const h=path.join(pdir,name+'.html');await fs.writeFile(h,html);const p=await b.newPage({viewport:{width:1440,height:1000}});await p.goto(pathToFileURL(h).href);await p.screenshot({path:path.join(pdir,name+'.png'),fullPage:true});await p.close();
 }
 await b.close();})();
