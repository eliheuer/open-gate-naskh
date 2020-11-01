#!/bin/bash
set -e

sh sources/build.sh
python3 documentation/print/booklet-test-recto.py
python3 documentation/print/booklet-shams-verso.py
python3 documentation/print/booklet-fatiha-recto.py
python3 documentation/print/booklet-bab-verso.py
python3 documentation/slide-decks/final-project-presentation/final-project-presentation.py
