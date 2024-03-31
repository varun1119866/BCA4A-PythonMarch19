#WAP to compute sum of first n natural numbers

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

n = int(input("Enter the value of n: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = sum_of_natural_numbers(n)
    print("Sum of the first", n, "natural numbers is:", result)
