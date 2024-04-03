 
def sum_of_natural_numbers_formula(n):
    return (n * (n + 1)) // 2

 
def sum_of_natural_numbers_loop(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum
 
def main():
 
    n = int(input("Enter the value of 'n': "))

    
    if n < 0:
        print("Please enter a non-negative integer.")
        return

    
    sum_formula = sum_of_natural_numbers_formula(n)
    print("Sum of the first", n, "natural numbers (using formula):", sum_formula)

     
    sum_loop = sum_of_natural_numbers_loop(n)
    print("Sum of the first", n, "natural numbers (using loop):", sum_loop)
 
 
main()
