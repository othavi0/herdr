# Rascunhos para o upstream (herdrdev/herdr). Nada publicado.
# Decisões: Discussion nova citando #4210, aviso do rename incluído, sem divulgação de IA.

## 1. Discussion (categoria Ideas, template "[idea]"), versão A escolhida

Título:
[idea] Brazilian Portuguese (pt-BR) docs and README

idea / problem:
I've been on Herdr every day for months and I keep wanting to send people around me to the docs, but the site and the README only have Simplified Chinese next to English, and there's nothing in Portuguese yet. #4210 asked about a Portuguese locale on Sep 15 and it's still sitting there with no reply, so I went ahead and scoped it properly.

requested change:
Add pt-BR in the same places zh-CN already lives, so nothing about the layout is new:
- a `pt-br/` folder next to `zh-cn/` in `docs/next/website/src/content/docs/` with all 22 pages, plus `pt-br` in `DEFAULT_LOCALES` and in the `release-docs-check` loops so the parity check covers it
- `docs/next/README.pt-BR.md` with a `Português` link in the language line, promoted at release by `versions.mjs` the same way as `README.zh-CN.md`

The Starlight locale entry lives in the website repo, so that one would be on your side.

why you want this:
I know every new locale is one more thing to keep in sync on each docs change, so I'm happy to be the one keeping pt-BR up to date, because I like this project a lot and I'd rather people here use it without the language getting in the way. The translation is already done in my fork following the zh-cn layout, so the PR is ready whenever it fits.

Side note, I was approved as `othavioquiliao` after #25 and later renamed the account to `othavi0`, so `.github/APPROVED_CONTRIBUTORS` still has the old handle.

## 2. PR (só depois do "ok" na Discussion)

Título:
docs: add brazilian portuguese docs and readme

Corpo:
Approved in discussion #<número>.

Adds Brazilian Portuguese in the same places Simplified Chinese already has:
- `docs/next/website/src/content/docs/pt-br/`: all 22 pages, same file names, links under `/pt-br/docs/`, and anchors pointing to the translated headings.
- `docs/next/README.pt-BR.md`, plus a `Português` link in the language line of `docs/next/README.md` and `docs/next/README.zh-CN.md`.
- `scripts/docs_translation_parity.py`, its test, and the `release-docs-check` loops in the `justfile` now include `pt-br`.
- `scripts/docs/versions.mjs` (with its integration test), `scripts/release.py`, and `.github/workflows/release.yml` promote `README.pt-BR.md` at release the same way as `README.zh-CN.md`.
- `.github/ISSUE_TEMPLATE/translation.yml` gets a Português option.

The Starlight `pt-br` locale lives in the website repo, so the pages need that entry before they show up on herdr.dev.

Validation: `test_docs_translation_parity`, `test_release`, `bun test scripts/docs/`, `node scripts/docs/versions.mjs check`, and `node scripts/docs/preview.mjs check` pass. I also rendered the pages in a local Starlight build with all four locales, and every pt-br anchor link resolves. No Rust code is touched.

## 3. Commits (em inglês, minúsculas, como o repo pede)

docs: add brazilian portuguese website docs
docs: add brazilian portuguese readme
chore: include pt-br in translation and release checks
