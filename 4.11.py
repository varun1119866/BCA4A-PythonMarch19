print ("Name: Arpita Chaudhary\nRoll No: 2210997047")

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
num = int(input("Enter a number to calculate its factorial: "))
print("Factorial of", num, "is", factorial(num))
