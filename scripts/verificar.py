from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,xml.etree.ElementTree as ET,sys,re
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
from PIL import Image
from pypdf import PdfReader
OUT=ROOT/'ENTREGA'

class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ['src','href'] and v:self.links.append(v)

def main():
 checks=[];errors=[]
 def check(ok,label):
  checks.append({'check':label,'passed':bool(ok)})
  if not ok:errors.append(label)
 manifests=[]
 for name in ['manifesto-logos','manifesto-artes']:manifests+=json.loads((ROOT/'docs'/(name+'.json')).read_text(encoding='utf-8'))
 check(len(manifests)==40,'40 artes originais: 14 de marca e 26 de redes/embalagens')
 for a in manifests:
  f=OUT/a['file'];svg=ET.parse(f).getroot()
  check(not svg.findall('.//{http://www.w3.org/2000/svg}text'),a['file']+' — texto em curvas')
  check(not any('http' in node.attrib.get('href','') and not node.attrib.get('href','').startswith('data:') for node in svg.iter()),a['file']+' — sem recurso externo')
  with Image.open(f.with_suffix('.png')) as im:
   check(im.size==(a['width'],a['height']),a['file']+' — PNG na dimensão correta')
   if a['file'].startswith('01-logos/') and not any(t in a['file'] for t in ['avatar','padrao']):
    alpha=im.getchannel('A').getextrema() if im.mode=='RGBA' else (255,255)
    check(alpha[0]==0 and alpha[1]>0,a['file']+' — transparência preservada')
  for text in a['text_bounds']:
   bb=text['bounds']
   check(not bb or (bb[0]>=0 and bb[1]>=0 and bb[2]<=a['width'] and bb[3]<=a['height']),a['file']+' — texto dentro da arte: '+text['text'])
 final_svg=list(OUT.rglob('*.svg'))
 for f in final_svg:
  try:ET.parse(f)
  except ET.ParseError:errors.append('XML inválido: '+f.relative_to(OUT).as_posix())
 check(len(list((OUT/'02-redes/feed').glob('*.png')))==9,'Nove posts de feed')
 check(len(list((OUT/'02-redes/stories').glob('*.png')))==4,'Quatro stories')
 check(len(list((OUT/'02-redes/destaques').glob('*.png')))==6,'Seis capas de destaque')
 check(len(list(OUT.rglob('editaveis/*.svg')))==26,'26 SVG com textos editáveis')
 for name in ['feed/03-editorial-looks.svg','stories/02-editorial.svg']:
  parent,filename=name.split('/')
  editable=ET.parse(OUT/'02-redes'/parent/'editaveis'/filename).getroot()
  notice=next(t for t in editable.findall('.//{http://www.w3.org/2000/svg}text') if 'IMAGEM GERADA POR IA' in ''.join(t.itertext()))
  phone_size=float(notice.attrib['font-size'])*390/1080
  check(phone_size>=10.5,name+' — aviso conceitual legível a 390px')
  if parent=='stories':check(float(notice.attrib['y'])<=1680,name+' — aviso afastado pelo menos 240px da base')
 for f in OUT.rglob('*.html'):
  parser=Links();content=f.read_text(encoding='utf-8');parser.feed(content)
  check('\ufffd' not in content,f.name+' — UTF-8 sem substituições')
  for link in parser.links:
   parsed=urlsplit(link)
   if not parsed.scheme and parsed.path:
    target=(f.parent/unquote(parsed.path)).resolve()
    check(target.is_file(),f.relative_to(OUT).as_posix()+' — link local: '+link)
 for f in OUT.rglob('*.pdf'):
  reader=PdfReader(f)
  expected=21 if f.name=='Manual-Aurevi.pdf' else 1 if f.parent.name=='03-embalagens' else None
  check(len(reader.pages)>0 and (expected is None or len(reader.pages)==expected),f.name+' — páginas: '+str(len(reader.pages)))
  if f.parent.name=='03-embalagens':
   a=next(a for a in manifests if Path(a['file']).stem==f.stem)
   page=reader.pages[0];w=float(page.mediabox.width)*25.4/72;h=float(page.mediabox.height)*25.4/72
   check(abs(w-a['physical_mm'][0])<0.5 and abs(h-a['physical_mm'][1])<0.5,f.name+' — medida física do PDF')
 links=json.loads((OUT/'07-mockups-kittl/links.json').read_text(encoding='utf-8'))
 check(len(links)==4,'Quatro mockups Kittl com links de edição')
 for m in links:
  check(m['visibleRatio']>=0.99,m['filename']+' — arte inteira visível no Kittl')
  check(bool(m['savedUploadId']),m['filename']+' — salvo na biblioteca Kittl')
  with Image.open(OUT/'07-mockups-kittl'/m['filename']) as im:check(im.size==(1080,1080),m['filename']+' — 1080×1080')
 for p in ['Fraunces-LICENCA.txt','Manrope-LICENCA.txt']:
  check('SIL OPEN FONT LICENSE' in (OUT/'06-fontes'/p).read_text(encoding='utf-8'),p+' — licença original incluída')
 check(not any('pesquisa' in p.parts for p in OUT.rglob('*')),'Pesquisa de terceiros fora da entrega')
 summary={'checks':len(checks),'passed':sum(c['passed'] for c in checks),'errors':errors,'results':checks}
 (ROOT/'.tools/verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in summary.items() if k!='results'},ensure_ascii=False))
 if errors:sys.exit(1)

if __name__=='__main__':main()
