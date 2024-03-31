print("NAME : RAGHAV \n ROLL NO : 2210997182")
import math

# Define the list of numbers
numbers = [12, 15, 17, 20, 22, 25, 28, 30]

# Calculate the mean
mean = sum(numbers) / len(numbers)

# Calculate the variance
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

# Calculate the standard deviation
std_deviation = math.sqrt(variance)

# Display the results
print("List of numbers:", numbers)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
