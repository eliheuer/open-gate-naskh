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
    stroke(0.2)
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

stroke(0.2)
fill(0)
rect(M*3,M*3, M*30, M*30)
stroke(None)

font("Input Mono Compressed")
fill(0.3)
fontSize(M*1)
text("GTL Naskh: 09-16-2020 Pre-alpha @ Git Commit 42cffeaa", (M*3.9, M*31))
text("WORK IN PROGRESS  https://gtl.world  WORK IN PROGRESS", (M*3.9, M*29))
text("WORK IN PROGRESS  https://gtl.world  WORK IN PROGRESS", (M*3.9, M*6))
text("Git Source: https://github.com/eliheuer/gtl-naskh.git", (M*3.9, M*4))

font("fonts/ttf/GTLNaskh-Regular.ttf")
fill(1)
#fontSize(M*1.5)
#text("الصلاة البهــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــائية الصغرى", (M*4, M*31))
#text("يا بهـــــــــــــــــــــــــــــــــــــــــــــــاء الأبهـــــــــــــــــــــــــــــــــــــــــــــــــــــى", (M*4, M*4))
fontSize(M*3)
text("أشــــــــــهد يا إلهي بأنّك خلقتني",               (M*4, M*25))
text("لعرفانك وعبادتــــــــــــــــــــــــــــــك",   (M*4, M*21))
text("أشــــــــــــــــــــــهد في هذا الحين",          (M*3.7, M*17))
text("بعجزي وقوّتك وضعـــــــــــــــــفي",                (M*3.9, M*13))
text("واقـــــــــــــتدارك وفقري وغنائك",               (M*4.1, M*9))
#text("لا إله إلاّ أنت المهيمن القيّوم",       (M*4, M*7))

# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
saveImage("documentation/instagram/salah-001.png")
print("\n[DrawBot]: specimen salah-1 updated")
