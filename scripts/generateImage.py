from drawBot import *
from fontTools.ttLib import TTFont
import os

def getMaxValue(font):
    instanceList = list(listFontVariations(font).items())
    if listFontVariations(font)['wght']:
        defaultValue = listFontVariations(font)['wght']['maxValue']
        axis = 'wght'
    elif listFontVariations(font)['wdth']:
        defaultValue = listFontVariations(font)['wdth']['defaultValue']
        axis = 'wdth'
    
    return axis, defaultValue

green = (60/225,181/225,74/225)

variablePath = './fonts/variable'
filename = os.listdir(variablePath)
fontfile = variablePath + f"/{[x for x in filename if '.ttf' in x][0]}"

w,h = 2000, 1000

ttLibFont = TTFont(fontfile)
fontName = ttLibFont['name'].getBestFamilyName()
version = ttLibFont['name'].getName(5,3,1)
designer = ttLibFont['name'].getName(9,3,1)
axis, defaultValue = getMaxValue(fontfile)
print(axis, defaultValue)

newPage(w,h)
fill(*green)
rect(0,0,w,h)
fill(0)
font(fontfile)

with savedState():
    fontSize(250)
    if axis == 'wght':
        fontVariations(wght=defaultValue)
    elif axis == 'wdth':
        fontVariations(wdth=defaultValue)

    text(f"{fontName}", (w/2,h/2.2), align='center')
fontSize(45)
font
text(f"{designer}", (w/2,h/3.6), align='center')
readmeFilePath = "![filename](filename.png)"
filePath = f"./documentation/images/{fontName.replace(' ','')}.png"

saveImage(f"./documentation/images/{fontName.replace(' ','')}.png")

with open('README.md', 'r') as f:
    data = f.read()
    
data= data.replace(readmeFilePath, f"![{fontName.replace(' ','')}Image]({filePath})")

with open('README.md', 'w') as f:
    f.write(data)
