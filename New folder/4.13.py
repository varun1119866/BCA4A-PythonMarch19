print("NAME : RAGHAV \n ROLL NO : 2210997182")
# Input the value of n from the user
n = int(input("Enter the value of n: "))

# Initialize the sum
total_sum = 0

# Compute the sum of the first n natural numbers
for i in range(1, n + 1):
    total_sum += i

# Display the sum
print("Sum of the first", n, "natural numbers:", total_sum)
