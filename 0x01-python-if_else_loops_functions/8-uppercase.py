#!/usr/bin/python3

def uppercase(str):
    for c in str:
        case = ord(c)
        if case >= 97 and case < 123:
            c = chr(case - 32)
        else:
            c = chr(case)
        print("{}".format(c), end='')
    print()
