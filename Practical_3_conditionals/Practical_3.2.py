#WAP to check if a Number is +ve, -ve or zero

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


num = int(input("Enter a number: "))

print(f"The number {num} is {check_number(num)}")
