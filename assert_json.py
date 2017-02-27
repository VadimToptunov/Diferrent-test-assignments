# "__author__" == "Vadim Toptunov"
# -*- coding: utf-8 -*-

# Script to compare a json with some ethalone JSON file.

import difflib

ethalone = "/your/ethalon/file/file.json"
json = raw_input("Input JSON file to compare with the ethalone: ")
# Set a json file to compare with the ethalone manually.


def assert_json(json, ethalone):
    if json.endswith(".json"):
        # Check the file has a json extension to prevent comparison with some other files than json
        with open(ethalon, 'r') as eth, open(json, 'r') as jso:
            # Open ethalon and the json to read
            rd1 = eth.read().splitlines()
            rd2 = jso.read().splitlines()
            difference = difflib.ndiff(rd1, rd2)
            # Find the difference between the files.
            for dff in difference:
                if not dff.startswith('+ '):
                    pass
                # Do nothing if the lines in files are identical or unique to ethalone
                else:
                    print "Here\'s a difference with the ethalone: \n"
                    for diff in difference:
                        if diff.startswith('+ '):
                            # Print lines which are unique to json.
                            print diff
                        else:
                            pass
    else:
        pass

assert_json(json, ethalone)
