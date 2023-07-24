def is_palindromic(number: int) -> bool:
    number_as_list = list(str(number))
    reversed_number_list = number_as_list[::-1]
    reversed_number_str = ''.join(reversed_number_list)
    reversed_number = int(reversed_number_str)
    if reversed_number == number:
        return True
    return False


def solution(number_of_digits: int) -> int | None:
    lower_border = 10**(number_of_digits - 1)
    # since the range not inclusive the last integer, I removed "+ 1"
    upper_border = 10**(number_of_digits)
    products: list[int] = []

    for number1 in range(lower_border, upper_border):
        for number2 in range(lower_border, upper_border):
            product = number1 * number2
            products.append(product)
    products.sort(reverse=True)
    for product in products:
        if is_palindromic(product):
            return product
    return None
