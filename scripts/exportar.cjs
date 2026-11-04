const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
const fs=require('node:fs/promises');const path=require('node:path');const {pathToFileURL}=require('node:url');
(async()=>{
 const out=path.resolve('ENTREGA');
 async function walk(dir){let a=[];for(const e of await fs.readdir(dir,{withFileTypes:true})){if(e.isDirectory()&&e.name!=='editaveis')a.push(...await walk(path.join(dir,e.name)));else if(e.isFile()&&e.name.endsWith('.svg'))a.push(path.join(dir,e.name));}return a;}
 const all=await walk(out);const selected=process.argv.slice(2);const targets=selected.length?all.filter(f=>selected.some(s=>f.replaceAll('\\','/').endsWith(s))):all;const browser=await chromium.launch({channel:'chrome',headless:true});
 const errors=[];let count=0;
 for(let i=0;i<targets.length;i+=3){await Promise.all(targets.slice(i,i+3).map(async file=>{
  const p=await browser.newPage();
  try{
   await p.goto(pathToFileURL(file).href,{waitUntil:'load'});
   const box=await p.evaluate(()=>{const s=document.querySelector('svg');return {w:s.viewBox.baseVal.width,h:s.viewBox.baseVal.height};});
   await p.setViewportSize({width:Math.round(box.w),height:Math.round(box.h)});
   await p.evaluate(({w,h})=>{const s=document.documentElement;s.setAttribute('width',w);s.setAttribute('height',h);s.style.display='block';s.style.width=w+'px';s.style.height=h+'px';},box);
   await p.screenshot({path:file.replace(/\.svg$/,'.png'),omitBackground:true});count++;
  }catch(e){errors.push({file,error:e.message});}finally{await p.close();}
 }));}
 console.log(JSON.stringify({exported:count,errors}));await browser.close();if(errors.length)process.exitCode=1;
})();
