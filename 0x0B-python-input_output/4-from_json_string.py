#!/usr/bin/python3
""" module """
import json


def from_json_string(my_str):
    """ From JSON string to Object function """
    return json.loads(my_str)
