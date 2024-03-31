import statistics

my_list = [10, 20, 30, 40, 50]

mean = statistics.mean(my_list)
variance = statistics.variance(my_list)
std_deviation = statistics.stdev(my_list)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
