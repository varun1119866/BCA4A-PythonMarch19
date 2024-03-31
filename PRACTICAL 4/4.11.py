# WAP to compute factorial of a Number

def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, ":", facto(num))
