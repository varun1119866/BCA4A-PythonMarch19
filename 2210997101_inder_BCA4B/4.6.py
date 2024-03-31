 
def fibonacci_sequence(n):
   
    fib_sequence = [0, 1]

    
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

 
def main():
   
    n = int(input("Enter the value of 'n': "))

    
    if n <= 0:
        print("Please enter a positive integer for 'n'.")
        return

     
    sequence = fibonacci_sequence(n)
    print("Fibonacci sequence up to the", n, "term:")
    print(sequence)

 

main()
