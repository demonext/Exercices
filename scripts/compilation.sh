#! /usr/bash

cd ../files/latex
cat enonces-preamble.tex latexvars enonces-body.tex > enonces_${1}.tex
xelatex enonces_${1}.tex
xelatex enonces_${1}.tex
mv enonces_${1}.pdf ../enonces
rm *${1}*
rm latexvars
