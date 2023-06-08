#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = int(len(sys.argv) - 1)
    total = 0

    for i in range(1, num + 1):
        arg = sys.argv[i]
        total += int(arg)

    print(total)
