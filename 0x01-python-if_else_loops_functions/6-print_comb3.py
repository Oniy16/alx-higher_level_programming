#!/usr/bin/python3
for x in range(0, 10):
    for x2 in range(x + 1, 10):
        if x == 8 and x2 == 9:
            print("{}{}".format(x, x2))
        else:
            print("{}{}".format(x, x2), end=", ")
