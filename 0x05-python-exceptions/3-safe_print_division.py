#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except zeroDivisionError:
        c  = None
    finally:
        print('Inside result: {}'.format(result))
        return result
