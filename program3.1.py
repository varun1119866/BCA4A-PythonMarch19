print("Shikha - 2210997218")
print(" ")

def check_divisibility(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return False
    elif num1 % num2 == 0:
        return True
    else:
        return False

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(" ")
# Check divisibility and print the result
if check_divisibility(num1, num2):
    print(f"{num1} is divisible by {num2}.")
else:
    print(f"{num1} is not divisible by {num2}.")
