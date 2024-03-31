# factorial of a number

print("Name: Ajay Singla")
print("Roll No: 2210997019")

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print(f"Factorial of {num} is {fact}")
