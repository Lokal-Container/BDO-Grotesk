import os
import shutil
from fontTools.ttLib.woff2 import main as woff2_compress

currentDir = os.path.dirname(os.path.realpath(__file__))
ttfDir = os.path.join(currentDir, '../fonts/ttf')
ttfFiles = os.listdir(ttfDir)

def compress_woff2(file):
    woff2_compress(['compress', os.path.join(ttfDir, file)])
    move_woff2(ttfDir, file)

def move_woff2(ttfDir, filename):
    webFontDir = os.path.join(currentDir, '../fonts/webfonts')
    # if folder webfonts does not exist, create it
    if not os.path.exists(webFontDir):
        os.makedirs(webFontDir)
    # if file woff2 already exists, remove it
    if os.path.exists(os.path.join(webFontDir, filename.replace('.ttf', '.woff2'))):
        os.remove(os.path.join(webFontDir, filename.replace('.ttf', '.woff2')))
    # move woff2 file to webfonts folder
    shutil.move(os.path.join(ttfDir, filename.replace('.ttf', '.woff2')), webFontDir)

for ttf in ttfFiles:
    if ttf.endswith('.ttf'):
        compress_woff2(ttf)