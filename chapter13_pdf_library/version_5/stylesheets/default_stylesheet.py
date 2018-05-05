# default_stylesheet.py

from reportlab.lib.fonts import tt2ps
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.rl_config import canvas_basefontname as _baseFontName

_baseFontNameB = tt2ps(_baseFontName,1,0)
_baseFontNameI = tt2ps(_baseFontName,0,1)
_baseFontNameBI = tt2ps(_baseFontName,1,1)


def get_stylesheet():
    """
    Create and return a custom default stylesheet
    """
    stylesheet = getSampleStyleSheet()
    
    stylesheet.add(ParagraphStyle(name='Bold',
                                  parent=stylesheet['BodyText'],
                                  fontName = _baseFontNameB)
                   )
    return stylesheet
    
