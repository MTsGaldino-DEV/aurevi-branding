const {chromium}=require('C:/Users/matheus.galdino/AppData/Local/npm-cache/_npx/e41f203b7505f1fb/node_modules/playwright');
const fs=require('node:fs/promises');
const path=require('node:path');
const refs=[
 {id:'kanoa',page:'https://www.behance.net/gallery/208303969/Kanoa-Identidade-Visual?locale=pt_BR',image:'https://mir-s3-cdn-cf.behance.net/project_modules/1400/ed34d3208303969.66ec35c793bea.png'},
 {id:'madu',page:'https://www.behance.net/gallery/175647547/Identidade-Visual-Loja-de-Roupa-Vestuario?locale=pt_BR',image:'https://mir-s3-cdn-cf.behance.net/project_modules/1400/32dbe9175647547.64b736fdb5f4c.jpg'},
 {id:'margot',page:'https://www.behance.net/gallery/137758259/Margot-luxe-streetwear-for-women-Branding-project?locale=pt_BR',image:'https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/e8f373137758259.6210c30cd727a.jpg'}
];
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const context=await browser.newContext({viewport:{width:1400,height:1000},locale:'pt-BR'});
 const results=await Promise.all(refs.map(async(ref)=>{
  const p=await context.newPage();const result={id:ref.id,page:ref.page,image:ref.image};
  try{const r=await p.goto(ref.page,{waitUntil:'domcontentloaded',timeout:30000});result.pageStatus=r?.status();result.title=await p.title();result.text=(await p.locator('body').innerText()).slice(0,2000);}catch(e){result.pageError=e.message;}
  try{const r=await p.goto(ref.image,{waitUntil:'load',timeout:30000});result.imageStatus=r?.status();if(r?.ok()){await fs.writeFile(path.join(__dirname,ref.id+'-referencia.jpg'),await r.body());await p.screenshot({path:path.join(__dirname,ref.id+'-imagem-no-playwright.png'),fullPage:true});}}catch(e){result.imageError=e.message;}
  await p.close();console.log(JSON.stringify(result));return result;
 }));
 await fs.writeFile(path.join(__dirname,'segunda-tentativa.json'),JSON.stringify(results,null,2));await browser.close();
})();
