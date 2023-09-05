def is_prime(number: int) -> int:
    for n in range(2, number + 1):
        if number % n == 0 and number != n:
            return False
    return True


def get_prime_number_at_index(index: int) -> int:
    primes: list[int] = []
    n = 2
    while len(primes) < index:
        if is_prime(n):
            print(n)
            primes.append(n)
        n += 1
    return primes[-1]


print(get_prime_number_at_index(10_001))
