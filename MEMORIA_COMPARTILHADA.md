# Aurevi — memória do projeto

Atualizada em 04/11/2026.

## Direção atual — feedback posterior prevalece

**Fotografia mais recente — prova realista:** usuário enviou outra modelo, de conjunto marrom diante de porta de madeira, e pediu o vestido escuro preservando ao máximo pose/aparência e com mais realismo. Edição concluída pelo recurso integrado em `FOTOGRAFIAS/03-prova-vestido-realista.png`: mesma pose com mão na cintura, rosto/cabelo aproximados da referência, quarto e sandálias preservados; vestido longo escuro com recorte e drapeado. Prompt em arquivo homônimo `-prompt.txt`. Conferida visualmente e cópia SHA-256 verificada. A foto anterior, com modelo de cabelos pretos no estúdio e AV Entrelaço, foi preservada em `FOTOGRAFIAS/02-estudio-modelo-cabelos-pretos.png` com prompt.

**Autorização de Git renovada para fotografias:** usuário primeiro informou que Claude cuidaria do commit; Codex interrompeu ações de Git. Depois pediu explicitamente, ao concluir a imagem, salvar em FOTOGRAFIAS e fazer commit/push. Remoto e main já estabelecidos por Claude (HEAD consultado 3e85820). Fazer commit desta etapa de fotografias e memória, preservando alterações/index de outros trabalhos, especialmente cache graft. Não presumir que GitHub foi atualizado antes de verificar o push.

**Referência mais recente — AV fluido e novo vermelho:** usuário enviou monograma dourado com duas diagonais e uma curva caligráfica sobre vermelho, pedindo esse estilo com A e V. Produzidos três refinamentos vetoriais em `REFINAMENTO-AV-FLUIDO/`: Encontro, Entrelaço e Ascensão. Em seguida enviou referência de vermelho quente e quase preto. Nova aproximação plana **#350403**, com luz #4A100B e sombra #210000 nas apresentações; não afirmar extração exata do anexo. Aplicada aos novos refinamentos, sem recolorir entregas históricas. SVGs/PNGs transparentes, composições, comparativo e PDF; gerador `scripts/av_fluido.py`. Ainda são estudos aguardando retorno.

**GitHub:** usuário autorizou explicitamente subir toda a pasta em `https://github.com/MTsGaldino-DEV/aurevi-branding.git`. Remoto inicialmente vazio; Git local inicializado em main e origin configurado. Em 04/11/2026 o usuário confirmou que não há dado sensível e pediu para subir tudo: `.gitignore` agora exclui apenas `__pycache__`/`*.pyc`; logs e JSONs de upload do Kittl e as extensões `.pyd` de `.tools/python` (antes excluídas por engano pela regra `*.py[cod]`) passaram a ser versionados; todos os entregáveis, fontes, pesquisas, scripts, dependências locais e históricos entram no repositório. Envio deve incluir os refinamentos e a cor mais recente; confirmar push e HEAD remoto antes de declarar concluído.

**Nova prioridade — remodelar a logo:** depois de aprovar a energia e os mockups, o usuário apontou que precisa de uma logo semelhante na linguagem, mas original, e pediu três modelos. Produzidos em `ESTUDOS-LOGO-AUTORAL/`: 01 Presença (serifas, corte ascendente no A), 02 Enlace (curvas, terminais suaves e gesto no A/R), 03 Vértice (sem serifa tradicional, cortes diagonais e AV escultural). Seis letras de cada escrita e três monogramas foram desenhados em caminhos próprios no script `scripts/logos_autorais.py`, sem glifos de fonte como logo; Manrope/Cormorant só nas legendas da prancha. Cada opção tem conjunto, AV e escrita em metálico, sangue e marfim, SVG/PNG transparente, além de apresentação. Comparativo SVG/PNG/PDF e ZIP `Aurevi-3-Logotipos-Autorais.zip`. Comparação mantém materiais e cores iguais. Aguardar preferência para refinar e aplicar ao kit; kit anterior preservado, não tratar aquela logo como decisão final do cliente.

**Kit completo — elegante e ousada (mais recente):** usuário aprovou a energia da foto de estúdio e pediu refazer a identidade nessa energia; esclareceu “elegante, mas ousado”, pediu logo dourada metálica e disse que os mockups estão perfeitos. Nova entrega em `IDENTIDADE-ELEGANTE-OUSADA/`, sem sobrescrever versões anteriores. Kit consolida AV01 curvo + escrita02 Cormorant com gesto no R como base desta aplicação. Paleta #450A10, #CFB77F, cinza mineral #9B9995, marfim #FAF6EF e grafite #242424. Tipografia Cormorant Garamond e Manrope; fontes OFL incluídas. Frase de campanha proposta: “Vista sua presença.”

Inclui manual/apresentação com 18 páginas (`Manual-Aurevi-Elegante-Ousada.pdf` e `APRESENTACAO.html`), visão geral PNG, 20 logos SVG/PNG (quatro composições × cinco acabamentos, incluindo dourado metálico transparente), nove posts, quatro stories, seis destaques, dois avatares, oito aplicações de embalagem/papelaria e três máscaras de hot stamping. Quinze SVGs com textos editáveis, PDFs físicos e guia de uso/conteúdo/fotografia/loja. Foto de estúdio aprovada e novo mockup de sacola/caixa/tag vermelho-ouro gerado pelo recurso integrado; dois mockups Kittl anteriores compatíveis reunidos com links e origem preservados. Prompts das imagens incluídos. Imagens conceituais identificadas; templates têm campos a preencher com dados reais.

Produção em `scripts/identidade_ousada.py`; exportação `scripts/ousada_exportar.cjs`; verificação/pacote `scripts/ousada_verificar.py --zip`. SVGs mestre em curvas; variante metálica preserva geometria e aplica gradiente/reflexo e relevo discreto. Cor plana/metal são arquivos distintos; máscaras físicas separadas. Conjunto de 52 artes, 250 checagens de dimensões/transparência/PDF/fontes/limites/contraste; Playwright offline sem imagens/fontes ausentes, erro ou overflow. Revisão visual corrigiu enquadramentos na capa, visão geral, story02 e página15, além do rodapé da grade do feed. Pacote final `Aurevi-Identidade-Elegante-Ousada.zip`. Nenhuma publicação ou mudança em contas. Próximo retorno é sobre o kit consolidado; não voltar à primeira direção verde/coral.

**Fotografia de estúdio:** usuário disse que a direção escura está bacana e pediu avançar para fotos. Solicitou modelo com vestido escuro em frente ao balcão, parede cinza de cimento e logo Aurevi atrás, em dourado polido com reflexos platinados, relevo 3D e leve desfoque. Três novas referências orientaram acabamento, parede e espessura do letreiro; modelo/vestido e arte AV01 + escrita02 vieram dos arquivos atuais. Gerada e conferida visualmente pelo recurso integrado: `FOTOGRAFIAS/01-estudio-cinza-logo-dourada.png` (vertical 1024×1536). Vestido inteiro visível, balcão atrás, AV e AUREVI dourados na parede cinza. Prompt exato em `FOTOGRAFIAS/01-estudio-cinza-prompt.txt`. Foto conceitual com modelo fictícia; originais e apresentações preservados. Aguardando retorno sobre essa fotografia; a aprovação da cor não equivale a escolha final entre todos os estudos de logo.

**Revisão mais recente de cor:** o cliente considerou #681E36 claro e pediu vermelho mais escuro, “cor de sangue”, depois pediu nova tentativa. Nova base proposta **#450A10**, com menos componente arroxeado; ouro #CFB77F e marfim #FAF6EF mantidos. Arquivos atuais em `DIRECAO-VERMELHO-ESCURO/`, PDF `Apresentacao-Aurevi-Vermelho-Escuro.pdf`. Vestido editado novamente pelo recurso integrado, escurecendo apenas a roupa; mockups Kittl regenerados e salvos. Sete páginas conferidas no Playwright offline, sem imagem/fonte ausente, erro, texto fora da página ou overflow móvel. Versões anteriores preservadas. Ainda aguarda escolha de escrita/AV; não afirmar aprovação final dessas opções.

O usuário rejeitou a leitura natural/ecológica da primeira entrega: foto de camisa/linho, kraft/ecobag e escrita minúscula Fraunces. Gostou da separação AV, mas pediu mais charme na escrita. Referências novas: Lunare para serifas/caixa alta; Jovana para bordô e dourado; AV com diagonais separadas e terminais curvos; depois símbolo abstrato de linhas finas/curvas em tecido.

Definiu **Aure = ouro; Vi = vida**. Estilo de roupa deve seguir Donna. Nova pesquisa com Playwright abriu Instagram e catálogo, com 12 imagens do feed e amostra de produtos. Vestidos com drapeado/renda/recortes, conjuntos produzidos e jeans/polo convivem; campanha vermelha de Natal não foi confundida com paleta fixa. Evidências em `pesquisa/revisao-02/`.

Usuário forneceu vestido marrom ajustado com drapeado lateral e fenda, autorizou outra modelo/fundo e depois pediu vestido na cor bordô para apresentação às sócias. Estudo gerado pelo recurso integrado e recolorido para bordô, com modelo fictícia e fundo liso. Arquivos/propmts em `DIRECAO-BORDO/editorial/`.

**Entrega de estudos atual:** `DIRECAO-BORDO/Apresentacao-Aurevi-Bordo.pdf` (sete páginas), `DIRECAO-BORDO/APRESENTACAO.html`, sete páginas PNG, dois monogramas AV (curvo e abstrato), três escritas em caixa alta, paleta, tag e dois novos mockups Kittl. ZIP: `Aurevi-Estudos-Bordo.zip`, 62 arquivos, ~15,5 MB, CRC passou. 45 checagens de arquivo passaram; Playwright offline sem falta de imagem/fonte, overflow ou erro JS. Estudo anterior `REVISAO-02/` foi intermediário com azul e alternativas; a apresentação bordô é a versão atual.

Paleta digital proposta: bordô #681E36, ouro champagne #CFB77F, marfim #FAF6EF. Códigos são aproximações da intenção da referência, não medição exata de fotografia/tecido.

Escritas em estudo: 01 Bodoni Moda (contraste alto), 02 Cormorant Garamond com gesto no R (recomendação), 03 Italiana (alongada). Fontes OFL e licenças incluídas. AV01 mantém iniciais reconhecíveis com contraste e curvas; AV02 é mais abstrato/monoline. Ainda não há escolha final do usuário/sócias entre os estudos. Não reaplicar silenciosamente a direção original aos próximos materiais e não dizer que o novo kit inteiro já foi atualizado.

Novos mockups Kittl: templates 9752/18518, sacolas claras de loja, sem kraft/ecobag. Aplicados com escrita02 bordô, visibleRatio1.0; salvos na pasta **Aurevi - estudos 02**, junto dos estudos intermediários. Plugin nativo disponível e autenticado; não repetir setup/login. Links de edição em `DIRECAO-BORDO/mockups/links.json`. Não há postagem, mensagem ou compra.

Próxima etapa: o usuário pode escolher escrita/AV e pedir refinamento; então aplicar a direção escolhida no kit e posts. Manter ENTREGA/ e ZIP inicial preservados para histórico.

## Pedido

Criar identidade completa de marca de roupas femininas Aurevi: logo, tipografia, cores, posts e ideias para loja. Usuário pediu Playwright para pesquisar @use_aurevi, @donna.oficial, bio e loja Donna e três projetos Behance.

## Definições do usuário

- Linha estilosa e de bom gosto, sem posicionamento de luxo.
- Direção escolhida explicitamente: “Essencial com personalidade — creme, verde profundo e coral”.
- Público ainda não definido; não inventar faixa etária, renda ou benefícios.
- Pediu nova tentativa de abrir referências após bloqueios.
- Aprovou explicitamente produzir o kit conforme `docs/direcao-criativa.md`, incluindo minúsculas, Fraunces + Manrope e “Seu jeito, bem vestido.”.
- Pediu uso do Kittl para mockups e concluiu o login OAuth. Depois pediu reconexão; confirmada.

## Estado

Pasta começou vazia e não é repositório Git. Instruções aplicáveis em `C:/APPWEB/AGENTS.md`; memória geral foi lida. Sem publicação ou mudanças nas contas.

Playwright 1.64.1 disponível pelo cache npm, Chrome instalado. Pesquisa e scripts em `pesquisa/`. Ambos os perfis Instagram e sites Donna abriram; Instagram sem login tem amostra limitada e modal de entrada. Imagens públicas foram baixadas para inspeção. Não reutilizar referências nas artes comerciais.

Páginas completas Behance retornaram 403 nas duas tentativas; imagens originais de Kanoa, Madu e Margot foram abertas no Playwright com HTTP 200 e inspecionadas. Dados da segunda tentativa em `pesquisa/segunda-tentativa.json`. Complemento textual obtido pela busca web.

Detalhamento em `docs/direcao-criativa.md` aprovado e implementado. Kit concluído em `ENTREGA/`; pacote `Aurevi-Kit-Identidade.zip`, 138 arquivos, 61.599.618 bytes. ZIP conferido por CRC e comparação SHA-256 de todos os arquivos contra os originais. Detalhes em `docs/pacote-final.json`.

Licenças Fraunces e Manrope verificadas nos arquivos oficiais Google Fonts: ambas SIL OFL 1.1. Contraste verde/creme 10,45:1 e verde/coral 4,63:1; creme/coral 2,26:1, inadequado para informação essencial. Relatório completo em `pesquisa/LEIA-ME.md`.

## Continuação

Entregues: manual HTML/PDF com 21 páginas; prévia geral PNG; 14 artes de marca em SVG/PNG; nove posts, quatro stories, seis capas; sete artes de embalagem, cinco PDFs físicos; 26 versões SVG com texto editável; guias de conteúdo e ideias de loja em MD/HTML/PDF; fontes com licenças; editorial conceitual original e prompt; quatro mockups Kittl; inventários CSV/JSON e registro de verificação.

Arquivos principais: `ENTREGA/COMECE-AQUI.html`, `ENTREGA/Manual-Aurevi.pdf`, `ENTREGA/Visao-geral-Aurevi.png`, `Aurevi-Kit-Identidade.zip`.

Identidade: creme #F4EFE6, verde #203C32, coral #E98673, areia #D9CCBA, tinta #242824. Logo tipográfico em curvas, base Fraunces peso 520, SOFT12/WONK0/opsz72; símbolo AV autoral. Logos não dependem de fontes instaladas. Textos editáveis requerem editor compatível; não são arquivos nativos de Canva/Adobe.

Kittl: conexão global adicionada com `codex mcp add kittl --url https://mcp.kittl.com/mcp`, usuário concluiu OAuth. Uso inicial via API oficial Codex app-server sem ler credenciais nem iniciar modelo; depois plugin nativo apareceu. Consulta nativa confirmou sete itens permanentes na pasta **Aurevi - identidade visual**, três artes de origem e quatro mockups. Templates gratuitos: sacola5853, ecobag4868, tag463, cartão1786. Todos com visibleRatio1.0. Links em `ENTREGA/07-mockups-kittl/links.json`. Nenhum crédito de geração foi consumido pelas renderizações determinísticas. Não refazer login ou criar pastas duplicadas.

Verificações finais: `python scripts/verificar.py` →343/343; `node scripts/verificar_navegador.cjs` →21páginas offline, fontes/imagens presentes, zero requisições externas, sem overflow em1440/390px, zoom funcional e texto editável carregando fonte. Revisão independente: um aviso IA pequeno foi reproduzido e corrigido (30px; story y1668); sem achados materiais pendentes. Registro em `ENTREGA/VERIFICACAO.md` e `docs/producao.md`.

Para reproduzir: fontes `scripts/preparar_fontes.py`; marca `scripts/gerar_identidade.py`; artes `scripts/gerar_artes.py`; PNG `scripts/exportar.cjs`; guias `scripts/conteudo_html.py` e `scripts/exportar_conteudo.cjs`; manual `scripts/gerar_manual.py` e `scripts/exportar_manual.cjs`; inventário `scripts/inventariar.py`; verificação; ZIP `scripts/empacotar.py`. Dependências Python locais em `.tools/python`. Ferramentas internas e pesquisa fora do ZIP.

Nenhuma publicação, mensagem enviada, commit, alteração de plano ou compra. Não é pedido de e-commerce. Templates precisam de catálogo/fotos/dados comerciais reais; impressão depende de fornecedor e prova. Personalizações futuras podem incorporar esses dados sem recriar o sistema base. Preservar os arquivos e autoria compartilhada.
