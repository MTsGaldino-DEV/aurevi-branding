from vetor import *

PHOTO=OUT/'05-editorial/editorial-conceitual.png'

def eyebrow(c,label,x=72,y=110,color=None):
    c.text(label,x,y,20,weight=600,spacing=4,color=color)

def bow(c,x,y,s,color=None):
    color=color or C['verde']
    c.path(f'M {x} {y+s*.65} Q {x+s*.15} {y-s*.15} {x+s*.45} {y+s*.5} Q {x+s*.75} {y-s*.12} {x+s} {y+s*.65}', 'none',color,s*.025)
    c.line(x+s*.45,y+s*.5,x+s*.35,y+s,color,s*.025)
    c.line(x+s*.45,y+s*.5,x+s*.62,y+s*.95,color,s*.025)

def main():
    items=[]
    def save(c,filename,status,notes='',kind='feed',physical=None):
        folder='02-redes/'+kind if kind in ['feed','stories','destaques'] else '03-embalagens'
        d=c.save(folder+'/'+filename+'.svg',editable=True,physical=physical)
        d.update({'status':status,'notes':notes,'kind':kind});items.append(d)
    # 01: warm graphic invitation. Quiet, clear, and fully usable without stock.
    c=Canvas(1080,1350,'01 — Apresentação Aurevi',C['creme'])
    eyebrow(c,'BOM GOSTO. DO SEU JEITO.')
    c.logo(73,205,930)
    c.rect(0,580,1080,630,C['verde'])
    c.sym(686,640,380,C['coral'])
    c.lines(['Seu jeito,','bem vestido.'],72,820,116,family='Fraunces',weight=450,color=C['creme'],leading=132)
    c.text('Prazer, somos a Aurevi.',76,1130,29,color=C['creme'])
    footer(c,'01 / A MARCA',C['verde'])
    save(c,'01-apresentacao','Pronto — marca')
    # 02: manifesto.
    c=Canvas(1080,1350,'02 — Manifesto',C['verde'])
    c.logo(72,78,310,C['creme']);c.circle(952,112,22,C['coral'])
    c.lines(['Vestir bem','é se sentir','você.'],72,410,128,family='Fraunces',weight=450,color=C['creme'],leading=145)
    c.line(76,888,334,888,C['coral'],6)
    c.lines(['Tem dias de sair. Dias de ficar.','E tantos jeitos de ser a gente.','A Aurevi combina com o seu.'],76,980,31,color=C['creme'],leading=51)
    footer(c,'02 / NOSSO JEITO',C['creme'])
    save(c,'02-manifesto','Pronto — marca')
    # 03: concept editorial. Clearly marked on the image.
    c=Canvas(1080,1350,'03 — Um look, mais de um plano',C['creme'])
    c.image(PHOTO,0,160,1080,900,'xMidYMin slice')
    c.rect(0,0,1080,160,C['creme']);c.logo(72,45,315)
    pill(c,'IDEIA DE LOOK',732,53,w=276)
    c.rect(0,1060,1080,290,C['verde'])
    c.text('Um look, mais de um plano.',64,1157,64,'Fraunces',450,C['creme'])
    c.text('Combine com o seu dia.',68,1220,28,color=C['creme'])
    c.text('EDITORIAL CONCEITUAL • IMAGEM GERADA POR IA',68,1305,30,color=C['creme'])
    save(c,'03-editorial-looks','Editorial conceitual','Imagem gerada; não representa peça do catálogo.')
    # 04: actual product photo slot.
    c=Canvas(1080,1350,'04 — Template detalhes',C['creme'])
    eyebrow(c,'UM OLHAR MAIS DE PERTO')
    c.text('O detalhe faz parte.',72,245,86,'Fraunces',450)
    c.rect(72,315,936,590,C['areia'])
    c.rect(103,346,874,528,'none',stroke=C['verde'],sw=1)
    c.lines(['INSIRA A FOTO REAL','DO DETALHE DA PEÇA'],540,595,24,weight=500,anchor='middle',leading=43)
    c.lines(['Textura, acabamento e movimento.','Mostre o que a foto de longe não conta.'],72,1005,31,leading=49)
    c.text('[Nome da peça] • [tecido conferido]',72,1134,24,weight=500)
    footer(c,'04 / DETALHES')
    save(c,'04-detalhes-template','Template — adaptar','Trocar a área de foto, nome da peça e tecido por dados reais.')
    # 05: guide of outfits using abstract clothing silhouette; no claims about stock.
    c=Canvas(1080,1350,'05 — Guia de combinações',C['areia'])
    c.logo(72,72,250)
    c.lines(['Cor que conversa.','Look que funciona.'],72,345,91,family='Fraunces',weight=450,leading=108)
    for i,(a,b,lab) in enumerate([(C['creme'],C['verde'],'CREME + VERDE'),(C['coral'],C['creme'],'CORAL + CREME'),(C['verde'],C['areia'],'VERDE + AREIA')]):
        x=72+i*320
        c.rect(x,615,296,330,a,148)
        c.path(f'M{x+148} 615 A148 148 0 0 1 {x+148} 911 Z',b)
        c.text(lab,x+148,1007,20,weight=600,anchor='middle',spacing=1)
    c.text('Salve para testar com o que você já tem.',72,1140,28)
    footer(c,'05 / COMBINAÇÕES')
    save(c,'05-combinacoes','Pronto — inspiração')
    # 06: behind the scenes adaptable.
    c=Canvas(1080,1350,'06 — Template bastidores',C['verde'])
    eyebrow(c,'POR AQUI, CADA ESCOLHA IMPORTA.',color=C['creme'])
    c.text('Por trás do look.',72,268,96,'Fraunces',450,C['creme'])
    c.rect(72,355,936,650,C['creme'])
    c.sym(427,510,226,C['coral'])
    c.text('SUA FOTO DOS BASTIDORES',540,835,24,weight=500,anchor='middle',spacing=1)
    c.lines(['Da escolha das peças ao cuidado','com cada pedido. Vem ver de perto.'],72,1090,31,color=C['creme'],leading=48)
    footer(c,'06 / BASTIDORES',C['creme'])
    save(c,'06-bastidores-template','Template — adaptar','Inserir foto real e conferir se a descrição corresponde à operação.')
    # 07: conversation / engagement.
    c=Canvas(1080,1350,'07 — Conversa com a comunidade',C['coral'])
    c.logo(72,72,290)
    c.text('ME CONTA UMA COISA:',72,330,22,weight=600,spacing=3)
    c.lines(['Hoje você','vai de…'],72,475,120,family='Fraunces',weight=450,leading=140)
    for y,label,num in [(775,'Um básico com presença','01'),(906,'Uma cor pra mudar o dia','02'),(1037,'Um look que já é favorito','03')]:
        c.rect(72,y,936,104,C['creme'],52)
        c.text(num,111,y+65,24,weight=600)
        c.text(label,178,y+65,30,weight=500)
    footer(c,'07 / CONVERSA')
    save(c,'07-seu-jeito','Pronto — interação')
    # 08: customer service without assuming a WhatsApp or ecommerce.
    c=Canvas(1080,1350,'08 — Como consultar uma peça',C['creme'])
    eyebrow(c,'PODE CHEGAR. A GENTE CONVERSA.')
    c.lines(['Gostou?','Vamos conversar.'],72,339,99,family='Fraunces',weight=450,leading=117)
    for i,(t,desc) in enumerate([('Mande a referência.','Uma foto ou o nome da peça já ajuda.'),('Conte o seu jeito.','Ocasião, tamanho e o que você prefere.'),('Confira os detalhes.','Consulte medidas e disponibilidade.')]):
        y=660+i*164
        c.circle(102,y-13,30,C['coral']);c.text(str(i+1),102,y-3,25,weight=600,anchor='middle')
        c.text(t,159,y,42,'Fraunces',450)
        c.text(desc,159,y+54,27)
    footer(c,'08 / ATENDIMENTO')
    save(c,'08-como-consultar','Pronto — atendimento','Definir canal e fluxo de compra antes de adicionar link ou botão externo.')
    # 09: invitation.
    c=Canvas(1080,1350,'09 — Convite Aurevi',C['verde'])
    c.sym(355,118,370,C['coral'])
    c.lines(['Tem espaço','pro seu jeito.'],540,660,103,family='Fraunces',weight=450,color=C['creme'],anchor='middle',leading=122)
    c.text('Inspiração para vestir a vida como ela é.',540,935,31,color=C['creme'],anchor='middle')
    c.logo(305,1040,470,C['creme'])
    footer(c,'09 / VEM COM A GENTE',C['creme'])
    save(c,'09-convite','Pronto — marca')
    # Stories. Keep top/bottom comfortable for platform UI overlays.
    c=Canvas(1080,1920,'Story 01 — Manifesto Aurevi',C['creme'])
    c.logo(72,260,480);c.sym(730,275,250,C['coral'])
    c.lines(['Seu jeito,','bem vestido.'],72,870,126,family='Fraunces',weight=450,leading=145)
    c.text('Esse é o nosso ponto de partida.',76,1190,32)
    c.rect(72,1440,936,175,C['verde'],6)
    c.text('Conheça a Aurevi.',540,1546,50,'Fraunces',450,C['creme'],anchor='middle')
    c.text('@use_aurevi',72,1740,24,weight=500)
    save(c,'01-boas-vindas','Pronto — marca',kind='stories')
    c=Canvas(1080,1920,'Story 02 — Editorial conceitual',C['creme'])
    c.image(PHOTO,0,180,1080,1350)
    c.rect(0,0,1080,260,C['creme']);c.logo(72,115,350)
    c.rect(0,1390,1080,530,C['verde'])
    c.lines(['Um look.','Vários planos.'],72,1500,82,family='Fraunces',weight=450,color=C['creme'],leading=95)
    c.text('EDITORIAL CONCEITUAL • IMAGEM GERADA POR IA',72,1668,30,color=C['creme'])
    save(c,'02-editorial','Editorial conceitual','Imagem gerada; substituir por catálogo real para anunciar produtos.',kind='stories')
    c=Canvas(1080,1920,'Story 03 — Enquete de cores',C['coral'])
    eyebrow(c,'QUAL É A SUA COMBINAÇÃO?',y=305)
    c.lines(['O look começa','com o seu jeito.'],72,590,100,family='Fraunces',weight=450,leading=120)
    for x,co,label in [(72,C['verde'],'VERDE + CREME'),(555,C['areia'],'AREIA + CORAL')]:
        c.rect(x,900,453,420,co,226)
        c.text(label,x+226,1410,22,weight=600,anchor='middle')
    c.rect(170,1510,740,200,C['creme'],18)
    c.text('ADICIONE UMA ENQUETE AQUI',540,1622,24,weight=600,anchor='middle')
    c.text('@use_aurevi',72,1780,24,weight=500)
    save(c,'03-enquete-template','Template — adicionar enquete','Sobrepor sticker de enquete no Instagram; o PNG não tem interação.',kind='stories')
    c=Canvas(1080,1920,'Story 04 — Template de peça',C['creme'])
    c.logo(72,220,350)
    c.rect(72,420,936,850,C['areia'])
    c.text('INSIRA SUA FOTO REAL',540,845,28,weight=500,anchor='middle')
    c.text('[Nome da peça]',72,1403,81,'Fraunces',450)
    c.text('[Tamanhos e cores disponíveis]',72,1485,29)
    c.text('[Preço e condição conferidos]',72,1540,29)
    pill(c,'CONSULTE OS DETALHES',72,1630,w=600,size=25)
    c.text('@use_aurevi',72,1785,24,weight=500)
    save(c,'04-peca-template','Template — adaptar','Inserir foto, nome, preço, tamanhos, estoque e canal reais antes de publicar.',kind='stories')
    # Highlight covers. Their icons fit the central circle crop.
    icons={
    'novidades':['M380 540 L465 540 L465 455 L540 380 L615 455 L615 540 L700 540 L615 625 L615 700 L540 625 L465 700 L465 615 Z'],
    'looks':['M460 410 L400 455 L350 560 L440 600 L440 710 L640 710 L640 600 L730 560 L680 455 L620 410 Q540 485 460 410 Z'],
    'detalhes':['M420 430 L620 430 L700 510 L700 700 L500 700 L420 620 Z','M560 500 A20 20 0 1 0 560 540 A20 20 0 1 0 560 500'],
    'sobre':['M430 650 L430 470 Q540 345 650 470 L650 650','M465 700 L615 700'],
    'duvidas':['M445 470 Q460 380 550 390 Q670 400 630 500 Q610 540 545 570 L545 610','M545 680 L545 690'],
    'comprar':['M405 490 L675 490 L700 710 L380 710 Z','M460 490 L460 440 Q540 340 620 440 L620 490'],
    }
    labels=['Novidades','Looks','Detalhes','Sobre','Dúvidas','Comprar']
    for (name,paths),label in zip(icons.items(),labels):
        c=Canvas(1080,1080,'Destaque — '+label,C['verde'])
        c.circle(540,540,265,'none',C['coral'],3)
        for d in paths:c.path(d,'none',C['creme'],14)
        save(c,name,'Pronto — capa',kind='destaques')
    # Print studies, mm sizes include 3mm bleed each side. Units = 10/mm.
    c=Canvas(610,1010,'Tag frente — 55×95mm + sangria 3mm',C['verde'])
    c.sym(195,208,220,C['coral'])
    c.logo(85,555,440,C['creme'])
    c.text('Seu jeito, bem vestido.',305,810,24,color=C['creme'],anchor='middle')
    save(c,'tag-frente','Arte de embalagem — validar gráfica','Corte 55×95mm; arquivo 61×101mm; sangria 3mm; furo a definir no gabarito.',kind='print',physical=(61,101))
    c=Canvas(610,1010,'Tag verso — 55×95mm + sangria 3mm',C['creme'])
    c.logo(85,110,270)
    c.text('DO SEU JEITO.',85,330,24,weight=600,spacing=2)
    for y,label in [(455,'PEÇA'),(590,'TAMANHO'),(725,'REFERÊNCIA')]:
        c.text(label,85,y,17,weight=600,spacing=2);c.line(85,y+55,525,y+55,C['verde'],1)
    c.text('@use_aurevi',85,910,23,weight=500)
    save(c,'tag-verso','Arte de embalagem — validar gráfica','Campos para preenchimento. Não substitui etiqueta de composição/cuidados. Corte 55×95mm, sangria 3mm.',kind='print',physical=(61,101))
    c=Canvas(960,610,'Cartão frente — 90×55mm + sangria 3mm',C['coral'])
    c.logo(85,85,450);c.sym(670,90,200,C['verde'])
    c.lines(['Que bom ter você','por aqui.'],85,365,62,family='Fraunces',weight=450,leading=73)
    c.text('@use_aurevi',85,535,22,weight=500)
    save(c,'cartao-frente','Arte de embalagem — validar gráfica','Corte 90×55mm; arquivo 96×61mm; sangria 3mm.',kind='print',physical=(96,61))
    c=Canvas(960,610,'Cartão verso — 90×55mm + sangria 3mm',C['creme'])
    c.text('Obrigada por escolher a Aurevi.',85,175,43,'Fraunces',450)
    c.lines(['Esperamos que essa escolha acompanhe','muitos momentos do seu jeito.','Se quiser compartilhar seu look, marque a gente.'],85,282,26,leading=47)
    c.logo(85,465,250)
    save(c,'cartao-verso','Arte de embalagem — validar gráfica','Não inclui cupom nem regra de troca não confirmada.',kind='print',physical=(96,61))
    c=Canvas(560,560,'Adesivo circular — diâmetro 50mm + sangria 3mm',C['coral'])
    c.sym(165,145,230,C['verde'])
    save(c,'adesivo-lacre','Arte de embalagem — validar gráfica','Corte circular Ø50mm centrado; arquivo 56×56mm; sangria 3mm. Faca separada com a gráfica.',kind='print',physical=(56,56))
    # A transparent design for deterministic Kittl placement, no invented bag dieline.
    c=Canvas(1400,880,'Arte de aplicação na sacola — sem gabarito')
    c.logo(100,180,1200,C['verde'])
    c.text('Seu jeito, bem vestido.',700,705,54,color=C['verde'],anchor='middle')
    save(c,'sacola-aplicacao','Estudo de aplicação','Arte transparente; escala e gabarito definidos pelo fabricante da sacola.',kind='print')
    # Two monocolor alternatives for dark or uncoated bags.
    c=Canvas(1400,880,'Arte creme de aplicação na sacola — sem gabarito')
    c.logo(100,180,1200,C['creme'])
    c.text('Seu jeito, bem vestido.',700,705,54,color=C['creme'],anchor='middle')
    save(c,'sacola-aplicacao-creme','Estudo de aplicação','Versão creme para substrato verde escuro.',kind='print')
    (ROOT/'docs/manifesto-artes.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(items)} artes: 9 feed, 4 stories, 6 destaques e 7 aplicações de embalagem.')

if __name__=='__main__':main()
