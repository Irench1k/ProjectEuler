import math


def smallest_divisor(number: int) -> int:
    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return n
    return number


def biggest_prime_factor(number: int) -> int:
    while True:
        smd = smallest_divisor(number)
        factor = number // smd
        if smd == number:
            return smd
        number = factor


print(biggest_prime_factor(600851475143))
