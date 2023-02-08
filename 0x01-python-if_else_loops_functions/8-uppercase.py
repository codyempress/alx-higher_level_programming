#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) <= 123 and ord(i) >= 97:
            print("{}\n".format(chr(ord(i) - 32)), end='')
        else:
            print("{}\n".format(i), end='')
