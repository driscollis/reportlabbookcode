# parsers.py

import json

from lxml import objectify


class JSON:
    """
    A way to "objectify" a json object to match
    the API we get from lxml.objectify
    """
    
    def __init__(self, data):
        self.member_name = data['patient']['member_name']
        self.member_id = data['patient']['member_id']
        self.group_num = data['patient']['group_num']
        self.group_name = data['patient']['group_name']
    
    
def parse_json(json_file):
    """
    Opens a JSON file and turns it into an object
    """
    with open(json_file) as f:
        data = json.load(f)
    
    return JSON(data)


def parse_xml(xml_file):
    """
    Opens an XML file and turns it into an lxml.objectify object
    """
    with open(xml_file) as f:
        xml = f.read()
        
    root = objectify.fromstring(xml)
    return root
