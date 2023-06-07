#!/usr/bin/python3

def uppercase(str):
    for c in str:
        case = ord(c)
        if case >= 97 and case < 123:
            print("{}".format(chr(case - 32)), end='')
        else:
            print(c, end='')
    print()
