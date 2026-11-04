"""Kit Aurevi: elegante e ousada. Arte vetorial e composição, sem editar fotos."""
from pathlib import Path
from html import escape
import sys, json, shutil, base64
from revisao02_estudos import logo, textpaths
from direcao_bordo import monogram

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'IDENTIDADE-ELEGANTE-OUSADA'
R='#450A10'; G='#CFB77F'; I='#FAF6EF'; C='#9B9995'; K='#242424'
ITEMS=[]
METAL='''<linearGradient id="metal" x1="0" y1="0" x2=".8" y2="1" gradientUnits="objectBoundingBox"><stop offset="0" stop-color="#6B5028"/><stop offset=".15" stop-color="#C9AC6C"/><stop offset=".29" stop-color="#FFF4C8"/><stop offset=".41" stop-color="#D7BF85"/><stop offset=".49" stop-color="#8A6B38"/><stop offset=".52" stop-color="#FFF9DE"/><stop offset=".65" stop-color="#E9D6A0"/><stop offset=".82" stop-color="#A7894C"/><stop offset="1" stop-color="#F4E7BF"/></linearGradient><filter id="bevel" x="-10%" y="-10%" width="120%" height="125%"><feGaussianBlur in="SourceAlpha" stdDeviation="1.2" result="blur"/><feSpecularLighting in="blur" surfaceScale="3" specularConstant=".85" specularExponent="22" lighting-color="#FFF9E8" result="light"><feDistantLight azimuth="235" elevation="48"/></feSpecularLighting><feComposite in="light" in2="SourceAlpha" operator="in" result="lit"/><feBlend in="SourceGraphic" in2="lit" mode="screen"/></filter>'''

def word(x,y,w,color):
    n,h=logo(1,color,w)
    return f'<g transform="translate({x} {y})">{n}</g>',h

class Art:
    def __init__(self,w,h,title,bg=None,physical=None):
        self.w=w;self.h=h;self.title=title;self.parts=[];self.bounds=[];self.physical=physical
        if bg:self.rect(0,0,w,h,bg)
    def rect(self,x,y,w,h,fill,rx=0):self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" rx="{rx}"/>')
    def line(self,x,y,x2,y2,color=G,sw=1):self.parts.append(f'<path d="M{x} {y} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{sw}"/>')
    def text(self,value,x,y,size=28,color=I,family='Manrope',weight=400,anchor='start',spacing=0):
        d,b,_,advance=textpaths(value,family,weight,size,spacing)
        dx=x-advance/2 if anchor=='middle' else x-advance if anchor=='end' else x
        node=f'<g aria-label="{escape(value,quote=True)}" transform="translate({dx} {y})"><path d="{d}" fill="{color}"/></g>'
        edit=f'<text x="{x}" y="{y}" font-family="{family}" font-weight="{weight}" font-size="{size}" letter-spacing="{spacing}" text-anchor="{anchor}" fill="{color}">{escape(value)}</text>'
        self.parts.append((node,edit))
        if b:self.bounds.append({'text':value,'x0':round(dx+b[0],2),'y0':round(y+b[1],2),'x1':round(dx+b[2],2),'y1':round(y+b[3],2)})
    def lines(self,values,x,y,size=70,color=I,family='Manrope',weight=400,leading=None,**kw):
        for j,s in enumerate(values):self.text(s,x,y+j*(leading or size*1.06),size,color,family,weight,**kw)
    def mark(self,x,y,w,color=G):
        n,h=word(x,y,w,color);self.parts.append(n);return h
    def av(self,x,y,w,color=G):self.parts.append(f'<g transform="translate({x} {y}) scale({w/270})">{monogram(color)}</g>')
    def lockup(self,x,y,w,color=G):
        self.av(x+w*.34,y,w*.32,color);self.mark(x,y+w*.38,w,color)
    def photo(self,path,x,y,w,h,fit='xMidYMid slice'):
        p=Path(path);data=base64.b64encode(p.read_bytes()).decode()
        self.parts.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" overflow="hidden"><image href="data:image/png;base64,{data}" width="{w}" height="{h}" preserveAspectRatio="{fit}"/></svg>')
    def svg(self,editable=False):
        fonts=''
        if editable:
            for fam in ['CormorantGaramond','Manrope']:
                b=base64.b64encode((OUT/'06-fontes'/f'{fam}.ttf').read_bytes()).decode()
                fonts+=f'@font-face{{font-family:{fam};font-weight:100 900;src:url(data:font/ttf;base64,{b})}}'
        attr=f'width="{self.w}" height="{self.h}"' if not self.physical else f'width="{self.physical[0]}mm" height="{self.physical[1]}mm"'
        body=''.join(a[1 if editable else 0] if isinstance(a,tuple) else a for a in self.parts)
        return f'<svg xmlns="http://www.w3.org/2000/svg" {attr} viewBox="0 0 {self.w} {self.h}" role="img"><title>{escape(self.title)}</title><defs>{METAL}<style>{fonts}</style></defs>{body}</svg>'
    def save(self,relative,edit=False,status='Arte de marca',note=''):
        p=OUT/relative;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(self.svg(),encoding='utf-8')
        if edit:
            q=p.parent/'editaveis'/p.name;q.parent.mkdir(exist_ok=True);q.write_text(self.svg(True),encoding='utf-8')
        ITEMS.append({'file':relative,'width':self.w,'height':self.h,'physical_mm':self.physical,'title':self.title,'status':status,'note':note,'text_bounds':self.bounds})

def footer(a,label,color=I,y=None):
    y=y or a.h-70;a.line(72,y-42,a.w-72,y-42,color,.8)
    a.text('@use_aurevi',72,y,21,color);a.text(label,a.w-72,y,19,color,anchor='end',spacing=1)

def top(a,label,color=G):a.text(label,72,112,19,color,weight=500,spacing=3)

def brand():
    colors=[('sangue',R),('ouro',G),('marfim',I),('grafite',K),('metalico','url(#metal)')]
    for name,col in colors:
        for kind in ['AV','AUREVI','principal','horizontal']:
            w,h={'AV':(840,760),'AUREVI':(1600,440),'principal':(1600,1000),'horizontal':(1800,420)}[kind]
            a=Art(w,h,'Aurevi — '+kind+' '+name)
            if kind=='AV':a.av(72,68,695,col)
            elif kind=='AUREVI':a.mark(90,92,1420,col)
            elif kind=='principal':a.lockup(150,85,1300,col)
            else:a.av(60,60,320,col);a.mark(480,112,1220,col)
            if name=='metalico':a.parts=['<g filter="url(#bevel)">'+p+'</g>' for p in a.parts]
            a.save(f'01-marca/{kind}-{name}.svg')
    for name,bg,col in [('vermelho',R,G),('cinza',C,R)]:
        a=Art(1080,1080,'Avatar Aurevi '+name,bg);a.av(220,220,640,'url(#metal)' if name=='vermelho' else col);a.save(f'02-redes/avatares/avatar-{name}.svg')

def social():
    photo=OUT/'04-fotografia/estudio-aurevi.png'
    def save(a,name,status='Arte de marca',note='',kind='feed'):a.save(f'02-redes/{kind}/{name}.svg',True,status,note)
    # Nine coherent tiles, with a deliberate balance of graphic and photograph.
    a=Art(1080,1350,'01 — Elegante e ousada',R);top(a,'AUREVI / MODA FEMININA');a.av(777,177,200,G)
    a.lines(['Elegante.','Ousada.','Aurevi.'],68,470,154,color=I,family='CormorantGaramond',weight=500,leading=163)
    a.line(76,964,320,964,G,3);a.text('Vista sua presença.',76,1050,36,G);footer(a,'A MARCA');save(a,'01-elegante-ousada')
    a=Art(1080,1350,'02 — Editorial de estúdio',K);a.photo(photo,0,0,1080,1238,'xMidYMin slice');a.rect(0,1238,1080,112,R)
    a.text('PRESENÇA EM CADA DETALHE.',60,1300,23,I,spacing=2);a.text('EDITORIAL CONCEITUAL · IA',1020,1329,16,G,anchor='end');save(a,'02-editorial','Editorial conceitual','Imagem gerada por IA, não anuncia peça real de estoque.')
    a=Art(1080,1350,'03 — Ouro e vida',I);top(a,'AURE + VI',R);a.lockup(130,215,820,R)
    a.text('Ouro no nome.',72,915,83,R,'CormorantGaramond',500);a.text('Vida no seu jeito.',72,1007,83,R,'CormorantGaramond',500)
    a.text('Elegância para vestir com atitude.',76,1138,30,K);footer(a,'NOSSA ESSÊNCIA',R);save(a,'03-ouro-vida')
    a=Art(1080,1350,'04 — Detalhes com presença',C);top(a,'UM OLHAR MAIS DE PERTO',R)
    a.text('O detalhe muda tudo.',70,263,93,R,'CormorantGaramond',500);a.photo(photo,72,330,936,700,'xMidYMid slice')
    a.rect(72,1060,936,150,R);a.text('Recortes, drapeados e movimento.',104,1124,29,I);a.text('Inspiração de styling · editorial conceitual IA',104,1173,20,G);footer(a,'DETALHES',R);save(a,'04-detalhes','Editorial conceitual','Recorte da fotografia de conceito; substituir pela foto real ao anunciar produto.')
    a=Art(1080,1350,'05 — Peça do dia — modelo editável',R);a.mark(72,60,340,G);a.rect(72,275,936,680,C)
    a.av(410,395,260,R);a.text('SUA FOTO DA PEÇA',540,785,26,R,anchor='middle',spacing=2)
    a.text('[Nome da peça]',72,1065,78,I,'CormorantGaramond',500);a.text('[Tamanhos e cores disponíveis]',76,1131,28,I)
    a.text('Consulte disponibilidade pelo direct.',76,1198,27,G);footer(a,'SEU PRÓXIMO LOOK');save(a,'05-peca-template','Template — preencher','Inserir foto, nome e disponibilidade reais antes de publicar.')
    a=Art(1080,1350,'06 — Vista sua presença',R);top(a,'ELEGÂNCIA COM ATITUDE');a.av(765,170,220,G)
    a.lines(['Tem looks','que chegam','com você.'],72,489,125,I,'CormorantGaramond',500,leading=137)
    a.line(76,944,320,944,G,3);a.text('Vista sua presença.',76,1040,40,G);a.mark(72,1110,400,I);footer(a,'AUREVI');save(a,'06-presenca')
    a=Art(1080,1350,'07 — Provador — modelo editável',I);top(a,'A PEÇA EM MOVIMENTO',R);a.text('No seu ritmo.',72,274,111,R,'CormorantGaramond',500)
    a.rect(72,340,936,640,C);a.av(426,448,230,R);a.text('FOTO OU CAPA DO SEU VÍDEO',540,831,24,R,anchor='middle')
    a.lines(['Mostre o caimento.','Conte os detalhes da peça.'],76,1068,31,K,leading=49);footer(a,'PROVADOR',R);save(a,'07-provador-template','Template — preencher','Substituir pelo provador real e revisar informações da peça.')
    a=Art(1080,1350,'08 — Inspiração de cores',C);top(a,'COMBINAÇÕES COM PERSONALIDADE',R)
    a.lines(['Vermelho profundo.','Ouro na medida.'],72,341,93,R,'CormorantGaramond',500,leading=108)
    for x,col in [(72,R),(390,G),(708,I)]:a.rect(x,670,300,300,col)
    for x,s in [(72,'PRESENÇA'),(390,'BRILHO'),(708,'EQUILÍBRIO')]:a.text(s,x,1019,20,R,spacing=2)
    a.text('Salve a inspiração para o próximo look.',72,1150,30,K);footer(a,'INSPIRAÇÃO',R);save(a,'08-combinacoes')
    a=Art(1080,1350,'09 — Convite à marca',R);a.lockup(150,150,780,'url(#metal)')
    a.lines(['Seu estilo.','Sua presença.'],72,866,103,I,'CormorantGaramond',500,leading=115)
    a.text('Conheça a Aurevi.',76,1120,34,G);footer(a,'@USE_AUREVI');save(a,'09-conheca')
    # Stories keep title and CTA within comfortable top/bottom UI margins.
    a=Art(1080,1920,'01 — Story manifesto',R);a.mark(100,240,880,G);a.av(390,570,300,G)
    a.lines(['Elegante.','Ousada.','Do seu jeito.'],90,1090,126,I,'CormorantGaramond',500,leading=137)
    a.line(96,1510,984,1510,G);a.text('VISTA SUA PRESENÇA.',96,1590,28,G,spacing=3);save(a,'01-manifesto',kind='stories')
    a=Art(1080,1920,'02 — Story editorial',R);a.photo(photo,0,200,1080,1390,'xMidYMid meet');a.rect(0,0,1080,210,R);a.mark(180,42,720,G)
    a.rect(0,1590,1080,330,R);a.text('Presença que veste.',80,1692,77,I,'CormorantGaramond',500);a.text('EDITORIAL CONCEITUAL · IA',80,1755,20,G);save(a,'02-editorial','Editorial conceitual','Não anuncia peça real de estoque.',kind='stories')
    a=Art(1080,1920,'03 — Story peça — modelo editável',I);top(a,'AUREVI / PROVADOR',R);a.text('O look da vez.',80,310,104,R,'CormorantGaramond',500)
    a.rect(80,390,920,950,C);a.av(395,650,280,R);a.text('SUA FOTO REAL AQUI',540,1090,25,R,anchor='middle')
    a.text('[Nome da peça]',80,1455,76,R,'CormorantGaramond',500);a.text('[Tamanhos / cores]',80,1520,29,K);a.rect(80,1590,920,120,R);a.text('FALE COM A GENTE NO DIRECT',540,1660,25,I,anchor='middle',spacing=1);save(a,'03-peca-template','Template — preencher',kind='stories')
    a=Art(1080,1920,'04 — Story interação',R);a.av(390,260,300,G);a.lines(['Qual detalhe','faz seu look?'],80,850,114,I,'CormorantGaramond',500,leading=126)
    a.text('RECORTE   /   DRAPEADO   /   ACESSÓRIO',80,1120,23,G);a.rect(80,1250,920,250,I,8);a.text('Adicione uma enquete do Instagram',540,1390,25,R,anchor='middle');a.text('A SUA PRESENÇA COMEÇA NA ESCOLHA.',80,1660,23,G,spacing=1);save(a,'04-enquete-template','Template — adicionar enquete',kind='stories')
    for n,name in enumerate(['Novidades','Looks','Provador','Detalhes','Aurevi','Atendimento'],1):
        a=Art(1080,1080,'Destaque '+name,R);a.av(340,240,400,G);a.text(name.upper(),540,745,28,I,anchor='middle',spacing=4);a.save(f'02-redes/destaques/{n:02}-{name.lower()}.svg')

def packaging():
    # One SVG unit is 0.1 mm. Tag/card include 3 mm bleed and 5 mm internal safety.
    a=Art(660,1060,'Tag frente — 60 × 100 mm + sangria',R,(66,106));a.lockup(85,190,490,G);a.text('@use_aurevi',330,911,22,I,anchor='middle');a.save('03-embalagens/tag-frente.svg',note='Corte 60×100 mm, sangria 3 mm; furo pelo fornecedor.')
    a=Art(660,1060,'Tag verso — 60 × 100 mm + sangria',I,(66,106));a.mark(90,160,480,R)
    a.lines(['Elegância','com atitude.'],80,475,83,R,'CormorantGaramond',500,leading=91);a.line(80,660,580,660,R)
    a.text('Conheça nossos looks.',80,745,25,K);a.text('@use_aurevi',80,805,28,R);a.text('Vista sua presença.',80,920,28,R);a.save('03-embalagens/tag-verso.svg',True,note='Tag de marca; não substitui etiqueta de composição.')
    a=Art(960,660,'Cartão de agradecimento — 90 × 60 mm + sangria',R,(96,66));a.av(690,85,175,G)
    a.lines(['Seu estilo merece','esse momento.'],85,300,72,I,'CormorantGaramond',500,leading=80);a.text('Obrigada por escolher a Aurevi.',85,496,25,I);a.text('@use_aurevi',85,565,23,G);a.save('03-embalagens/cartao-agradecimento.svg',True,note='Corte 90×60 mm; sangria 3 mm.')
    a=Art(960,660,'Cartão da marca — 90 × 60 mm + sangria',I,(96,66));a.lockup(220,80,520,R);a.text('@use_aurevi',480,530,27,R,anchor='middle');a.save('03-embalagens/cartao-marca.svg',note='Corte 90×60 mm; sangria 3 mm.')
    a=Art(560,560,'Adesivo redondo — diâmetro 50 mm + sangria',R,(56,56));a.av(125,90,310,G);a.text('AUREVI',280,440,36,I,'CormorantGaramond',500,anchor='middle',spacing=5);a.save('03-embalagens/adesivo-redondo.svg',note='Faca circular 50 mm, centralizada; sangria 3 mm. Arte de fundo quadrada.')
    a=Art(1800,2000,'Frente de sacola — área gráfica 180 × 200 mm',R,(180,200));a.lockup(280,485,1240,G);a.text('@use_aurevi',900,1760,43,I,anchor='middle');a.save('03-embalagens/sacola-frente.svg',note='Área gráfica frontal, não é faca industrial; dimensões finais dependem da sacola.')
    a=Art(2200,1600,'Tampa de caixa — área gráfica 220 × 160 mm',R,(220,160));a.lockup(480,230,1240,G);a.save('03-embalagens/caixa-tampa.svg',note='Área gráfica da tampa, não é faca industrial.')
    a=Art(1000,1000,'Padrão AV — módulo 100 × 100 mm',I,(100,100))
    for j in range(4):
        for k in range(4):a.av(25+k*250+(125 if j%2 else 0),15+j*250,90,R)
    a.save('03-embalagens/padrao-AV.svg',note='Módulo de repetição para papel de seda e interiores; sangramento decorativo nas bordas é intencional.')
    # Separate monochrome foil masks make the chosen finishing actionable.
    for kind,w,h,x,y,mw in [('tag',660,1060,85,190,490),('sacola',1800,2000,280,485,1240),('caixa',2200,1600,480,230,1240)]:
        a=Art(w,h,'Máscara de hot stamping — '+kind,physical=(w/10,h/10));a.lockup(x,y,mw,'#000000');a.save(f'03-embalagens/mascaras-hot-stamping/{kind}.svg',note='Preto indica acabamento metálico; alinhar à arte correspondente. Não imprimir preto no lugar do metal.')

def write_guides():
    guide='''# Aurevi — elegante e ousada

Elegância com atitude. A direção nasce da fotografia de estúdio aprovada: vestido vermelho profundo, parede cinza e marca em dourado polido. Aure significa ouro; Vi, vida. A marca veste estilo e bom gosto, sem presumir posicionamento de luxo.

## Sistema visual

AV curvo separado + AUREVI em caixa alta com gesto no R. A logo mestre permanece em curvas, independente de fontes instaladas. Cormorant Garamond 500/600 para títulos; Manrope 400/500/600 para textos e informações. Cormorant no texto é apoio: não redigitar a logo para reconstruí-la.

Vermelho sangue #450A10; ouro champagne #CFB77F; cinza mineral #9B9995; marfim #FAF6EF; grafite #242424. Vermelho como presença, cinza como espaço, marfim como leitura e ouro como detalhe. O cinza não muda a cor do vestido. Relevo, reflexos e metal aparecem em aplicações e na variante metálica, sem alterar o desenho da marca.

A pasta 01-marca contém AV, escrita, composição principal e horizontal em cinco acabamentos. As versões metálicas SVG/PNG simulam o reflexo para uso digital; a produção física pede material metálico real, por exemplo hot stamping champagne ou letras-caixa de metal com frente polida. O código HEX não especifica um metal. Escolher a amostra do fornecedor à luz do ambiente. Máscaras de acabamento em 03-embalagens/mascaras-hot-stamping.

## Uso da logo

Preservar respiro mínimo de 1/4 da largura do AV ao redor do símbolo. Para o conjunto, respiro de uma altura de letra A nas laterais. Largura sugerida mínima: conjunto 180 px ou 35 mm; escrita 140 px ou 28 mm; AV 40 px ou 10 mm. Abaixo disso, conferir reprodução; usar a marca em uma cor. Não esticar, inclinar, acrescentar brilhos, contornos ou sombras às versões planas. O ouro metálico precisa de fundo limpo; para fotos carregadas, usar uma faixa sólida vermelha ou a marca em marfim.

## Fotografia

Estúdio com luz ampla e suave, pele natural e tecido bem exposto. Parede cinza mineral, balcão discreto atrás da modelo, metal dourado com reflexos claros e desfoque leve no letreiro. Mostrar a roupa inteira e variar entre corpo inteiro, caimento e detalhe; enquadramentos intencionais sem cortar pés nas fotos de corpo inteiro. Poses confiantes, gestos naturais e uma peça por imagem de catálogo. Nas fotos reais, preservar a cor e os detalhes do produto. Vídeo curto: frontal, lateral, costas e detalhe em movimento. Sem filtros que clareiem o vermelho ou o levem ao magenta.

As imagens de 04-fotografia e o novo mockup 05-mockups/embalagens-vermelho-ouro.png são conceituais, geradas por IA. Não representam estoque ou uma loja já executada. Ao anunciar produtos, substituir pelos registros reais. Posts editoriais estão identificados como conceito. Dois mockups Kittl anteriores foram reunidos, com links de edição e origem preservados; são complementos, não novas renderizações.

## Conteúdo e voz

Frases curtas, seguras e próximas. Mostrar a roupa e explicar o detalhe que ajuda a escolher. Frase de campanha proposta: “Vista sua presença.” Usar “Elegante. Ousada. Aurevi.” como manifestação visual. Evitar superlativos, promessas de exclusividade e informações não conferidas.

Bio sugerida: “Moda feminina com elegância e atitude. / Looks com presença, do seu jeito. / Fale com a gente no direct ↓”. Adaptar última linha ao canal real.

### Sequência inicial de nove posts

1. 01-elegante-ousada — apresentação: “Elegância no traço. Atitude no jeito de vestir. Conheça a Aurevi.” CTA: acompanhe @use_aurevi.
2. 02-editorial — “Recortes, movimento e uma presença que chama o olhar.” Identificar como editorial conceitual. Ao virar anúncio, usar a peça real.
3. 03-ouro-vida — “Aure, de ouro. Vi, de vida. Um nome que encontra o brilho no seu jeito de ser.” CTA: conheça a marca.
4. 04-detalhes — “O detalhe muda a leitura do look. Qual é o seu favorito?” Editorial conceitual até substituir por foto real.
5. 05-peca-template — foto + nome + tamanhos/cores conferidos. Legenda: “[Nome]: [detalhe real de caimento]. Consulte disponibilidade pelo direct.” Preencher antes de publicar.
6. 06-presenca — “Tem looks que chegam com você. Vista sua presença.” CTA: salve a inspiração.
7. 07-provador-template — gravar peça frontal/lateral/costas; mostrar acabamento. Legenda: “Veja [nome] em movimento. Tire suas dúvidas no direct.” Preencher antes de publicar.
8. 08-combinacoes — “Vermelho profundo e dourado na medida: uma inspiração para combinar com atitude.” CTA: salve para testar.
9. 09-conheca — “Seu estilo. Sua presença. Bem-vinda à Aurevi.” CTA: conheça os looks pelo canal real da loja.

A numeração indica ordem de leitura da sequência, não montagem obrigatória de mosaico. Se desejar a grade 3×3 da apresentação como grade do perfil, publicar do 09 ao 01. As artes funcionam individualmente. Não dependem de emendas.

### Stories e destaques

Quatro stories: manifesto, editorial, peça real editável, enquete editável. Aplicar sticker nativo na área indicada e remover o texto de instrução. Manter informações importantes entre 250 e 1700 px em uma tela 1080×1920; conferir a interface no aparelho. Destaques: Novidades, Looks, Provador, Detalhes, Aurevi e Atendimento. O AV central aparece no recorte circular; o nome também pode ser colocado no título do destaque.

### Ritmo sugerido de duas semanas

Semana 1: apresentação (segunda), editorial (quarta), essência (sexta), detalhe (domingo). Stories de bastidores e enquete entre as publicações. Semana 2: peça real (segunda), presença (quarta), provador (sexta), combinação (sábado), convite (domingo). Ajustar à capacidade de produzir conteúdo real. Não prometer lançamento, desconto ou reposição sem confirmação.

## Experiência de loja

1. Recepção: parede cinza mineral e letreiro AV/AUREVI em metal champagne polido, com relevo e iluminação lateral suave. Balcão com frente cinza e detalhe dourado estreito. Ajustar dimensões ao espaço, sem supor uma obra já definida.
2. Provador: luz frontal difusa, espelho de corpo inteiro e fundo limpo. Evitar spots isolados no topo que alterem a percepção do caimento. Um apoio para bolsa e acessórios ajuda a experiência.
3. Exposição: looks completos com poucos acessórios. Agrupar por combinação e ocasião; uma faixa de vermelho da marca pode destacar a área principal sem pintar todo o espaço.
4. Embalagem: sacola estruturada vermelho profundo, marca pequena em hot stamping champagne e alça de fita tonal. Seda marfim com AV vermelho discreto; tag e cartão com a mesma hierarquia.
5. Atendimento: perguntar sobre ocasião, preferência de caimento e tamanho; mostrar detalhes reais e alternativas. Falar com segurança e proximidade.
6. Conteúdo no espaço: reservar um ponto fixo para fotos de produto, mantendo luz, enquadramento e balanço de branco consistentes com a campanha.

## Produção e edição

PNG: pronto para apresentação e publicação conforme o status da peça. SVG em curvas: escala sem depender de fonte. SVG em editaveis: textos comuns editáveis, logo preservada em curvas; fontes OFL incluídas. Não são projetos nativos de Canva/Adobe/Kittl. Imagens estão incorporadas nas artes SVG, que abrem offline.

Tag: corte 60×100 mm + 3 mm de sangria. Cartões: corte 90×60 mm + 3 mm. Adesivo: círculo 50 mm, com arte 56×56 mm incluindo sangria. Frente de sacola 180×200 mm e tampa de caixa 220×160 mm são áreas gráficas; solicitar faca e especificações ao fornecedor. PDF acompanha a dimensão externa da arte; não inclui marcas de corte. Refilo é centralizado nas dimensões de corte descritas. A tag é de marca e não substitui a etiqueta têxtil de composição e conservação.

Provar cor e metal no material real. Arquivos digitais são RGB; não afirmar equivalência Pantone/CMYK. Não criar QR code sem destino confirmado. O perfil usado é o informado: @use_aurevi. Nenhuma publicação ou mensagem foi enviada.
'''
    (OUT/'07-guias/Guia-de-uso-conteudo-e-loja.md').write_text(guide,encoding='utf-8')
    (OUT/'LEIA-ME.md').write_text('''# Aurevi — elegante e ousada

Comece pelo Manual-Aurevi-Elegante-Ousada.pdf ou abra APRESENTACAO.html no navegador. Visao-geral.png reúne a direção em uma imagem.

- 01-marca: vinte logos SVG + PNG, incluindo dourado metálico com fundo transparente.
- 02-redes: nove posts, quatro stories, seis destaques e dois avatares. PNGs, SVGs em curvas e textos editáveis onde aplicável.
- 03-embalagens: oito aplicações, três máscaras de hot stamping, SVGs, PNGs e PDFs físicos.
- 04-fotografia: imagem de estúdio aprovada e prompt.
- 05-mockups: novo conjunto vermelho/ouro e dois mockups Kittl anteriores, com links.
- 06-fontes: Cormorant Garamond e Manrope + licenças OFL.
- 07-guias: conteúdo, fotografia, aplicações e ideias para a loja.

Peças com [colchetes] são modelos a preencher. Fotos de IA são conceitos, não estoque. Os arquivos de embalagem indicam dimensões e sangria; frente de sacola e tampa de caixa são áreas gráficas, não facas industriais. Dourado metálico digital é simulação; acabamento físico depende de material/prova do fornecedor.
''',encoding='utf-8')

def img(src,cls='',style=''):return f'<img src="{src}" class="{cls}" style="{style}" alt="{escape(Path(src).stem)}">'
def page(n,kicker,title,content,cls=''):
    return f'<section class="sheet"><article class="page {cls}"><header><span>AUREVI</span><span>{kicker}</span></header><h1>{title}</h1>{content}<footer><span>ELEGANTE E OUSADA</span><span>{n:02} / 18</span></footer></article></section>'
def cards(items):return '<div class="cards">'+''.join(f'<div><h3>{h}</h3><p>{p}</p></div>' for h,p in items)+'</div>'

def manual():
    pages=[]
    pages.append(f'''<section class="sheet"><article class="page cover"><div class="cover-copy"><div class="eyebrow">IDENTIDADE VISUAL · AUREVI</div>{img('01-marca/principal-metalico.svg','cover-logo')}<h1>Elegante.<br>Ousada.<br><em>Aurevi.</em></h1><p>Ouro no nome. Vida na presença.</p><small>DIREÇÃO VISUAL / NOVEMBRO 2026</small></div><div class="cover-photo">{img('04-fotografia/estudio-aurevi.png')}<span>EDITORIAL CONCEITUAL · IA</span></div></article></section>''')
    pages.append(page(2,'ESSÊNCIA','Elegância com atitude.',f'''<div class="two"><div><p class="lead">A roupa tem presença.<br>A marca acompanha.</p><p>O vermelho profundo traz intensidade. As letras esculpidas e o dourado polido dão elegância. O cinza abre espaço para a roupa aparecer.</p><p><b>Aure</b>, de ouro. <b>Vi</b>, de vida.<br>Bom gosto com personalidade, para vestir do seu jeito.</p><blockquote>Vista sua presença.</blockquote><p class="small">Frase de campanha proposta para esta direção.</p></div><div class="photo-card">{img('05-mockups/embalagens-vermelho-ouro.png')}<p class="small">Conceito de embalagem · imagem gerada por IA.</p></div></div>'''))
    pages.append(page(3,'MARCA PRINCIPAL','Uma assinatura com presença.',f'''<div class="logo-hero red">{img('01-marca/principal-metalico.svg')}</div><div class="three variants"><div class="ivory">{img('01-marca/horizontal-sangue.svg')}</div><div class="red">{img('01-marca/AUREVI-marfim.svg')}</div><div class="grey">{img('01-marca/AV-sangue.svg')}</div></div><p>AV curvo e separado. AUREVI em maiúsculas, com contraste de traços e um gesto no R. Conjunto principal, horizontal, escrita e símbolo funcionam como família.</p>'''))
    pages.append(page(4,'ACABAMENTO','O dourado que chama o olhar.',f'''<div class="two"><div class="metal-panel">{img('01-marca/principal-metalico.svg')}<span>DOURADO METÁLICO · FUNDO TRANSPARENTE</span></div><div><p class="lead">Luz clara.<br>Metal polido.<br>Volume real.</p><p>No digital, a variante metálica simula reflexos champagne e platinados. O desenho continua igual ao da marca plana.</p><p>Na loja, letras em relevo com frente polida e laterais aparentes. Na embalagem, hot stamping champagne aplicado à máscara vetorial.</p><p class="small">O HEX define a aproximação plana. O brilho vem do material, da luz e da prova física.</p><div class="metal-strip">{img('01-marca/AV-metalico.svg')}{img('01-marca/AUREVI-ouro.svg')}</div></div></div>'''))
    cols=[('Vermelho sangue',R,'PRESENÇA'),('Ouro champagne',G,'ACABAMENTO'),('Cinza mineral',C,'ESPAÇO'),('Marfim',I,'LEITURA'),('Grafite',K,'INFORMAÇÃO')]
    swatches=''.join(f'<div class="swatch" style="background:{col};color:{I if col in [R,K] else R}"><span>{role}</span><strong>{name}</strong><code>{col}</code></div>' for name,col,role in cols)
    pages.append(page(5,'PALETA','Intensidade, luz e equilíbrio.',f'''<div class="swatches">{swatches}</div><div class="three color-notes"><div><h3>Vermelho + ouro</h3><p>Assinatura, embalagem e manifestações fortes da marca.</p></div><div><h3>Cinza + vermelho</h3><p>Espaço, fotografia e composições que valorizam a peça.</p></div><div><h3>Marfim + grafite</h3><p>Informação clara, textos de apoio e dados do produto.</p></div></div><p>Usar ouro em detalhes e áreas de marca. Para textos pequenos, priorizar marfim sobre vermelho ou grafite sobre marfim. Cinza mineral é cor de apoio.</p><p class="small">Paleta digital RGB. O ouro metálico exige material ou simulação própria; não é uma tinta HEX com brilho.</p>'''))
    pages.append(page(6,'TIPOGRAFIA','Expressão no título. Clareza no detalhe.',f'''<div class="two type"><div><span class="eyebrow">CORMORANT GARAMOND / 500–600</span><div class="specimen">Vista sua<br><em>presença.</em></div><p class="alphabet">Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj<br>Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt<br>Uu Vv Ww Xx Yy Zz · 0123456789</p></div><div><span class="eyebrow">MANROPE / 400–500–600</span><h2 class="sans">Informação que<br>ajuda a escolher.</h2><p>Nome da peça, tamanhos, cores e atendimento. Texto direto e legível, com respiro.</p><div class="type-scale"><b>Título · 80–140 px</b><b>Apoio · 28–36 px</b><b>Informação · 22–28 px</b></div><p class="small">Referência para artes de 1080 px. Ajustar ao conteúdo. Logo mestre em curvas; não redigitar para reconstruí-la. Fontes e licenças OFL incluídas.</p></div></div>'''))
    pages.append(page(7,'REGRAS DE USO','O desenho merece espaço.',f'''<div class="rules"><div class="rule-logo ivory">{img('01-marca/horizontal-sangue.svg')}<span>RESPIRO AO REDOR DA MARCA</span></div>{cards([('Área de proteção','AV: ao menos ¼ de sua largura. Conjunto: uma altura de letra A nas laterais.'),('Tamanho sugerido','Conjunto ≥ 180 px / 35 mm. Escrita ≥ 140 px / 28 mm. AV ≥ 40 px / 10 mm.'),('Contraste','Ouro ou marfim sobre vermelho. Vermelho sobre marfim ou cinza. Em foto, prefira fundo limpo.'),('Integridade','Preserve proporção, desenho e cores. Não estique, incline, contorne ou acrescente efeitos à marca plana.')])}</div><p class="small">O relevo pertence às aplicações e à variante metálica. Para tamanhos menores, usar uma cor e conferir a reprodução do traço.</p>'''))
    pages.append(page(8,'FOTOGRAFIA','A roupa em primeiro plano.',f'''<div class="two photo-direction"><div class="tall-photo">{img('04-fotografia/estudio-aurevi.png')}</div><div><p class="lead">Confiante.<br>Natural.<br>Marcante.</p>{cards([('Luz','Ampla e suave. Pele natural, textura e cor da roupa preservadas.'),('Cenário','Parede cinza, balcão discreto, marca dourada em relevo e desfoque leve.'),('Enquadramento','Corpo inteiro para caimento; aproximação para recortes e acabamento.'),('Movimento','Frente, lateral, costas e detalhe. Gestos simples, sem pose forçada.')])}<p class="small">Imagem conceitual gerada por IA. Para venda de uma peça, fotografar o produto real.</p></div></div>'''))
    pages.append(page(9,'EMBALAGEM','A experiência continua nas mãos.',f'''<div class="pack-hero">{img('05-mockups/embalagens-vermelho-ouro.png')}</div><div class="three"><div><h3>Sacola estruturada</h3><p>Vermelho profundo, alça tonal e marca em ouro na medida.</p></div><div><h3>Caixa + seda</h3><p>Exterior intenso. Interior marfim e padrão AV discreto.</p></div><div><h3>Tag + cartão</h3><p>A mesma assinatura em cada ponto de contato.</p></div></div><p class="small">Mockup conceitual · IA. Artes e máscaras vetoriais de acabamento acompanham o kit.</p>'''))
    thumbs=''.join('<div>'+img('03-embalagens/'+f+'.svg')+f'<span>{label}</span></div>' for f,label in [('tag-frente','TAG / FRENTE'),('tag-verso','TAG / VERSO'),('cartao-agradecimento','CARTÃO'),('adesivo-redondo','ADESIVO')])
    pages.append(page(10,'PAPELARIA E PRODUÇÃO','Pequenos formatos. A mesma força.',f'''<div class="print-grid">{thumbs}</div><div class="three"><div><h3>Medidas e sangria</h3><p>Tag 60×100 mm. Cartão 90×60 mm. Adesivo Ø50 mm. Sangria de 3 mm nos arquivos.</p></div><div><h3>Áreas gráficas</h3><p>Sacola 180×200 mm e tampa 220×160 mm. Ajustar à faca e ao material do fornecedor.</p></div><div><h3>Acabamento metálico</h3><p>Máscaras separadas para tag, sacola e caixa. Solicitar prova de cor e amostra do ouro.</p></div></div><p class="small">PDFs em dimensão física; SVGs em curvas. A tag de marca não substitui a etiqueta têxtil. A frente de sacola não é uma faca industrial.</p>'''))
    feed=sorted((OUT/'02-redes/feed').glob('*.svg'))
    grid='<div class="feed-grid">'+''.join(img('02-redes/feed/'+p.name) for p in feed)+'</div>'
    pages.append(page(11,'INSTAGRAM / FEED','Uma presença que se reconhece.',f'''<div class="feed-layout">{grid}<div><p class="lead">Foto forte.<br>Palavra precisa.<br>Respiro.</p><p>Nove artes em 1080×1350 px. Vermelho, cinza e marfim se alternam com o editorial aprovado.</p><p>As peças funcionam sozinhas. Não dependem de emendas para formar a identidade.</p><p class="small">Dois modelos pedem fotos e informações reais. Editoriais conceituais estão identificados.</p></div></div>'''))
    stories=''.join(img('02-redes/stories/'+p.name) for p in sorted((OUT/'02-redes/stories').glob('*.svg')))
    pages.append(page(12,'INSTAGRAM / STORIES','Conversa com personalidade.',f'''<div class="story-grid">{stories}</div><p>Manifesto, editorial, peça real e enquete. Quatro artes 1080×1920 px, com espaço para informações e interação.</p><p class="small">Preencher dados reais e substituir os textos de instrução. Adicionar enquete pelo Instagram. Conferir as áreas da interface no aparelho.</p>'''))
    highlights=''.join('<div>'+img('02-redes/destaques/'+p.name)+f'<span>{p.stem[3:].upper()}</span></div>' for p in sorted((OUT/'02-redes/destaques').glob('*.svg')))
    pages.append(page(13,'PERFIL E DESTAQUES','A marca antes do primeiro clique.',f'''<div class="two"><div class="profile"><div class="profile-top">{img('02-redes/avatares/avatar-vermelho.svg')}<div><h3>@use_aurevi</h3><p>Aurevi · Moda feminina</p></div></div><p>Moda feminina com elegância e atitude.<br>Looks com presença, do seu jeito.<br>Fale com a gente no direct ↓</p><small>BIO SUGERIDA · AJUSTAR O CANAL REAL</small></div><div><p class="lead">Organização<br>que acolhe.</p><p>Novidades e Looks abrem o desejo. Provador e Detalhes ajudam a escolher. Aurevi e Atendimento aproximam a marca.</p><p>AV central para o avatar e os recortes circulares dos destaques.</p></div></div><div class="highlight-grid">{highlights}</div>'''))
    pages.append(page(14,'VOZ E CONTEÚDO','Segura. Próxima. Com atitude.',f'''<div class="two"><div><blockquote>Tem looks<br>que chegam<br>com você.</blockquote><p class="lead">Vista sua presença.</p><p>Frases curtas. Convites diretos.<br>O detalhe da roupa ajuda a conversa.</p></div><div>{cards([('Marca','“Aure, de ouro. Vi, de vida. Elegância para vestir com atitude.”'),('Produto','“[Nome da peça]: [detalhe real de caimento]. Consulte a disponibilidade pelo direct.”'),('Interação','“Qual detalhe faz seu look: recorte, drapeado ou acessório?”'),('Conteúdo real','Nome, tecido, tamanhos e cores só entram depois de conferidos. Os modelos editáveis indicam o que preencher.')])}<p class="small">Legendas para os nove posts e ritmo de duas semanas no guia de conteúdo incluído.</p></div></div>'''))
    pages.append(page(15,'EXPERIÊNCIA DE LOJA','Um cenário à altura do look.',f'''<div class="two"><div class="store-photo">{img('04-fotografia/estudio-aurevi.png')}</div><div>{cards([('Recepção','Cinza mineral, balcão limpo e letras em dourado polido. Luz suave para valorizar relevo e reflexos.'),('Provador','Espelho de corpo inteiro, iluminação frontal difusa e apoio para acessórios.'),('Exposição','Looks completos, espaço entre peças e combinações que orientam a escolha.'),('Atendimento','Entender ocasião e caimento desejado. Mostrar detalhes reais e alternativas com proximidade.'),('Conteúdo','Um ponto fixo de fotografia mantém luz, cor e enquadramento consistentes.')])}</div></div>'''))
    pages.append(page(16,'MOCKUPS KITTL','A marca em uso.',f'''<div class="two kittl">{img('05-mockups/kittl-sacola-boutique.png')}{img('05-mockups/kittl-sacola-em-uso.png')}</div><p>Dois mockups Kittl já produzidos no projeto, reunidos como aplicações complementares da escrita. Links de edição e origem preservados em <b>05-mockups/links-kittl.json</b>.</p><p class="small">O novo conjunto vermelho e ouro da página 09 orienta o acabamento desta direção. Estes dois exemplos anteriores mostram a marca em situações de uso.</p>'''))
    pages.append(page(17,'KIT DE ARQUIVOS','Pronto para apresentar. Fácil de aplicar.',cards([('01 / Marca','AV, escrita, composição e horizontal. Cinco acabamentos; SVG e PNG com fundo transparente. Ouro plano e metálico.'),('02 / Redes','9 posts, 4 stories, 6 destaques e 2 avatares. Textos editáveis em SVG onde aplicável.'),('03 / Embalagens','Tags, cartões, adesivo, sacola, caixa, padrão AV e máscaras de hot stamping. PDFs físicos.'),('04–05 / Imagens','Editorial de estúdio, novo mockup vermelho/ouro, prompts e dois mockups Kittl com links.'),('06 / Tipografia','Cormorant Garamond e Manrope, com licenças OFL. Desenho da logo preservado em curvas.'),('07 / Guias','Uso da marca, fotografia, legendas, calendário e ideias para a experiência de loja.')])+'''<p class="small">Artes finais em curvas e modelos com texto editável. Não são projetos nativos de Canva/Adobe. Fotos conceituais devem ser substituídas por fotos reais ao anunciar estoque.</p>'''))
    pages.append(f'''<section class="sheet"><article class="page last"><div class="eyebrow">AURE = OURO / VI = VIDA</div>{img('01-marca/principal-metalico.svg')}<h1>Elegância no traço.<br>Atitude na presença.</h1><p>Vista sua presença.</p><span>@use_aurevi</span></article></section>''')
    css='''@font-face{font-family:Cormorant;src:url('06-fontes/CormorantGaramond.ttf');font-weight:300 700}@font-face{font-family:Manrope;src:url('06-fontes/Manrope.ttf');font-weight:200 800}*{box-sizing:border-box}body{margin:0;background:#262323;color:#242424;font:24px/1.55 Manrope,sans-serif}nav{position:sticky;top:0;z-index:10;background:#242424;color:#FAF6EF;padding:12px 28px;display:flex;justify-content:space-between;font-size:14px}nav a{color:#CFB77F}.sheet{position:relative;margin:26px auto;width:1600px;height:1000px;overflow:hidden}.page{position:absolute;top:0;left:0;width:1600px;height:1000px;overflow:hidden;background:#FAF6EF;padding:55px 78px 76px;transform-origin:top left}.page header,.page footer{display:flex;justify-content:space-between;font-size:14px;letter-spacing:3px;color:#450A10}.page header{padding-bottom:16px;border-bottom:1px solid #450a1030}.page footer{position:absolute;bottom:30px;left:78px;right:78px;font-size:12px}.page h1{font:500 76px/1.03 Cormorant,serif;color:#450A10;margin:30px 0 35px;letter-spacing:-1px}.page h2{font:500 58px/1.1 Cormorant;color:#450A10}.page h3{font-size:24px;line-height:1.25;color:#450A10;margin:0 0 12px}.page p{margin:0 0 22px}.page img{display:block;max-width:100%;object-fit:contain}.small{font-size:17px;line-height:1.6}.lead{font:500 54px/1.05 Cormorant;color:#450A10;margin:0 0 28px!important}.eyebrow{font-size:16px;letter-spacing:3px;color:#450A10}.two{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start}.three{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}.red{background:#450A10}.ivory{background:#FAF6EF}.grey{background:#9B9995}blockquote{font:500 72px/1.05 Cormorant;color:#450A10;margin:32px 0 20px}.cover{padding:0;display:grid;grid-template-columns:58.333333% 41.666667%;background:#450A10;color:#FAF6EF}.cover-copy{padding:55px 70px;position:relative}.cover .eyebrow{color:#CFB77F;font-size:14px}.cover-logo{width:470px;height:295px;margin:26px auto 20px}.cover h1{color:#FAF6EF;font-size:112px;line-height:.9;margin:18px 0 35px}.cover h1 em{color:#CFB77F;font-style:normal}.cover p{font-size:25px}.cover small{display:block;font-size:12px;letter-spacing:2px;margin-top:52px;color:#CFB77F}.cover-photo{position:relative;height:1000px}.cover-photo img{width:100%;height:100%;object-fit:cover;object-position:center}.cover-photo span{position:absolute;bottom:26px;right:28px;color:#FAF6EF;font-size:12px;letter-spacing:2px;text-shadow:0 1px 4px #000}.photo-card img{width:100%;height:490px;object-fit:cover}.photo-card p{margin-top:14px}.logo-hero{height:445px;display:grid;place-items:center}.logo-hero img{width:690px;height:420px}.variants{margin:24px 0}.variants>div{height:115px;display:flex;align-items:center;justify-content:center;padding:18px}.variants img{max-height:90px;max-width:330px}.metal-panel{height:650px;background:#9B9995;display:flex;align-items:center;justify-content:center;flex-direction:column;padding:30px}.metal-panel img{width:580px;height:470px}.metal-panel span{font-size:12px;color:#450A10;letter-spacing:2px;margin-top:15px}.metal-strip{display:flex;gap:30px;height:120px}.metal-strip img:first-child{width:120px}.metal-strip img:last-child{width:330px}.swatches{display:grid;grid-template-columns:2fr 1.1fr 1.1fr 1.1fr 1.1fr;height:390px;gap:0;margin-bottom:35px}.swatch{display:flex;flex-direction:column;justify-content:flex-end;padding:24px 20px}.swatch span{font-size:11px;letter-spacing:1.5px}.swatch strong{font-size:22px;font-weight:500;line-height:1.2;margin:15px 0 12px}.swatch code{font:18px Manrope}.color-notes{margin-bottom:20px}.color-notes p{font-size:21px}.specimen{font:500 123px/.95 Cormorant;color:#450A10;margin:54px 0 45px}.alphabet{font:500 31px/1.6 Cormorant}.sans{font-family:Manrope!important;font-size:42px!important;line-height:1.3!important;margin:50px 0 30px}.type-scale{display:grid;gap:18px;padding:25px 0 35px;font-size:26px}.type-scale b{font-weight:500}.rules{display:grid;grid-template-columns:1fr 1fr;gap:55px}.rule-logo{height:540px;border:1px solid #450a1040;display:flex;align-items:center;justify-content:center;flex-direction:column;padding:45px}.rule-logo img{width:100%;padding:38px;border:1px dashed #450a1060}.rule-logo span{font-size:13px;letter-spacing:2px;margin-top:55px}.cards{display:grid;grid-template-columns:1fr 1fr;gap:32px}.cards>div{border-top:1px solid #450a1040;padding-top:22px}.cards p{font-size:22px;line-height:1.55;margin-bottom:10px}.rules .cards{grid-template-columns:1fr}.rules .cards p{font-size:20px}.photo-direction{grid-template-columns:46% 1fr;gap:70px}.tall-photo{height:690px;display:flex;justify-content:center}.tall-photo img{height:100%;width:auto}.photo-direction .cards{gap:22px}.photo-direction .cards p{font-size:20px}.photo-direction .lead{font-size:55px}.pack-hero{height:510px;margin-bottom:25px}.pack-hero img{height:100%;width:100%;object-fit:cover;object-position:50% 47%}.print-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:30px;height:430px;margin-bottom:35px}.print-grid>div{background:#e7e3dd;padding:20px;display:flex;align-items:center;justify-content:center;flex-direction:column}.print-grid img{max-height:340px;max-width:280px}.print-grid span{font-size:12px;letter-spacing:2px;margin-top:18px}.page .three p{font-size:21px}.feed-layout{display:grid;grid-template-columns:690px 1fr;gap:80px}.feed-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;width:650px}.feed-grid img{width:100%;height:215px;object-fit:contain}.feed-layout .lead{margin-top:70px!important}.story-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;margin:10px auto 30px;width:1260px}.story-grid img{width:100%;height:560px}.profile{padding:38px;background:#eae6df}.profile-top{display:flex;gap:25px;align-items:center;margin-bottom:26px}.profile-top img{width:120px;height:120px;border-radius:50%}.profile-top p{font-size:20px;margin:8px 0}.profile small{font-size:12px;letter-spacing:1px}.highlight-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:28px;margin-top:40px}.highlight-grid img{width:160px;height:160px;border-radius:50%;margin:auto}.highlight-grid span{display:block;text-align:center;font-size:13px;margin-top:18px;letter-spacing:1px}.store-photo{height:660px}.store-photo img{width:100%;height:100%;object-fit:cover;object-position:50% 18%}.kittl{margin:10px 0 30px;gap:30px}.kittl img{width:100%;height:540px;object-fit:cover}.last{background:#450A10;color:#FAF6EF;text-align:center;padding-top:65px}.last .eyebrow{color:#CFB77F}.last img{width:750px;height:470px;margin:20px auto 0}.last h1{font-size:79px;color:#FAF6EF;margin:5px 0 30px}.last p{color:#CFB77F;font-size:29px}.last>span{font-size:16px;letter-spacing:3px}.page .cards:only-of-type{gap:32px}.page> .cards{margin-top:20px}.page> .cards>div{min-height:155px}@page{size:400mm 250mm;margin:0}@media print{body{background:white}nav{display:none}.sheet{margin:0!important;width:1600px!important;height:1000px!important;break-after:page}.page{transform:none!important}.sheet:last-child{break-after:auto}}'''
    css+='.store-photo{background:#9B9995}.store-photo img{object-fit:contain;object-position:center}'
    script='''function fit(){document.querySelectorAll('.sheet').forEach(s=>{let scale=Math.min(1,(innerWidth-24)/1600);s.style.width=(1600*scale)+'px';s.style.height=(1000*scale)+'px';s.firstElementChild.style.transform='scale('+scale+')'})}addEventListener('resize',fit);fit();'''
    html=f'<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aurevi — Elegante e ousada</title><style>{css}</style><nav><span>AUREVI / IDENTIDADE VISUAL</span><a href="Manual-Aurevi-Elegante-Ousada.pdf">BAIXAR PDF</a></nav><main>{"".join(pages)}</main><script>{script}</script></html>'
    (OUT/'APRESENTACAO.html').write_text(html,encoding='utf-8')
    # An actual deliverable contact sheet, exported by Playwright.
    overview=f'''<!doctype html><html><meta charset="utf-8"><style>@font-face{{font-family:M;src:url('06-fontes/Manrope.ttf')}}@font-face{{font-family:C;src:url('06-fontes/CormorantGaramond.ttf')}}*{{box-sizing:border-box}}body{{margin:0;width:1800px;background:{I};font:26px M;color:{R}}}.top{{height:650px;display:grid;grid-template-columns:1fr 1fr;background:{R};color:{I}}}.copy{{padding:45px 65px}}.copy img{{width:100%;height:285px}}h1{{font:500 82px/.95 C;margin:20px 0}}.photo{{width:100%;height:650px;object-fit:cover;object-position:50% 0%}}.palette{{display:flex;height:140px}}.palette div{{flex:1;padding:42px 30px;font-size:20px}}.main{{padding:55px;display:grid;grid-template-columns:1fr 1fr;gap:45px}}.pack{{width:100%;height:540px;object-fit:cover}}h2{{font:500 52px C;margin:0 0 25px}}.logos{{background:{C};height:360px;display:flex;align-items:center;justify-content:center}}.logos img{{width:90%;height:300px}}.feed{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.feed img{{width:100%}}.paper{{display:flex;gap:18px;height:355px;margin-top:28px}}.paper img{{width:45%;height:100%;object-fit:contain}}.end{{padding:25px 55px 50px;font-size:18px}}</style><div class="top"><div class="copy">{img('01-marca/horizontal-metalico.svg')}<h1>Elegante.<br>Ousada. Aurevi.</h1><p>Ouro no nome. Vida na presença.</p></div>{img('04-fotografia/estudio-aurevi.png','photo')}</div><div class="palette">{''.join(f'<div style="background:{col};color:{I if col in [R,K] else R}">{name}<br>{col}</div>' for name,col,role in cols)}</div><div class="main"><div><h2>Metal, presença e acabamento.</h2><div class="logos">{img('01-marca/principal-metalico.svg')}</div><br>{img('05-mockups/embalagens-vermelho-ouro.png','pack')}<div class="paper">{img('03-embalagens/tag-frente.svg')}{img('03-embalagens/cartao-agradecimento.svg')}</div></div><div><h2>Uma linguagem para cada contato.</h2><div class="feed">{''.join(img('02-redes/feed/'+p.name) for p in feed)}</div><p>Cormorant Garamond + Manrope</p><p>Vermelho sangue · ouro champagne<br>cinza mineral · marfim · grafite</p></div></div><div class="end">AUREVI / IDENTIDADE VISUAL · Fotografia e novo mockup conceituais, gerados por IA.</div></html>'''
    (OUT/'VISAO-GERAL.html').write_text(overview,encoding='utf-8')

def main():
    for folder in ['01-marca','02-redes','03-embalagens','04-fotografia','05-mockups','06-fontes','07-guias']:(OUT/folder).mkdir(parents=True,exist_ok=True)
    for name in ['CormorantGaramond.ttf','CormorantGaramond-OFL.txt','Manrope.ttf','Manrope-OFL.txt']:shutil.copy2(ROOT/'DIRECAO-VERMELHO-ESCURO/fontes'/name,OUT/'06-fontes'/name)
    shutil.copy2(ROOT/'FOTOGRAFIAS/01-estudio-cinza-logo-dourada.png',OUT/'04-fotografia/estudio-aurevi.png')
    shutil.copy2(ROOT/'FOTOGRAFIAS/01-estudio-cinza-prompt.txt',OUT/'04-fotografia/prompt-estudio.txt')
    for name in ['sacola-boutique','sacola-em-uso']:shutil.copy2(ROOT/f'DIRECAO-VERMELHO-ESCURO/mockups/{name}.png',OUT/f'05-mockups/kittl-{name}.png')
    shutil.copy2(ROOT/'DIRECAO-VERMELHO-ESCURO/mockups/links.json',OUT/'05-mockups/links-kittl.json')
    if not (OUT/'05-mockups/embalagens-vermelho-ouro.png').exists():raise SystemExit('Salvar o mockup gerado antes de produzir o kit.')
    brand();social();packaging();write_guides();manual()
    (OUT/'inventario.json').write_text(json.dumps(ITEMS,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'paleta.json').write_text(json.dumps({'vermelho_sangue':R,'ouro_champagne':G,'cinza_mineral':C,'marfim':I,'grafite':K,'nota':'RGB. Ouro metálico é acabamento físico ou simulação separada, não um HEX.'},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'artes':len(ITEMS),'feed':9,'stories':4,'destaques':6,'avatares':2,'logos':20,'paginas':18}))

if __name__=='__main__':main()
