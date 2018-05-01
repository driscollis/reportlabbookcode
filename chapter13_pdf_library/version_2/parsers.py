# parsers.py

import json

from lxml import objectify


class Claim:
    
    def __init__(self, data):
        """
        Accepts a data dictionary and turns it into a
        claim object
        """
        pass

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
        
        self.claims = []
        data_claims = ['patient']['claims']['claim']
        if isinstance(data_claims, dict):
            # only a single claim exists
            claim = Claim(data_claims) 
            self.claims.append(claim)
        else:
            # claims is a list
            for claim in data_claims:
                self.claims.append(Claim(claim))
    
    
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
