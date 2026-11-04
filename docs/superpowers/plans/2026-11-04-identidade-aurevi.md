# Aurevi — plano de produção da identidade

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** produzir o kit de identidade aprovado, pronto para revisão e uso local.

**Architecture:** arte vetorial e conteúdo gerados de fontes locais, com SVG em curvas para logos e PNG exportado pelo Chrome/Playwright. Manual HTML local com PDF, arquivos de fontes com licenças e pacote ZIP portável.

**Tech Stack:** Python/fontTools para vetores tipográficos; SVG; HTML/CSS; Node/Playwright para exportação e inspeção; geração de imagem pelo recurso integrado.

**Spec:** `docs/direcao-criativa.md`, aprovado explicitamente pelo usuário em 04/11/2026.

## Global Constraints

- Linha estilosa e de bom gosto, sem posicionamento de luxo.
- Creme `#F4EFE6`, verde `#203C32`, coral `#E98673`, areia `#D9CCBA`, tinta `#242824`.
- Logo em minúsculas, Fraunces + Manrope, assinatura “Seu jeito, bem vestido.”
- Nove posts 1080×1350; quatro stories 1080×1920; seis capas 1080×1080.
- Não inventar catálogo, preços, estoque, benefícios, depoimentos, canais ou localização.
- Não publicar externamente. Referências de terceiros fora do kit comercial.

## Review Focus

- SVG do logo deve abrir sem fontes instaladas: verificar ausência de elementos text/font externos.
- PNG transparente deve preservar alpha: conferir canal e dimensões com Pillow.
- Templates com foto/dados pendentes devem ser claramente identificados no inventário e na apresentação.
- PDF e manual local devem carregar todas as fontes e imagens sem internet: abrir em contexto offline.
- Texto não pode vazar das artes: inspecionar contatos, miniaturas e páginas renderizadas em Playwright.

### Task 1: Marca e arquivos base

**Files:** `scripts/gerar_identidade.py`, `ENTREGA/01-logos/`, `ENTREGA/06-fontes/`, `ENTREGA/cores.json`.

**Interfaces:** produz SVG autocontidos e fontes locais para todos os demais materiais.

- [x] Baixar Fraunces e Manrope e suas licenças oficiais; conferir integridade.
- [x] Criar wordmark em curvas com espaçamento ajustado, símbolo AV autoral, variantes e avatar.
- [x] Conferir contraste, caixa do desenho e legibilidade em redução.

### Task 2: Artes e conteúdo

**Files:** `scripts/gerar_artes.py`, `ENTREGA/02-redes/`, `ENTREGA/03-embalagens/`, `ENTREGA/04-conteudo/`, `ENTREGA/05-editorial/`.

**Interfaces:** consome vetores/fontes/cores; produz artes SVG autocontidas com texto em curvas e conteúdo Markdown/CSV.

- [x] Criar imagem editorial conceitual pelo recurso integrado e salvar no projeto com prompt e atribuição de natureza conceitual.
- [x] Compor nove posts, quatro stories, seis capas e aplicações de tag, cartão, adesivo e sacola.
- [x] Escrever legendas, roteiros, bio, calendário de quatro semanas, ideias para loja e instruções de adaptação.
- [x] Distinguir peças prontas de apresentação de marca, editoriais e templates dependentes de catálogo real.

### Task 3: Manual e exportações

**Files:** `scripts/gerar_manual.py`, `scripts/exportar.cjs`, `ENTREGA/COMECE-AQUI.html`, `ENTREGA/Manual-Aurevi.pdf`, `ENTREGA/LEIA-ME.md`, `ENTREGA/inventario.json`.

**Interfaces:** consome SVG e conteúdo; produz apresentação local, PDF, PNG, contato visual e inventário.

- [x] Compor manual visual com usos, reduções, tipografia, paleta, fotografia, feed e aplicações.
- [x] Exportar PNG nas dimensões corretas e PDF com recursos locais.
- [x] Inspecionar manual, contato das artes e exemplos em alta resolução no Playwright.
- [x] Conferir SVG, alpha, dimensões, contagens, links locais e carregamento offline.

### Task 4: Revisão e entrega

**Files:** `ENTREGA/VERIFICACAO.md`, `Aurevi-Kit-Identidade.zip`, `MEMORIA_COMPARTILHADA.md`.

- [x] Pedir revisão independente do pacote contra especificação; corrigir problemas materiais.
- [x] Gerar ZIP apenas com entregáveis e licenças, sem pesquisa de terceiros.
- [x] Atualizar memória com decisões, comandos de reprodução, evidências e limites.
- [x] Entregar links diretos para manual, prévia e ZIP. Sem publicação ou commit (pasta sem Git).

Execução no próprio fluxo desta sessão, conforme autorização para produzir o kit; não há novo ponto de aprovação para decisões rotineiras.
