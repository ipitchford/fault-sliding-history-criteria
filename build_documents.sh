#!/usr/bin/env bash
# Build the manuscript PDF only (pandoc + citeproc + pdflatex).
set -eu
cd "$(dirname "$0")"
mkdir -p output tmp/pdfs

pandoc manuscript.md \
    --from markdown+tex_math_dollars+tex_math_single_backslash+autolink_bare_uris+raw_tex \
    --standalone \
    --citeproc --bibliography=refs.bib \
    -V geometry:a4paper,margin=23mm \
    -V fontsize=11pt \
    -H header.tex \
    --resource-path=. \
    -o tmp/pdfs/manuscript.tex
for pass in 1 2 3; do
    timeout 300 pdflatex -interaction=nonstopmode -halt-on-error \
        -output-directory tmp/pdfs tmp/pdfs/manuscript.tex \
        > "tmp/pdfs/manuscript_build_${pass}.txt" </dev/null
done
cp tmp/pdfs/manuscript.pdf output/fault_locking_manuscript.pdf
printf 'Built %s\n' output/fault_locking_manuscript.pdf
