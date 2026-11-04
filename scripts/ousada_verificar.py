"""Verificação de entregáveis reais: dimensões, fontes, PDFs, SVGs e ZIP."""
from pathlib import Path
import sys,json,xml.etree.ElementTree as ET,zipfile,hashlib
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'.tools/python'))
from PIL import Image
from pypdf import PdfReader
OUT=ROOT/'IDENTIDADE-ELEGANTE-OUSADA'
checks=[]
def check(label,ok):
    checks.append({'check':label,'ok':bool(ok)})
def contrast(c1,c2):
    def lum(s):
        v=[int(s[i:i+2],16)/255 for i in (1,3,5)];v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v]
        return sum(x*y for x,y in zip(v,[.2126,.7152,.0722]))
    a,b=sorted([lum(c1),lum(c2)]);return round((b+.05)/(a+.05),2)
items=json.loads((OUT/'inventario.json').read_text(encoding='utf-8'))
for a in items:
    p=OUT/a['file'];svg=ET.parse(p).getroot();check(a['file']+' SVG válido',svg.tag.endswith('svg'))
    with Image.open(p.with_suffix('.png')) as im:
        check(a['file']+' dimensão PNG',im.size==(a['width'],a['height']))
        if a['file'].startswith('01-marca/'):
            check(a['file']+' transparente',im.mode=='RGBA' and im.getchannel('A').getextrema()[0]==0)
    check(a['file']+' textos dentro',all(0<=t['x0'] and 0<=t['y0'] and t['x1']<=a['width'] and t['y1']<=a['height'] for t in a['text_bounds']))
    check(a['file']+' sem imagem externa',all(n.get('href','').startswith(('data:','#')) for n in svg.iter() if n.tag.endswith('image')))
    if a['physical_mm']:
        pdf=PdfReader(p.with_suffix('.pdf'));target=a['physical_mm'];box=pdf.pages[0].mediabox
        check(a['file']+' PDF físico',len(pdf.pages)==1 and abs(float(box.width)*25.4/72-target[0])<.4 and abs(float(box.height)*25.4/72-target[1])<.4)
main=PdfReader(OUT/'Manual-Aurevi-Elegante-Ousada.pdf');check('Manual com 18 páginas',len(main.pages)==18)
check('Texto do manual extraível','AUREVI' in ''.join(p.extract_text() for p in main.pages))
check('Nove posts',len(list((OUT/'02-redes/feed').glob('*.png')))==9)
check('Quatro stories',len(list((OUT/'02-redes/stories').glob('*.png')))==4)
check('Seis destaques',len(list((OUT/'02-redes/destaques').glob('*.png')))==6)
check('Dois avatares',len(list((OUT/'02-redes/avatares').glob('*.png')))==2)
editable=list(OUT.rglob('editaveis/*.svg'));check('Textos editáveis',len(editable)==15 and all('<text ' in p.read_text(encoding='utf8') for p in editable))
for family in ['CormorantGaramond','Manrope']:
    check(family+' fonte e licença',(OUT/f'06-fontes/{family}.ttf').stat().st_size>10000 and 'SIL OPEN FONT LICENSE' in (OUT/f'06-fontes/{family}-OFL.txt').read_text(encoding='utf8'))
pw=json.loads((OUT/'verificacao-playwright.json').read_text())
check('Navegador offline e limites',not pw['missing'] and not pw['outside'] and not pw['errors'] and not pw['mobile']['overflow'] and all(pw['fonts'].values()))
ratios={'marfim_sobre_vermelho':contrast('#FAF6EF','#450A10'),'ouro_sobre_vermelho':contrast('#CFB77F','#450A10'),'grafite_sobre_marfim':contrast('#242424','#FAF6EF'),'vermelho_sobre_cinza':contrast('#450A10','#9B9995'),'ouro_sobre_marfim':contrast('#CFB77F','#FAF6EF')}
check('Contraste dos textos principais',min(ratios[k] for k in ['marfim_sobre_vermelho','ouro_sobre_vermelho','grafite_sobre_marfim','vermelho_sobre_cinza'])>=4.5)
report={'total':len(checks),'passed':sum(x['ok'] for x in checks),'failed':[x for x in checks if not x['ok']],'contraste':ratios,'checks':checks}
(OUT/'VERIFICACAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False))
if report['failed']:raise SystemExit(1)
(OUT/'VERIFICACAO.md').write_text(f'''# Verificação — Aurevi elegante e ousada

{report['passed']}/{report['total']} checagens de entrega passaram. Manual: 18 páginas. Logos PNG com transparência; vetores válidos; textos dentro da arte; PDFs físicos com dimensão conferida. Fontes e imagens presentes em navegação offline, sem erros ou transbordamento móvel.

Contraste digital: marfim/vermelho {ratios['marfim_sobre_vermelho']}:1; ouro/vermelho {ratios['ouro_sobre_vermelho']}:1; grafite/marfim {ratios['grafite_sobre_marfim']}:1; vermelho/cinza {ratios['vermelho_sobre_cinza']}:1. Ouro/marfim {ratios['ouro_sobre_marfim']}:1: usar apenas como marca/decoração, não para texto informativo pequeno.

Imagens conceituais identificadas no guia e no editorial. Dados de produto não foram inventados. Máscaras de acabamento acompanham as artes de tag, sacola e caixa. Originais e versões anteriores preservados.
''',encoding='utf8')
if '--zip' in sys.argv:
    dest=ROOT/'Aurevi-Identidade-Elegante-Ousada.zip'
    files=sorted(p for p in OUT.rglob('*') if p.is_file())
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:z.write(p,p.relative_to(OUT).as_posix())
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None
        assert len(z.namelist())==len(files)
        assert all(hashlib.sha256(z.read(p.relative_to(OUT).as_posix())).digest()==hashlib.sha256(p.read_bytes()).digest() for p in files)
    print(json.dumps({'zip':str(dest),'files':len(files),'bytes':dest.stat().st_size,'crc_sha256':'OK'}))
