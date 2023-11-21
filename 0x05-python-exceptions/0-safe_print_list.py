#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_to_prt = 0

    try:
        for index in my_list:
            if num_to_prt < x:
                print(index, end="")
                num_to_prt += 1
    except error as er:
        print("An error occurred:", er)

    print()
    return num_to_prt
