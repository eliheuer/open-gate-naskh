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

txt = '''الحمد لله الّذي أنطق ورقاء البيان على أفنان دوحة التّبيان بفنون الألحان على أنّه لا إله إلّا هو قد أبدع الأكوان واخترع الإمكان بمشيّته الأوّليّة الّتي بها خلق ما كان وما يكون والحمد لله الّذي زيَّن سماءَ الحقيقة بشمس المعاني والعرفان الّتي رُقم عليها من القلم الأعلى الملك لله المقتدر المهيمن القيّوم الّذي أظهر البحرَ الأعظم المجتمعَ من الماء الجاري من عين الهاء المنتهية إلى الاسم الأقدم الّذي منه فصّلت النّقطة الأوّليّة وظهرت الكلمة الجامعة وبرزت الحقيقة والشّريعة ومنه طار الموحّدون إلى هواء المكاشفة والحضور والمخلصون إلى منظر ربّهم العزيز الودود والصّلاة والسّلام على مطلع الأسماء الحسنى والصّفات العليا الّذي في كلّ حرف من إسمه كُنِزت الأسماء وبه زُيِّن الوجود من الغيب والشّهود وسُمّي بمحمّد في ملكوت الأسماء وبأحمد في جبروت البقاء وعلى آله وصحبه من هذا اليوم إلى يوم فيه ينطق لسان العظمة الملك لله الواحد القهّار قد حضر بين يدينا كتابُكَ واطّلعنا على ما فيه من إشاراتك نسأل الله أن يؤيّدك على ما يحبّ ويرضى ويقرّبَك إلى ساحل البحر الّذي يموج باسم ربّك الأعلى وتنطق كلّ قطرة منه إنّه لا إله إلّا هو وإنّه لخالق الأسماء وفاطر السّماء'''


# create a formatted string
t = FormattedString(fontSize=U*2.)
# set alignment
t.align("justified")
# add text

t.font("fonts/ttf/OpenGateNaskh-Regular.ttf")
t.lineHeight(U*4.)
t += txt
t += "\n"
textBox(t, (U*8, U*8.3, U*24, U*42))


fill(0)
stroke(0)
rect(U*12.5, U*55.5, U*16, U*4)
fill(1)
rect(U*12, U*56, U*16, U*4)

stroke(None)
fill(0)
font("fonts/ttf/OpenGateNaskh-Regular.ttf")
fontSize(U*2)
text("تفسير سورة الشمس",              (U*13.5,  U*57.5))
fontSize(U*2)
text("بســــــــــــــــــــــــم الله الرحمـن الرحيم",              (U*11.7,  U*52))

# TYPEOGRAPHY
# SAVE THE IMAGE IN THIS SCRIPT'S DIRECTORY LOCATION
# POST-PROCESS: gifsicle -i text-specimen.gif --optimize=16 -o output.gif
# POST_PROCESS: pdfjam --nup 2x1 booklet-test-verso.pdf booklet-test-recto.pdf --landscape --outfile out.pdf
saveImage("documentation/print/booklet-shams-verso.pdf")
