Tarefa: rodada 2 da tradução pt-BR da documentação do Herdr. Fidelidade ao inglês primeiro, depois polimento final de estilo.

Worktree: <checkout>
Alvo: docs/next/website/src/content/docs/pt-br/<pagina>.mdx
Fonte: docs/next/website/src/content/docs/<pagina>.mdx

Leia inteiros antes de editar: tools/pt-br/pt-br-guia.md, /home/othavio/.claude/skills/humanize-pt-br/SKILL.md, /home/othavio/.claude/skills/humanize-pt-br/references/patterns-pt-br.md, /home/othavio/.claude/plugins/cache/pstack-claude/pstack/0.9.45/skills/unslop/SKILL.md.

Passo 1, fidelidade (o mais importante). Para cada arquivo, compare pt-br com inglês parágrafo por parágrafo, item de lista por item, linha de tabela por linha. Procure:
- fato, número, unidade, versão, flag, chave de config, nome de comando, estado ou tecla que falta, sobra ou mudou;
- condição invertida ou afrouxada ("never" virou "normalmente", "unless" virou "if", "only" sumiu, "must" virou "pode");
- item de lista ou linha de tabela faltando ou fundido;
- nota, aviso ou exemplo omitido;
- texto de interface do Herdr que foi traduzido (deve ficar em inglês, ver guia);
- sentido errado por falso cognato ou leitura errada do inglês.
Corrija cada divergência no pt-br para dizer exatamente o que o inglês diz.

Passo 2, polimento. Nos trechos que você corrigiu, e em qualquer marca de IA ou calque que ainda sobrou, aplique humanize-pt-br (modo "Arquivo", registro técnico neutro, sem "eu", sem opinião) e unslop (sem travessão, dois-pontos só antes de lista/código/exemplo, voz ativa, frase curta, palavra simples). Não reescreva o que já está bom.

Regras:
- TÍTULOS CONGELADOS: não altere texto de título; proposta vai no relatório como "título: <atual> -> <proposto>". Não altere links nem âncoras.
- Não-fabricação: nada que não esteja no inglês.
- Edite SOMENTE os arquivos pt-br da sua lista, com Edit pequenos. Não rode git, não instale nada, não faça perguntas.
- Um arquivo por vez, checker zerado antes do próximo:
python3 tools/pt-br/locale_check.py --docs-root <checkout>/docs/next/website/src/content/docs --locale pt-br --inline-code --files <arquivo.mdx>
As linhas "warning: inline code" comparam o código inline entre crases do inglês e do pt-br. Zere cada uma, salvo quando o inglês tem o termo em código e a tradução precisa dele em prosa por gramática (explique no relatório). O código inline do inglês deve aparecer no pt-br.

Relatório final (dado cru): por arquivo, a lista de divergências de fidelidade corrigidas (uma linha cada: o que o inglês diz, o que o pt-br dizia), a contagem de ajustes de estilo, títulos propostos, saída final do checker.

Contexto: as rodadas anteriores sinalizaram trechos ambíguos e decisões de tradução nos relatórios tools/pt-br/r0-relatorios.md e r1-relatorios.md. Leia a parte do seu lote e confira cada item contra o inglês.
