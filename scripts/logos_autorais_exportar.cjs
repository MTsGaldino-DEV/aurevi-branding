const fs=require('node:fs/promises'),path=require('node:path');
const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
const root=path.resolve(process.argv[2]||'ESTUDOS-LOGO-AUTORAL');
async function scan(dir){let a=[];for(const d of await fs.readdir(dir,{withFileTypes:true})){const p=path.join(dir,d.name);if(d.isDirectory())a.push(...await scan(p));else if(p.endsWith('.svg'))a.push(p)}return a}
(async()=>{const b=await chromium.launch({channel:'chrome',headless:true});const c=await b.newContext({offline:true});const p=await c.newPage();let errors=[];p.on('pageerror',e=>errors.push(e.message));
for(const file of await scan(root)){
 const svg=await fs.readFile(file,'utf8');const dims=svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);const w=+dims[1],h=+dims[2];
 await p.setViewportSize({width:w,height:h});await p.setContent('<!doctype html><html><head><style>html,body{margin:0;background:transparent}svg{display:block}</style></head><body>'+svg+'</body></html>');
 await p.screenshot({path:file.replace('.svg','.png'),omitBackground:true});
 if(file.endsWith('Comparativo.svg')||file.endsWith('Apresentacao.svg')){
  await p.addStyleTag({content:`@page{size:${w/6}mm ${h/6}mm;margin:0}@media print{svg{width:${w/6}mm!important;height:${h/6}mm!important}}`});
  await p.pdf({path:file.replace('.svg','.pdf'),printBackground:true,preferCSSPageSize:true});
 }
}await b.close();if(errors.length)throw Error(JSON.stringify(errors));console.log('SVGs e PDFs exportados; sem erros de navegador.');})().catch(e=>{console.error(e);process.exit(1)});
