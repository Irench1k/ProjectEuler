def fibonacci_sequence(max_value):
    n1 = 0
    n2 = 1
    sum = 0
    while n1 + n2 <= max_value:
        nth = n1 + n2
        n1 = n2
        n2 = nth

        if nth % 2 == 0:
            even_number = nth
            sum = even_number + sum
        
    return sum

result = fibonacci_sequence(4000000)
print(f"The result is {result}")
