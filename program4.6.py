print("Shikha - 2210997218")
print(" ")

# Program to display the Fibonacci sequence up to the nth term
n = int(input("Enter the value of n: "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, ":", a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        nth = a + b
        a = b
        b = nth
        count += 1
