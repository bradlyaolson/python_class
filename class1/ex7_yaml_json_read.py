#!/usr/bin/env python
'''
Write a Python program that reads both the YAML file and the JSON file created
in exercise6 and pretty prints the data structure that is returned.
'''

import yaml
import json

from pprint import pprint as pp

def output_format(list_1, str_1):

    print '\n\n'
    print str_1
    pp(list_1)

def main():

    yaml_file = 'yaml_file.yml'
    json_file = 'json_file.json'

    with open(yaml_file) as f:
        yaml_list = yaml.load(f)

    with open(json_file) as f:
        json_list = json.load(f)

    output_format(yaml_list, ' YAML File:')
    output_format(json_list, ' JSON File:')
    print '\n'

if __name__ == "__main__":
    main()
