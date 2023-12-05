#!/usr/bin/python3
""" my module """
import json


def save_to_json_file(my_obj, filename):
    """ Save Object to file  """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
