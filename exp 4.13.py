def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

n = int(input("Enter the value of n: "))
print("Sum of first", n, "natural numbers:", sum_of_natural_numbers(n))
