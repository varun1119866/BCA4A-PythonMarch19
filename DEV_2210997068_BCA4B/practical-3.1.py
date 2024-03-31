#WAP to check if one No. is divisible by the other or not
print("name-dev,rollno-2210997068")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")
