# find_installed_fonts.py

import os

from fontTools import ttLib
from reportlab import rl_settings

def find_installed_ttf_fonts():
    installed_fonts = []
    for folder in rl_settings.TTFSearchPath:
        if os.path.exists(folder):
            for entry in os.scandir(folder):
                if entry.name.endswith('.ttf'):
                    installed_fonts.append(entry.path)
    return installed_fonts

def get_font_names(font_paths):
    fonts = {}
    for font in font_paths:
        tt = ttLib.TTFont(font)
        name = ''
        family = ''
        for record in tt['name'].names:
            if record.nameID == 4 and not name:
                if '\000' in str(record.string):
                    name = unicode(record.string, 'utf-16-be').encode('utf-8')
                else:
                    name = record.string
            elif record.nameID == 1 and not family:
                if '\000' in str(record.string):
                    family = unicode(record.string, 'utf-16-be').encode('utf-8')
                else:
                    family = record.string
            if name and family:
                break
        fonts[name] = font
    return fonts


if __name__ == '__main__':
    paths = find_installed_ttf_fonts()
    get_font_names(paths)