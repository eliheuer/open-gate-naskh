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
star(MH+U*18, MV+U*59, 9, U*2, U*1.3)
strokeWidth(1)
oval(MH+U*2.5, MV+U*58.5, U*1, U*1)
oval(MH+U*2.5, MV+U*4.5, U*1, U*1)
oval(MH+U*32.5, MV+U*58.5, U*1, U*1)
oval(MH+U*32.5, MV+U*4.5, U*1, U*1)
strokeWidth(1)

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

txt2 ='''قل الله يكفي عن كلّ شيء ولا يكفي عن الله ربّك من شيء لا في السّموات ولا في الأرض ولا بينهما إنّه كان علاّما كافيا قديرا'''
# create a formatted string
t2 = FormattedString(fontSize=U*2.7)
# set alignment
t2.align("justified")
# add text
t2.font("fonts/ttf/OpenGateNaskh-Regular.ttf")
t2.lineHeight(U*4.)
t2 += txt2
t2 += "\n"
textBox(t2, (U*8, U*8.5, U*24, U*46))

txt3 ='''هل من مفرج غير الله قل سبحان الله هو الله كل عِباد له وكل بأمره قائمون'''
# create a formatted string
t3 = FormattedString(fontSize=U*2.7)
# set alignment
t3.align("justified")
# add text
t3.font("fonts/ttf/OpenGateNaskh-Regular.ttf")
t3.lineHeight(U*4.)
t3 += txt3
t3 += "\n"
textBox(t3, (U*8, U*8.5, U*24, U*18))

fill(0)
stroke(0)
#rect(U*12.25, U*55.75, U*16, U*4)
fill(1)
#rect(U*12, U*56, U*16, U*4)

stroke(None)
fill(0)
font("fonts/ttf/OpenGateNaskh-Regular.ttf")
fontSize(U*6)
text("٢",              (U*29.8,  U*56))
text("٣",              (U*28.7,  U*28))
fontSize(U*2)
#text("بســـــــــــــــم الله الرحمـن الرحيـــــــــــــــــــم",  (U*8,  U*52))
#fontSize(U*1.2)
text("١٨",                            (U*19.3, U*62.4))

# TYPEOGRAPHY
# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
# POST_PROCESS: pdfjam --nup 2x1 booklet-test-verso.pdf booklet-test-recto.pdf --landscape --outfile out.pdf
saveImage("documentation/print/booklet-bab-verso.pdf")
print("Updated booklet bab verso")
