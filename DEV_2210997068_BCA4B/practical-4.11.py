# WAP to compute factorial of a Number
print("name-dev,rollno-2210997068")
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")
