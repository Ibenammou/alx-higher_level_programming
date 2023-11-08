#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        lis = []
        for n in my_list:
            if n == search:
                lis.append(replace)
            else:
                lis.append(n)
        return(lis)
    else:
        return(my_list)
