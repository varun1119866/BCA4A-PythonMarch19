# WAP to calculate the mean, variance and std. deviation of a given list of numbers

raw_list = [10, 20, 30, 40, 50]
mean = sum(raw_list) / len(raw_list)
variance = sum((x - mean) ** 2 for x in raw_list) / len(raw_list)
std_dev = variance ** 0.5

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
