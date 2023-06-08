#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    args = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if args != 3:
        print("Usage: ./100-my_calculator.py {} {} {}")
        exit (1)
    elif (operator != '+' and operator != '-' and operator != '*' and operator != '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)
    else:
        if operator == '+':
            result = a + b
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == '-':
            result = a - b
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == '*':
            result = a * b
            print("{} {} {} = {}".format(a, operator, b, result))
        elif operator == '/':
            result = a / b
            print("{} {} {} = {}".format(a, operator, b, result))
