import statistics

def calculate_statistics(numbers):
    # Mean
    mean = statistics.mean(numbers)

    # Variance
    variance = statistics.variance(numbers)

    # Standard Deviation
    std_deviation = statistics.stdev(numbers)

    return mean, variance, std_deviation

def main():
    # Input list of numbers
    numbers = [float(x) for x in input("Enter a list of numbers separated by space: ").split()]

    # Calculate statistics
    mean, variance, std_deviation = calculate_statistics(numbers)

    # Print results
    print("Mean:", mean)
    print("Variance:", variance)
    print("Standard Deviation:", std_deviation)

if _name_ == "_main_":
    main()
