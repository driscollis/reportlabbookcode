# util.py

import configparser
import importlib
import os

from stylesheets import default_stylesheet


class ConfigObj:
    """
    Create a configuration object
    """
    
    def __init__(self):
        cfg_path = 'config.ini'
        # Set some defaults
        self.logo_path = None
        self.right_margin = 36
        self.left_margin = 36
        self.top_margin = 18
        self.bottom_margin = 18
        self.style = None
        self.output_dir = None
        
        if os.path.exists(cfg_path):
            config = configparser.ConfigParser()
            config.read(cfg_path)
            self.logo_path = config.get('General', 'logo_path')
            self.right_margin = int(config.get('General', 'right_margin'))
            self.left_margin = int(config.get('General', 'left_margin'))
            self.top_margin = int(config.get('General', 'top_margin'))
            self.bottom_margin = int(config.get('General', 'bottom_margin'))
            self.style = config.get('General', 'style')
            self.output_dir = config.get('General', 'output_dir')


def get_stylesheet():
    """
    Returns the stylesheet object
    """
    config = ConfigObj()
    
    try:
        path = os.path.abspath(os.path.join('stylesheets', 
                                            '{}.py'.format(config.style)))
        spec = importlib.util.spec_from_file_location(config.style, path)
        stylesheet =  importlib.util.module_from_spec(spec)
        spec.loader.exec_module(stylesheet)
        getSampleStyleSheet = stylesheet.get_stylesheet
    except (ImportError, FileNotFoundError):
        getSampleStyleSheet = default_stylesheet.get_stylesheet
        
    return getSampleStyleSheet()