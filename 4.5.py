def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    num = int(input("Enter a number to compute its factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact = factorial(num)
        print("Factorial of", num, ":", fact)

if _name_ == "_main_":
    main()
