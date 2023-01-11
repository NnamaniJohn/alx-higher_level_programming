#!/usr/bin/python3

"""add item module"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    my_data = load_from_json_file(filename)
except Exception:
    my_data = []

for i in range(1, len(sys.argv)):
    my_data.append(sys.argv[i])

save_to_json_file(my_data, filename)
