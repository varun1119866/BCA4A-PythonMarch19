def fibonacci_sequence(n):
    # Initialize the first two terms of the sequence
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def main():
    n = int(input("Enter the value of n to generate Fibonacci sequence up to nth term: "))

    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fib_sequence = fibonacci_sequence(n)
        print("Fibonacci sequence up to the", n, "th term:")
        print(fib_sequence)

if _name_ == "_main_":
    main()
