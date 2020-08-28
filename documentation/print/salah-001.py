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
    strokeWidth(2)
    stroke(0.1)
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

# MAIN
new_page()
#grid() # Toggle for grid view

font("fonts/ttf/GTLNaskh-Regular.ttf")
fill(0)
fontSize(M*1.5)
text("الصلاة البهـــــــــــــــــــــــــــــــــــــــــــــــــائية الصغرى", (M*3, M*34))
text("يا بهــــــــــــــــــــــــــــــــاء الأبهــــــــــــــــــــــــــــــــــى", (M*3, M*1.1))
fontSize(M*3)
text("أشـــــهد يا إلهي بأنّك خلقتني", (M*3.3, M*30))
text("لعرفانك وعبادتــــــــــــــــــك", (M*3.1, M*25))
text("أشـــــــــــــهد في هذا الحين", (M*3.1, M*20))
text("بعجزي وقوّتك وضعـــــــــــفي", (M*3.2, M*15))
text("واقــــــتدارك وفقري وغنآئك", (M*3.2, M*10))
text("لا إله إلاّ أنت المهيمن القيّوم", (M*3, M*5))

# Boarder
strokeWidth(4)
stroke(0)
fill(None)
oval(M*1, M*1, M*1, M*1)
oval(M*1, M*34,M*1, M*1)
oval(M*34,M*34,M*1, M*1)
oval(M*34,M*1, M*1, M*1)
lineCap("round")
line((M*1.5, M*3),  (M*1.5, M*33))
line((M*34.5, M*3), (M*34.5, M*33))
#line((M*3,M*34.5),  (M*33, M*34.5))
#line((M*3,M*1.5),   (M*33, M*1.5))

# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
saveImage("documentation/print/salah-001.pdf")
print("\n[DrawBot]: specimen salah-001 pdf updated")
