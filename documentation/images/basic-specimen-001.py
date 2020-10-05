# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

# CONSTANTS
W = 1080  # Width
H = 1080  # Height
M = 30    # Margin
U = 30    # Unit (Grid Unit)

# DRAWS A GRID
def grid():
    strokeWidth(1)
    stroke(0.1)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(34):
        polygon( (M+step_X, M), (M+step_X, H-M) )
        step_X += increment_X
    for y in range(34):
        polygon( (M, M+step_Y), (W-M, M+step_Y) )
        step_Y += increment_Y
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))
    fill(0.9)
    stroke(None)

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)

# MAIN
new_page()
grid() # Toggle for grid view

stroke(0.4)
fill(0)
#rect(M*2,M*2, M*32, M*32)
stroke(None)

font("Input Mono Compressed")
#fill(0.4)
#fontSize(30)
#text("GTL Naskh: 09-22-2020 Pre-alpha @ Git Commit 42cffeaa", (M*3, M*32))
#text("WORK IN PROGRESS  https://gtl.world  WORK IN PROGRESS", (M*3, M*30))
#text("WORK IN PROGRESS  https://gtl.world  WORK IN PROGRESS", (M*3, M*5))
#text("Git Source: https://github.com/eliheuer/gtl-naskh.git", (M*3, M*3))

font("fonts/ttf/GTLNaskh-Regular.ttf")
fill(1)
fontSize(M*3)
text("اإأ ب ببب ت تتت ث ثثث",                (M*7.7, M*32))
text("ج ججج ح ححح خ خخخ ي ييي",              (M*5, M*28.5))
text("س سسس ش ششش ن ننن",                    (M*5.5, M*24.5))
text("ص صصص ض ضضض ",                         (M*10.6, M*20.5))
text("ط ططط ظ ظظظ ك ككك ",                   (M*7, M*16.5))
text(" ف ففف ق ققق ع ععع غ غغغ",             (M*7.3, M*12.5))
#text("ل للل لا لأ لإ لآ ء ",                     (M*18.9, M*8.5))
#text("١٢٣٤٥٦٧٨٩٠ ﷲ وـوؤـؤ ر ز  م ممم ",      (M*2, M*4.5))

# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
saveImage("documentation/images/basic-specimen-001.png")
print("[DrawBot]: basic specimen 001 updated")
