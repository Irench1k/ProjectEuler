import math


def three_digits_palindromic(number: int) -> bool:
    first_digit = number // 100
    last_digit = number % 10
    return first_digit == last_digit


def is_palindromic(number: int) -> bool:
    number_of_digits = int(math.log10(number)) + 1
    first_digit = number // 10**(number_of_digits - 1)
    last_digit = number % 10

    while first_digit == last_digit:
        pass