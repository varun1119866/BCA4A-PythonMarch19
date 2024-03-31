#WAP that prints multiplication table of a number using for loop.

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

num = int(input("Enter the number for which you want to print the multiplication table: "))

print("Multiplication table of", num, ":")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
