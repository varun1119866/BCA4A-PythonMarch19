 
def factorial(n):
     
    if n == 0 or n == 1:
        return 1
    else:
       
        return n * factorial(n - 1)
 
def main():
    
    num = int(input("Enter a number to compute its factorial: "))

    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        
        fact = factorial(num)
        print("Factorial of", num, "is", fact)

 
main()
