"""Upload only Aurevi artwork and use deterministic Kittl mockup templates."""
from pathlib import Path
from urllib.request import Request,urlopen
import json,sys
from kittl_connector import Bridge,STATE,ROOT,safe

def data(result):
 if result.get('isError'):raise RuntimeError(str(safe(result)))
 if result.get('structuredContent'):return result['structuredContent']
 for c in result.get('content',[]):
  if c.get('type')=='text':
   try:return json.loads(c['text'])
   except ValueError:pass
 return result

def upload(b,filename,initial=None):
 result=data(initial or b.tool('kittl-upload-image',{}))
 request=Request(result['signedUrl'],data=filename.read_bytes(),headers={'Content-Type':'image/png'},method='PUT')
 with urlopen(request,timeout=90) as r:assert r.status in [200,201,204]
 print('Uploaded',filename.name,'objectId:',result['objectId'])
 return result['objectId']

def main():
 b=Bridge()
 try:
  teams=data(json.loads((STATE/'teams.json').read_text(encoding='utf-8')))
  uploads_file=STATE/'artwork-ids.json'
  if uploads_file.exists():ids=json.loads(uploads_file.read_text())
  else:
   ids={}
   # Logo PNGs were exported from the exact approved vector artwork.
   for name,filename in [('sacola','03-embalagens/sacola-aplicacao.png'),('logo','01-logos/logo-verde.png'),('cartao','03-embalagens/cartao-frente.png')]:
    initial=json.loads((STATE/'upload-inicial.json').read_text()) if not ids and (STATE/'upload-inicial.json').exists() else None
    ids[name]=upload(b,ROOT/'ENTREGA'/filename,initial)
   uploads_file.write_text(json.dumps(ids,indent=2))
  args={'workspaceId':teams['defaultTeamId'],'size':1080,'backgroundColor':'#f4efe6','renders':[
   {'mockupTemplateId':5853,'designs':[{'image':ids['sacola'],'placement':{'anchor':'center','size':'large'}}]},
   {'mockupTemplateId':4868,'designs':[{'image':ids['sacola'],'placement':{'anchor':'center','size':'large'}}]},
   {'mockupTemplateId':463,'designs':[{'image':ids['logo'],'placement':{'anchor':'center','size':'large'}}]},
   {'mockupTemplateId':1786,'designs':[{'image':ids['cartao'],'placement':{'anchor':'center','size':'fill'}}]},
  ]}
  r=b.tool('kittl-render-mockup',args)
  (STATE/'mockups-result.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
  print(json.dumps(safe(r),ensure_ascii=False)[:22000])
 finally:b.close()
if __name__=='__main__':main()
