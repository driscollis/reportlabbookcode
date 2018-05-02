# parsers.py

import json

from lxml import objectify

class String(str):
    """
    Custom string sub-class to emulate the "strings"
    returned from lxml
    """
    
    @property
    def text(self):
        """
        Return the str
        """
        return self

class Claim:
    """
    Represents the data that makes up a claim
    """
    
    def __init__(self, data):
        self.amount_billed = String(data['amount_billed'])
        self.amount_remaining = String(data['amount_remaining'])
        self.coinsurance = String(data['coinsurance'])
        self.copay = String(data['copay'])
        self.deductible = String(data['deductible'])
        self.description = String(data['description'])
        self.member_rate = String(data['member_rate'])
        self.pending = String(data['pending'])
        self.plan_pays = String(data['plan_pays'])
        self.received_date = String(data['received_date'])
        self.total_owed = String(data['total_owed'])


class Claims:
    """
    Represents a series of Claim objects
    """
    
    def __init__(self, data):
        """
        Accepts a data dictionary and turns it into a
        claim object
        """
        self.data = data
    
    def getchildren(self):
        """
        Return all the children claim
        """
        data_claims = self.data['patient']['claims']['claim']
        claims = []
        if isinstance(data_claims, dict):
            # only a single claim exists
            claim = Claim(data_claims) 
            claims.append(claim)
        else:
            # claims is a list
            for claim in data_claims:
                claims.append(Claim(claim))
        return claims
    

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
        self.claim_id = data['patient']['claim_id']
        self.date = data['patient']['date']
        self.received_date = data['patient']['received_date']
        self.sent_to = data['patient']['sent_to']
        self.amount_owed = data['patient']['amount_owed']
        self.amount_paid = data['patient']['amount_paid']
        
        self.claims = Claims(data)
        
    
    
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
