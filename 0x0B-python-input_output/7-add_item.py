#!/usr/bin/python3
""" my module """
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Load existing list from the file if it exists
    m_list = load_from_json_file(filename)
except FileNotFoundError:
    # Create an empty list if the file doesn't exist
    m_list = []

