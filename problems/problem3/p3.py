def get_factors(number: int) -> list[int]:
    """Takes a positive integer and returns all factors of this number."""
    factors: list[int] = []
    for n in range(number+1):
        if n != 0 and number % n == 0:
            factors.append(n)
            print(f"get_factors: {n}, {number}")
    return factors
 

def is_prime(number: int) -> bool:
    """Takes a number and returns True if the number is prime."""
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        print(f"is_prime: {number} / {i}")
    return True


def get_biggest_prime_factor(number: int) -> int:
    """Takes a positive integer and returns the largest prime factor of it."""
    all_factors = get_factors(number)
    prime_factors: list[int] = []

    for factor in all_factors:
        if is_prime(factor):
            prime_factors.append(factor)
        print(f"get_prime_factors: {factor}")
    return prime_factors[-1]


print(get_biggest_prime_factor(6000))
