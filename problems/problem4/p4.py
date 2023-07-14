def palindromic_number(number1: int, number2: int):
    number = number1 * number2
    number = list(str(number))
    reversed_number = number[::-1]
    if number == reversed_number:
        return int(''.join([str(i) for i in number]))
    return "not a palidromic"


print(palindromic_number(999, 999))
