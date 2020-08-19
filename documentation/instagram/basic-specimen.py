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
text("Foundry: https://gtl.world", (M*1, M*29))

font("fonts/ttf/GTLNaskh-Regular.ttf")
fontSize(M*2)

text("اأإ ب ببب ت تتت ث ثثث ج ججج ح ححح", (M*2.9, M*26))
text("خ خخخ دذرزو س سسس ش ششش ه ههه", (M*3, M*23))
text("ص صصص ض ضضض ط ططط ع ععع غ غغغ", (M*3.2, M*20))
text("غ غغغ ف ففف ق ققق ك ككك ل للل م ممم ن ننن", (M*2.1, M*17))

text("أشــــــــهد يا إلهي بأنّك خلقتني لعرفانك وعبادتك", (M*1, M*14))
text("أشـــــــــــــــــهد في هذا الحين بعجزي وقوّتك", (M*1, M*11))
text("وضعفي واقتدارك وفقري وغنائك لا إله إلاّ أنـــت", (M*1, M*8))
text("لا إله إلاّ أنت المهيمن القيّوم", (M*14.1, M*5))
text("يا بهاء الأبــــــــــــــهى", (M*1, M*2))


# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
saveImage("documentation/instagram/basic-specimen-001.png")
print("\n[DrawBot]: specimens updated")
