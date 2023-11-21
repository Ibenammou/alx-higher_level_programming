#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        safe = fct(*args)
        return safe
    except Exception as er:
        print("Exception:", er, file=sys.stderr)
        return None
