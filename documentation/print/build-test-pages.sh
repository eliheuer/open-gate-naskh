#!/bin/bash
set -e

pdfjam --nup 2x1 booklet-shams-verso.pdf booklet-test-recto.pdf --landscape --outfile booklet-test-1.pdf
pdfjam --nup 2x1 booklet-bab-verso.pdf booklet-fatiha-recto.pdf --landscape --outfile booklet-test-2.pdf
