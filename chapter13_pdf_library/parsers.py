import json


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
    with open(json_file) as f:
        data = json.load(f)
    
    return JSON(data)