def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def main():
    n = int(input("Enter the value of n: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        sum_natural_numbers = sum_of_natural_numbers(n)
        print("Sum of the first", n, "natural numbers:", sum_natural_numbers)

if _name_ == "_main_":
    main()
