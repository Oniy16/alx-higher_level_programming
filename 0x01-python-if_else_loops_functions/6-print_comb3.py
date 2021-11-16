#!/usr/bin/python3
for i in range(48, 58):
    x = i+1
    for x in range(48, 58):
        print('{}{}'.format(chr(i),chr(x), end=", "))
