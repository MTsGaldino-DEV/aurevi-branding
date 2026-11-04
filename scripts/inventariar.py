from pathlib import Path
import json,csv,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools/python'))
from PIL import Image
OUT=ROOT/'ENTREGA'

def main():
 arts=[]
 for name in ['manifesto-logos','manifesto-artes']:
  arts+=json.loads((ROOT/'docs'/(name+'.json')).read_text(encoding='utf-8'))
 descriptions={}
 for a in arts:
  for suffix in ['.svg','.png','.pdf']:
   descriptions[str(Path(a['file']).with_suffix(suffix)).replace('\\','/')]=a
  descriptions[str(Path(a['file']).parent/'editaveis'/Path(a['file']).name).replace('\\','/')]=dict(a,status='Editável — conferir fontes e conteúdo')
 results=[]
 for p in sorted(OUT.rglob('*')):
  if not p.is_file() or p.name in ['inventario.json','inventario.csv','VERIFICACAO.md']:continue
  rel=p.relative_to(OUT).as_posix();a=descriptions.get(rel,{})
  rec={'arquivo':rel,'formato':p.suffix.removeprefix('.'),'bytes':p.stat().st_size,'largura_px':'','altura_px':'','medida_mm':a.get('physical_mm') or '', 'estado':a.get('status','Recurso de apoio'),'observacoes':a.get('notes',''),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
  if p.suffix=='.png':
   with Image.open(p) as im:rec.update(largura_px=im.width,altura_px=im.height)
  elif p.suffix=='.svg':rec.update(largura_px=a.get('width',''),altura_px=a.get('height',''))
  if rel.startswith('01-logos/'):rec['estado']='Marca — pronto'
  elif rel.startswith('07-mockups-kittl/'):
   rec['estado']='Mockup Kittl — estudo de aplicação'
  results.append(rec)
 meta={'marca':'Aurevi','versao':'1.0','data':'2026-11-04','observacao':'Lista exclui os dois inventários e VERIFICACAO.md para evitar referência circular. Para SVG físico, os números de largura/altura são unidades do viewBox; a medida em mm define o tamanho de impressão.','arquivos':results}
 (OUT/'inventario.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
 with (OUT/'inventario.csv').open('w',encoding='utf-8-sig',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=list(results[0]),delimiter=';');writer.writeheader();writer.writerows(results)
 print('Inventário:',len(results),'arquivos; excluídos inventários e registro de verificação.')

if __name__=='__main__':main()
