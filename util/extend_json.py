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

def flatten_dict(mydict):
        result = {}
        for key, value in mydict.iteritems():
                result["name"] = key
                if isinstance(value, dict):
                        mylist = []
#                        for k, v in value.iteritems():
#                            r["name"] = key;
#                            r["children"] = flatten_list(value)
                        mylist.append(flatten_dict(value))
                        result["children"] = mylist
                if isinstance(value, list):
                        result["children"] = flatten_list(value)

        return result

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
        result = {}
        result["children"] = result_list;
        return result;

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
