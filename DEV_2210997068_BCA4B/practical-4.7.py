# WAP that prints multiplication table of a umber using for loop.
print("name-dev,rollno-2210997068")
num = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
