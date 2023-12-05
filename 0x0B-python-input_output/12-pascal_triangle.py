#!/usr/bin/python3
"""Define the pascal triangle"""


def pascal_triangle(n):
    """ Pascal Triangle"""
    ret = []
    if n <= 0:
        return ret
    for r in range(n):
        for c in range(r + 1):
            if c == 0:
                ret.append([1])
            elif c == r:
                ret[r].append(1)
            else:
                ret[r].append(ret[r - 1][c] + ret[r - 1][c - 1])
    return ret
