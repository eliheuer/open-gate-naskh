# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# Note: Run this script from the project root directory with DrawBot installed in editable mode.
# Note: e.g. $ python3 documentation/slide-decks/final-project-presentation/final-project-presentation.py
# Typeface Used: https://github.com/undercasetype/Fraunces
# Typeface Used: https://input.fontbureau.com
# Unit Space: 72dpi (dots per inch)
from drawBot import *
import math

# CONSTANTS
W = 1920  # Width
H = 1080  # Height
M = 80    # Margin
U = 40    # Unit

# Draws a Grid
def grid():
    strokeWidth(1)
    stroke(0.9)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(44):
        polygon( (M+step_X, M), (M+step_X, H-M) )
        step_X += increment_X
    for y in range(24):
        polygon( (M, M+step_Y), (W-M, M+step_Y) )
        step_Y += increment_Y
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# New Page
def new_page():
    newPage(W, H)
    fill(0.8)
    rect(-2, -2, W+2, H+2)

# Set & Test Font
font("fonts/Fraunces\[SOFT,WONK,opsz,wght\].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

new_page() #--------------------------------------------------#
# SETUP
font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
grid() # Toggle for grid view
stroke(None)
fill(0)
# TYPEOGRAPHY
fontSize(U*1)
fontVariations(wght = 700 )
text("Eli Heuer: Open Gate Naskh",                          (M, (U*24)+4))
fontVariations(wght = 400 )
font("fonts/InputMonoCompressed-Regular.ttf")
text("Final Project Presentation",  (M, (U*22)+4))
text("Arabic Type Design",                 (M, (U*21)+4))
text("Summer 2020",                        (M, (U*20)+4))
# IMAGES #----------------------------------------------------#
#image("images/qalam-photo.png", (M*11, M), alpha=1)
#image("images/ref-001.png", (M*19, M*5), alpha=1)
#image("images/ref-002.png", ((M*6)+U, M*4), alpha=1)
# Shapes #----------------------------------------------------#
#oval(M*3,M,M,M)
#rect(M*2,M*4,M,M)
#-------------------------------------------------------------#


new_page() #--------------------------------------------------#
# SETUP
grid() # Toggle for grid view
stroke(None)
fill(0)

# TYPEOGRAPHY
fontSize(U*3)
font("fonts/ttf/OpenGateNaskh-Regular.ttf")
text("اإأ ب ببب ت تتت ث ثثث",             (U*19, U*22))
text("ج ججج ح ححح خ خخخ ي ييي",           (U*5, U*20))
text("س سسس ش ششش ن ننن",                 (U*5, U*18))
text("ص صصص ض ضضض ",                      (U*5, U*16))
text("ط ططط ظ ظظظ ك ككك ",                (U*5, U*14))
text(" ف ففف ق ققق ع ععع غ غغغ",          (U*5, U*12))
#text("ل للل لا لأ لإ لآ ء ",                 (M*18.9, M*8.5))
#text("١٢٣٤٥٦٧٨٩٠ ﷲ وـوؤـؤ ر ز  م ممم ",  (M*2, M*4.5))


stroke(0)
strokeWidth(1)
line( ( M, M+U ), ( W-M, M+U ) )
stroke(None)
font("fonts/InputMonoCompressed-Regular.ttf")
fontSize(U*0.8)
text("Page 2/19",                    (M, M))
text("Basic Character Set",          (M+(U*16.25), M))
text("Monday, September 28th, 2020", (M+(U*32.5), M))


# Saving and post-processing
saveImage("documentation/slide-decks/final-project-presentation/final-project-presentation.pdf")
