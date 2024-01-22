import os
import shutil
from fontTools.ttLib.woff2 import main as woff2_compress
from fontTools.ttLib import TTFont

currentDir = os.path.dirname(os.path.realpath(__file__))
ttfDir = os.path.join(currentDir, '../fonts/ttf')
ttfFiles = os.listdir(ttfDir)
varDir = os.path.join(currentDir, '../fonts/variable')
varFiles = os.listdir(varDir)

def compress_woff2(Dir, file):
    woff2_compress(['compress', os.path.join(Dir, file)])
    move_woff2(Dir, file)

def move_woff2(Dir, filename):
    # check if the file is a static font or variable font

    webFontDir = os.path.join(currentDir, '../fonts/webfonts')
    webVarDir = os.path.join(currentDir, '../fonts/webfonts/variable')
    
    font = TTFont(os.path.join(Dir, filename))

    if 'fvar' in font:
        if not os.path.exists(webVarDir):
            os.makedirs(webVarDir)

        if os.path.exists(os.path.join(webVarDir, filename.replace('.ttf', '.woff2'))):
            os.remove(os.path.join(webVarDir, filename.replace('.ttf', '.woff2')))

        shutil.move(os.path.join(varDir, filename.replace('.ttf', '.woff2')), webVarDir)
        print('Moved to webfonts/variable folder: ' + filename.replace('.ttf', '.woff2'))

    if not 'fvar' in font:
        if not os.path.exists(webFontDir):
            os.makedirs(webFontDir)

        if os.path.exists(os.path.join(webFontDir, filename.replace('.ttf', '.woff2'))):
            os.remove(os.path.join(webFontDir, filename.replace('.ttf', '.woff2')))

        shutil.move(os.path.join(ttfDir, filename.replace('.ttf', '.woff2')), webFontDir)
        print('Moved to webfonts folder: ' + filename.replace('.ttf', '.woff2'))


if __name__ == '__main__':
    if ttfFiles:
        print('Compressing TTF files...')
        for file in ttfFiles:
            if file.endswith('.ttf'):
                compress_woff2(ttfDir, file)
    
    if varFiles:
        print('Compressing variable TTF files...')
        for file in varFiles:
            if file.endswith('.ttf'):
                compress_woff2(varDir, file)