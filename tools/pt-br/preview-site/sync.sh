#!/bin/sh
# Uso: ./sync.sh <checkout-do-herdr>. Copia a doc para o layout do protótipo (/docs/ e /<locale>/docs/).
SRC=${1:?informe o caminho do checkout do herdr}/docs/next/website/src/content/docs
DST=$(dirname "$0")/src/content/docs
rm -rf "$DST"; mkdir -p "$DST/docs" "$(dirname "$0")/src/public/assets"
cp "$1/assets/logo.svg" "$(dirname "$0")/src/public/assets/logo.svg"
cp "$SRC"/*.mdx "$DST/docs/"
for l in ja zh-cn pt-br; do
  [ -d "$SRC/$l" ] || continue
  mkdir -p "$DST/$l/docs"; cp "$SRC/$l"/*.mdx "$DST/$l/docs/"
done
