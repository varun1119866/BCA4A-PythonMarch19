#WAP to display cube of first 10 even numbers

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def is_even(num):
    return num % 2 == 0

count = 0
num = 2  
while count < 10:
    if is_even(num):
        cube = num ** 3
        print(f"The cube of {num} is: {cube}")
        count += 1
    num += 2 
