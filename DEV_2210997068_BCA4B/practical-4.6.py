# Write a program to display the Fibonacci sequences up to nth term where n is provided by the user.
print("name-dev,rollno-2210997068")
n = int(input("Enter the value of n: "))
a, b = 0, 1
fib_sequence = [a, b]

while b < n:
    a, b = b, a + b
    if b < n:
        fib_sequence.append(b)

print(f"Fibonacci sequence up to {n}: {fib_sequence}")
