import statistics

numbers = [2, 4, 6, 8, 10]

mean = statistics.mean(numbers)
print("Mean:", mean)

variance = statistics.variance(numbers)
print("Variance:", variance)

std_deviation = statistics.stdev(numbers)
print("Standard Deviation:", std_deviation)