from pathlib import Path
from functools import lru_cache
from html import escape
import sys,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'REVISAO-02'
sys.path.insert(0,str(ROOT/'.tools/python'))
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

PALETTES=[
 {'id':'01','name':'Azul noite + ouro','colors':['#233A57','#FAF7F2','#BE9B57'],'names':['Azul noite','Porcelana','Ouro suave'],'reason':'A opção mais próxima da elegância da referência. O azul dá presença; o ouro entra na assinatura e nos acabamentos.'},
 {'id':'02','name':'Bordô + champagne','colors':['#62273C','#F7EEE5','#C2A475'],'names':['Bordô','Champagne','Ouro acetinado'],'reason':'Mais calor e personalidade feminina. Conversa com vestidos, produção de look e ocasiões especiais.'},
 {'id':'03','name':'Grafite + rosa pérola','colors':['#2B2931','#F2E3E4','#B4945C'],'names':['Grafite','Rosa pérola','Ouro discreto'],'reason':'Uma direção atual e delicada, que deixa as cores das roupas aparecerem e mantém contraste de boutique.'},
]
LOGOS=[('01-editorial','BodoniModa',500,'Editorial','Contraste entre traços finos e grossos; caixa alta e presença de marca de moda.'),('02-assinatura','CormorantGaramond',500,'Assinatura','Traço mais expressivo e um prolongamento discreto no R. Mais gesto no nome.'),('03-contemporanea','Italiana',400,'Contemporânea','Letras alongadas, desenho leve e uma leitura mais limpa e contemporânea.')]

@lru_cache(None)
def font(fam,weight=400):
 p=OUT/'fontes'/(fam+'.ttf')
 if fam=='Manrope':p=ROOT/'ENTREGA/06-fontes/Manrope.ttf'
 tt=TTFont(p);loc={}
 if 'fvar'in tt:
  axes={a.axisTag for a in tt['fvar'].axes}
  if 'wght'in axes:loc['wght']=weight
  if 'opsz'in axes:loc['opsz']=96
 gs=tt.getGlyphSet(location=loc);hf=hb.Font(hb.Face(p.read_bytes()));hf.set_variations(loc)
 return tt,gs,hf,tt['head'].unitsPerEm

def textpaths(value,fam,weight,size,spacing=0,kern=None):
 tt,gs,hf,upm=font(fam,weight);buf=hb.Buffer();buf.add_str(value);buf.guess_segment_properties();hb.shape(hf,buf,{'kern':True,'liga':False});s=size/upm
 pen=SVGPathPen(gs);bp=BoundsPen(gs);cursor=0;starts=[]
 for i,(info,p) in enumerate(zip(buf.glyph_infos,buf.glyph_positions)):
  starts.append(cursor);g=gs[tt.getGlyphOrder()[info.codepoint]];t=(s,0,0,-s,cursor+p.x_offset*s,-p.y_offset*s)
  g.draw(TransformPen(pen,t));g.draw(TransformPen(bp,t));cursor+=p.x_advance*s+spacing+(kern[i] if kern and i<len(kern) else 0)
 return pen.getCommands(),bp.bounds,starts,cursor-spacing

def label(value,x,y,size=24,color='#233A57',anchor='start',spacing=0):
 d,b,_,advance=textpaths(value,'Manrope',400,size,spacing)
 if anchor=='middle':x-=advance/2
 elif anchor=='end':x-=advance
 return f'<g aria-label="{escape(value,quote=True)}" transform="translate({x} {y})"><path d="{d}" fill="{color}"/></g>'

def logo(idx,color='#233A57',w=1450):
 _,fam,weight,_,_=LOGOS[idx]
 d,bb,starts,_=textpaths('AUREVI',fam,weight,240,spacing=4,kern=[-9,-8,-5,-7,-4])
 tail=''
 if idx==1:
  x=starts[2]+133
  tail=f'<path d="M{x} -5 C{x+35} 30 {x+97} 43 {x+156} 10" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>'
  bb=(bb[0],bb[1],max(bb[2],x+156),43)
 scale=w/(bb[2]-bb[0]);h=(bb[3]-bb[1])*scale
 return f'<g aria-label="AUREVI" transform="scale({scale}) translate({-bb[0]} {-bb[1]})"><path d="{d}" fill="{color}"/>{tail}</g>',h

def svg(body,w,h,title):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title)}</title>{body}</svg>'
def save(name,body,w,h,title):
 p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(svg(body,w,h,title),encoding='utf-8')

def av(idx,color):
 if idx==0:
  path='M8 88 L38 12 Q40 7 43 12 L76 88 L65 88 L40 29 L18 88 Z M25 65 L59 65 L63 74 L22 74 Z M49 13 L60 13 L81 65 L94 31 Q98 21 109 20 L109 30 Q104 31 102 37 L83 88 L77 88 Z'
 elif idx==1:
  # Preserve two open diagonals and add a subtle serif/contrast treatment.
  path='M7 88 L11 85 L39 12 Q40 9 42 12 L73 85 L79 88 L58 88 L63 85 L40 29 L19 85 L25 88 Z M27 64 L54 64 L57 68 L25 68 Z M49 12 L65 12 L60 15 L82 69 L102 16 L97 12 L112 12 L106 16 L79 88 L75 88 Z'
 else:
  path='M8 88 L38 14 Q40 8 43 14 L74 88 L64 88 L40 31 L18 88 Z M27 65 L55 65 L59 73 L24 73 Z M51 14 L60 14 L82 68 L99 25 Q103 15 113 14 L113 22 Q107 23 105 29 L82 88 L77 88 Z'
 return f'<path d="{path}" fill="{color}"/>'

def main():
 (OUT/'logos').mkdir(parents=True,exist_ok=True)
 for i,(key,_,_,name,desc)in enumerate(LOGOS):
  for suffix,color in [('azul','#233A57'),('branco','#FAF7F2')]:
   mark,h=logo(i,color,1450);body=f'<g transform="translate(75 50)">{mark}</g>'
   body+=label('MODA FEMININA',800,430,28,color,'middle',spacing=8)
   save('logos/'+key+'-'+suffix+'.svg',body,1600,500,'Aurevi — estudo '+name)
  # An individual sheet makes each study easy to compare/download.
  mark,h=logo(i,'#233A57',1240)
  body='<rect width="1600" height="700" fill="#FAF7F2"/>'+label('ESTUDO '+str(i+1).zfill(2)+' / '+name.upper(),80,85,22)
  body+=f'<g transform="translate(180 230)">{mark}</g>'+label(desc,80,605,23)
  save('logos/'+key+'-prancha.svg',body,1600,700,'Estudo tipográfico '+str(i+1))
 for i,title in enumerate(['Original aprovado no detalhe','Contraste mais fino','Curva mais leve']):
  body='<rect width="800" height="800" fill="#FAF7F2"/>'+f'<g transform="translate(155 160) scale(4.2)">{av(i,"#233A57")}</g>'
  body+=label(title,400,695,24,anchor='middle')
  save('av/0'+str(i+1)+'.svg',body,800,800,'AV — '+title)
 # Mockup source: actual designed vectors, transparent background.
 for i,p in enumerate(PALETTES):
  mark,h=logo(0,p['colors'][0],1280)
  body=f'<g transform="translate(160 130)">{mark}</g>'+label('MODA FEMININA',800,510,28,p['colors'][0],'middle',6)
  save('aplicacoes/logo-paleta-'+p['id']+'.svg',body,1600,650,'Aurevi — aplicação '+p['name'])
 # A flat tag study using the refined AV; no fabricated production claims.
 p=PALETTES[0];body=f'<rect width="600" height="1020" fill="{p["colors"][0]}"/>'
 body+=f'<g transform="translate(180 145) scale(2.1)">{av(1,p["colors"][2])}</g>'
 mark,h=logo(0,p['colors'][1],460);body+=f'<g transform="translate(70 500)">{mark}</g>'
 body+=label('MODA FEMININA',300,710,20,p['colors'][1],'middle',4)
 body+=label('@use_aurevi',300,938,20,p['colors'][1],'middle')
 save('aplicacoes/tag-estudo.svg',body,600,1020,'Tag — estudo em azul noite e ouro')
 (OUT/'paletas.json').write_text(json.dumps(PALETTES,ensure_ascii=False,indent=2),encoding='utf-8')
 print('Três estudos tipográficos, três paletas e três versões do AV criados em curvas.')

if __name__=='__main__':main()
