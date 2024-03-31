def multiplication_table(number):
    print("Multiplication table of", number, ":")
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

def main():
    number = int(input("Enter the number to generate its multiplication table: "))
    multiplication_table(number)

if _name_ == "_main_":
    main()
