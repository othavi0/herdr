## Lote A (socket-api, concepts, agent-skill, marketplace, config-reference)
- checker: só marketplace -> /pt-br/docs/plugins/#trust-and-security (outro lote).
- Termos: rótulos UI em inglês (Space, Agents, Online, Attention, Done); raw -> "cru"; authoritative -> "de referência"/"não autoritativas"; rollups -> agregações; provenance -> procedência; entrypoint -> ponto de entrada; tiled pane -> painel lado a lado; Mouse UI -> UI com mouse.
- AMBÍGUO/FIDELIDADE p/ R2: socket-api omitiu "desktop" em "desktop positions are relative to the full Herdr frame"; "mobile Agents list"; concepts "Navigate mode ... surface"; "agent.wait is server-owned".
## Lote B (configuration, integrations, index, quick-start)
- checker 0. Âncoras já traduzidas: #painéis, #atalhos-de-teclado, #anexação-remota.
- Texto de link palpite: "Adicionar suporte ao Herdr no seu agente" (integrations), "Como trabalhar com o Herdr" (quick-start), "Referência de configuração" -> alinhar com títulos reais.
- Termos: manifest de tela; ciclo de vida; handoff ao vivo; modos Prefix/Navigate/Copy/Resize em inglês; Central de Notificações; fallback -> "reserva"/"recorre a"; pill -> marcador; rollups -> resumos por workspace (Lote A usou "agregações" — divergência).
- Ambíguos: integrations:56 permissões; integrations:209 "this change" (texto de changelog no inglês); configuration:597 opt-in; configuration:173.
## Lote C (cli-reference, plugins, troubleshooting, how-to-work)
- checker 0; inline code multiset igual. Links alinhados com títulos pt-br.
- marketplace.mdx:21 #trust-and-security -> #confiança-e-segurança (fixer resolve).
- Termos: tiled -> "em blocos" (A usou "lado a lado" — divergência); link/unlink -> vincular/desvincular; startup hooks -> hooks de inicialização; host surface -> interface do host; chord -> combinação de teclas; clipboard -> área de transferência; phone -> celular; socket API em prosa -> "API de socket" (título da página A "Socket API"?).
## Lote D (install, agents, keyboard, persistence-remote, connecting-machines, session-state, windows-beta, agent-automation, add-herdr-support)
- checker 0; âncoras já traduzidas; rollups -> "agregação de estados"; viewport -> área visível; primitive -> primitiva; windows-beta status suportado/parcial/preview/não suportado; ssh agent -> "agent SSH".
- Ambíguos: agents tabela Integration role traduzida (estado e sessão / sessão / nenhum) + `session`; "Agent sidebar row" ; install "endpoint-generation-1 servers".
