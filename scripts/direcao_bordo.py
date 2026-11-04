from pathlib import Path
from html import escape
import json,shutil
from revisao02_estudos import logo,label,svg

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'DIRECAO-BORDO'
BORDO='#681E36';GOLD='#CFB77F';IVORY='#FAF6EF';INK='#2D1A22'

def monogram(color):
    # Original construction based on the requested split diagonals and curled terminals.
    # A and V remain separately readable; the open A does not use a crossbar.
    a='M69 18 L161 226 L137 226 L65 61 L28 158 C14 193 31 218 58 217 C73 217 85 209 92 195 L92 218 C83 231 67 237 50 236 C18 235 4 211 10 184 C12 174 18 159 24 144 Z'
    v='M99 18 L125 18 L202 189 L245 88 C264 43 240 13 210 24 C198 28 188 38 183 51 L183 27 C194 17 205 12 220 13 C256 14 276 49 256 95 L199 230 L192 230 Z'
    return f'<g aria-label="AV"><path d="{a}" fill="{color}"/><path d="{v}" fill="{color}"/></g>'

def abstract_monogram(color):
    # Two parallel stems, connected by open curved returns; drawn for this study.
    return f'<g aria-label="AV — gesto abstrato" fill="none" stroke="{color}" stroke-width="4.6" stroke-linecap="round" stroke-linejoin="round"><path d="M122 24 L210 228 C177 252 132 245 98 215 C49 172 49 121 84 84 C103 64 116 44 122 24 Z"/><path d="M85 82 L171 270 C195 244 219 228 241 203 C273 167 281 124 259 96 C244 77 222 70 198 72"/></g>'

def save(name,body,w,h,title):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(svg(body,w,h,title),encoding='utf-8')

def main():
    for folder in ['fontes','editorial','logos','mockups']: (OUT/folder).mkdir(parents=True,exist_ok=True)
    for p in (ROOT/'REVISAO-02/fontes').iterdir():
        if p.is_file():shutil.copy2(p,OUT/'fontes'/p.name)
    shutil.copy2(ROOT/'REVISAO-02/editorial/vestido-estudo.png',OUT/'editorial/vestido-estudo.png')
    for name,color in [('bordo',BORDO),('ouro',GOLD),('marfim',IVORY)]:
        body=f'<g transform="translate(96 70) scale(2.4)">{monogram(color)}</g>'
        save('logos/AV-'+name+'.svg',body,840,720,'Aurevi — AV curvo '+name)
        body=f'<g transform="translate(85 20) scale(2.4)">{abstract_monogram(color)}</g>'
        save('logos/AV-gesto-'+name+'.svg',body,840,720,'Aurevi — AV abstrato '+name)
        mark,h=logo(1,color,1320)
        body=f'<g transform="translate(140 80)">{mark}</g>'+label('MODA FEMININA',800,475,25,color,'middle',7)
        save('logos/AUREVI-assinatura-'+name+'.svg',body,1600,560,'Aurevi — assinatura em estudo '+name)
    for i,key in enumerate(['01-editorial','02-assinatura','03-contemporanea']):
        for name,color in [('bordo',BORDO),('marfim',IVORY)]:
            mark,h=logo(i,color,1320);body=f'<g transform="translate(140 75)">{mark}</g>'+label('MODA FEMININA',800,475,25,color,'middle',7)
            save('logos/'+key+'-'+name+'.svg',body,1600,560,'Aurevi — opção '+str(i+1)+' '+name)
    # A lockup is useful for context; logo and monogram also remain independent.
    for name,color in [('bordo',BORDO),('ouro',GOLD)]:
        body=f'<g transform="translate(594 50) scale(1.5)">{monogram(color)}</g>'
        mark,h=logo(1,color,1280);body+=f'<g transform="translate(160 510)">{mark}</g>'+label('MODA FEMININA',800,905,26,color,'middle',8)
        save('logos/composicao-'+name+'.svg',body,1600,1040,'Aurevi — composição AV e nome '+name)
    # A flat tag: polished burgundy/gold, no natural-paper cues.
    body=f'<rect width="620" height="1060" fill="{BORDO}"/>'
    body+=f'<g transform="translate(170 150) scale(1.05)">{monogram(GOLD)}</g>'
    mark,h=logo(1,IVORY,470);body+=f'<g transform="translate(75 645)">{mark}</g>'+label('MODA FEMININA',310,840,18,IVORY,'middle',4)
    body+=label('@use_aurevi',310,980,20,GOLD,'middle')
    save('tag-estudo.svg',body,620,1060,'Aurevi — estudo de tag bordô e ouro')
    palette={'direcao':'Bordô e ouro, conforme referências enviadas pelo cliente','bordo':BORDO,'ouro_champagne':GOLD,'marfim':IVORY,'tinta':INK,'nota':'Aproximações digitais propostas, não cores extraídas com precisão do tecido fotografado; acabamento metálico depende de material e prova.'}
    (OUT/'paleta.json').write_text(json.dumps(palette,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Direção bordô criada: AV curvo, três escritas e tag; arquivos anteriores preservados.')

if __name__=='__main__':main()
