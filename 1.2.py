def calculate_average(subject1, subject2, subject3):
    total_marks = subject1 + subject2 + subject3
    average_marks = total_marks / 3
    return average_marks

def main():
    subject1 = float(input("Enter marks for subject 1: "))
    subject2 = float(input("Enter marks for subject 2: "))
    subject3 = float(input("Enter marks for subject 3: "))

    average = calculate_average(subject1, subject2, subject3)

    print("Average marks:", average)

if _name_ == "_main_":
    main()
