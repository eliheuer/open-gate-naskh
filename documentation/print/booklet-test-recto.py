# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# Note: Run this script from the project root directory with DrawBot installed in editable mode.
# Note: e.g. $ python3 documentation/slide-decks/final-project-presentation/final-project-presentation.py
# Typeface Used: https://github.com/undercasetype/Fraunces
# Typeface Used: https://input.fontbureau.com
# Unit Space: 72dpi (dots per inch)
from drawBot import *
import math

# CONSTANTS
W =  396  # Width
H =  612  # Height
MH = 9*2 # Margin Horizonal
MV = 9*4 # Margin Vertical
U =  9    # Unit

# Draws a Grid
def grid(unit):
    strokeWidth(1)
    step_X = 0
    step_Y = 0
    increment_X = unit
    increment_Y = unit
    for x in range(40):
        polygon( (MH+step_X, MV), (MH+step_X, H-MV) )
        step_X += increment_X
    for y in range(64):
        polygon( (MH, MV+step_Y), (W-MH, MV+step_Y) )
        step_Y += increment_Y
    fill(None)
    rect(MH, MV, W-(2*MH), H-(2*MV))

# Draws a star
# Code adapted from a tweet by Just van Rossum
def star(x, y, n, r1, r2):
    stroke(0)
    fill(None)
    pts = []
    for i in range(n * 2):
        a = i * pi / n
        r = r2 if i % 2 else r1
        pts.append((x + r * sin(a), y + r * cos(a)))
    polygon(*pts)

# New Page
def new_page():
    newPage(W, H)
    #fill(0.8)
    #rect(-2, -2, W+2, H+2)

# Set & Test Font
#font("fonts/Fraunces\[SOFT,WONK,opsz,wght\].ttf")
#for axis, data in listFontVariations().items():
#    print((axis, data))

new_page() #--------------------------------------------------#
# SETUP
#font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
stroke(0.9)
#grid(U) # Toggle for grid view
stroke(1,0,0,0.2)
#grid(U*4)
stroke(None)
fill(0)

stroke(0)
fill(None)
lineJoin("round")
oval(MH+U*20, MV+U*57, U*4, U*4)
star(MH+U*22, MV+U*59, 9, U*2, U*1.3)
strokeWidth(1)
oval(MH+U*6.5, MV+U*58.5, U*1, U*1)
oval(MH+U*6.5, MV+U*4.5, U*1, U*1)
oval(MH+U*36.5, MV+U*58.5, U*1, U*1)
oval(MH+U*36.5, MV+U*4.5, U*1, U*1)
strokeWidth(1)

#rect(MH+U*12, MV+U*57, U*2, U*2)
rect(MH+U*16, MV+U*58, U*2, U*2)
rect(MH+U*14, MV+U*58, U*2, U*2)
rect(MH+U*12., MV+U*58, U*2, U*2)
rect(MH+U*10., MV+U*58, U*2, U*2)
rect(MH+U*8., MV+U*58, U*2, U*2)
#rect(MH+U*0., MV+U*58, U*2, U*2)

rect(MH+U*26, MV+U*58, U*2, U*2)
rect(MH+U*28, MV+U*58, U*2, U*2)
rect(MH+U*30, MV+U*58, U*2, U*2)
rect(MH+U*32, MV+U*58, U*2, U*2)
rect(MH+U*34, MV+U*58, U*2, U*2)
rect(MH+U*36, MV+U*58, U*2, U*2)

step = 0
for i in range(28):
    rect(MH+U*6., MV+((U*58)-step), U*2, U*2)
    step += U*2

step = 0
for i in range(28):
    rect(MH+U*36., MV+((U*58)-step), U*2, U*2)
    step += U*2

step = 0
for i in range(14):
    rect(MH+U*8.+step, MV+((U*4)), U*2, U*2)
    step += U*2

# TYPEOGRAPHY
fontSize(U*2.8)
font("fonts/ttf/OpenGateNaskh-Regular.ttf")
stroke(None)
fill(0)
text("أشــــهد يا إلهي بأنّك خلقتني",              (U*11.8,  U*56))
text("لعرفانك وعبادتــــــــــــــــــــــك",   (U*11.9,  U*48))
text("أشـــــــــــــــــهد في هذا الحين",        (U*11.9,  U*40))
text("بعجزي وقوّتك وضعــــــــــفي",              (U*11.75,  U*32))
text("واقـــــــتدارك وفقري وغنائك",               (U*12.0, U*24))
text("لا إله إلاّ أنت المهيمن القيّوم",           (U*11.9,  U*16))

font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
fontVariations(wght = 600 )
fontSize(U*1.2)
text("ash’hadu ya ilahi be an’naka khalaqtani", (U*12.5, U*52))
text("lee erfanekah wa ebadatek",               (U*16.3, U*44))
text("ash’hadu fee hadal heen",                 (U*17.0, U*36))
text("be ajzee wa quatekah, wa da’afi",         (U*15.0, U*28))
text("wa iqtedarekah, wa faqree wa qana’ekah",  (U*12.3, U*20))
text("la illaha illa antal muhaimenol qayoom",  (U*12.7, U*12))
font("fonts/ttf/OpenGateNaskh-Regular.ttf")
fontSize(U*2)
text("١٩",                                      (U*23.37, U*62.4))

# TYPEOGRAPHY
# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
saveImage("documentation/print/booklet-test-recto.pdf")
print("Updated booklet test recto")
