# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# Note: Run this script from the project root directory with DrawBot installed in editable mode.
# Note: e.g. $ python3 documentation/slide-decks/final-project-presentation/final-project-presentation.py
# Typeface Used: https://github.com/undercasetype/Fraunces
# Typeface Used: https://input.fontbureau.com
# Unit Space: 72dpi (dots per inch)
from drawBot import *
from datetime import date
import math

# CONSTANTS
W = 1920  # Width
H = 1080  # Height
M = 80    # Margin
U = 40    # Unit
TODAY = str(date.today())

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
    fill(0.7)
    rect(-2, -2, W+2, H+2)

# Set & Test Font
font("fonts/Fraunces\[SOFT,WONK,opsz,wght\].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

new_page() #--------------------------------------------------#
# SETUP
font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
#font("fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf")
grid() # Toggle for grid view
stroke(None)
fill(0)


# IMAGES #----------------------------------------------------#
image("documentation/slide-decks/final-project-presentation/images/d-1920.jpg", (0, 0), alpha=1)

# TYPEOGRAPHY
fill(1)
fontSize(U*2.5)
fontVariations(wght = 700 )
text("Open Gate Naskh",                          (M, (U*23)+4))
font("fonts/InputMonoCompressed-Regular.ttf")
fontSize(U*0.8)
text("Final Project Presentation",  (M, (U*21)+4))
text("Arabic Type Design",                 (M, (U*20)+4))
text("Summer 2020",                        (M, (U*19)+4))
text("Eli Heuer",                          (M, (U*18)+4))
#image("images/ref-001.png", (M*19, M*5), alpha=1)
#image("images/ref-002.png", ((M*6)+U, M*4), alpha=1)
# Shapes #----------------------------------------------------#
#oval(M*3,M,M,M)
#rect(M*2,M*4,M,M)
#-------------------------------------------------------------#


new_page() #--------------------------------------------------#
# SETUP
#grid() # Toggle for grid view
stroke(None)
fill(0)
#rect(0,0,W,H)
#fill(1)

# TYPEOGRAPHY
fontSize(U*2.9)
font("fonts/ttf/OpenGateNaskh-Regular.ttf")
text("اأإآ ب ببب ت تتت ة ث ثثث ج ججج ح ححح",    (M+(U*1.2), U*22))
text("خ خخخ س سسس ش ششش ص صصص",               (M+(U*2.1), U*18))
text("ض ضضض ط ططط ظ ظظظ ع ععع ورزدذ",               (M+(U*0.6), U*14))
text("غ غغغ ف ففف ق ققق ك ككك ل للل م ممم",         (M+(U*1), U*10))
text("١٢٣٤٥٦٧٨٩٠ ن ننن ه ههه ي ييي لا لإ لأ  الله لله",         (M+(U*0.8), U*6))


stroke(0)
strokeWidth(2)
line( ( M, M+U ), ( W-M, M+U ) )
stroke(None)
font("fonts/InputMonoCompressed-Regular.ttf")
fontSize(U*0.8)
text("Page 2/9",                    (M, M))
text("Basic Glyph Set",          (M+(U*18.), M))
text(TODAY, (M+(U*39.8), M))



new_page() #--------------------------------------------------#
#grid() # Toggle for grid view
stroke(None)
fill(0)
#rect(0,0,W,H)
#fill(1)

# IMAGES #----------------------------------------------------#
image("documentation/slide-decks/final-project-presentation/images/a-1920.jpg", (0, 0), alpha=1)

# TYPEOGRAPHY
font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
#font("fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf")
fill(1)
fontSize(U*2.5)
fontVariations(wght = 700 )
text("Origins",                          (M, (U*23)+4))
font("fonts/InputMonoCompressed-Regular.ttf")
fontSize(U*0.8)
text("This typeface is",  (M, (U*21)+4))
text("designed for a small",                 (M, (U*20)+4))
text("book publishing project.",                        (M, (U*19)+4))




new_page() #--------------------------------------------------#
#grid() # Toggle for grid view
stroke(None)
fill(0)
#rect(0,0,W,H)
#fill(1)

# IMAGES #----------------------------------------------------#
image("documentation/slide-decks/final-project-presentation/images/h-1920.jpg", (0, -200), alpha=1)


new_page() #--------------------------------------------------#
#grid() # Toggle for grid view
stroke(None)
fill(0)
#rect(0,0,W,H)
#fill(1)

# IMAGES #----------------------------------------------------#
image("documentation/slide-decks/final-project-presentation/images/c-1920.jpg", (0, -100), alpha=1)

# TYPEOGRAPHY
font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
#font("fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf")
fill(1)
fontSize(U*2.5)
fontVariations(wght = 700 )
text("Design Details",                          (M, (U*23)+4))
font("fonts/InputMonoCompressed-Regular.ttf")
fontSize(U*0.8)
text("Git Repo:         https://github.com/eliheuer/open-gate-naskh",  (M, (U*21)+4))
text("License:          SIL Open Font License, Version 1.1",            (M, (U*20)+4))
text("Designer:         Eli Heuer",                                    (M, (U*19)+4))
text("Designer URL:     https://elih.blog",                       (M, (U*18)+4))
text("Manufacturer:     GTL Type Label",                          (M, (U*17)+4))
text("Manufacturer URL: https://gtl.world",                   (M, (U*16)+4))
text("Version:          Pre-Alpha",                           (M, (U*15)+4))
text("File Size:        24k",                           (M, (U*14)+4))
text("UPM:              1024",                    (M, (U*13)+4))



new_page() #--------------------------------------------------#
#grid() # Toggle for grid view
stroke(None)
fill(0)
#rect(0,0,W,H)
#fill(1)

# IMAGES #----------------------------------------------------#
image("documentation/slide-decks/final-project-presentation/images/f-1920.jpg", (0, -100), alpha=1)




new_page() #--------------------------------------------------#
# SETUP
#grid() # Toggle for grid view
stroke(None)
fill(0)
rect(0,0,W,H)
fill(1)



# TYPEOGRAPHY
font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
#font("fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf")
fill(1)
fontSize(U*2.5)
fontVariations(wght = 700 )
text("Example T",                          (M, (U*23)+4))
text("ext",                          (M+444, (U*23)+4))
#font("fonts/InputMonoCompressed-Regular.ttf")
#fontSize(U*0.8)
#text("Twitter:           @eliheuer",  (M, (U*21)+4))
#text("Instagram:         eli.heuer",            (M, (U*20)+4))
#text("Blog:              https://elih.blog",            (M, (U*19)+4))
#text("Email:             elih@protonmail.com",            (M, (U*18)+4))
# IMAGES #----------------------------------------------------#
#image("documentation/slide-decks/final-project-presentation/images/b-640.jpg", (U*22, U*9), alpha=1)

# TYPEOGRAPHY
fontSize(U*2.5)
stroke(None)
fill(1)
font("fonts/ttf/OpenGateNaskh-Regular.ttf")

text("كن فيكون",    (M+(U*34.5), M+(U*18)))
text("استان تهران",    (M+(U*35), M+(U*15)))
text("الكتاب",    (M+(U*37.9), M+(U*12)))
text("سبحان الله",    (M+(U*35.2), M+(U*9)))
text("مشكین قلم",    (M+(U*34), M+(U*6)))
text("الرحمـن الرحيم",    (M+(U*33.2), M+(U*3)))



txt = '''الحمد لله الّذي أنطق ورقاء البيان على أفنان دوحة التّبيان بفنون الألحان على أنّه لا إله إلّا هو قد أبدع الأكوان واخترع الإمكان بمشيّته الأوّليّة الّتي بها خلق ما كان وما يكون والحمد لله لّذي سماءَ الحقيقة بشمس المعاني والعرفان الّتي رُقم عليها من القلم الأعلى الملك لله المقتدر المهيمن القيّوم الّذي أظهر البحرَ الأعظم المجتمعَ من الماء الجاري من عين الهاء المنتهية إلى الاسم الأقدم الّذي منه فصّلت النّقطة الأوّليّة وظهرت الكلمة الجامعة وبرزت الحقيقة والشّريعة ومنه طار الموحّدون إلى هواء المكاشفة والحضور والمخلصون إلى منظر ربّهم العزيز الودود والصّلاة والسّلام على مطلع الأسماء الحسنى والصّفات العليا الّذي في كلّ حرف من إسمه كُنِزت الأسماء وبه زُيِّن الوجود من الغيب والشّهود وسُمّي بمحمّد في ملكوت الأسماء وبأحمد في جبروت البقاء وعلى آله وصحبه من هذا اليوم إلى يوم فيه ينطق لسان العظمة الملك لله الواحد القهّار قد حضر بين يدينا كتابُكَ واطّلعنا على ما فيه من إشاراتك نسأل الله أن يؤيّدك على ما يحبّ ويرضى ويقرّبَك إلى ساحل البحر الّذي يموج باسم ربّك الأعلى وتنطق كلّ قطرة منه إنّه لا إله إلّا هو وإنّه لخالق الأسماء وفاطر السّماء'''

# create a formatted string
t = FormattedString(fontSize=U*2.)
# set alignment
t.align("justified")
# add text
t.font("fonts/ttf/OpenGateNaskh-Regular.ttf")
t.fill(1)
t.lineHeight(U*3.)
t += txt
t += "\n"
t.fill(1)
textBox(t, (U*16, U*4, U*17, U*18))

# create a formatted string
t = FormattedString(fontSize=U*1.)
# set alignment
t.align("justified")
# add text
t.font("fonts/ttf/OpenGateNaskh-Regular.ttf")
t.fill(1)
t.lineHeight(U*1.5)
t += txt
t += "\n"
textBox(t, (M*1, U*4, U*11, U*17))

stroke(1)
strokeWidth(2)
line( ( M, M+U ), ( W-M, M+U ) )
stroke(None)
fill(1)
font("fonts/InputMonoCompressed-Regular.ttf")
fontSize(U*0.8)
text("Page 7/9",                    (M, M))
text("Example Text",          (M+(U*19.5), M))
text(TODAY, (M+(U*39.8), M))





new_page() #--------------------------------------------------#
#grid() # Toggle for grid view
stroke(None)
fill(0)
#rect(0,0,W,H)
#fill(1)

# IMAGES #----------------------------------------------------#
image("documentation/slide-decks/final-project-presentation/images/e-1920.jpg", (0, -100), alpha=1)
















new_page() #--------------------------------------------------#
# SETUP
grid() # Toggle for grid view
stroke(None)
fill(0)
rect(0,0,W,H)
fill(1)



# TYPEOGRAPHY
font("fonts/Fraunces[SOFT,WONK,opsz,wght].ttf")
#font("fonts/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf")
fill(1)
fontSize(U*2.5)
fontVariations(wght = 700 )
text("Thank Y",                          (M, (U*23)+4))
text("ou!",                          (M+350, (U*23)+4))
font("fonts/InputMonoCompressed-Regular.ttf")
fontSize(U*0.8)
text("Twitter:           @eliheuer",  (M, (U*21)+4))
text("Instagram:         eli.heuer",            (M, (U*20)+4))
text("Blog:              https://elih.blog",            (M, (U*19)+4))
text("Email:             elih@protonmail.com",            (M, (U*18)+4))

# IMAGES #----------------------------------------------------#
image("documentation/slide-decks/final-project-presentation/images/b-640.jpg", (U*22, U*9), alpha=1)

# TYPEOGRAPHY
fontSize(U*10)
stroke(2)
fill(0)
font("fonts/ttf/OpenGateNaskh-Regular.ttf")

for i in range(19):
    text("شكرا",    ((M+(U*0))+(i*24), (U*6.5)+(i*8)))


stroke(1)
strokeWidth(2)
line( ( M, M+U ), ( W-M, M+U ) )
stroke(None)
fill(1)
font("fonts/InputMonoCompressed-Regular.ttf")
fontSize(U*0.8)
text("Page 9/9",                    (M, M))
text("Thank You!",          (M+(U*19.), M))
text(TODAY, (M+(U*39.8), M))


# Saving and post-processing
saveImage("documentation/slide-decks/final-project-presentation/eli-heuer-final-project-presentation.pdf")
print("Updated final slide deck")
