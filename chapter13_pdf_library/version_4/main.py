# main.py

import argparse
import os
import pdf_creator

from parsers import parse_json, parse_xml


def get_args():
    parser = argparse.ArgumentParser(
            description="Custom PDF Header with Logos")
    parser.add_argument('-d', '--data_file', 
                        action='store',
                        required=True,
                        help="The data file path",
                        dest='data_file')
    parser.add_argument('-f', '-filepath', '--filepath',
                        action='store',
                        required=True,
                        help="The output file path",
                        dest='path')
    arguments = parser.parse_args()

    return arguments


def main():
    arguments = get_args()
    supported_ext_types = ['.json', '.xml']
    
    # Get the file extension
    _, ext = os.path.splitext(arguments.data_file)
    
    if ext not in supported_ext_types:
        msg = 'PDF Creator only accepts the following file types: ' \
        '{}. Got {}'
        raise RuntimeError(msg.format(str(supported_ext_types, ext)))
        
    if ext == '.xml':
        data = parse_xml(arguments.data_file)
    elif ext == '.json':
        data = parse_json(arguments.data_file)
        
    eob = pdf_creator.EOB(data,
                          pdf_file=arguments.path)
    eob.save()
    
if __name__ == '__main__':
    main()