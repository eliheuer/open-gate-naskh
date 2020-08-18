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
    stroke(0.5,0,0)
    step_X = 0
    step_Y = 0
    increment_X = U
    increment_Y = U
    for x in range(36):
        polygon( (M+step_X, M), (M+step_X, H-M) )
        step_X += increment_X
    for y in range(36):
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
#grid() # Toggle for grid view

font("Helvetica Bold")
fontSize(M*0.75)
fill(0.9)
text("GTL Naskh", (M*1, M*34))
font("Helvetica")
text("Date: Mon Aug 17 01:11:23 PDT 2020", (M*1, M*32))
text("Git Repository: https://github.com/eliheuer/gtl-naskh.git", (M*1, M*31))
text("Git Commit: 6514145e7fdf58487dd883f1ebc639d0cb1702f1", (M*1, M*30))

font("fonts/ttf/GTLNaskh-Regular.ttf")
fontSize(M*2)

text("اأإ ب ببب ت تتت ث ثثث ج ججج ح ححح", (M*2.4, M*26))
text("خ خخخ د ذ ر ز و س سسس ش ششش", (M*4.8, M*23))
text("ص صصص ض ضضض ط ططط ظ ظظظ ع ععع", (M*2, M*20))
text("ف ففف ق ققق ك ككك ل للل م ممم ن ننن ههه", (M*2.2, M*17))

text("أشهد يا إلهي بأنّك خلقتني لعرفانك وعبادتك", (M*7, M*14))
text("أشهد في هذا الحين بعجزي وقوّتك", (M*11, M*11))
text("وضعفي واقتدارك وفقري وغنآئك", (M*14, M*8))
text("لا إله إلاّ أنت المهيمن القيّوم", (M*14.2, M*5))

fontSize(M*20)
text("و", (M*5, M*5))

fontSize(M*6)
text("يا بهاء", (M*24, M*30))
# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
saveImage("documentation/instagram/basic-specimen-001.png")
