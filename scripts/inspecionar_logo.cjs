const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
const path=require('node:path');
(async()=>{
const b=await chromium.launch({channel:'chrome',headless:true});const p=await b.newPage({viewport:{width:1400,height:900}});
await p.setContent('<body style="margin:0;background:#F4EFE6;display:grid;grid-template-columns:2fr 1fr;align-items:center;height:900px"><img style="width:90%;margin:5%" src="file:///'+path.resolve('ENTREGA/01-logos/logo-verde.svg').replaceAll('\\','/')+'"><img style="width:80%" src="file:///'+path.resolve('ENTREGA/01-logos/simbolo-verde.svg').replaceAll('\\','/')+'"></body>');
// A file-backed page allows image loading under Chrome local-file rules.
const fs=require('node:fs/promises');await fs.mkdir('.tools/previews',{recursive:true});const html=await p.content();await fs.writeFile('.tools/previews/logo.html',html);await p.goto('file:///'+path.resolve('.tools/previews/logo.html').replaceAll('\\','/'));await p.screenshot({path:'.tools/previews/logo.png'});await b.close();})();
