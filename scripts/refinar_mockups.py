from pathlib import Path
import json
from kittl_connector import Bridge,STATE,safe
from kittl_mockups import data

b=Bridge()
try:
 teams=data(json.loads((STATE/'teams.json').read_text(encoding='utf-8')))
 ids=json.loads((STATE/'artwork-ids.json').read_text())
 # Exact placement avoids expanding to the broad rectangular mask of tilted cards.
 result=b.tool('kittl-render-mockup',{'workspaceId':teams['defaultTeamId'],'size':1080,'backgroundColor':'#f4efe6','renders':[
  {'mockupTemplateId':463,'designs':[{'image':ids['logo'],'placement':{'centerX':0.535,'centerY':0.535,'maxSize':0.31}}]},
  {'mockupTemplateId':1786,'designs':[{'image':ids['cartao'],'placement':{'centerX':0.51,'centerY':0.473,'maxSize':0.48}}]}
 ]})
 d=data(result)
 orig=json.loads((STATE/'mockups-result.json').read_text(encoding='utf-8'))
 od=data(orig);od['renders'][2:]=d['renders'];orig['content'][0]['text']=json.dumps(od,ensure_ascii=False)
 # Strip draft previews because they no longer correspond to the refined outputs.
 orig['content']=orig['content'][:1]
 (STATE/'mockups-result.json').write_text(json.dumps(orig,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(safe(d),ensure_ascii=False)[:6500])
finally:b.close()
