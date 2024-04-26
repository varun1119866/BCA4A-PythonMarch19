#WAP to calculate the mean, variance and std. deviation of given list of numbers
import statistics

new_list = [10, 20, 30, 40, 50, 60, 70]

mean = statistics.mean(new_list)
variance = statistics.variance(new_list)
std_dev = statistics.stdev(new_list)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")