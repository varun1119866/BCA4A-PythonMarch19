#WAP to calculate the mean, variance and std. deviation of given list of numbers
import statistics

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

numbers = [4, 5, 8, 9, 11, 15, 18]

# mean
mean = statistics.mean(numbers)

# variance
variance = statistics.variance(numbers)

# standard deviation
std_deviation = statistics.stdev(numbers)

print("Given list of numbers:", numbers)
print("Mean:", mean)
print("Variance:", variance)
print("Standard deviation:", std_deviation)
