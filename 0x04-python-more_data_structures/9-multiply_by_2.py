#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary:
        dic = {}
        for k in a_dictionary.keys():
            dic[k] = a_dictionary[k] * 2
    return(dic)
