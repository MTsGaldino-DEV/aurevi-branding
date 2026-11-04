const fs=require('node:fs/promises');
const path=require('node:path');
(async()=>{
 const targets=[];
 for(const id of ['aurevi-instagram','donna-instagram']){
  const data=JSON.parse(await fs.readFile(path.join(__dirname,id+'.json'),'utf8'));
  const imgs=data.images.filter(x=>!x.src.startsWith('data:'));
  targets.push([id+'-avatar.jpg',imgs[0].src]);
  const posts=imgs.filter(x=>x.width>200).slice(0,id==='aurevi-instagram'?1:3);
  posts.forEach((img,i)=>targets.push([id+'-post-'+(i+1)+'.jpg',img.src]));
 }
 targets.push(['kanoa-letras.png','https://mir-s3-cdn-cf.behance.net/project_modules/1400/ed34d3208303969.66ec35c793bea.png']);
 targets.push(['kanoa-sacola.png','https://mir-s3-cdn-cf.behance.net/project_modules/1400/cab66a208303969.66ec35c792897.png']);
 await Promise.all(targets.map(async([name,url])=>{try{const r=await fetch(url);if(!r.ok)throw Error(String(r.status));await fs.writeFile(path.join(__dirname,name),Buffer.from(await r.arrayBuffer()));console.log(name+' OK');}catch(e){console.log(name+' '+e.message);}}));
})();
