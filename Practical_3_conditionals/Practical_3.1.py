#WAP to check if one No. is divisible by the other or not

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def check_divisibility(num1, num2):
    if num2 == 0:
        return False 
    if num1 % num2 == 0:
        return True
    else:
        return False
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if check_divisibility(num1, num2):
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")
