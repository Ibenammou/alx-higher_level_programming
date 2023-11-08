#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        key = ""
        scoreMax = 0
        for k in a_dictionary.keys():
            if a_dictionary[k] > scoreMax:
                key = k
                scoreMax = a_dictionary[k]
        return(key)
    else:
        return(None)
