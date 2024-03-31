marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
avg_marks = sum(marks) / len(marks)
print(f"Average marks: {avg_marks}")
