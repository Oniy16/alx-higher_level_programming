#!/usr/bin/python
def divisible_by_2(my_list=[]):
    result = []
    for x in range(len(my_list)):
        if my_list [x] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
