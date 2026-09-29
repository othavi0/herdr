# Guia de tradução pt-BR da documentação do Herdr

Este guia é o contrato de todo agente que traduz ou revisa `docs/next/website/src/content/docs/pt-br/*.mdx`. Não edite este arquivo.

## Fonte e alvo

- A fonte é sempre o inglês em `docs/next/website/src/content/docs/<pagina>.mdx`. O japonês (`ja/`) serve só para ver a estrutura de uma página traduzida, nunca como fonte de texto.
- O alvo é `docs/next/website/src/content/docs/pt-br/<pagina>.mdx`, com o mesmo nome de arquivo.
- Não acrescente nem remova conteúdo. Todo fato, número, flag, nome e exemplo vem do inglês. Nada de nota do tradutor.

## O que não se traduz (o checker quebra se mudar)

- Blocos de código cercados por ``` ficam idênticos ao inglês, byte a byte, inclusive comentários e prompts em inglês dentro deles.
- Código inline entre crases fica igual: comandos, flags, chaves de config, valores de API (`idle`, `working`, `blocked`, `done`), nomes de arquivo, teclas (`prefix+b`, `ctrl+shift+v`).
- Linhas `import` ganham um `../` a mais no caminho relativo (`'../../components/X.astro'` vira `'../../../components/X.astro'`). Import de pacote (`'@astrojs/starlight/components'`) fica igual.
- Chaves do frontmatter ficam iguais e na mesma ordem. Traduza só os valores de texto: `title`, `description`, `hero.tagline`, `actions[].text`. Caminho de imagem no frontmatter ganha um `../` a mais.
- Componentes MDX (`<Card>`, `<CardGrid>`, `<ConfigReference />`) mantêm nome e atributos; traduza só o texto de `title="..."` e o conteúdo.
- Diretivas do Starlight (`:::note`, `:::tip[...]`, `:::caution[...]`) mantêm a sintaxe; traduza o título entre colchetes e o conteúdo.
- Textos da interface do Herdr (itens de menu, badges, rótulos que o app mostra) ficam em inglês, porque o app só existe em inglês. Ex.: **Reachable**, `! auth`, `reload config`. Quando ajudar, explique em português logo depois, sem traduzir o rótulo.
- URLs externas ficam iguais.

## Links internos

- Link para página da doc: `/docs/<pagina>/` vira `/pt-br/docs/<pagina>/`. Sem exceção (o japonês tem links esquecidos em `/docs/`, não copie).
- Links fora de `/docs/` (ex.: `/plugins/`) ficam iguais.
- Âncora (`#...`) aponta para o título traduzido da página de destino. A âncora é o slug do título em pt-BR: minúsculas, acentos mantidos, pontuação removida (crases, dois-pontos, parênteses, pontos, vírgulas, `?`), cada espaço vira `-`. Ex.: `## Atalhos de teclado` vira `#atalhos-de-teclado`; `## Configuração do tema` vira `#configuração-do-tema`; `` ## `reload config` `` vira `#reload-config`.
- Se a página de destino ainda não estiver traduzida, deixe a âncora em inglês. A sessão principal roda um checker e corrige âncoras depois.

## Títulos

- Mesma quantidade de títulos, mesmos níveis (`##`, `###`), mesma ordem. O CI compara a sequência de níveis.
- Caixa de frase: só a primeira palavra e nomes próprios com maiúscula ("Início rápido", não "Início Rápido").

## Glossário

| Inglês | pt-BR | Observação |
|---|---|---|
| pane | painel | "split pane" = dividir o painel |
| tab | aba | |
| workspace | workspace | masculino: "o workspace" |
| sidebar | barra lateral | |
| session | sessão | |
| server / client | servidor / cliente | |
| agent | agente | "coding agent" = agente de programação |
| keybinding / keybind | atalho de teclado, atalho | |
| prefix (key) | prefixo, tecla de prefixo | |
| detach / attach / reattach | desanexar / anexar / reanexar | na primeira ocorrência da página: "desanexar (detach)" |
| terminal multiplexer | multiplexador de terminal | |
| mouse-first / mouse-native | pensado para o mouse | |
| popup | popup | |
| worktree | worktree | |
| plugin, hook, socket, prompt, token, TUI, CLI, API, marketplace | mantêm o termo em inglês | "o plugin", "o hook", "o socket" |
| machine (remote) | máquina | |
| config / config file | configuração / arquivo de configuração | `config.toml` fica em código |
| release / stable / preview channel | versão / canal estável / canal preview | |
| install / update | instalar / atualizar | |
| troubleshooting | solução de problemas | |
| quick start | início rápido | |
| state (agent) idle / working / blocked / done | ocioso / trabalhando / bloqueado / concluído | em prosa; em código fica o valor em inglês |
| default | padrão | "por padrão" |
| scrollback | histórico de rolagem | |
| copy mode | modo de cópia | |
| notification | notificação | |

Termo que não está aqui: use o que um dev brasileiro usaria na conversa. Se ele fala em inglês (deploy, commit, branch, shell), mantenha em inglês sem itálico.

## Tom e estilo

- Trate o leitor por "você". Instrução no imperativo: "Execute", "Abra", "Adicione".
- Registro técnico neutro, como uma boa doc em português. Sem gíria, sem "a gente", sem exclamação.
- Frase curta e direta; divida frase longa do inglês em duas quando ficar pesada em português.
- Sem travessão (— ou –) em lugar nenhum da prosa. Use ponto ou vírgula. Os blocos de código ficam como estão.
- Dois-pontos só antes de lista, bloco de código ou exemplo.
- Aspas retas (").
- Sem vocabulário de IA ("crucial", "robusto", "abrangente", "potencializar", "fomentar", "é importante notar que").
- Voz ativa com o agente nomeado ("O Herdr salva a sessão", não "A sessão é salva").
- Pontuação e ortografia do português brasileiro (Acordo de 1990), com todos os acentos.

## Verificação que todo agente roda nos seus arquivos

```bash
python3 ~/.cache/herdr-2026-09-29/locale_check.py \
  --docs-root <checkout>/docs/next/website/src/content/docs \
  --locale pt-br --files <arquivo1.mdx>,<arquivo2.mdx>
```

Erros de âncora para páginas de outro lote podem ficar; todo o resto tem que zerar. Também rode:

```bash
rg -n '—|–' <seus arquivos pt-br>   # tem que voltar vazio fora de blocos de código
```

## Termos unificados depois da rodada 0 (valem para todos os lotes)

Os tradutores escolheram termos diferentes em alguns casos. A partir daqui, use estes e troque as outras formas que encontrar:

| Inglês | Use | Troque |
|---|---|---|
| rollup / rolled-up state | agregação / estado agregado | "resumos por workspace", "agregações" soltas sem dizer do quê |
| tiled (layout, pane) | lado a lado ("painel lado a lado", "layout lado a lado") | "em blocos", "em bloco" |
| fallback | fallback | "valor de reserva", "reserva" |
| report (agente informa estado) | informar / informe | "relatar", "relato" |
| viewport | área visível | "viewport" em prosa |
| chord | combinação de teclas | "chord", "combinação" solta quando ambígua |
| link / unlink (plugin) | vincular / desvincular | |
| socket API (em prosa) | API de socket | "Socket API" em prosa (o título da página fica como está) |
| modos da interface com nome próprio (Prefix, Navigate, Copy, Resize mode) | "modo Navigate", "modo Copy" quando o inglês usa o nome com maiúscula | quando o inglês usa minúscula genérica ("resize mode"), "modo de redimensionamento" |
| ssh-agent / agent forwarding | "agent SSH", "encaminhamento do agent SSH" | "agente" (reservado ao agente de programação) |
| supported / not supported (tabelas) | com suporte / sem suporte | "suportado", "não suportado" |
