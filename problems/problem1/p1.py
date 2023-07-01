def summation_of_multiples(number: int) -> int:
    sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            sum = n + sum
    return sum


print(summation_of_multiples(number=1000))
