#!/usr/bin/env bash
# Build the Quarto site with the preview profile and publish it to
# https://sannerlab.github.io/preview/quarto/ (gh-pages branch, folder preview/quarto).
# The live Jekyll site is not touched: its deploy keeps the preview/ folder (clean-exclude).
# Run from anywhere:  bash _scripts/deploy-preview.sh
set -euo pipefail
SRC_DIR=$(cd "$(dirname "$0")/.." && pwd)
cd "$SRC_DIR"

[ -z "$(git status --porcelain)" ] || { echo "Commit your changes first."; exit 1; }
git push -u origin quarto

quarto render --profile preview
SRC=$(git rev-parse --short HEAD)

W=$(mktemp -d)
trap 'git -C "$SRC_DIR" worktree remove --force "$W" 2>/dev/null || true' EXIT
git fetch -q origin gh-pages
git worktree add -q --detach "$W" origin/gh-pages
mkdir -p "$W/preview"
rm -rf "$W/preview/quarto"
cp -r _site "$W/preview/quarto"
git -C "$W" add preview/quarto
if git -C "$W" diff --cached --quiet; then
  echo "Preview already up to date."
else
  git -C "$W" commit -q -m "Update Quarto preview at /preview/quarto/ (from quarto@$SRC)"
  git -C "$W" push origin HEAD:gh-pages
fi
echo "Done. Live in a few minutes at https://sannerlab.github.io/preview/quarto/"
