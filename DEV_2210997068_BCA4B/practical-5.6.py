# WAP to calculate the mean, variance and std. deviation of given list of numbers
print("name-dev,rollno-2210997068")
import statistics

my_list = [1, 2, 3, 4, 5]
mean = statistics.mean(my_list)
variance = statistics.variance(my_list)
std_dev = statistics.stdev(my_list)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
