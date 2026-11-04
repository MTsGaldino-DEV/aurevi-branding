from pathlib import Path
from html import escape
import json
from vetor import OUT,C

pages=[]

def img(src,cls='',alt='',style=''):
    return f'<img src="{escape(src,quote=True)}" class="{cls}" alt="{escape(alt,quote=True)}" style="{style}">'

def page(kicker,title,body,cls='',id=None):
    n=len(pages)+1
    ident=id or 'pagina-'+str(n)
    header=f'<div class="eyebrow">{kicker}</div><h2>{title}</h2>' if title else ''
    pages.append(f'<div class="sheet" id="{ident}"><section class="page {cls}" aria-label="{escape(kicker)}"><div class="inner">{header}{body}</div><footer><span>AUREVI · IDENTIDADE VISUAL</span><span>2026 &nbsp; / &nbsp; {n:02d}</span></footer></section></div>')

def card(num,title,body):
    return f'<article class="card"><span class="number">{num}</span><h3>{title}</h3><p>{body}</p></article>'

def build():
    photo='05-editorial/editorial-conceitual.png'
    logo='01-logos/logo-verde.svg'
    sym='01-logos/simbolo-verde.svg'
    # 01 — cover.
    page('AUREVI / ESSENCIAL COM PERSONALIDADE','',f'''
    <div class="cover-left"><div class="eyebrow">IDENTIDADE VISUAL &nbsp; / &nbsp; 2026</div>
    {img(logo,'cover-logo','Aurevi')}
    <h1>Bom gosto.<br>Do seu jeito.</h1>
    <div class="cover-tag"><i></i><p>Seu jeito, bem vestido.</p></div>
    <p class="cover-edition">Sistema visual · Versão 1.0<br>Logo, linguagem e aplicações.</p></div>
    <div class="cover-photo">{img(photo,alt='Editorial conceitual da Aurevi')}<span class="photo-credit">EDITORIAL CONCEITUAL · IMAGEM GERADA POR IA</span></div>
    ''','cover','inicio')
    # 02.
    page('01 / ESSÊNCIA','Estilo para a vida real.',f'''
    <div class="two"><div><p class="lead">Uma marca feminina de bom gosto, com personalidade e espaço para o jeito de cada mulher.</p>
    <p>Vestir bem começa em se reconhecer. A Aurevi propõe combinações, conversa sobre detalhes e aproxima a moda dos momentos reais do dia.</p>
    <div class="quote">Seu jeito,<br><em>bem vestido.</em></div></div>
    <div class="stack">{card('01','Estilo','Combinações que inspiram escolhas próprias.')}{card('02','Proximidade','Uma conversa simples, atenta e acolhedora.')}{card('03','Cuidado','Clareza na informação e atenção aos detalhes.')}</div></div>
    ''')
    # 03.
    page('02 / A MARCA','Um nome com presença.',f'''
    <div class="brand-stage">{img(logo,alt='Logo principal Aurevi')}</div>
    <div class="brand-bottom"><div><h3>A marca principal</h3><p class="small">Letras em minúsculas, serifas com corpo e curvas acolhedoras. Espaçamento ajustado a partir da Fraunces, em peso 520.</p></div>
    <div class="symbol-stage">{img(sym,alt='Símbolo AV')}<div><h3>A + V</h3><p class="small">Duas iniciais em diálogo. A diagonal e a curva sugerem o encontro e a dobra de um tecido.</p></div></div></div>
    ''','', 'marca')
    # 04.
    page('03 / PROPORÇÃO E RESPIRO','Espaço para ser lida.',f'''
    <div class="two protect"><div><div class="clearbox">{img(logo,alt='Logo com área de proteção')}<span>x</span></div>
    <p class="small">Área livre mínima em todos os lados: <b>x = ¼ da altura visível das letras.</b> O limite considera o desenho das letras, e não a borda do arquivo.</p></div>
    <div><h3>Reduções de partida</h3><p>Nome: <b>120 px / 25 mm</b>.<br>Símbolo: <b>32 px / 8 mm</b>.<br>Com “Moda feminina”: <b>220 px / 45 mm</b>.</p>
    <div class="reduction">{img(logo,style='width:120px',alt='Logo a 120 pixels')}{img(sym,style='width:32px',alt='Símbolo a 32 pixels')}</div>
    <p class="small">Verificar a leitura no suporte real. Bordado, baixo relevo e impressão em superfície porosa podem exigir traços maiores e prova do fornecedor.</p></div></div>
    ''')
    # 05.
    page('04 / VERSÕES','A mesma marca, em cada contexto.',f'''
    <div class="versions"><div class="sample cream">{img(logo,alt='Logo verde')}<span>VERDE / FUNDO CLARO</span></div>
    <div class="sample green">{img('01-logos/logo-creme.svg',alt='Logo creme')}<span>CREME / FUNDO VERDE</span></div>
    <div class="sample white">{img('01-logos/logo-preto.svg',alt='Logo preto')}<span>PRETO / UMA TINTA</span></div>
    <div class="sample black">{img('01-logos/logo-branco.svg',alt='Logo branco')}<span>BRANCO / NEGATIVO</span></div></div>
    <div class="rules"><p class="small"><b>Preservar:</b> proporção, contraste e área de proteção.</p><p class="small"><b>Evitar:</b> esticar, inclinar, aplicar sombra, contorno ou colocar sobre uma foto sem leitura.</p></div>
    ''')
    # 06.
    swatches=''.join(f'<div class="swatch" style="background:{C[key]};color:{C["creme"] if key in ["verde","tinta"] else C["verde"]}"><b>{label}</b><span>{C[key]}</span><small>{purpose}</small></div>' for key,label,purpose in [('creme','Creme','A base e o respiro.'),('verde','Verde profundo','Presença e reconhecimento.'),('coral','Coral','Um ponto de energia.'),('areia','Areia','Apoio e equilíbrio.'),('tinta','Tinta','Informação clara.')])
    page('05 / CORES','Natural, com um ponto de cor.',f'''
    <div class="swatches">{swatches}</div>
    <div class="two color-notes"><div><h3>O ritmo da paleta</h3><p>60% creme · 25% verde · 10% areia · 5% coral, como ponto de partida nas artes gráficas. As fotos trazem as cores reais da roupa.</p></div>
    <div><h3>Leitura em primeiro lugar</h3><p class="small">Verde/creme: 10,45:1. Verde/coral: 4,63:1. Para texto, usar verde ou tinta nos fundos claros. Creme/coral: 2,26:1; essa dupla fica para decoração.</p><p class="small">Cores digitais em sRGB. Para impressão, converter com o perfil indicado pela gráfica e validar uma prova física.</p></div></div>
    ''','', 'cores')
    # 07.
    page('06 / TIPOGRAFIA','Personalidade + clareza.',f'''
    <div class="two type"><div><div class="type-name">FRAUNCES / TÍTULOS</div><div class="aa serif">Aa</div><h3 class="serif">Seu jeito, bem vestido.</h3><p class="small">Títulos em pesos 400–500. Logo em 520. Nas artes: SOFT 12, WONK 0, tamanho óptico 72.</p><p class="alphabet serif">Aa Bb Cc · ç ã é ê í ó</p></div>
    <div><div class="type-name">MANROPE / INFORMAÇÃO</div><div class="aa sans">Aa</div><h3 class="sans">Moda que conversa.</h3><p class="small">Texto em 400. Apoios em 500. Chamadas em 600. Boa leitura para medidas, tamanhos, preços e atendimento.</p><p class="alphabet sans">Aa Bb Cc · ç ã é ê í ó</p></div></div>
    <div class="type-scale"><span>FEED 1080 PX</span><b>Título 88–128 px</b><b>Apoio 28–36 px</b><b>Rótulo 18–24 px</b></div>
    ''','', 'tipografia')
    # 08.
    page('07 / ELEMENTOS','Uma dobra, muitas possibilidades.',f'''
    <div class="two"><div class="pattern">{img('01-logos/padrao-dobras.svg',alt='Padrão de dobras AV')}</div>
    <div><p class="lead">O símbolo também vira detalhe.</p><p>Usar isolado, em repetição espaçada ou como recorte amplo. Alternar com áreas lisas para manter o sistema leve.</p>
    <div class="element-demo">{img(sym,alt='Símbolo isolado')}<span class="coral-dot"></span><span class="thin-line"></span></div>
    <p class="small">O coral marca um ponto de atenção. Linhas finas organizam a informação. O padrão é apoio; a roupa e o nome continuam sendo os protagonistas.</p></div></div>
    ''')
    # 09.
    page('08 / FOTOGRAFIA','Perto da roupa. Perto da vida.',f'''
    <div class="two photo-direction"><figure>{img(photo,alt='Referência editorial conceitual')}<figcaption>EDITORIAL CONCEITUAL · IMAGEM GERADA POR IA</figcaption></figure>
    <div class="stack">{card('01','Luz que acolhe','Luz natural ou uniforme. Fundo claro, gestos espontâneos e espaço para respirar.')}{card('02','Cor e caimento reais','Mostrar a peça de frente, de lado e em detalhe. Preservar textura e cor, sem filtros que mudem o produto.')}{card('03','Informação que ajuda','Fotografar o catálogo real. Só associar nome, preço, tecido e disponibilidade depois de conferir cada dado.')}</div></div>
    ''')
    # 10.
    page('09 / LINGUAGEM','Bom gosto também na conversa.',f'''
    <div class="two"><div><div class="voice-quote">“Qual combinação<br>tem mais a<br><em>sua cara?</em>”</div><p class="small">Uma voz próxima, segura e cuidadosa. Convidar a experimentar, perguntar e escolher.</p></div>
    <div><h3>O perfil da Aurevi</h3><p class="small">AUREVI | Moda feminina</p><div class="bio">Seu jeito, bem vestido.<br>Moda feminina e inspiração para a vida real.<br>Conheça a Aurevi. ↓</div>
    <p class="small">A seta depende de um link configurado. Sem link, usar “Vem conhecer o nosso jeito.”</p><h3>Frases para o dia a dia</h3><p class="small">“Um look, mais de um plano.”<br>“Olha esse detalhe de perto.”<br>“Me conta a ocasião e o tamanho que procura.”</p></div></div>
    ''')
    # 11.
    files=sorted((OUT/'02-redes/feed').glob('*.svg'))
    grid=''.join(img(str(f.relative_to(OUT)).replace('\\','/'),alt=f.stem) for f in files)
    page('10 / INSTAGRAM','Um feed com ritmo.',f'''
    <div class="feed-layout"><div><p class="lead">Marca, inspiração,<br>conversa e produto.</p><p>Alternar áreas claras, verde e pequenos pontos de coral. Dar espaço às fotografias reais quando o catálogo estiver pronto.</p><div class="status-key"><span>6 artes gráficas de marca, dica e atendimento</span><span>1 editorial conceitual identificado</span><span>2 templates de foto real</span></div>
    <p class="small">Grade de apresentação. A disposição no perfil depende da ordem de publicação e dos recortes da plataforma. Cada arquivo também funciona sozinho.</p></div><div class="feed-grid">{grid}</div></div>
    ''','', 'redes')
    # 12.
    examples=''.join(f'<figure>{img("02-redes/feed/"+f,alt=title)}<figcaption><b>{title}</b><br>{status}</figcaption></figure>' for f,title,status in [('01-apresentacao.svg','Apresentação','Pronta para apresentar a marca.'),('03-editorial-looks.svg','Editorial conceitual','Imagem gerada; não anuncia estoque.'),('04-detalhes-template.svg','Detalhe de produto','Inserir foto e informações reais.')])
    page('11 / POSTS','Cada peça tem uma função.',f'<div class="three post-examples">{examples}</div><p class="small">SVG em curvas + PNG nas pastas principais. Versões com textos editáveis nas subpastas “editaveis”. Legendas e instruções no Guia de conteúdo.</p>')
    # 13.
    stories=''.join(f'<figure>{img("02-redes/stories/"+f,alt=t)}<figcaption><b>{t}</b><br>{desc}</figcaption></figure>' for f,t,desc in [('01-boas-vindas.svg','01 / Apresentar','Pronto para a marca.'),('02-editorial.svg','02 / Inspirar','Editorial conceitual.'),('03-enquete-template.svg','03 / Conversar','Adicionar sticker de enquete.'),('04-peca-template.svg','04 / Mostrar','Inserir peça e dados reais.')])
    page('12 / STORIES','Uma sequência que aproxima.',f'<div class="four stories">{stories}</div><p class="small">Arquivos 1080×1920. A composição preserva folga no topo e na base. Verificar a prévia no aplicativo; stickers e links são adicionados no Instagram.</p>')
    # 14.
    names=[('novidades','Novidades'),('looks','Looks'),('detalhes','Detalhes'),('sobre','Sobre'),('duvidas','Dúvidas'),('comprar','Comprar')]
    highlights=''.join(f'<figure>{img("02-redes/destaques/"+key+".svg",alt=title)}<figcaption>{title}</figcaption></figure>' for key,title in names)
    page('13 / DESTAQUES','O essencial, fácil de encontrar.',f'''
    <div class="profile"><div class="account">{img('01-logos/avatar.svg',alt='Avatar Aurevi')}<div><b>@use_aurevi</b><p>AUREVI | Moda feminina</p><span>Seu jeito, bem vestido.</span></div></div><div class="highlights">{highlights}</div></div>
    <div class="two"><p>Ícones no centro, cor consistente e recorte circular. O nome de cada destaque é escrito no campo do Instagram.</p><p class="small">Criar destaques quando houver conteúdo correspondente. “Comprar” precisa explicar o fluxo real. “Elas usam” pode entrar depois, com fotos e autorização de clientes reais.</p></div>
    ''')
    # 15.
    flats=''.join(f'<figure>{img("03-embalagens/"+f,alt=t)}<figcaption>{t}</figcaption></figure>' for f,t in [('tag-frente.svg','Tag / frente'),('tag-verso.svg','Tag / verso'),('cartao-frente.svg','Cartão / frente'),('adesivo-lacre.svg','Lacre / símbolo')])
    page('14 / PAPEL E EMBALAGEM','Cuidado que acompanha a peça.',f'''
    <div class="four packaging">{flats}</div>
    <div class="three print-spec"><div><h3>Tag</h3><p class="small">Corte sugerido: 55×95 mm.<br>Arquivo: 61×101 mm, com 3 mm de sangria. Furo conforme gabarito.</p></div><div><h3>Cartão</h3><p class="small">Corte sugerido: 90×55 mm.<br>Arquivo: 96×61 mm, com 3 mm de sangria. Frente e verso separados.</p></div><div><h3>Lacre</h3><p class="small">Corte circular: Ø50 mm.<br>Arquivo: 56×56 mm, com 3 mm de sangria. Faca a definir com a gráfica.</p></div></div>
    <p class="small">Artes RGB em curvas, com medidas sugeridas. A gráfica deve confirmar escala, papel, cor, faca e acabamento antes de produzir. A tag comercial não substitui a etiqueta de composição e cuidados.</p>
    ''','', 'embalagens')
    # 16,17.
    mockdata=json.loads((OUT/'07-mockups-kittl/links.json').read_text(encoding='utf-8')) if (OUT/'07-mockups-kittl/links.json').exists() else []
    def mockfigure(filename,title,desc):
        link=next((m.get('editUrl','') for m in mockdata if m['filename']==filename),'')
        caption=f'<b>{title}</b> · {desc}'
        if link:caption+=f' · <a href="{escape(link,quote=True)}">Abrir no Kittl ↗</a>'
        return f'<figure>{img("07-mockups-kittl/"+filename,alt=title)}<figcaption>{caption}</figcaption></figure>'
    page('15 / MOCKUPS KΙTTL','A marca encontra a matéria.',f'<div class="two mockups">{mockfigure("01-sacola.png","Sacola","Aplicação em papel claro.")}{mockfigure("02-ecobag.png","Ecobag","Alternativa em tecido.")}</div><p class="small">Renderizações determinísticas criadas no Kittl com os vetores da Aurevi. As cenas demonstram aplicação; material, cor e tamanho finais dependem do fornecedor.</p>','', 'mockups')
    page('16 / MOCKUPS KΙTTL','Os pequenos cuidados.',f'<div class="two mockups">{mockfigure("03-tag-clara.png","Tag clara","Alternativa com o nome em verde.")}{mockfigure("04-cartao.png","Cartão coral","Aplicação da arte de agradecimento.")}</div><p class="small">Mockups e artes salvos localmente e na biblioteca do Kittl. Os links abrem a edição no serviço e podem exigir login. As artes planas estão na pasta de embalagens.</p>')
    # 18.
    page('17 / EXPERIÊNCIA','O cuidado aparece no conjunto.',f'''
    <div class="experience"><div class="experience-statement">Do primeiro<br>“oi” ao<br><em>último detalhe.</em>{img(sym,alt='Símbolo Aurevi')}</div><div class="stack">{card('01','Um cenário simples','Fundo creme, luz uniforme e fotos consistentes da roupa real.')}{card('02','Uma boa conversa','Perguntar ocasião, tamanho e preferência. Conferir informação antes de oferecer.')}{card('03','Uma embalagem coerente','Começar com embalagem neutra, nome legível e um detalhe coral. Testar uma amostra antes de produzir em quantidade.')}</div></div>
    <p class="small">As ideias valem para operação online ou física, conforme o que existir. Fachada e ambientação precisam de medidas e contexto próprios; o guia de ideias detalha os próximos passos.</p>
    ''')
    # 19.
    calendar=''.join(card(n,t,b) for n,t,b in [('01','Apresentar','Apresentação, manifesto e convite. Mostrar o que a Aurevi acredita e ouvir a comunidade.'),('02','Inspirar','Combinações, editorial conceitual e conversa. Observar preferências e dúvidas.'),('03','Mostrar','Detalhes e bastidores reais. Vídeo de uma peça em três ângulos.'),('04','Ajudar','Como consultar, formas de combinar e respostas às dúvidas recebidas.')])
    page('18 / CONTEÚDO','Quatro semanas para começar.',f'<div class="four calendar">{calendar}</div><div class="two"><p>Três publicações principais por semana, ajustadas à capacidade real da equipe. Stories acompanham o que houver para mostrar.</p><p class="small">O calendário inclui as nove artes do kit e três pautas novas para produzir com o catálogo real. Sem catálogo, mostrar o processo da marca e dicas gerais. Legendas, roteiros e instruções estão no guia de conteúdo.</p></div>')
    # 20.
    page('19 / USO DOS ARQUIVOS','Do arquivo ao dia a dia.',f'''
    <div class="two"><div><h3>Para publicar</h3><p class="small">Usar o PNG da pasta “02-redes”. Ler o estado da peça no inventário. Templates exigem foto e dados reais; o editorial deve manter o aviso de imagem conceitual.</p><h3>Para editar</h3><p class="small">Instalar as fontes de “06-fontes” e abrir o SVG de “editaveis” em editor compatível. As versões principais em curvas mantêm o desenho ao importar, mas os textos viram formas.</p><h3>Para imprimir</h3><p class="small">Enviar SVG em curvas e a ficha de medidas ao fornecedor. Confirmar perfil de cor, corte, sangria e acabamento. A sacola é uma arte de aplicação, sem faca ou gabarito de fabricação.</p></div>
    <div class="file-list"><a href="01-logos/logo-verde.svg">01 · Logos e símbolo ↗</a><a href="02-redes/feed/01-apresentacao.png">02 · Feed, stories e destaques ↗</a><a href="03-embalagens/tag-frente.svg">03 · Artes de embalagem ↗</a><a href="04-conteudo/Guia-de-conteudo.html">04 · Legendas e calendário ↗</a><a href="05-editorial/LEIA-ME.txt">05 · Editorial conceitual ↗</a><a href="06-fontes/Fraunces-LICENCA.txt">06 · Fontes e licenças ↗</a><a href="07-mockups-kittl/links.json">07 · Mockups Kittl ↗</a><a href="inventario.csv">Inventário dos arquivos ↗</a></div></div>
    ''')
    # 21.
    page('20 / CRÉDITOS E CONTINUIDADE','Uma base para crescer.',f'''
    <div class="two"><div class="closing-brand">{img(logo,alt='Aurevi')}<div class="serif closing-tag">Seu jeito,<br>bem vestido.</div><div class="mini-swatches">{''.join('<i style="background:'+v+'"></i>' for v in C.values())}</div></div>
    <div><h3>Tipografia</h3><p class="small">Fraunces: Undercase Type, Phaedra Charles e Flavia Zimbardi.<br>Manrope: Mikhail Sharanda / Manrope Project Authors.<br>Arquivos originais com SIL Open Font License 1.1 incluídos.</p><h3>Imagem e mockups</h3><p class="small">Editorial original gerado por IA no recurso integrado; prompt incluído. Mockups criados pelo <a href="https://www.kittl.com/mcp">Kittl MCP</a> com templates do próprio serviço. Usar conforme os termos da conta.</p><h3>Referências estudadas</h3><p class="small"><a href="https://www.instagram.com/donna.oficial/">Donna</a> · <a href="https://www.behance.net/gallery/208303969/Kanoa-Identidade-Visual">Kanoa / Amanda Karen</a> · <a href="https://www.behance.net/gallery/175647547/Identidade-Visual-Loja-de-Roupa-Vestuario">Madu / Junior Fergom</a> · <a href="https://www.behance.net/gallery/137758259/Margot-luxe-streetwear-for-women-Branding-project">Margot / APUCHADES</a>. Nenhuma arte dessas marcas compõe o kit da Aurevi.</p><p class="small">Versão 1.0 · 04/11/2026.<br>Catálogo, operação e provas de impressão podem ser incorporados a partir desta base.</p></div></div>
    ''')
    css='''
    @font-face{font-family:Fraunces;src:url('06-fontes/Fraunces.ttf');font-weight:100 900;font-style:normal}
    @font-face{font-family:Fraunces;src:url('06-fontes/Fraunces-Italic.ttf');font-weight:100 900;font-style:italic}
    @font-face{font-family:Manrope;src:url('06-fontes/Manrope.ttf');font-weight:200 800}
    *{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#ddd6ca;color:#203c32;font-family:Manrope,sans-serif}a{color:inherit;text-underline-offset:5px}nav{height:72px;padding:0 32px;background:#f4efe6ee;backdrop-filter:blur(10px);display:flex;align-items:center;gap:26px;position:sticky;top:0;z-index:5;border-bottom:1px solid #203c3222;font-size:14px}nav img{width:130px}nav .grow{flex:1}nav a{text-decoration:none}nav button{border:1px solid #203c32;background:transparent;color:#203c32;padding:9px 15px;border-radius:24px;font:inherit;cursor:pointer}.download{background:#203c32;color:#f4efe6;padding:10px 18px;border-radius:24px}
    main{padding:32px}.sheet{width:calc(1600px * var(--scale,1));height:calc(1000px * var(--scale,1));margin:0 auto 32px;position:relative;box-shadow:0 8px 40px #203c3210;scroll-margin-top:104px}.page{width:1600px;height:1000px;position:absolute;left:0;top:0;overflow:hidden;background:#f4efe6;transform:scale(var(--scale,1));transform-origin:top left}.inner{padding:66px 80px 70px}.eyebrow{font-size:17px;font-weight:600;letter-spacing:3.5px}.page h2{font:450 67px/1.08 Fraunces,serif;letter-spacing:-1.5px;margin:20px 0 40px;font-variation-settings:'SOFT' 12,'WONK' 0,'opsz' 72}h1,h3,.serif,.quote,.voice-quote{font-family:Fraunces,serif;font-weight:450;font-variation-settings:'SOFT' 12,'WONK' 0,'opsz' 72}h3{font-size:38px;line-height:1.15;margin:0 0 15px}p{font-size:27px;line-height:1.52;margin:0 0 26px}p.lead{font-size:36px;line-height:1.4}.small{font-size:21px;line-height:1.55}b{font-weight:600}em{font-weight:400}footer{position:absolute;bottom:28px;left:80px;right:80px;border-top:1px solid #203c3233;padding-top:15px;display:flex;justify-content:space-between;font-size:13px;letter-spacing:1.3px}.two{display:grid;grid-template-columns:1fr 1fr;gap:70px}.three{display:grid;grid-template-columns:repeat(3,1fr);gap:36px}.four{display:grid;grid-template-columns:repeat(4,1fr);gap:30px}figure{margin:0}figcaption{font-size:18px;line-height:1.5;margin-top:12px}img{max-width:100%;display:block}.stack{display:grid;gap:20px}.card{border-top:1px solid #203c3238;padding:22px 0 0;position:relative}.number{font-size:16px;letter-spacing:2px;display:block;margin-bottom:13px;color:#547165}.card h3{font-size:36px}.card p{font-size:24px;margin-bottom:10px}.quote{font-size:87px;line-height:1.05;margin-top:52px;letter-spacing:-2px}.quote em{color:#47715f}.cover .inner{padding:0}.cover-left{position:absolute;left:80px;top:72px;width:790px}.cover-logo{width:790px;margin:93px 0 40px}.cover h1{font-size:91px;line-height:1.06;letter-spacing:-2px;margin:0 0 40px}.cover-tag{display:flex;align-items:center;gap:18px}.cover-tag i{width:20px;height:20px;background:#e98673;border-radius:50%}.cover-tag p{font-size:27px;margin:0}.cover-edition{font-size:17px;line-height:1.6;margin-top:56px}.cover-photo{position:absolute;right:0;top:0;width:640px;height:1000px}.cover-photo img{width:100%;height:100%;object-fit:cover;object-position:65% center}.photo-credit{position:absolute;right:18px;bottom:30px;writing-mode:vertical-rl;font-size:10px;letter-spacing:1px;background:#f4efe6bd;padding:10px 6px}.cover footer{right:720px}.brand-stage{height:400px;display:flex;align-items:center;border-bottom:1px solid #203c3233}.brand-stage img{width:1150px;margin:auto}.brand-bottom{display:grid;grid-template-columns:1fr 1fr;gap:80px;margin-top:30px}.symbol-stage{display:flex;align-items:center;gap:28px}.symbol-stage img{width:190px}.symbol-stage .small{margin:0}.clearbox{height:400px;border:2px dashed #a78e76;display:flex;align-items:center;padding:60px;margin:20px 0 30px;position:relative}.clearbox span{position:absolute;top:12px;left:20px;font-size:26px}.protect{padding-top:20px}.protect .small{margin-top:28px}.reduction{display:flex;align-items:center;gap:48px;min-height:110px;background:#fff8;padding:25px 38px}.versions{display:grid;grid-template-columns:1fr 1fr;gap:24px}.sample{height:270px;position:relative;padding:30px 90px;display:flex;align-items:center;justify-content:center}.sample img{width:500px}.sample span{position:absolute;left:28px;bottom:20px;font-size:14px;letter-spacing:2px}.cream{background:#e8dfd2}.green{background:#203c32;color:#f4efe6}.white{background:white}.black{background:#242824;color:white}.rules{display:flex;justify-content:space-between;gap:70px;margin-top:32px}.rules p{width:50%}.swatches{display:flex;width:100%;height:400px;gap:14px}.swatch{flex:1;padding:28px 24px;display:flex;flex-direction:column;justify-content:flex-end}.swatch b{font-size:25px;line-height:1.3}.swatch span{font-size:20px;margin-top:14px}.swatch small{font-size:16px;margin-top:20px}.color-notes{margin-top:42px}.type{gap:110px}.type-name{font-size:17px;font-weight:600;letter-spacing:2px}.aa{font-size:210px;line-height:1.2;letter-spacing:-7px;margin:0 0 20px}.sans{font-family:Manrope,sans-serif;font-weight:500}.alphabet{font-size:36px}.type-scale{border-top:1px solid #203c3240;padding-top:24px;display:flex;align-items:center;justify-content:space-between;font-size:24px;margin-top:26px}.type-scale span{font-size:16px;letter-spacing:2px}.pattern{height:650px;overflow:hidden;background:#eae1d4}.pattern img{width:100%;height:100%;object-fit:cover}.element-demo{height:220px;display:flex;align-items:center;justify-content:space-between;gap:30px}.element-demo img{width:190px}.coral-dot{display:block;background:#e98673;width:74px;height:74px;border-radius:50%}.thin-line{height:2px;width:170px;background:#203c32}.photo-direction{grid-template-columns:600px 1fr}.photo-direction figure img{width:500px;height:625px;object-fit:cover}.photo-direction figcaption{font-size:13px;letter-spacing:1px}.photo-direction .card{padding-top:14px}.photo-direction .stack{gap:14px}.photo-direction .card p{font-size:22px}.voice-quote{font-size:82px;line-height:1.15;letter-spacing:-2px;margin:10px 0 45px}.bio{font-size:25px;line-height:1.65;background:#e8dfd2;padding:30px;margin:22px 0}.feed-layout{display:grid;grid-template-columns:1fr 640px;gap:75px}.feed-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:-90px}.feed-grid img{width:100%}.status-key{display:grid;gap:14px;margin:35px 0}.status-key span{font-size:19px;border-left:6px solid #e98673;padding-left:16px}.post-examples{padding:0 60px;gap:60px;margin-bottom:28px}.post-examples img{width:100%;height:500px;object-fit:contain}.post-examples figcaption{font-size:20px}.stories{gap:62px;margin:0 24px 26px}.stories img{height:520px;width:100%;object-fit:contain}.stories figcaption{font-size:18px}.profile{background:#fff7;padding:35px 65px 40px;margin-bottom:38px}.account{display:flex;align-items:center;gap:40px;margin-bottom:45px}.account>img{width:128px;height:128px;border-radius:50%}.account b{font-size:30px}.account p{font-size:23px;margin:10px 0}.account span{font-size:22px}.highlights{display:flex;justify-content:space-between;gap:45px}.highlights figure{text-align:center;width:130px}.highlights img{width:118px;height:118px;border-radius:50%;margin:auto}.highlights figcaption{font-size:20px}.packaging{height:380px;align-items:center;gap:32px;margin-bottom:46px}.packaging figure{height:100%;display:flex;flex-direction:column;align-items:center}.packaging img{height:330px;max-width:100%;object-fit:contain}.packaging figure:nth-child(3) img{width:360px}.packaging figure:nth-child(4) img{width:245px;height:245px;border-radius:50%;margin-top:55px}.packaging figcaption{margin-top:auto;font-size:20px}.print-spec{margin-bottom:24px;gap:45px}.print-spec h3{font-size:30px}.print-spec p{font-size:19px}.mockups{gap:36px;margin:0 100px 22px}.mockups img{width:100%;height:550px;object-fit:cover}.mockups figcaption{font-size:17px}.experience{display:grid;grid-template-columns:1fr 1fr;gap:80px;margin-bottom:28px}.experience-statement{font:450 78px/1.07 Fraunces,serif;letter-spacing:-2px}.experience-statement img{width:185px;margin-top:40px}.experience .stack{gap:22px}.experience .card p{font-size:22px}.calendar{margin:20px 0 65px}.calendar .card{background:#e9e0d3;border:0;padding:30px 26px;min-height:380px}.calendar .card:nth-child(2){background:#203c32;color:#f4efe6}.calendar .card:nth-child(2) .number{color:#e98673}.calendar .card:nth-child(3){background:#e98673}.calendar .number{font-size:40px;font-family:Fraunces}.calendar p{font-size:23px}.file-list{display:grid;align-content:start;border-top:1px solid #203c3230}.file-list a{font-size:23px;text-decoration:none;border-bottom:1px solid #203c3230;padding:18px 0}.closing-brand{padding-top:40px}.closing-brand>img{width:640px}.closing-tag{font-size:76px;line-height:1.1;letter-spacing:-2px;margin:42px 0}.mini-swatches{display:flex;width:380px;height:55px;gap:8px}.mini-swatches i{flex:1}.page:last-child .small{font-size:20px}body.real main{overflow-x:auto}body.real .sheet{--scale:1!important}
    @media(max-width:700px){nav{padding:0 14px;gap:14px;font-size:12px}nav img{width:90px}nav a.jump{display:none}main{padding:12px}.sheet{margin-bottom:12px}nav button{padding:8px}.download{padding:8px 10px}}
    @page{size:1600px 1000px;margin:0}@media print{html,body{background:none}nav{display:none}main{padding:0}.sheet{width:1600px!important;height:1000px!important;margin:0;box-shadow:none;break-after:page;page-break-after:always;scroll-margin:0}.sheet:last-child{break-after:auto;page-break-after:auto}.page{position:relative;transform:none!important}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}a{text-decoration:none}}
    '''
    html='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Aurevi · Identidade visual</title><style>'+css+'</style></head><body><nav>'+img(logo,alt='Aurevi')+'<a class="jump" href="#marca">Marca</a><a class="jump" href="#cores">Cores</a><a class="jump" href="#redes">Instagram</a><a class="jump" href="#mockups">Mockups</a><span class="grow"></span><button type="button" id="zoom" aria-pressed="false">Tamanho real</button><a class="download" href="Manual-Aurevi.pdf">Abrir PDF ↗</a></nav><main>'+''.join(pages)+'''</main><script>
    function resize(){document.documentElement.style.setProperty('--scale',Math.min(1,(innerWidth-(innerWidth<700?24:64))/1600))}resize();addEventListener('resize',resize);document.getElementById('zoom').onclick=function(){const real=document.body.classList.toggle('real');this.textContent=real?'Ajustar à tela':'Tamanho real';this.setAttribute('aria-pressed',real)};
    </script></body></html>'''
    (OUT/'COMECE-AQUI.html').write_text(html,encoding='utf-8')
    print(f'Manual local criado: {len(pages)} páginas.')

if __name__=='__main__':build()
