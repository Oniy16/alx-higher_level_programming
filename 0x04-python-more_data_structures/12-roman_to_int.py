#!/usr/bin/python3

# 12-roman_to_int.py
# Yonatan Ashenafi <yonathanashenafi@gmail.com>


def roman_to_int(roman_string):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M': 1000}
    if not isinstance(roman_string, str):
        return (0)
    no = 0

    for x in range(len(roman_string)):
        if roman.get(roman_string[x], 0) == 0:
          return (0)

      if (x != (len(roman_string) - 1 ) and
            roman[roman_string[x]] < roman[roman_string[x + 1]]):
            no += roman[roman_string[x]] * -1

      else:
          no += roman[roman_string[x]]
    return (no)
