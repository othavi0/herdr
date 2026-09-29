Esta issue registra onde está a proposta da tradução pt-BR para o `herdrdev/herdr` e o que fazer quando o mantenedor responder. Um agente que receber "verifica se foi aprovado" consegue seguir daqui sem outro contexto.

## Estado em 2026-09-29

- A proposta está em https://github.com/herdrdev/herdr/discussions/4753, na categoria Ideas, aberta pela conta `othavi0`.
- A tradução está pronta em duas branches deste fork:
  - `docs/pt-br` tem a versão do fork, com os READMEs da raiz. É o PR #4.
  - `docs/pt-br-upstream` é a versão para o upstream. Ela parte do `master` do `herdrdev/herdr` em `dbe3a236` e tem dois commits em inglês, `416a226e docs: add brazilian portuguese website docs` e `32237f7c docs: add brazilian portuguese readme`. Ela mexe só em `docs/next/` e nos scripts, e as 5 páginas que mudaram no inglês até `dbe3a236` já estão sincronizadas.
- As ferramentas (guia de estilo, checker, corretor de âncoras, protótipo e rascunhos) estão na branch `tools/pt-br-translation`, em `tools/pt-br/`. O `tools/pt-br/README.md` explica cada arquivo.

## O que estamos esperando

1. **A resposta do mantenedor na Discussion herdrdev/herdr#4753.** O `CONTRIBUTING.md` do upstream exige discussão e aprovação antes de mudanças maiores. O precedente é a Discussion herdrdev/herdr#1976 do README em chinês, que recebeu "good idea, please open a pr for it!" do `ogulcancelik` antes do PR herdrdev/herdr#1990.
2. **A lista de contribuidores aprovados.** A conta aparece como `othavioquiliao` em `.github/APPROVED_CONTRIBUTORS`, porque esse era o nome dela quando o PR herdrdev/herdr#25 foi mesclado. O nome atual é `othavi0`. O workflow `.github/workflows/pr-gate.yml` compara o login do autor do PR com a lista e fecha na hora o PR de quem não está nela. A Discussion avisa a troca de nome no fim.

## Como verificar

```bash
gh api graphql -f query='{repository(owner:"herdrdev",name:"herdr"){discussion(number:4753){closed answer{body} comments(first:20){nodes{author{login} body createdAt}}}}}'
gh api repos/herdrdev/herdr/contents/.github/APPROVED_CONTRIBUTORS --jq .content | base64 -d | grep -in 'othavi'
cat .github/MAINTAINERS
```

Só conta como aprovação um comentário de alguém listado em `.github/MAINTAINERS` do upstream.

## O que fazer em cada caso

- **Aprovado e `othavi0` na lista.** Siga "Abrir o PR" abaixo.
- **Aprovado, mas a lista ainda tem só `othavioquiliao`.** Não abra o PR, porque o gate fecha na hora. Avise o Othavio e mostre o texto de uma resposta curta na Discussion lembrando a troca de nome.
- **O mantenedor pediu mudanças.** Resuma o pedido para o Othavio e proponha o ajuste antes de mexer na branch.
- **Recusado ou fechado.** Avise o Othavio. Não insista em outra Discussion nem abra PR.
- **Sem resposta.** Informe a data do último comentário e não faça nada.

## Abrir o PR (só depois da aprovação)

1. Atualize `docs/pt-br-upstream` com o `master` do upstream (`git fetch https://github.com/herdrdev/herdr.git master` e rebase).
2. Se as páginas em inglês mudaram desde `dbe3a236`, sincronize o pt-br. O passo a passo está em `tools/pt-br/README.md`, na seção "Atualizar o pt-br depois de mudanças no inglês".
3. Deixe as ferramentas à mão com `git worktree add ../pt-br-tooling origin/tools/pt-br-translation`. Depois rode e zere:

   ```bash
   python3 ../pt-br-tooling/tools/pt-br/locale_check.py --docs-root docs/next/website/src/content/docs --locale pt-br --inline-code
   python3 scripts/docs_translation_parity.py --docs-root docs/next/website/src/content/docs
   python3 -m unittest scripts.test_docs_translation_parity scripts.test_release
   bun test scripts/docs/
   ```

4. Mostre ao Othavio o corpo do PR que está em `../pt-br-tooling/tools/pt-br/upstream-rascunhos.md`, com o número da Discussion preenchido, e espere o ok dele.
5. Abra o PR com `gh pr create --repo herdrdev/herdr --base master --head othavi0:docs/pt-br-upstream --title "docs: add brazilian portuguese docs and readme"`.

## Regras que não mudam

- Nada é publicado no `herdrdev/herdr` sem o ok do Othavio no texto final.
- Commits para o upstream em inglês, minúsculos, sem `fixes`, `closes` ou `resolves`.
- Não editar o `README.md` da raiz, o `CHANGELOG.md`, `docs/versions/` nem `docs/preview/` no upstream. O release promove os READMEs de `docs/next/`.

## Handoff: o que já sabemos

Esta seção junta o contexto da sessão de 2026-09-29, para quem pegar esta issue não precisar redescobrir nada.

### Como o upstream traduz a documentação

- O site tem dois idiomas além do inglês, em `docs/next/website/src/content/docs/ja/` e `zh-cn/`. As 22 páginas de cada um têm o mesmo nome de arquivo do inglês, e só `title` e `description` do frontmatter são traduzidos.
- O mantenedor, Ogulcan Celik (`ogulcancelik`), criou o japonês e o chinês do site num commit só, o `d36a6ded` de 2026-07-06. O template `.github/ISSUE_TEMPLATE/translation.yml` diz que essas traduções são "LLM-generated from the English source".
- Não existe script que traduza sozinho. Quem muda uma página em inglês atualiza as traduções no mesmo commit. O `scripts/docs_translation_parity.py` só confere se os arquivos existem e se a sequência de títulos bate com o inglês, sem olhar o texto. Por isso muitos commits mudam o inglês e deixam a tradução para trás sem o CI perceber.
- O README em chinês (`README.zh-CN.md`) veio depois, de um contribuidor externo aprovado, pela Discussion herdrdev/herdr#1976 e pelo PR herdrdev/herdr#1990. O japonês não tem README. A tradução pt-BR segue o chinês, com site e README.
- O site é renderizado num repositório privado. Registrar o locale `pt-br` no Starlight é trabalho do mantenedor, e a Discussion avisa isso.
- Outras propostas de idioma estão sem resposta do mantenedor desde julho e agosto: coreano (herdrdev/herdr#1450), francês (herdrdev/herdr#2725) e zh-TW (herdrdev/herdr#2362). Também está sem resposta a herdrdev/herdr#4210, sobre português, que parece um rascunho de outra pessoa publicado por engano.

### O que a tradução pt-BR inclui

- As 22 páginas em `pt-br/`, com links em `/pt-br/docs/<pagina>/` e âncoras apontando para os títulos traduzidos.
- `pt-br` em `DEFAULT_LOCALES` do script de paridade, nos testes dele e nos dois laços de `release-docs-check` do `justfile`.
- A opção "Português do Brasil" em `translation.yml` e a pasta `pt-br` citada na auditoria de pré-release (`.agents/skills/herdr-pre-release-audit/references/pre-release-audit.md`).
- `docs/next/README.pt-BR.md` e o link `Português` no seletor de idioma de `docs/next/README.md` e `docs/next/README.zh-CN.md`.
- O README entra na promoção do release nos mesmos pontos que o `README.zh-CN.md`: `scripts/docs/versions.mjs` com o teste de integração, `scripts/release.py`, o `test -f` do `justfile` e o `release.yml`.

### Como a tradução foi feita

- **Rodada 0, tradução.** Quatro agentes traduziram do inglês, cada um com um lote de arquivos, seguindo `tools/pt-br/pt-br-guia.md`.
- **Rodada 1, estilo.** Os revisores aplicaram as skills `humanize-pt-br` e `unslop`.
- **Rodada 2, fidelidade.** Os revisores compararam cada parágrafo com o inglês e corrigiram 33 trechos com fato faltando, sobrando ou trocado.
- O README passou por tradução e por uma revisão de fidelidade e estilo.
- O `locale_check.py` confere blocos de código, código inline, imports, links e âncoras. Os slugs dele batem com os ids que o Starlight gera: conferi 199 títulos pt-br num build local.

### Decisões já tomadas pelo Othavio

- Só pt-BR, sem pt-PT.
- O modelo é o chinês simplificado: site e README.
- Na Discussion, entrou o aviso da conta renomeada e não entrou a frase de divulgação de IA.
- O texto da Discussion segue `~/Projects/x-posts/voice.md`, o tom de dev sênior cansado mas feliz de ajudar. Prosa em inglês no nome dele segue esse arquivo.
- Para o upstream, os commits são em inglês e só `docs/next/` muda. No fork (PR #4), os commits são em português e os READMEs da raiz também mudam.

### Armadilhas

- **Conta renomeada.** O merge do PR herdrdev/herdr#25 diz "from othavioquiliao/...", e hoje o GitHub mostra o PR como sendo de `othavi0`. O `pr-gate.yml` compara `pr.user.login` em minúsculas com a lista, então só o mantenedor resolve isso atualizando a lista. O CONTRIBUTING proíbe pedir para entrar na lista. A Discussion só informa a troca de nome.
- **CI do fork.** O check `validate` falha no fork porque ele não tem as tags de release (`v0.9.1`). Com as tags do upstream buscadas localmente, `node scripts/docs/versions.mjs check` passa.
- **Ferramentas faltando na máquina.** `just` não está instalado. Os laços de `release-docs-check` rodam direto no bash. `bun test scripts/release-workflows.test.ts` tem 1 falha que já existia antes da tradução, porque o teste chama o `just`.
- **Desvio do inglês.** Entre a base da tradução (`fc86d866`) e `dbe3a236`, o upstream mudou 5 páginas em inglês: `agents`, `configuration`, `integrations`, `socket-api` e `add-herdr-support`. Elas já foram sincronizadas. Antes do PR, confira de novo com `git diff dbe3a236 <novo master> -- 'docs/next/website/src/content/docs/*.mdx'`, excluindo as pastas de idioma.
- **Referências no fork.** Aqui `#N` aponta para o fork. Para citar o upstream, escreva `herdrdev/herdr#N`.
