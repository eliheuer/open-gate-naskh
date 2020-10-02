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
    for x in range(32):
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
stroke(0.8)
#grid(U) # Toggle for grid view
stroke(1,0,0,0.5)
#grid(U*4)
stroke(None)
fill(0)

stroke(0)
fill(None)
lineJoin("round")
oval(MH+U*16, MV+U*57, U*4, U*4)
star(MH+U*18, MV+U*59, 9, U*2, U*1)

#rect(MH+U*12, MV+U*57, U*2, U*2)
rect(MH+U*12, MV+U*58, U*2, U*2)
rect(MH+U*10, MV+U*58, U*2, U*2)
rect(MH+U*8., MV+U*58, U*2, U*2)
rect(MH+U*6., MV+U*58, U*2, U*2)
rect(MH+U*4., MV+U*58, U*2, U*2)
#rect(MH+U*0., MV+U*58, U*2, U*2)

rect(MH+U*22, MV+U*58, U*2, U*2)
rect(MH+U*24, MV+U*58, U*2, U*2)
rect(MH+U*26, MV+U*58, U*2, U*2)
rect(MH+U*28, MV+U*58, U*2, U*2)
rect(MH+U*30, MV+U*58, U*2, U*2)
rect(MH+U*32, MV+U*58, U*2, U*2)

step = 0
for i in range(28):
    rect(MH+U*2., MV+((U*58)-step), U*2, U*2)
    step += U*2

step = 0
for i in range(28):
    rect(MH+U*32., MV+((U*58)-step), U*2, U*2)
    step += U*2

step = 0
for i in range(14):
    rect(MH+U*4.+step, MV+((U*4)), U*2, U*2)
    step += U*2

stroke(None)
fill(0)
font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
fontVariations(wght = 600 )
fontSize(U*1.2)
text("19",                                      (U*19.4, U*62.6))

txt = '''sewi mi o! mi toki wawa e ni: sina pali e mi tawa seme? mi o sona e sina. mi o olin e sina. tenpo ni la mi sona e ni: mi anpa. sina wawa. mi jo lili. sina jo mute. sina sewi wan. sina awen e ale. lon la sina lon.'''

# create a formatted string
t = FormattedString(fontSize=12)
# set alignment
t.align("justified")
# add text
t.font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
t.fontVariations(wght = 600 )
t.lineHeight(U*1.7)
t += txt
t += txt
t += txt
t += txt
t += txt
t += "\n"
textBox(t, (U*8, U*13.4, U*24, U*40))

font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
fontVariations(wght = 800 )
fontSize(U*2)
text("toki pona",  (U*15.3, U*56))

# TYPEOGRAPHY
# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
# POST_PROCESS: pdfjam --nup 2x1 booklet-test-verso.pdf booklet-test-recto.pdf --landscape --outfile out.pdf
saveImage("documentation/print/booklet-test-verso.pdf")
