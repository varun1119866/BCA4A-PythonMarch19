print("NAME : Khushi\n ROLL NO : 2210997120")
# Input the value of n from the user
n = int(input("Enter the value of n: "))

# Initialize the first two terms of the Fibonacci sequence
a, b = 0, 1

# Display the Fibonacci sequence up to nth term
print("Fibonacci sequence up to nth term:")
print(a, end=" ")  # Print the first term
while n > 1:  # Loop to generate the Fibonacci sequence
    print(b, end=" ")  # Print the current term
    a, b = b, a + b  # Generate the next term
    n -= 1  # Decrease the remaining count of terms
