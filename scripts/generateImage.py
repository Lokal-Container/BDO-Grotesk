from drawBot import *
from fontTools.ttLib import TTFont
import os

green = (60/225,181/225,74/225)

variablePath = './fonts/variable'
filename = os.listdir(variablePath)
fontfile = variablePath + f"/{filename[0]}"
w,h = 2000, 1000
newPage(w,h)
ttLibFont = TTFont(variablePath + f"/{filename[0]}")
fontName = ttLibFont['name'].getBestFamilyName()
chars="""AaBbCcDd
0123456789
↱?!#@%&
"""
fill(1)
rect(0,0,w,h)
fill(*green)
fontSize(200)
font(variablePath + f"/{filename[0]}")

text(f"“{fontName}”\n{chars}", (w/2,h/1.35), align='center')

readmeFilePath = "![filename](filename.png)"
filePath = f"./documentation/images/{fontName.replace(' ','')}.png"

saveImage(f"./documentation/images/{fontName.replace(' ','')}.png")

with open('README.md', 'r') as f:
    data = f.read()
    
data= data.replace(readmeFilePath, f"![{fontName.replace(' ','')}Image]({filePath})")
print(data)
with open('README.md', 'w') as f:
    f.write(data)
