 
def multiplication_table(number):
    print("Multiplication table of", number, ":")
    for i in range(1, 11):   
        print(number, "x", i, "=", number * i)

# Main function
def main():
   
    number = int(input("Enter a number: "))

    
    multiplication_table(number)

 
main()
