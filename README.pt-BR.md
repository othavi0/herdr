# herdr


<p align="center">
  <img src="assets/logo.png" alt="herdr" width="100" />
</p>

<p align="center">
  <a href="https://herdr.dev">herdr.dev</a> · <a href="#instalação">Instalação</a> · <a href="https://herdr.dev/pt-br/docs/quick-start/">Início rápido</a> · <a href="https://herdr.dev/pt-br/docs/">Documentação</a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · Português
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-666666?labelColor=333333" alt="Licença Apache 2.0" /></a>
  <a href="https://github.com/herdrdev/herdr/releases"><img src="https://img.shields.io/github/downloads/herdrdev/herdr/total?labelColor=333333&color=666666" alt="Total de downloads das versões no GitHub" /></a>
  <a href="https://github.com/herdrdev/herdr/stargazers"><img src="https://img.shields.io/github/stars/herdrdev/herdr?labelColor=333333&color=666666&logo=github" alt="Estrelas no GitHub" /></a>
  <a href="https://github.com/herdrdev/herdr/releases/latest"><img src="https://img.shields.io/github/v/release/herdrdev/herdr?label=release&labelColor=333333&color=666666" alt="Última versão estável" /></a>
  <a href="https://formulae.brew.sh/formula/herdr"><img src="https://img.shields.io/homebrew/v/herdr?label=homebrew&labelColor=333333&color=666666" alt="Versão no Homebrew" /></a>
  <a href="https://x.com/herdrdev"><img src="https://img.shields.io/badge/follow-%40herdrdev-000000?logo=x&logoColor=white" alt="Siga @herdrdev no X" /></a>
</p>

---

https://github.com/user-attachments/assets/043ec09f-4bdd-41d5-aee0-8fda6b83e267

**O runtime onde seus agentes de programação vivem.**

- **Desanexe (detach) sem parar o trabalho.** O Herdr mantém os terminais rodando em um servidor em segundo plano quando você fecha o cliente ou perde a conexão SSH. Depois que o servidor ou a máquina reinicia, o Herdr restaura o layout salvo e pode retomar as sessões dos agentes com suporte. Os processos originais não sobrevivem. [Estado da sessão →](https://herdr.dev/pt-br/docs/session-state/)
- **Várias máquinas, uma janela.** Mantenha juntos o trabalho local e as máquinas SSH salvas, com uma lista combinada de agentes e reconexões independentes. [Máquinas remotas →](https://herdr.dev/pt-br/docs/connecting-machines/)
- **Sem caçar o agente travado.** O Herdr marca cada painel como trabalhando, bloqueado ou ocioso. Quando um agente para e precisa de uma resposta, o Herdr avisa.
- **Feito para agentes.** Os agentes controlam o Herdr pela CLI e pela API de socket. Eles podem criar painéis, enviar prompts uns aos outros e esperar até que outro agente esteja bloqueado de fato. [Skill do agente →](https://herdr.dev/pt-br/docs/agent-skill/)
- **Roda o que você já roda.** Claude Code, Codex, Cursor, OpenCode, Grok e os demais. O Herdr não encapsula nem substitui essas ferramentas. Ele controla os terminais delas.
- **Teclado e mouse, os dois de primeira classe.** Teclas de prefixo no estilo tmux *e* clicar, arrastar, dividir. Escolha conforme o momento, não conforme a ferramenta.
- **Plugins.** Estenda painéis e fluxos de trabalho. [Explore o marketplace →](https://herdr.dev/plugins/)
- **Um binário Rust, sem Electron.** Roda em qualquer terminal que você já use.

---

## Instalação

```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

Ou `brew install herdr` · `mise use -g herdr` · Windows: `powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"` · [Windows com proteção de endpoint](https://herdr.dev/pt-br/docs/windows-beta/) · [binários](https://github.com/herdrdev/herdr/releases)

Depois, inicie o Herdr onde o trabalho está:

```bash
herdr
```

Execute seus agentes, divida os painéis e vá embora. `ctrl+b q` desanexa, `herdr` reanexa. [Início rápido →](https://herdr.dev/pt-br/docs/quick-start/)

## Documentação

Tudo fica em [herdr.dev/docs](https://herdr.dev/pt-br/docs/): [Início rápido](https://herdr.dev/pt-br/docs/quick-start/) · [Conceitos](https://herdr.dev/pt-br/docs/concepts/) · [Agentes com suporte](https://herdr.dev/pt-br/docs/agents/) · [Teclado](https://herdr.dev/pt-br/docs/keyboard/) · [Configuração](https://herdr.dev/pt-br/docs/configuration/) · [Estado da sessão](https://herdr.dev/pt-br/docs/session-state/) · [Conectar máquinas](https://herdr.dev/pt-br/docs/connecting-machines/) · [Acesso remoto](https://herdr.dev/pt-br/docs/persistence-remote/) · [Integrações](https://herdr.dev/pt-br/docs/integrations/) · [Plugins](https://herdr.dev/pt-br/docs/plugins/) · [API de socket](https://herdr.dev/pt-br/docs/socket-api/)

## Agradecimentos

O [SPONSORS.md](./SPONSORS.md) lista todos os patrocinadores e apoiadores que o projeto já teve. Obrigado 🐑

Empresas e parcerias: hey@herdr.dev

## Instruções para agentes

Se você é um agente de IA que ajuda neste repositório, leia o [`AGENTS.md`](./AGENTS.md) antes de fazer mudanças e leia o [`CONTRIBUTING.md`](./CONTRIBUTING.md) antes de abrir issues ou PRs.

## Desenvolvimento

```bash
git clone https://github.com/herdrdev/herdr
cd herdr
cargo build --release

just test        # unit tests
just check       # formatting, tests, and maintenance checks
```

## Licença

O Herdr usa a [Apache License 2.0](LICENSE).
