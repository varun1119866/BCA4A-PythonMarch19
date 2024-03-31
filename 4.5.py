def main():
    start = 4
    end = 40
    step = 4

    total_sum = 0
    current_number = start

    while current_number <= end:
        total_sum += current_number
        current_number += step

    print("Sum of the series:", total_sum)

if _name_ == "_main_":
    main()
