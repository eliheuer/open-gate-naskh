# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

# CONSTANTS
W = 1920  # Width
H = 1080  # Height
M = 80    # Margin
U = 40    # Unit

# DRAWS A GRID
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

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0.8)
    rect(-2, -2, W+2, H+2)

# Set Font
font("fonts/Inter.otf")
for axis, data in listFontVariations().items():
    print((axis, data))

new_page() #--------------------------------------------------#
# SETUP
font("fonts/Inter.otf")
#grid() # Toggle for grid view
stroke(None)
fill(0)

# TYPEOGRAPHY
fontSize(U*0.9)
fontVariations(wght = 700 )
text("Eli Heuer",                          (M, (U*24)+4))
fontVariations(wght = 400 )
text("Design Brief, Research, and Sketches",  (M, (U*22)+4))
text("Arabic Type Design",                 (M, (U*21)+4))
text("Summer 2020",                        (M, (U*20)+4))

# IMAGES
image("images/qalam-photo.png", (M*11, M), alpha=1)
#image("images/ref-001.png", (M*19, M*5), alpha=1)
#image("images/ref-002.png", ((M*6)+U, M*4), alpha=1)

# Shapes
#oval(M*3,M,M,M)
#rect(M*2,M*4,M,M)

new_page() #--------------------------------------------------#
# SETUP
font("fonts/Inter.otf")
#grid() # Toggle for grid view
stroke(None)
fill(0)

brief = '''
The client for this project is a new small press book publishing project. This publisher aims to make inslamic studies material Bahai/babi/shaykhi avaiable in interlinear Arabic/Persian with latin transliteratio for a US audiance.

The style is Naskh with Persian influences. Based losly on the handwriting and calligraphy of Mírzá Ḥusayn-i-Isfahání AKA Mis͟hkín-Qalam, a calligrapher from 19th-century Persia.
'''
#fontSize(U*0.8)
#fontVariations(wght= 400 )
#textBox(brief,(M, M, M*10, (U*22)+4), align="left")

fontSize(U*0.8)
fontVariations(wght= 700 )
text("Design Brief",     (M,   (U*24)+4))
text("Function:",        (M,   (U*12)+4))
text("Personality:",     (M*12, (U*22)+4))
text("Characteristics:", (M*12, (U*12)+4))

fontVariations(wght= 400 )
text("The client for this project is a new small-press",     (M,   (U*22)+4))
text("book publishing project. The typeface will be used",     (M,   (U*21)+4))
text("instead of Amiri for interlinear typesetting and ",     (M,   (U*20)+4))
text("should be easy to read for adults learning Arabic.",     (M,   (U*19)+4))

text("The style is Naskh, with influences from Qajar era",     (M,   (U*17)+4))
text("Persian calligraphy and manuscripts. Specifically the",     (M,   (U*16)+4))
text("handwriting and calligraphy of Mírzá Ḥusayn-i-Isfahání",     (M,   (U*15)+4))
text("AKA Mis͟hkín-Qalam.",     (M,   (U*14)+4))

text("Islamic studies publishing",      (M,   (U*11)+4))
text("Interlinear typesetting",    (M,   (U*10)+4))
text("Manuscript translation",     (M,   (U*9)+4))
text("Qurʼān tajweed typesetting",             (M,   (U*8)+4))
text("Easy to read for children",  (M,   (U*7)+4))
text("Easy to read for adults learning Arabic",  (M,   (U*6)+4))
text("Good for pocket-size book printing",  (M,   (U*5)+4))

text("Futuristic",     (M*12, (U*21)+4))
text("Utopian",     (M*12, (U*20)+4))
text("Solarpunk",     (M*12, (U*19)+4))
text("Egalitarian", (M*12, (U*18)+4))
text("Simple", (M*12, (U*17)+4))
text("Global", (M*12, (U*16)+4))

text("Smallest possible file size",  (M*12,   (U*11)+4))
text("Easy to use with DrawBot/LaTeX",  (M*12,   (U*10)+4))
text("Big Arabic, small Latin",  (M*12,   (U*9)+4))
text("Slight nastaʼlīq pen angle",  (M*12,   (U*8)+4))
text("Slight nastaʼlīq pen rotation",  (M*12,   (U*7)+4))
text("Wide (variable font wdth axis?)",  (M*12,   (U*6)+4))
text("Good vertical metrics",  (M*12,   (U*5)+4))

#text("Personality:",     (M*12, (U*22)+4))
#text("Charicteristics:", (M*12, (U*10)+4))
image("images/qalam-001.gif",    (M*19, M), alpha=1)
image("images/qalam-002.gif",    (M*19, M*8), alpha=1)
image("images/qalam-003.gif",    (M*19, M*10), alpha=1)

new_page() #--------------------------------------------------#
font("fonts/Inter.otf")
#grid() # Toggle for grid view
stroke(None)
fill(0)

fontSize(U*0.8)
fontVariations(wght= 700 )
text("Amiri",             (M*19,  (U*18)+4))
fontVariations(wght= 400 )
text("By Khaled Hosny",  (M*19,  (U*17)+4))

fontVariations(wght= 700 )
text("Markazi Text",          (M*19,  (U*12)+4))
fontVariations(wght= 400 )
text("By Borna Izadpanah",    (M*19,  (U*11)+4))

fontVariations(wght= 700 )
text("Mirza",           (M*19,  (U*6)+4))
fontVariations(wght= 400 )
text("By KB Studio",    (M*19,  (U*5)+4))

# TYPEOGRAPHY
fontSize(U*0.8)
fontVariations(wght = 700 )
text("Research: Similar Typefaces",     (M,   (U*24)+4))

fontSize((M*1.5))
font("fonts/Amiri-Regular.ttf")
text("هل من مفرج غير الله قل سبحن الله", (M, U*18))

font("fonts/MarkaziText-Bold.ttf")
text("هل من مفرج غير الله قل سبحن الله", (M*2.3, U*12))

fontSize(M*1.4)
font("fonts/Mirza-Regular.ttf")
text("هل من مفرج غير الله قل سبحن الله", (M+U+(U*0.75), U*6))


new_page() #--------------------------------------------------#
font("fonts/Inter.otf")
grid() # Toggle for grid view
stroke(None)
fill(0)

# TYPEOGRAPHY
fontSize(U*0.9)
fontVariations(wght= 700 )
text("Sketches",                          (M, (U*24)+4))

# IMAGES
image("images/sketch-001.gif",    (M*2, M*2), alpha=1)
image("images/sketch-002.gif",    (M*13, M*2), alpha=1)

# Shapes
#rect(M*13,M*2,M*9,M*9)
#rect(M*2,M*2,M*9,M*9)


new_page() #--------------------------------------------------#
font("fonts/Inter.otf")
grid() # Toggle for grid view
stroke(None)
fill(0)

# TYPEOGRAPHY
fontSize(U*0.9)
fontVariations(wght= 700 )
text("Sketches",                          (M, (U*24)+4))

# IMAGES
image("images/sketch-003.gif",    (M*2, M*2), alpha=1)
image("images/sketch-004.gif",    (M*13, M*2), alpha=1)


new_page() #--------------------------------------------------#
font("fonts/Inter.otf")
grid() # Toggle for grid view
stroke(None)
fill(0)

# TYPEOGRAPHY
fontSize(U*0.9)
fontVariations(wght= 700 )
text("Calligraphy Sketches",                          (M, (U*24)+4))

# IMAGES
image("images/pen-001.gif",    (M*2, M*2), alpha=1)
image("images/pen-002.gif",    (M*13, M*2), alpha=1)

new_page() #--------------------------------------------------#
font("fonts/Inter.otf")
grid() # Toggle for grid view
stroke(None)
fill(0)

# TYPEOGRAPHY
fontSize(U*0.9)
fontVariations(wght= 700 )
text("Digital Sketches",                          (M, (U*24)+4))

# IMAGES
image("images/digi-001.gif",    (M*2, M*2), alpha=1)
image("images/digi-002.gif",    (M*13, M*2), alpha=1)

new_page() #--------------------------------------------------#
font("fonts/Inter.otf")
grid() # Toggle for grid view
stroke(None)
fill(0)

# TYPEOGRAPHY
fontSize(U*0.9)
fontVariations(wght= 700 )
text("Glyphs Sketch",                          (M, (U*24)+4))

# IMAGES
image("images/glyphs.png",    (0, 0), alpha=1)
#image("images/dsketch-001.gif",    (M*13, M*2), alpha=1)

saveImage("first-sketches.pdf")
