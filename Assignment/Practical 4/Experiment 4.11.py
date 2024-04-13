# factorial of a number
print("Name: Dhriti Gandhi\nRoll No: 2210997070")

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print(f"Factorial of {num} is {fact}")