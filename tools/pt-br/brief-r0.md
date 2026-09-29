Tarefa: traduzir páginas da documentação do Herdr do inglês para português brasileiro.

Worktree: <checkout>
Fonte: docs/next/website/src/content/docs/<pagina>.mdx
Alvo: docs/next/website/src/content/docs/pt-br/<pagina>.mdx (crie a pasta pt-br se não existir)

Antes de começar, leia inteiro o guia tools/pt-br/pt-br-guia.md. Ele é o contrato: glossário, o que não se traduz, links, âncoras, títulos, tom. Leia também /home/othavio/.claude/plugins/cache/pstack-claude/pstack/0.9.45/skills/unslop/SKILL.md e /home/othavio/.claude/skills/humanize-pt-br/SKILL.md, e aplique as regras deles já na tradução (registro técnico neutro, sem "eu", sem opinião, sem travessão).

Regras de escopo:
- Escreva SOMENTE os arquivos pt-br da sua lista. Não edite nenhum outro arquivo: nem o inglês, nem ja/zh-cn, nem o guia, nem os scripts em ~/.cache, nem docs/versions ou docs/preview.
- Não rode git (nenhum comando), não instale pacotes.
- Não faça perguntas; decida pelo guia. Termo fora do glossário: registre no relatório.
- Trabalhe um arquivo por vez: leia o inglês inteiro, escreva o pt-br completo, rode o checker só nesse arquivo, corrija até zerar (exceto âncora/página de outro lote ainda não traduzida), e só então passe para o próximo.
- Para arquivo grande, escreva em partes com Write + Edit em vez de uma resposta única gigante, e confira no fim que o arquivo terminou (última seção do inglês presente).

Checker:
python3 tools/pt-br/locale_check.py --docs-root <checkout>/docs/next/website/src/content/docs --locale pt-br --files <arquivo.mdx>

Paridade de títulos (o CI roda esta):
python3 <checkout>/scripts/docs_translation_parity.py --docs-root <checkout>/docs/next/website/src/content/docs --locale pt-br
(vai reclamar das páginas de outros lotes que ainda não existem; ignore essas e olhe só as suas)

Relatório final (curto, dado cru): arquivos escritos com contagem de linhas pt-br vs inglês, saída final do checker para seus arquivos, termos fora do glossário que você decidiu e como, e qualquer trecho do inglês que você achou ambíguo.
