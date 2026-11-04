# Produção — Aurevi

Plano: `docs/superpowers/plans/2026-11-04-identidade-aurevi.md`.

## Decisões de execução

- Aprovação recebida em 04/11/2026 para produzir o kit conforme documento.
- Execução local nesta sessão. Pasta não é repositório Git; rotinas de worktree, commit e revisão de branch não se aplicam. Preservar pesquisa e documentos.
- Trata-se de produção gráfica reversível, sem aplicação de software em operação: verificar arquivos, medidas e qualidade visual, sem testes unitários que espelhem o script de desenho.
- PNG e PDF são documentos RGB de apresentação. Aplicações de embalagem incluem orientações de medida/sangria e dependem do fornecedor para homologação de impressão.
- Logo será em curvas; as artes terão SVG com textos editáveis e fontes incluídas, além de versões em curvas para portabilidade.

## Interfaces

1 → 2/3: cores/fontes e funções vetoriais; nomes de pastas fixados pelo plano. Sem conflitos.
2 → 3: artes e conteúdo locais, sem imagens de terceiros; manual usa caminhos relativos. Sem conflitos.
3 → 4: inventário registra apenas entregáveis; ZIP não inclui `pesquisa/` nem ferramentas internas. Sem conflitos.

## Estado

- Task 1: completa. 14 SVG/PNG de marca; fontes oficiais e licenças verificadas; logos em curvas.
- Task 2: completa. Nove posts, quatro stories, seis capas, sete artes de embalagem; versões em curvas e texto editável. Conteúdo em Markdown, HTML e PDF; editorial original com prompt.
- Task 3: completa. Manual de 21 páginas exportado, zero imagens ausentes, zero erros JavaScript e zero elementos de texto fora das páginas. Prévia geral criada.
- Task 4: completa. Revisão concluída; ajuste de legibilidade aplicado, 343/343 verificações passaram. ZIP de 138 arquivos criado, CRC e comparação de todos os arquivos com os originais passaram. Memória atualizada.

## Kittl

Usuário pediu explicitamente uso do Kittl para mockups. Servidor adicionado pelo comando oficial e usuário concluiu OAuth. Como o conjunto de ferramentas desta conversa não recarregou, uso pelo método oficial `mcpServer/tool/call` do Codex app-server, via cliente JSON-RPC local. Nenhuma credencial foi lida pelo script e nenhum turno de modelo/agente foi iniciado nesse transporte.

Quatro mockups finais criados em templates gratuitos: sacola 5853, ecobag 4868, tag clara 463 e cartão 1786. Posições finais com visibleRatio 1.0 nos quatro. Artes de origem e mockups salvos permanentemente na biblioteca Kittl, pasta “Aurevi - identidade visual”. Não houve consumo de créditos de geração, contratação ou mudança de plano. Links de edição em `ENTREGA/07-mockups-kittl/links.json`.

## Ajustes verificados

- Exportação de SVG corrigida para tratar documento SVG, que não possui `head` HTML. 40 PNG exportados sem erro.
- Foto do post editorial ajustada para preservar o rosto no enquadramento; original mantido.
- Tag e cartão Kittl tiveram escala e posição corrigidas por renderização determinística, sem redesenhar a arte. Originais foram promovidos à biblioteca antes de repetir o cartão para evitar referência temporária indisponível.

## Revisão independente final

Revisor encontrou um único item importante: aviso de IA pequeno no post 03 e story 02 e próximo da base do story. Verificação reproduziu os três aspectos antes da correção (340/343). Correção: aviso de 30 px nas duas artes; aviso do story em y1668, afastado 252 px da base; painel e títulos do story ajustados. Artes e PDF reexportados; 343/343 verificações finais passaram. Abertura offline e apresentação móvel passaram sem erros ou rolagem horizontal involuntária.

Nenhum crítico ou menor pendente. Os itens considerados e deixados fora pelo revisor foram avaliados: capas/lacre só com ícones são editáveis como vetores; PDF Type3 contém CharProcs; prévias internas antigas não integram a entrega; homologação gráfica/editor específico/catálogo/publicação continuam limites documentados; preferências estéticas pessoais não alteram o brief. Essas observações não deixaram entrega solicitada faltante.

O plugin Kittl nativo passou a aparecer durante a finalização. Nova consulta autenticada de times e biblioteca confirmou sete itens permanentes, incluindo os quatro mockups. Não houve necessidade de repetir login.
