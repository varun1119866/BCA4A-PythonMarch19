def calculate_average_marks(subject1, subject2, subject3):
    return (subject1 + subject2 + subject3) / 3

subject1 = float(input("Enter marks of subject 1: "))
subject2 = float(input("Enter marks of subject 2: "))
subject3 = float(input("Enter marks of subject 3: "))

average_marks = calculate_average_marks(subject1, subject2, subject3)

print("Average marks:", average_marks)