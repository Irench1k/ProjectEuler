def is_palindromic(number):
    number = list(str(number))
    reversed_number = number[::-1]
    if number == reversed_number:
        return int(''.join([str(i) for i in number]))
    return "not a palidromic"


print(is_palindromic(23))
