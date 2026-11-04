from kittl_connector import Bridge,STATE,ROOT,safe
from kittl_mockups import data
from urllib.request import urlopen
import json

def main():
 b=Bridge()
 try:
  teams=data(json.loads((STATE/'teams.json').read_text(encoding='utf-8')));team=teams['defaultTeamId']
  ids=json.loads((STATE/'artwork-ids.json').read_text())
  raw=json.loads((STATE/'mockups-result.json').read_text(encoding='utf-8'));current=data(raw)
  if current['renders'][3]['designs'][0]['visibleRatio']<0.99:
   result=b.tool('kittl-render-mockup',{'workspaceId':team,'size':1080,'backgroundColor':'#f4efe6','renders':[{'mockupTemplateId':1786,'designs':[{'image':ids['cartao']}]}]})
   result=data(result);current['renders'][3]=result['renders'][0]
   raw['content'][0]['text']=json.dumps(current,ensure_ascii=False)
   (STATE/'mockups-result.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2),encoding='utf-8')
  names=['01-sacola','02-ecobag','03-tag-clara','04-cartao']
  out=ROOT/'ENTREGA/07-mockups-kittl';out.mkdir(parents=True,exist_ok=True)
  for name,r in zip(names,current['renders']):
   (out/(name+'.png')).write_bytes(urlopen(r['url'],timeout=90).read())
   print(name,'visibleRatio',r['designs'][0]['visibleRatio'])
  (STATE/'mockups-metadata.json').write_text(json.dumps([dict(r,filename=n+'.png') for n,r in zip(names,current['renders'])],ensure_ascii=False,indent=2),encoding='utf-8')
  # Persist after inspection, with an explicit CLI flag.
  import sys
  if '--save' in sys.argv:
   folder_file=STATE/'folder.json'
   if folder_file.exists():folder=data(json.loads(folder_file.read_text(encoding='utf-8')))
   else:
    fr=b.tool('kittl-create-upload-folder',{'workspaceId':team,'name':'Aurevi - identidade visual'})
    folder_file.write_text(json.dumps(fr,ensure_ascii=False,indent=2),encoding='utf-8');folder=data(fr)
   print('Folder response keys:',list(folder.keys()))
   fid=folder.get('id') or folder.get('folder',{}).get('id')
   if not fid:raise RuntimeError('Folder ID missing')
   saved=[]
   for name,oid in [(n,r['objectId']) for n,r in zip(names,current['renders'])]+list(ids.items()):
    args={'workspaceId':team,'objectId':oid,'name':'Aurevi - '+name,'folderId':fid}
    r=b.tool('kittl-save-image-to-library',args);d=data(r);saved.append({'name':name,'result':d})
    print('Saved',name)
   (STATE/'saved-library.json').write_text(json.dumps(saved,ensure_ascii=False,indent=2),encoding='utf-8')
 finally:b.close()
if __name__=='__main__':main()
