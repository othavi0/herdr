### idea / problem

I've been on Herdr every day for months and I keep wanting to send people around me to the docs, but the site and the README only have Simplified Chinese next to English, and there's nothing in Portuguese yet. #4210 asked about a Portuguese locale on Sep 15 and it's still sitting there with no reply, so I went ahead and scoped it properly.

### requested change

Add pt-BR in the same places zh-CN already lives, so nothing about the layout is new:

- a `pt-br/` folder next to `zh-cn/` in `docs/next/website/src/content/docs/` with all 22 pages, plus `pt-br` in `DEFAULT_LOCALES` and in the `release-docs-check` loops so the parity check covers it
- `docs/next/README.pt-BR.md` with a `Português` link in the language line, promoted at release by `versions.mjs` the same way as `README.zh-CN.md`

The Starlight locale entry lives in the website repo, so that one would be on your side.

### why you want this

I know every new locale is one more thing to keep in sync on each docs change, so I'm happy to be the one keeping pt-BR up to date, because I like this project a lot and I'd rather people here use it without the language getting in the way. The translation is already done in my fork following the zh-cn layout, so the PR is ready whenever it fits.

Side note, I was approved as `othavioquiliao` after #25 and later renamed the account to `othavi0`, so `.github/APPROVED_CONTRIBUTORS` still has the old handle.
