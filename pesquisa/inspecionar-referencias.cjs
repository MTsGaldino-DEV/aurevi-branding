const { chromium } = require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
const fs = require('node:fs/promises');
const path = require('node:path');
const targets = [
 ['aurevi-instagram','https://www.instagram.com/use_aurevi/'],
 ['donna-instagram','https://www.instagram.com/donna.oficial/'],
 ['donna-bio','https://bio.lojadonnaoficial.com.br/'],
 ['donna-loja','https://www.lojadonnaoficial.com.br/'],
 ['kanoa-behance','https://www.behance.net/gallery/208303969/Kanoa-Identidade-Visual'],
 ['vestuario-behance','https://www.behance.net/gallery/175647547/Identidade-Visual-Loja-de-Roupa-Vestuario'],
 ['margot-behance','https://www.behance.net/gallery/137758259/Margot-luxe-streetwear-for-women-Branding-project']
];
(async()=>{
 const dir=__dirname;
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:1100},locale:'pt-BR'});
 const reports=[];
 for(let i=0;i<targets.length;i+=3){
  await Promise.all(targets.slice(i,i+3).map(async([id,url])=>{
   const page=await context.newPage();
   let status=null,error=null;
   try { const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:45000});status=response?.status();await page.waitForTimeout(5500); }catch(e){error=e.message;}
   try {
    await page.screenshot({path:path.join(dir,id+'.png'),fullPage:true,timeout:20000});
    const data=await page.evaluate(()=>({title:document.title,url:location.href,text:document.body?.innerText,meta:[...document.querySelectorAll('meta[property],meta[name="description"]')].map(m=>({key:m.getAttribute('property')||m.name,value:m.content})),images:[...document.images].filter(i=>i.naturalWidth>100).map(i=>({src:i.currentSrc,alt:i.alt,width:i.naturalWidth,height:i.naturalHeight})),fonts:[...new Set([...document.querySelectorAll('h1,h2,p,a')].slice(0,100).map(e=>getComputedStyle(e).fontFamily))]}));
    await fs.writeFile(path.join(dir,id+'.json'),JSON.stringify({id,status,error,...data},null,2));
    reports.push({id,status,error,title:data.title,text:data.text?.slice(0,1800),images:data.images?.slice(0,5),fonts:data.fonts});
   }catch(e){reports.push({id,status,error:e.message});}
   await page.close();
  }));
  console.log(JSON.stringify(reports.slice(-3),null,2));
 }
 await fs.writeFile(path.join(dir,'resultado.json'),JSON.stringify(reports,null,2));
 await browser.close();
})();
