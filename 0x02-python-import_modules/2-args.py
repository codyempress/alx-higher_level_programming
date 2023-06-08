#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv) - 1

    if num == 1:
        print("{} argument:".format(num))
        print("1: {}".format(sys.argv[1]))
    elif num == 0:
        print("0 arguments.")
    elif num > 1:
        print("{} arguments:".format(num))

        for ar in range(1, num + 1):
            print("{}: {}".format(ar, sys.argv[ar]))
