#!/usr/bin/python3
from sys import argv

x, ret = 1, 0

if __name__ == '__main__':
    while x < len(argv):
        ret += int(argv[x])
        x += 1
    print(ret)
