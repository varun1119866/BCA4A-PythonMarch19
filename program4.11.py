print("Shikha - 2210997218")
print(" ")

# Input the number to calculate factorial
num = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1

# Calculate factorial
for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)
