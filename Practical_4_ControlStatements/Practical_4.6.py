#Write a program to display the Fibonacci sequences up to nth term where n is provided by the user.

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def fibonacci_sequence(n):
    a, b = 0, 1
    fib_sequence = [a, b] 
    for _ in range(2, n):
        a, b = b, a + b
        fib_sequence.append(b)
    return fib_sequence

n = int(input("Enter the number of terms for Fibonacci sequence: "))
if n <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    fib_sequence = fibonacci_sequence(n)
    print("Fibonacci sequence up to", n, "terms:")
    print(fib_sequence)

