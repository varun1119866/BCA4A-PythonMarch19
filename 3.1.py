num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"{num1} is {'divisible' if num1 % num2 == 0 else 'not divisible'} by {num2}")
