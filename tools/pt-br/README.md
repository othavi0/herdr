# Ferramentas da tradução pt-BR

Esta branch guarda o que foi usado para traduzir a documentação do Herdr para português brasileiro. Ela não vai para o upstream. A tradução em si está em `docs/pt-br` (PR #4 do fork) e em `docs/pt-br-upstream` (a versão pronta para o PR no `herdrdev/herdr`).

## Arquivos

- `pt-br-guia.md` é o contrato de estilo: glossário, termos unificados, o que não se traduz, links e âncoras.
- `locale_check.py` compara cada página traduzida com o inglês: chaves do frontmatter, imports, blocos de código, destinos de link e âncoras. Com `--inline-code`, também avisa quando o código inline diverge.
- `fix_anchors.py` troca âncoras em inglês pelos slugs dos títulos traduzidos. Pode rodar de novo sem efeito colateral.
- `rename_heading.py` renomeia um título pt-br e atualiza todo link que aponta para ele.
- `brief-r0.md`, `brief-r1.md` e `brief-r2.md` são os prompts das três rodadas (tradução, estilo, fidelidade).
- `r0-relatorios.md`, `r1-relatorios.md` e `r2-relatorios.md` resumem o que cada rodada mudou.
- `discussion-body.md` é o texto publicado em https://github.com/herdrdev/herdr/discussions/4753.
- `upstream-rascunhos.md` tem o corpo do PR para o upstream e as mensagens de commit em inglês.
- `preview-site/` monta um Starlight local com os quatro idiomas para ver as páginas renderizadas.

## Checar uma branch

```bash
python3 tools/pt-br/locale_check.py --docs-root <checkout>/docs/next/website/src/content/docs --locale pt-br --inline-code
python3 <checkout>/scripts/docs_translation_parity.py --docs-root <checkout>/docs/next/website/src/content/docs
```

Os dois saem com código 0 quando a tradução está alinhada com o inglês.

## Atualizar o pt-br depois de mudanças no inglês

1. Gere o diff do inglês desde a última sincronização: `git diff <base> <novo> -- docs/next/website/src/content/docs/*.mdx`.
2. Aplique cada hunk na página pt-br correspondente, seguindo `pt-br-guia.md`.
3. Rode `fix_anchors.py` e os dois checks acima até zerarem.

## Ver renderizado

```bash
cd tools/pt-br/preview-site
npm install
./sync.sh <checkout>
npx astro dev --port 4381
```

Abra `http://localhost:4381/pt-br/docs/`.
