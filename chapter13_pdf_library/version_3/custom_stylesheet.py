# custom_stylesheet.py

from reportlab.lib.colors import blue
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.fonts import tt2ps
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.rl_config import canvas_basefontname as _baseFontName

_baseFontNameB = tt2ps(_baseFontName,1,0)
_baseFontNameI = tt2ps(_baseFontName,0,1)
_baseFontNameBI = tt2ps(_baseFontName,1,1)


def get_custom_stylesheet_1():
    """
    Create and return a custom stylesheet
    """
    stylesheet = StyleSheet1()
    
    stylesheet.add(ParagraphStyle(name='Normal',
                                  fontName=_baseFontName,
                                  fontSize=12,
                                  leading=14,
                                  textColor=blue)
                   )

    stylesheet.add(ParagraphStyle(name='BodyText',
                                  parent=stylesheet['Normal'],
                                  spaceBefore=6)
                   )
    
    stylesheet.add(ParagraphStyle(name='Italic',
                                  parent=stylesheet['BodyText'],
                                  fontName = _baseFontNameI)
                   )
    
    stylesheet.add(ParagraphStyle(name='Bold',
                                  parent=stylesheet['BodyText'],
                                  fontName = _baseFontNameB)
                   )    

    stylesheet.add(ParagraphStyle(name='Heading1',
                                  parent=stylesheet['Normal'],
                                  fontName = _baseFontNameB,
                                  fontSize=20,
                                  leading=24,
                                  spaceAfter=6),
                   alias='h1')
    
    return stylesheet