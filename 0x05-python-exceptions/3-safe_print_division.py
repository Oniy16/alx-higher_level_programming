#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0

    try:
        c = a / b
    except zeroDivisionError:
        result  = None
    finally:
        print('Inside result: {}'.format(result))
        return result
