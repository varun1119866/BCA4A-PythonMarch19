#fabonacci series
print("Name: Dhruv \nRoll No: 2210997071\n")

num = int(input("Enter a number: "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci sequence:")
while count <= num:
    print(sum)
    a = b
    b = sum
    sum = a + b
    count += 1