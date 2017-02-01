#!/usr/bin/env python
import yaml
import json

def dump():
    yaml_file = 'ex6_test.yml'
    json_file = 'ex6_test.json'

    dict_1 = {
        'ip_addr': '10.10.10.10',
        'Device_Type': 'Router',
        'Platform': 'DC',
        'model':    '2951'
    }

    list_1 = {
        'confreg',
        'uptime',
        'dir',
        dict_1
    }

    with open("yaml_file", "w") as f:
        f.write(yaml.dump(list_1, default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(list_1, f)

if __name__ == "__main__":
    dump()
