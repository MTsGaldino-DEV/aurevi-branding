from pathlib import Path
from urllib.request import urlopen
import json
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'ENTREGA/07-mockups-kittl';out.mkdir(parents=True,exist_ok=True)
raw=json.loads((ROOT/'.tools/kittl/mockups-result.json').read_text(encoding='utf-8'))
data=json.loads(raw['content'][0]['text'])
names=['01-sacola','02-ecobag','03-tag-clara','04-cartao']
for name,r in zip(names,data['renders']):
 p=out/(name+'.png');p.write_bytes(urlopen(r['url'],timeout=60).read())
 print(name,'visibleRatio:',r['designs'][0]['visibleRatio'])
(ROOT/'.tools/kittl/mockups-metadata.json').write_text(json.dumps([dict(r,filename=n+'.png') for n,r in zip(names,data['renders'])],ensure_ascii=False,indent=2),encoding='utf-8')
