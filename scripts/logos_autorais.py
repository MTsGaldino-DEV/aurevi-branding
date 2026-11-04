"""Três estudos Aurevi: letras e AV desenhados em caminhos próprios."""
from pathlib import Path
import json
from identidade_ousada import Art, METAL, R, G, I, C, K

ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'ESTUDOS-LOGO-AUTORAL'

# All six letters in each study are constructed here. No font glyphs are used
# in the wordmarks; Manrope is used only for the explanatory presentation text.
PRESENCA={
'A':(196,[
'M0 240 L0 235 Q15 234 21 217 L96 -2 L102 -2 L25 221 Q20 235 40 235 L40 240 Z',
'M96 -2 L111 -2 L190 222 Q194 234 210 235 L210 240 L145 240 L145 235 Q164 235 159 221 L98 39 Z',
'M48 151 L163 142 L166 150 L45 159 Z']),
'U':(191,['M0 0 H64 V5 H47 V164 C47 211 68 237 107 237 C148 237 169 209 169 165 V5 H148 V0 H195 V5 H177 V167 C177 217 151 246 104 246 C54 246 19 221 19 167 V5 H0 Z']),
'R':(209,[
'M0 0 H66 V5 H48 V235 H70 V240 H0 V235 H19 V5 H0 Z',
'M44 0 H104 C156 0 184 20 184 64 C184 106 153 127 102 127 H43 V120 H100 C133 120 153 102 153 64 C153 26 136 7 100 7 H44 Z',
'M91 122 H123 L181 217 Q191 234 211 235 V240 H173 Q165 236 156 221 L100 133 Z']),
'E':(168,[
'M0 0 H166 L169 47 H163 C159 16 145 7 116 7 H48 V112 H106 Q133 112 137 85 H143 V148 H137 Q132 120 106 120 H48 V233 H119 C149 233 162 219 170 190 H176 L171 240 H0 V235 H19 V5 H0 Z']),
'V':(205,['M0 0 H64 V5 H45 L111 203 L181 5 H160 V0 H206 V5 H190 L106 243 H99 L19 16 Q15 5 0 5 Z']),
'I':(80,['M0 0 H80 V5 H55 V235 H80 V240 H0 V235 H25 V5 H0 Z'])}

ENLACE={
'A':(202,[
'M17 198 C-6 250 11 260 35 252 C51 247 61 236 65 221 L65 241 C55 254 43 263 27 264 C-6 267 -21 244 -2 201 L89 0 Q94 -11 99 0 L197 227 Q202 237 215 238 V243 H150 V238 Q169 238 163 221 L92 49 L26 199 Z',
'M47 153 C79 142 112 139 145 146 L148 153 C113 145 79 149 43 163 Z']),
'U':(187,['M-1 0 H65 V5 Q47 5 47 21 V164 C47 214 66 239 101 239 C139 239 162 215 162 168 V22 Q162 5 142 5 V0 H191 V5 Q171 5 171 22 V171 C171 219 144 248 100 248 C51 248 19 223 19 172 V22 Q19 5 -1 5 Z']),
'R':(204,[
'M0 0 H63 V5 Q47 5 47 20 V224 Q47 238 66 238 V243 H0 V238 Q19 238 19 224 V20 Q19 5 0 5 Z',
'M43 0 H99 C151 0 182 22 182 61 C182 102 155 123 107 126 H43 V119 H98 C131 119 151 98 151 62 C151 26 135 7 96 7 H43 Z',
'M86 119 C110 117 123 132 135 152 L165 207 C179 232 195 238 213 224 L211 235 C184 255 160 243 145 218 L113 159 C104 141 96 132 86 130 Z']),
'E':(163,['M0 0 H164 L162 46 H156 Q155 8 118 8 H47 V111 H101 Q127 111 131 85 H137 V148 H131 Q127 119 101 119 H47 V235 H111 Q153 235 166 197 H172 L162 243 H0 V238 Q19 238 19 222 V20 Q19 5 0 5 Z']),
'V':(196,['M-2 0 H63 V5 Q43 5 48 20 L109 199 L174 23 Q181 5 158 5 V0 H204 V5 Q191 5 183 25 L105 242 Q102 250 98 242 L19 22 Q14 5 -2 5 Z']),
'I':(74,['M0 0 H76 V5 Q51 5 51 22 V221 Q51 238 76 238 V243 H0 V238 Q25 238 25 221 V22 Q25 5 0 5 Z'])}

VERTICE={
'A':(192,[
'M0 240 L91 0 H108 L198 240 H166 L94 45 L20 240 Z',
'M44 159 L146 134 L150 145 L40 171 Z']),
'U':(191,['M11 0 H40 V166 C40 209 62 234 101 234 C142 234 164 210 164 166 V0 H175 V170 C175 219 147 248 99 248 C48 248 11 220 11 170 Z']),
'R':(202,[
'M12 0 H94 C149 0 181 19 181 61 C181 101 154 121 108 126 L197 240 H160 L77 123 H40 V240 H12 Z M40 9 V114 H95 C130 114 150 96 150 61 C150 27 130 9 94 9 Z']),
'E':(160,['M12 0 H165 V10 H41 V104 H141 V114 H41 V230 H171 V240 H12 Z']),
'V':(196,['M0 0 H33 L112 199 L184 0 H198 L109 242 H94 Z']),
'I':(62,['M18 0 H48 V240 H18 Z'])}

MODELS=[
 {'id':'01','key':'presenca','name':'Presença','glyphs':PRESENCA,'spacing':22,'scaleX':1,
  'tag':'CLÁSSICA COM PERSONALIDADE',
  'desc':['Serifas precisas e contraste de traços.','O corte ascendente no A dá assinatura.'],
  'av':[
   'M14 244 L94 15 H104 L24 244 H0 V239 Q10 238 14 227 Z',
   'M94 15 H119 L205 244 H173 L99 49 Z',
   'M45 160 L168 146 L172 155 L41 170 Z',
   'M135 15 H167 L247 216 L316 15 H327 L245 249 H232 Z',
   'M131 15 H184 V21 H131 Z M299 15 H341 V21 H299 Z']},
 {'id':'02','key':'enlace','name':'Enlace','glyphs':ENLACE,'spacing':20,'scaleX':.96,
  'tag':'FEMININA E EXPRESSIVA',
  'desc':['Curvas com movimento e terminais suaves.','Um gesto mais envolvente no AV e no nome.'],
  'av':[
   'M23 211 C8 242 20 261 45 258 C61 257 74 246 80 230 L79 250 C65 267 47 273 30 268 C3 261 -3 237 11 207 L103 9 Q108 -1 113 9 L209 240 H178 L106 62 Z',
   'M49 158 C80 145 113 142 145 150 L151 163 C116 152 81 155 43 171 Z',
   'M138 12 H168 L240 204 C274 152 299 109 301 72 C302 38 278 19 254 31 C246 35 241 44 239 55 L231 51 C234 28 250 16 269 17 C298 19 316 41 311 76 C306 124 276 183 239 246 H229 Z']},
 {'id':'03','key':'vertice','name':'Vértice','glyphs':VERTICE,'spacing':28,'scaleX':.92,
  'tag':'ESCULTURAL E OUSADA',
  'desc':['Desenho limpo com cortes diagonais.','O AV vira uma assinatura arquitetônica.'],
  'av':[
   'M3 231 L92 11 H116 L199 231 H167 L98 49 L22 231 Z',
   'M42 158 L149 132 L155 144 L36 173 Z',
   'M146 34 H180 L248 204 L312 34 H327 L247 255 H228 Z']}
]

def wordmark(m,color):
    x=0;parts=[]
    for letter in 'AUREVI':
        advance,paths=m['glyphs'][letter]
        for d in paths:parts.append(f'<path d="{d}" fill="{color}" fill-rule="evenodd" transform="translate({x} 0)"/>')
        x+=advance+m['spacing']
    # Fixed generous viewBox includes swashes and serif overshoots.
    return ''.join(parts),x-m['spacing']+38

def mark(a,m,x,y,w,color,metal=False):
    nodes,raw=wordmark(m,color);scale=w/raw
    a.parts.append(f'<g aria-label="AUREVI" transform="translate({x+17*scale} {y+12*scale}) scale({scale})"'+(' filter="url(#bevel)"' if metal else '')+'>'+nodes+'</g>')

def symbol(a,m,x,y,w,color,metal=False):
    # Common viewBox encompasses deliberately different monograms.
    s=w/360;a.parts.append(f'<g aria-label="AV" transform="translate({x+10*s} {y}) scale({s})"'+(' filter="url(#bevel)"' if metal else '')+'>'+''.join(f'<path d="{d}" fill="{color}" fill-rule="evenodd"/>' for d in m['av'])+'</g>')

def lockup(a,m,x,y,w,color,metal=False):
    symbol(a,m,x+w*.32,y,w*.36,color,metal);mark(a,m,x,y+w*.40,w,color,metal)

def generate():
    OUT.mkdir(exist_ok=True)
    # Art.save from the preceding kit uses its own destination, so save locally.
    def save(a,relative):
        p=OUT/relative;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(a.svg(),encoding='utf8')
    for m in MODELS:
        for finish,col in [('metalico','url(#metal)'),('sangue',R),('marfim',I)]:
            metal=finish=='metalico'
            a=Art(2000,1250,'Aurevi — '+m['name']+' / '+finish);lockup(a,m,140,130,1720,col,metal);save(a,f'{m["id"]}-{m["key"]}/logo-{finish}.svg')
            a=Art(900,850,'AV — '+m['name']+' / '+finish);symbol(a,m,80,100,740,col,metal);save(a,f'{m["id"]}-{m["key"]}/AV-{finish}.svg')
            a=Art(2000,600,'AUREVI — '+m['name']+' / '+finish);mark(a,m,100,85,1800,col,metal);save(a,f'{m["id"]}-{m["key"]}/escrita-{finish}.svg')
        a=Art(1600,1100,'Aurevi — estudo '+m['id']+' / '+m['name'],I)
        a.text('AUREVI / ESTUDO '+m['id'],70,65,18,R,spacing=3)
        a.rect(50,112,1000,690,R);lockup(a,m,125,180,850,'url(#metal)',True)
        a.rect(1080,112,470,690,C);symbol(a,m,1150,260,330,'url(#metal)',True)
        a.text(m['name'],70,915,75,R,'CormorantGaramond',500)
        a.text(m['tag'],590,875,19,R,spacing=1)
        for j,line in enumerate(m['desc']):a.text(line,590,933+j*40,25,K)
        a.text('Letras e monograma desenhados em vetor para este estudo.',70,1040,18,R)
        save(a,f'{m["id"]}-{m["key"]}/Apresentacao.svg')
    # Large common board makes shape comparison possible without material bias.
    a=Art(2400,1650,'Aurevi — três estudos autorais',I)
    a.text('AUREVI / ESTUDOS DE LOGOTIPO',70,82,22,R,spacing=3)
    a.text('Três caminhos. A mesma presença.',65,198,102,R,'CormorantGaramond',500)
    for j,m in enumerate(MODELS):
        x=65+j*770
        a.rect(x,270,730,780,R)
        lockup(a,m,x+55,390,620,'url(#metal)',True)
        a.text(m['id']+' / '+m['name'],x+15,1130,52,R,'CormorantGaramond',500)
        a.text(m['tag'],x+15,1190,17,R,spacing=1)
        for k,line in enumerate(m['desc']):a.text(line,x+15,1240+k*35,22,K)
        mark(a,m,x+15,1350,680,R)
    a.text('DOURADO METÁLICO + VERMELHO SANGUE / COMPARAÇÃO EM UMA COR ABAIXO',65,1590,20,R,spacing=1)
    save(a,'Comparativo.svg')
    notes='''# Aurevi — três estudos de logotipo

Pedido: algo próximo da linguagem elegante e ousada aprovada, com desenho próprio. Os três estudos mantêm o vermelho profundo e o dourado metálico. As seis letras de cada escrita e os três AVs foram construídos em caminhos vetoriais neste estudo, sem usar glifos de uma fonte como logotipo.

01 — Presença: serifa de contraste alto, AV de diagonais separadas e um corte ascendente no A. É o caminho de maior continuidade com a energia aprovada, com uma nova estrutura nas letras.

02 — Enlace: curvas e terminais mais suaves; A com retorno curvo, R com perna em movimento e AV mais envolvente. A opção mais expressiva e feminina.

03 — Vértice: contraste e cortes diagonais em uma construção sem serifa tradicional. AV escultural com deslocamento entre as iniciais. A opção mais contemporânea e ousada.

Minha recomendação inicial: 01 Presença, pelo equilíbrio entre elegância, leitura e personalidade. O 02 é o caminho para acentuar movimento; o 03 para tornar a marca mais gráfica.

Cada pasta tem composição principal, AV e escrita em SVG e PNG, nos acabamentos metálico, vermelho e marfim. PNGs de marca têm fundo transparente. Os vetores preservam o desenho em qualquer tamanho. O metal é uma simulação digital; a versão em uma cor permite avaliar o desenho e orientar a reprodução física.

As três opções são estudos para comparação; o kit anterior fica preservado. A aplicação geral pode seguir o modelo escolhido após o seu retorno. Não misturar as escritas e símbolos de opções diferentes.
'''
    (OUT/'LEIA-ME.md').write_text(notes,encoding='utf8')
    (OUT/'modelos.json').write_text(json.dumps([{k:v for k,v in m.items() if k not in ['glyphs','av']} for m in MODELS],ensure_ascii=False,indent=2),encoding='utf8')
    print('3 modelos autorais / 27 logos SVG / 3 apresentações / 1 comparativo.')

if __name__=='__main__':generate()
