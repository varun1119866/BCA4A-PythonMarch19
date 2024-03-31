def check_divisibility(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    elif num1 % num2 == 0:
        return f"{num1} is divisible by {num2}"
    else:
        return f"{num1} is not divisible by {num2}"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(check_divisibility(num1, num2))