#!/usr/bin/python3
def magic_calculation(a, b):
    """magic_calculation

    Args:
        a:
        b:

    Return:
        Bytecodes
    """
    if a < b:
        ret = a + b
    elif a > b:
        ret = a * b
    elif a == b:
        ret = a % b
    else:
        ret = None
    return ret
