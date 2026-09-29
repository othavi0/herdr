Tarefa: rodada 1 de revisão de estilo da tradução pt-BR da documentação do Herdr. Os arquivos já estão traduzidos; você melhora a prosa em português.

Worktree: <checkout>
Alvo: docs/next/website/src/content/docs/pt-br/<pagina>.mdx
Fonte em inglês (só para conferir sentido): docs/next/website/src/content/docs/<pagina>.mdx

Leia inteiros, antes de editar:
1. tools/pt-br/pt-br-guia.md (contrato: glossário, o que não se traduz, links, tom).
2. /home/othavio/.claude/skills/humanize-pt-br/SKILL.md e /home/othavio/.claude/skills/humanize-pt-br/references/patterns-pt-br.md.
3. /home/othavio/.claude/plugins/cache/pstack-claude/pstack/0.9.45/skills/unslop/SKILL.md.

Como aplicar:
- humanize-pt-br no modo "Arquivo": reescreva só a prosa, preservando código, frontmatter (exceto os valores de texto), links e componentes. Registro técnico neutro de manual: sem "eu", sem opinião, sem gíria. Os falsos positivos do catálogo valem (texto técnico plano é voz humana legítima).
- unslop: todas as regras, adaptadas ao português (sem travessão, dois-pontos só antes de lista/código/exemplo, voz ativa com agente nomeado, palavra simples, frase curta).
- Procure em especial: calque do inglês (ordem de palavras, "é usado para", gerúndio em excesso, "o mesmo" como pronome, "através de" no sentido de "por meio de" ou "com", "de forma a", "realizar"), repetição de "você" desnecessária, voz passiva, frases longas que pedem ponto, termos que fogem do glossário, acentuação e crase.
- Não-fabricação: nada de fato, número, nome ou exemplo que não esteja no inglês. Não remova informação. Se o pt-br atual perdeu ou inverteu algo do inglês, corrija para o sentido do inglês.
- TÍTULOS CONGELADOS: não altere o texto de nenhum título (#, ##, ###...). Outras páginas apontam âncoras para eles. Se um título tem erro real (gramática, termo fora do glossário), NÃO edite; liste no relatório como "título: <atual> -> <proposto>".
- Não altere o destino de nenhum link nem âncora. O texto visível do link pode mudar: quando ele cita outra página, use o `title` do frontmatter da página pt-br de destino (ou o título da seção, para link com âncora).
- Aplique a seção "Termos unificados depois da rodada 0" do guia: troque as formas antigas pelas novas em toda a prosa dos seus arquivos.

Regras de escopo:
- Edite SOMENTE os arquivos pt-br da sua lista. Nenhum outro arquivo. Não rode git, não instale nada, não faça perguntas.
- Um arquivo por vez: leia o pt-br e o inglês inteiros, edite com Edit (vários Edit pequenos, não reescreva o arquivo inteiro com Write), rode o checker nesse arquivo e zere antes de passar ao próximo.

Checker:
python3 tools/pt-br/locale_check.py --docs-root <checkout>/docs/next/website/src/content/docs --locale pt-br --files <arquivo.mdx>
Travessão: rg -n '—|–' <arquivo pt-br> (só pode aparecer dentro de bloco de código idêntico ao inglês).

Relatório final (dado cru): por arquivo, número aproximado de trechos alterados e os 3 tipos de problema mais frequentes; títulos propostos; saída final do checker.
