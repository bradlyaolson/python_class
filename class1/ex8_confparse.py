#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

def main():

    cisco_cfg = CiscoConfParse('cisco_ipsec.txt')
    crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")
    crypto_maps = crypto_maps[0]
    crypto_maps.all_children
for child in crypto_maps.all_children:
...   print child.text

    # 
    # for c_map in crypto_maps:
    #     print
    #     print c_map.text
    #     for child in c_map.children:
    #         print child.text
    # print
    #
if __name__ == "__main__":
    main()
