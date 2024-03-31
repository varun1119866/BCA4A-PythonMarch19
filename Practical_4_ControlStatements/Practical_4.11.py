# WAP to compute factorial of a number

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

num = int(input("Enter a number to compute its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("Factorial of", num, "is:", result)