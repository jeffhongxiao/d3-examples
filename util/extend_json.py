#!/usr/bin/env python2

import json
import sys

def load_data(filename):
        with open(filename) as data_file:
                data = json.load(data_file)
                return data

def json_pprint(json_obj):
        print json.dumps(json_obj,
        sort_keys=False, indent=2, separators=(',', ': '))

def flatten_list(mylist):
        result = []
        for item in mylist:
                entry = {}
                entry["name"] = item
                result.append(entry)
        return result

def smart_flatten(myobj):
    if isinstance(myobj, list):
        result_list = flatten_list(myobj);
        return result_list;

    if isinstance(myobj, dict):
        result_list = []
        for key, value in myobj.iteritems():
            r = {}
            r["name"] = key
            r["children"] = smart_flatten(value)

            result_list.append(r)
        return result_list;

if __name__ == "__main__":
        data = load_data("input.json")
        ####data = load_data(sys.stdin)

        mydict = smart_flatten(data)
        json_pprint(mydict)
