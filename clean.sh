#!/bin/bash
set -ex

cd docs
mv *data*md /tmp  2>/dev/null || true
mv assets/*json /tmp  2>/dev/null || true
find . -regex './...md'  | xargs -I {}  mv {} /tmp  # e.g. I5.md
find . -regex './....md'  | xargs -I {}  mv {} /tmp # e.g. AVM.md
find . -regex './.....md'  | xargs -I {}  mv {} /tmp # e.g. ADAL.md
find ./api/cect -regex '.*.md'  | xargs -I {}  mv {} /tmp # e.g. ./api/cect/Cook2020DataReader.md
find . -regex './[MpRSgGUIOdumv].....md' |  xargs -I {}  mv {} /tmp
rm -rf site/*
cd ..

