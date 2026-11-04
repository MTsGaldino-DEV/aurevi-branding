from kittl_connector import Bridge,STATE,ROOT,safe
from kittl_mockups import data,upload
from urllib.request import urlopen
import json

def main():
 b=Bridge()
 try:
  team=data(json.loads((STATE/'teams.json').read_text(encoding='utf-8')))['defaultTeamId']
  fp=STATE/'folder.json'
  if fp.exists():folder=data(json.loads(fp.read_text(encoding='utf-8')))
  else:
   r=b.tool('kittl-create-upload-folder',{'workspaceId':team,'name':'Aurevi - identidade visual'})
   fp.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8');folder=data(r)
  fid=folder.get('id') or folder.get('folder',{}).get('id')
  if not fid:raise RuntimeError('Missing folder id; response keys '+str(list(folder)))
  savedfile=STATE/'saved-library.json'
  saved=json.loads(savedfile.read_text(encoding='utf-8')) if savedfile.exists() else {}
  ids=json.loads((STATE/'artwork-ids.json').read_text())
  for name,file in [('sacola','03-embalagens/sacola-aplicacao.png'),('logo','01-logos/logo-verde.png'),('cartao','03-embalagens/cartao-frente.png')]:
   if name in saved:continue
   r=b.tool('kittl-save-image-to-library',{'workspaceId':team,'objectId':ids[name],'name':'Aurevi - arte '+name,'folderId':fid})
   if r.get('isError'):
    print('Refreshing temporary source:',name)
    oid=upload(b,ROOT/'ENTREGA'/file)
    r=b.tool('kittl-save-image-to-library',{'workspaceId':team,'objectId':oid,'name':'Aurevi - arte '+name,'folderId':fid})
   d=data(r);saved[name]=d;savedfile.write_text(json.dumps(saved,ensure_ascii=False,indent=2),encoding='utf-8')
   print('Saved source',name,json.dumps(safe(d))[:1100])
  print('Sources ready. Folder ID:',fid)
  if '--mockups' in __import__('sys').argv:
   raw=json.loads((STATE/'mockups-metadata.json').read_text(encoding='utf-8'))
   links=[]
   for m in raw:
    name=m['filename'].removesuffix('.png')
    assert all(d['visibleRatio']>=0.99 for d in m['designs']),name
    if name not in saved:
     r=b.tool('kittl-save-image-to-library',{'workspaceId':team,'objectId':m['objectId'],'name':'Aurevi - mockup '+name,'folderId':fid})
     saved[name]=data(r);savedfile.write_text(json.dumps(saved,ensure_ascii=False,indent=2),encoding='utf-8')
     print('Saved final mockup',name)
    links.append({'filename':m['filename'],'templateId':m['mockupTemplateId'],'templateName':m['name'],'editUrl':m['editUrl'],'savedUploadId':saved[name]['uploadId'],'visibleRatio':m['designs'][0]['visibleRatio']})
   dest=ROOT/'ENTREGA/07-mockups-kittl'
   (dest/'links.json').write_text(json.dumps(links,ensure_ascii=False,indent=2),encoding='utf-8')
   md='# Aurevi — mockups criados no Kittl\n\nQuatro renderizações com as artes originais da Aurevi, pelo Kittl MCP autenticado. Templates usados sem consumo de créditos de geração. Artes de origem e mockups finais foram salvos na biblioteca, na pasta **Aurevi - identidade visual**.\n\n'
   for link in links:md+='- ['+link['filename']+']('+link['editUrl']+') — template '+str(link['templateId'])+'; arte inteira visível.\n'
   md+='\nOs PNG locais têm 1080×1080 px. Os links retornados pelo Kittl abrem a composição para edição no serviço e podem exigir login. A exportação em maior resolução pode ser feita no próprio editor, conforme os recursos da conta. Não houve contratação ou alteração de plano.\n\nSacola e ecobag demonstram aplicações da assinatura. A tag clara é uma alternativa com o nome em verde; não reproduz a tag verde da arte plana. O cartão usa a arte coral com uma margem clara própria do template. Materiais e acabamentos são ilustrativos; confirmar com o fornecedor antes de fabricar.\n\nCriado com [Kittl MCP](https://www.kittl.com/mcp). O uso dos templates e exportações segue os termos da conta Kittl.\n'
   (dest/'LEIA-ME.md').write_text(md,encoding='utf-8')
 finally:b.close()
if __name__=='__main__':main()
