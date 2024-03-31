print("NAME : KHUSHI \n ROLL NO : 2210997120")
# Input the number from the user
number = int(input("Enter a number: "))

# Initialize the factorial variable
factorial = 1

# Compute the factorial
for i in range(1, number + 1):
    factorial *= i

# Display the factorial
print("Factorial of", number, "is", factorial)
