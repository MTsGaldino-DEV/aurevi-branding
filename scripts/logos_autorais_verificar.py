from pathlib import Path
import sys,json,zipfile,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'.tools/python'))
from PIL import Image
from pypdf import PdfReader
OUT=ROOT/'ESTUDOS-LOGO-AUTORAL';checks=[]
for p in sorted(OUT.rglob('*.svg')):
    s=ET.parse(p).getroot();w,h=map(float,s.get('viewBox').split()[2:])
    with Image.open(p.with_suffix('.png')) as im:
        assert im.size==(w,h),p
        checks.append(str(p.relative_to(OUT))+' dimensão')
        if p.name not in ['Comparativo.svg','Apresentacao.svg']:
            assert im.mode=='RGBA' and im.getchannel('A').getextrema()[0]==0,p
            checks.append(str(p.relative_to(OUT))+' transparência')
    assert all(n.get('href','').startswith(('data:','#')) for n in s.iter() if n.tag.endswith('image'))
for p in OUT.rglob('*.pdf'):
    assert len(PdfReader(p).pages)==1,p
    checks.append(str(p.relative_to(OUT))+' página PDF')
assert len(list(OUT.rglob('logo-metalico.svg')))==3
assert len(list(OUT.rglob('escrita-sangue.svg')))==3
assert len(list(OUT.rglob('AV-metalico.svg')))==3
report={'checks':len(checks),'passed':len(checks),'models':3,'svg':31,'pdf':4,'png':31,'note':'Desenhos e comparação inspecionados visualmente; wordmarks próprios em caminhos, sem fonte usada como logo.'}
(OUT/'VERIFICACAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
dest=ROOT/'Aurevi-3-Logotipos-Autorais.zip';files=sorted(p for p in OUT.rglob('*') if p.is_file())
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,p.relative_to(OUT).as_posix())
with zipfile.ZipFile(dest) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(files)
    assert all(hashlib.sha256(z.read(p.relative_to(OUT).as_posix())).digest()==hashlib.sha256(p.read_bytes()).digest() for p in files)
print(json.dumps({'verification':report,'zip_files':len(files),'zip_bytes':dest.stat().st_size,'CRC_SHA256':'OK'},ensure_ascii=False))
