#!/bin/bash
fontmake -g sources/OpenGateNaskh.glyphs -o ttf
rm -rf instance_ufo
mkdir -p fonts/ttf
#cp -r master_ufo/*.designspace sources/
#cp -r master_ufo/*.ufo sources/
rm -rf master_ufo
cp -r master_ttf/*.ttf fonts/ttf/
rm -rf master_ttf

#python3 documentation/images/basic-specimen-001.py
#python3 documentation/images/salah-001.py
