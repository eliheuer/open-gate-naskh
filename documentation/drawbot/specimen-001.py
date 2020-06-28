# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,1024,64,64

# DRAWS A GRID
def grid():
    stroke(0.2)
    strokeWidth(1)
    rect(M+M, M+M, W-(4*M), H-(4*M))
    stpX, stpY = 0, 0
    incX, incY = M/2, M/2
    for x in range(25):
        polygon(((M+M)+stpX, M+M),
                ((M+M)+stpX, H-(M+M)))
        stpX += incX
    for y in range(25):
        polygon((M+M, (M+M)+stpY),
                (W-(M+M), (M+M)+stpY))
        stpY += incY

# REMAP INPUT RANGE TO VF AXIS RANGE
# (E.G. SINE WAVE(-1,1) to WGHT(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan  = inputMax  - inputMin   # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)

# NEW PAGE
def new_page():
    newPage(W, H)
    frameDuration(1/24)
    fill(0)
    rect(-2, -2, W+2, H+2)

# MAIN
for axis, data in listFontVariations().items(): print((axis, data))
font("../../fonts/variable/Open-Gate_Mono-VF.ttf")
varWght = 0
step = -1
for frame in range(F):
    new_page()
    font("../../fonts/variable/Open-Gate-Mono-VF.ttf")
    grid() # Toggle for grid view
    fill(0)
    fill(1)
    stroke(None)
    fontSize((M*5))
    print("Sine step:", sin(step))

    varWght = remap(sin(step),-1,1,300,700)
    fontVariations(wght=varWght)
    text("كتاب", (M*4, M*11.5))

    varWght = remap(sin(step+0.5),-1,1,300,700)
    fontVariations(wght=varWght)
    text("كتاب", (M*4, M*8.5))

    varWght = remap(sin(step+1),-1,1,300,700)
    fontVariations(wght=varWght)
    text("كتاب", (M*4, M*5.5))

    varWght = remap(sin(step+1.5),-1,1,300,700)
    fontVariations(wght=varWght)
    text("كتاب", (M*4, M*2.5))

    step += 0.1
saveImage("../specimens/specimen-001.gif")
