#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        black_list = []
        som = 0
        for i in my_list:
            if i not in black_list:
                som += i
                black_list.append(i)
        return(som)
