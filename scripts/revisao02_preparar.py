from pathlib import Path
from urllib.request import urlopen
import json
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'REVISAO-02'
(DEST/'fontes').mkdir(parents=True,exist_ok=True)
for family,name in [('bodonimoda','BodoniModa'),('cormorantgaramond','CormorantGaramond'),('italiana','Italiana')]:
    records=json.load(urlopen('https://api.github.com/repos/google/fonts/contents/ofl/'+family))
    font=next(r for r in records if r['name'].endswith('.ttf') and 'Italic' not in r['name'])
    lic=next(r for r in records if r['name']=='OFL.txt')
    (DEST/'fontes'/(name+'.ttf')).write_bytes(urlopen(font['download_url']).read())
    text=urlopen(lic['download_url']).read()
    assert b'SIL OPEN FONT LICENSE' in text
    (DEST/'fontes'/(name+'-OFL.txt')).write_bytes(text)
    print(name,'e licença OFL obtidos da fonte oficial.')
