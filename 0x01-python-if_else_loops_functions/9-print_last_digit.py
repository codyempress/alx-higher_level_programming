#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1

    new = number % 10
    print(new, end='')
    return new
