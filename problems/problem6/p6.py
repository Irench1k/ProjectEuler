def sum_of_squares(n: int) -> float:
    sum1: float = (n/6) * (n + 1) * ((2 * n) + 1)
    return sum1


def sum_of_the_sequance(n: int) -> float:
    sum2: float = (n/2) * (1 + n)
    squared_sum = sum2 ** 2
    return squared_sum


def difference(n: int) -> float:
    sum1 = sum_of_squares(n)
    squared_sum = sum_of_the_sequance(n)
    result = squared_sum - sum1
    return result


print(sum_of_squares(100))
print(sum_of_the_sequance(100))
print(difference(100))
