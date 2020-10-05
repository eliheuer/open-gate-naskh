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


oval(MH+U*10, MV+U*45, U*2, U*2)
oval(MH+U*10, MV+U*41, U*2, U*2)
oval(MH+U*10, MV+U*37, U*2, U*2)
oval(MH+U*10, MV+U*33, U*2, U*2)
oval(MH+U*10, MV+U*29, U*2, U*2)
oval(MH+U*10, MV+U*25, U*2, U*2)
oval(MH+U*17, MV+U*9, U*2, U*2)

star(MH+U*11, MV+U*46, 9, U*1, U*1.3)
star(MH+U*11, MV+U*42, 9, U*1, U*1.3)
star(MH+U*11, MV+U*38, 9, U*1, U*1.3)
star(MH+U*11, MV+U*34, 9, U*1, U*1.3)
star(MH+U*11, MV+U*30, 9, U*1, U*1.3)
star(MH+U*11, MV+U*26, 9, U*1, U*1.3)
star(MH+U*18, MV+U*10, 9, U*1, U*1.3)







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


fill(0)
stroke(0)
rect(U*12.25, U*53.75, U*24, U*6)
fill(1)
rect(U*12, U*54, U*24, U*6)


# TYPEOGRAPHY
fontSize(U*2.7)
font("fonts/ttf/OpenGateNaskh-Regular.ttf")
stroke(None)
fill(0)
text("بســـــم الله الرحمـن الرحيم",  (U*14.7,  U*50))
text("الحمد لله رب العلميـــــن",     (U*14.9,  U*46))
text("الرحمـــــــــــن الرحيـــــــــــــــم",           (U*14.7,  U*42))
text("ملك يوم الديــــــــــــــــــــــن",            (U*14.9,   U*38))
text("إياك نعبد وإياك نستعين",   (U*15.2,  U*34))
text("اهدنا الصراط المستقيـــــم",    (U*14.7,  U*30))
text("صراط الذين أنعمت عليهــــم",    (U*11.8,  U*26))
text("غير الـــــــــــــــــــمغضوب",    (U*14,  U*22))
text("عليهــــــــــــــــم ولا",    (U*17,  U*18))
text("لضاليـــن",    (U*22,  U*14))

font("fonts/ttf/OpenGateNaskh-Regular.ttf")
fontSize(U*2)
text("١٩",                                      (U*23.37, U*62.4))

font("fonts/ttf/OpenGateNaskh-Regular.ttf")
fontSize(U*5.4)
text("سورة الفاتحة",           (U*13.2, U*55.75))

font("fonts/ttf/OpenGateNaskh-Regular.ttf")
fontSize(U*1.6)
text("١",           (U*12.75, U*49.5))
text("٢",           (U*12.75, U*45.5))
text("٣",           (U*12.75, U*41.5))
text("٤",           (U*12.75, U*37.5))
text("٥",           (U*12.75, U*33.5))
text("٦",           (U*12.75, U*29.5))
text("٧",           (U*19.5, U*13.5))

# TYPEOGRAPHY
# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
saveImage("documentation/print/booklet-fatiha-recto.pdf")
print("Updated booklet fatiha recto")
