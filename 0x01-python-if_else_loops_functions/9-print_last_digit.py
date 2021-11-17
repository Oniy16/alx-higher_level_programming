#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number and return it."""
    if number >= 0:
        last_digit = number % 10
    elif number < 0:
        last_digit = (number * -1) % 10

    print(last_digit, end='')
    return last_digit
