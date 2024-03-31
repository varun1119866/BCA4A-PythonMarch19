def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

number = int(input("Enter a number: "))
multiplication_table(number)
