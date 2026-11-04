"""Refinamento AV com contraste, diagonais e gesto caligráfico."""
from pathlib import Path
import json
from identidade_ousada import Art,G,I,C,K
from logos_autorais import MODELS,mark

ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'REFINAMENTO-AV-FLUIDO'
R='#350403'
RED_GRADIENT='<linearGradient id="vermelho" x1="0" y1="0" x2=".65" y2="1"><stop offset="0" stop-color="#4A100B"/><stop offset=".45" stop-color="#350403"/><stop offset="1" stop-color="#210000"/></linearGradient>'

MODELS_AV=[
 ('01','encontro','Encontro',[
  # A: a long fine left leg and a contrasting right stem with a crisp apex.
  'M9 549 V543 Q26 543 33 522 L222 46 H232 L42 526 Q36 542 59 543 V549 Z',
  'M222 46 L244 46 L425 520 Q433 541 458 543 V549 H365 V543 Q396 543 386 518 L229 99 Z',
  # V: deliberately separated parallel diagonal, sharp lower vertex.
  'M294 78 H339 V85 Q325 86 330 101 L490 496 L647 99 Q654 84 632 84 V78 H688 V85 Q665 85 657 107 L485 550 H470 L308 109 Q300 88 283 85 V78 Z',
  # Rising swash is also the crossbar of A, with an open upturned ending.
  'M-1 548 C45 385 143 332 292 322 C411 313 518 322 598 263 C638 233 649 193 633 158 L645 153 C668 201 652 243 610 277 C528 340 414 328 293 335 C153 344 67 390 36 508 Q25 537 53 543 V549 Z'
 ],'A e V separados, com uma curva que une a composição.'),
 ('02','entrelaco','Entrelaço',[
  # A top has a short hairline; the lower left curve completes its gesture.
  'M159 201 L225 40 H240 L441 519 Q450 541 473 543 V549 H382 V543 Q412 543 402 518 L232 92 L171 205 Z',
  'M302 91 H340 L507 491 L661 92 H673 L503 549 H487 Z',
  'M-3 548 C22 521 26 480 53 434 C102 350 201 329 314 322 C466 312 587 291 619 220 C632 191 630 164 620 141 L632 136 C647 166 648 195 633 230 C599 310 470 326 315 336 C201 343 112 367 74 439 C50 483 38 527 65 542 V549 Z',
  'M296 91 H357 V98 H296 Z M642 91 H686 V98 H642 Z'
 ],'Mais próximo do gesto da referência, com o V aberto à direita.'),
 ('03','ascensao','Ascensão',[
  # A fine base returns to its apex; V ends in a restrained curved terminal.
  'M20 550 C8 525 16 504 29 474 L211 45 H225 L38 483 Q18 529 49 543 V550 Z',
  'M211 45 H236 L426 520 Q435 541 460 544 V550 H367 V544 Q397 544 386 517 L219 99 Z',
  'M300 79 H343 L509 496 L633 170 C650 127 643 98 620 84 L626 75 C665 88 672 127 651 181 L510 550 H490 L318 111 Q311 91 293 86 V79 Z',
  'M-5 547 C22 440 95 373 219 345 C339 317 439 345 531 292 C576 266 592 231 583 196 L596 192 C608 238 589 279 539 307 C446 361 344 331 223 359 C116 384 53 443 32 513 Q26 538 55 544 V550 Z'
 ],'Curva mais ampla, ponta marcada e movimento ascendente.')]

def av(a,paths,x,y,w,color,metal=False):
    s=w/740
    a.parts.append(f'<g aria-label="AV" transform="translate({x+20*s} {y}) scale({s})"'+(' filter="url(#bevel)"' if metal else '')+'>'+''.join(f'<path d="{d}" fill="{color}"/>' for d in paths)+'</g>')

def save(a,name):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(a.svg().replace('<defs>','<defs>'+RED_GRADIENT,1),encoding='utf8')

def main():
    OUT.mkdir(exist_ok=True)
    for ident,key,name,paths,desc in MODELS_AV:
        for finish,color in [('metalico','url(#metal)'),('sangue',R),('marfim',I)]:
            a=Art(1400,1400,'Aurevi — AV '+name+' '+finish);av(a,paths,150,210,1100,color,finish=='metalico');save(a,f'{ident}-{key}/AV-{finish}.svg')
        a=Art(1800,1600,'Aurevi — composição AV '+name)
        av(a,paths,420,100,960,'url(#metal)',True);mark(a,MODELS[0],140,1100,1520,'url(#metal)',True);save(a,f'{ident}-{key}/composicao-metalica.svg')
        a=Art(1400,1400,'Aurevi — apresentação AV '+name,'url(#vermelho)')
        a.text('AUREVI / '+ident+' — '+name.upper(),65,90,20,G,spacing=2)
        av(a,paths,170,300,1060,'url(#metal)',True)
        a.text('ELEGANTE. OUSADA. AUREVI.',700,1225,21,I,anchor='middle',spacing=3);save(a,f'{ident}-{key}/Apresentacao.svg')
    a=Art(2400,1440,'Aurevi — monogramas AV fluidos',I)
    a.text('AUREVI / REFINAMENTO DO MONOGRAMA',65,80,22,R,spacing=3)
    a.text('A + V. Elegância em movimento.',60,195,100,R,'CormorantGaramond',500)
    for j,(ident,key,name,paths,desc) in enumerate(MODELS_AV):
        x=65+j*770;a.rect(x,270,730,790,'url(#vermelho)')
        av(a,paths,x+60,460,610,'url(#metal)',True)
        a.text(ident+' / '+name,x+10,1150,51,R,'CormorantGaramond',500)
        # The explanatory copy is split manually so no line crowds another option.
        labels=[['A e V separados. Uma curva','une e dá movimento ao conjunto.'],['O gesto mais próximo da referência,','com o V aberto à direita.'],['Curva ampla, ponta marcada','e movimento ascendente.']][j]
        for k,t in enumerate(labels):a.text(t,x+10,1220+k*37,23,K)
    a.text('ESTUDOS EM DOURADO METÁLICO / VETORES E VERSÕES EM UMA COR INCLUÍDOS',65,1375,20,R,spacing=1)
    save(a,'Comparativo.svg')
    (OUT/'LEIA-ME.md').write_text('''# Aurevi — AV fluido

Refinamento após a nova referência enviada pelo cliente: diagonais alongadas, contraste de espessura, dourado metálico e uma curva caligráfica que atravessa o conjunto. Os três desenhos foram construídos em vetor para representar A e V.

Vermelho mais recente: #350403 como aproximação digital plana do fundo quente e quase preto enviado pelo cliente. Aplicações usam uma variação suave de #4A100B a #210000 para representar a luz da referência; não é medição exata dos pixels do anexo. O tom anterior #450A10 fica nas entregas históricas.

01 Encontro: iniciais completas e separadas, unidas visualmente pela curva. Minha recomendação inicial para equilibrar leitura e gesto.

02 Entrelaço: A mais gestual, com uma interrupção intencional no traço esquerdo; V aberto à direita. É a aproximação mais expressiva da referência.

03 Ascensão: curva ampla e um pequeno retorno no topo do V. Mais movimento, com ponta inferior marcada.

Cada pasta contém AV em metal simulado, vermelho e marfim (SVG + PNG transparente); uma aplicação sobre vermelho e uma composição metálica com o nome AUREVI. A escrita nessa composição é o estudo Presença, incluída apenas para avaliar o conjunto; a seleção da escrita e do símbolo continua aberta. Não aplicar automaticamente essas opções ao kit anterior sem o retorno do cliente.

Os arquivos preservam o desenho vetorial. O metal digital é uma simulação; o acabamento físico depende do material e da prova de produção.
''',encoding='utf8')
    (OUT/'paleta.json').write_text(json.dumps({'vermelho_plano':R,'luz':'#4A100B','sombra':'#210000','ouro_plano':G,'nota':'Aproximações visuais da nova referência, não amostragem exata do anexo.'},ensure_ascii=False,indent=2),encoding='utf8')
    print('3 refinamentos AV / 16 SVGs / novo vermelho #350403.')

if __name__=='__main__':main()
