# Pesquisa de referências — Aurevi

Data da inspeção: 04/11/2026, conforme fuso do cliente (America/Sao_Paulo).

## Como foi feita

Playwright 1.64.1, executado em Node.js com Chrome instalado, em modo headless, viewport de 1440×1100, idioma pt-BR. A segunda tentativa usou viewport de 1400×1000. Acesso público, sem login. Cada página recebeu captura e extração de texto, metadados, fontes computadas e endereços de imagens carregadas.

`inspecionar-referencias.cjs` contém a primeira inspeção. `baixar-evidencias.cjs` baixa uma amostra das imagens observadas. `reabrir-behance.cjs` registra a segunda tentativa solicitada pelo usuário e abre imagens originais no navegador.

O script usa o pacote Playwright do cache npm deste computador. Para executar em outro computador, instalar Playwright e ajustar o `require` para a instalação local; o usuário autorizou instalação se necessária. Os scripts são ferramentas de pesquisa, não dependências de um aplicativo Aurevi.

## Resultado por fonte

| Fonte | Resultado e alcance |
| --- | --- |
| https://www.instagram.com/use_aurevi/ | HTTP 200. Bio, avatar e uma publicação pública carregados. O Instagram mostra convite de login; a captura da página contém essa sobreposição. Avatar e post também foram inspecionados como imagens originais. |
| https://www.instagram.com/donna.oficial/ | HTTP 200. Bio, destaques e amostra inicial de posts. Mesmo limite de acesso sem login. Não foram analisados todos os vídeos, legendas ou carrosséis. |
| https://bio.lojadonnaoficial.com.br/ | HTTP 200. Página de links e atalhos comerciais carregada e capturada. |
| https://www.lojadonnaoficial.com.br/ | HTTP 200. Página inicial e imagens públicas carregadas e capturadas. A versão apresentada ao navegador difere do extrato recebido pela ferramenta de busca; a observação visual usa a captura do Playwright. |
| https://www.behance.net/gallery/208303969/Kanoa-Identidade-Visual | Página completa retorna 403, inclusive na nova tentativa com idioma explícito. Duas imagens originais obtidas e inspecionadas. Na segunda tentativa, imagem principal abriu no Playwright com HTTP 200. |
| https://www.behance.net/gallery/175647547/Identidade-Visual-Loja-de-Roupa-Vestuario | Página completa retorna 403 nas tentativas. Texto do autor disponível na busca; imagem original das tags abriu no Playwright com HTTP 200. Projeto corresponde a Madu Moda Feminina, de Junior Fergom. |
| https://www.behance.net/gallery/137758259/Margot-luxe-streetwear-for-women-Branding-project | Página completa bloqueada; imagem original de cartões e fotografia abriu no Playwright com HTTP 200. Texto do autor consultado pela busca. Projeto de APUCHADES. |

## Evidências

- Primeira tentativa: arquivos `*-instagram.json`, `donna-bio.json`, `donna-loja.json`, `*-behance.json` e capturas com os mesmos nomes.
- Segunda tentativa: `segunda-tentativa.json` e `*-imagem-no-playwright.png`.
- Imagens observadas: `aurevi-instagram-post-1.jpg`, avatars, três posts da Donna, `kanoa-letras.png`, `kanoa-sacola.png`, `kanoa-referencia.jpg`, `madu-referencia.jpg` e `margot-referencia.jpg`. A extensão `.jpg` de alguns arquivos é apenas o nome de arquivo; o corpo original da imagem foi preservado sem conversão e pode ser PNG/WebP.
- `resultado.json` consolida a saída original. URLs de CDN do Instagram são temporárias e podem expirar. JSON guarda dados públicos da inspeção, não sessão autenticada.

As imagens de terceiros são referências internas. Não fazem parte das peças comerciais da Aurevi nem são banco de fotos licenciado para a marca. Não reproduzir marcas, desenhos de letras, padrões ou textos das referências.

## Leitura criativa

O post observado da Aurevi combina tecido acetinado creme, serifas finas e espaçamento amplo. A proposta escolhida preserva cuidado visual, acrescentando letras mais firmes e presença de cor para sustentar bom gosto cotidiano.

A Donna demonstra clareza comercial: peças em modelos, novidades, destaques e vários caminhos de atendimento/compra. A Aurevi pode adotar essa clareza usando seus próprios canais, produtos e benefícios comprovados.

As imagens de Kanoa mostram contraste entre letras de desenho particular, cor e fotografia; as da Madu mostram consistência entre identidade e embalagem; a da Margot mostra composição limpa e fotografia natural. Essas são interpretações de design a partir da amostra observada, não declarações dos autores sobre a Aurevi.

## Pesquisa de tipografia

Verificados diretamente em 04/11/2026 os metadados e textos de licença oficiais:

- https://raw.githubusercontent.com/google/fonts/main/ofl/fraunces/METADATA.pb — HTTP 200; Fraunces, categoria serif; fonte variável e versão itálica.
- https://raw.githubusercontent.com/google/fonts/main/ofl/fraunces/OFL.txt — HTTP 200; SIL Open Font License 1.1.
- https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/METADATA.pb — HTTP 200; Manrope, categoria sans-serif; fonte variável.
- https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/OFL.txt — HTTP 200; SIL Open Font License 1.1.

Licenças permitem o uso em documentos e o compartilhamento da fonte sob seus termos. A entrega deverá acompanhar os arquivos originais de licença. O documento de proposta não afirma disponibilidade dessas famílias em todas as versões do Canva ou de aplicativos de terceiros.

## Limites

Contadores e benefícios comerciais mudam e não foram usados para deduzir resultados financeiros, público comprador ou desempenho da concorrente. A pesquisa não comprova exclusividade de nome/símbolo, disponibilidade de domínio ou registro de marca.
