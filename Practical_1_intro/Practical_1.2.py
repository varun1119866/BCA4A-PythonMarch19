#WAP to calculate Avg. marks of 3 subjects

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def average_marks(sub1, sub2, sub3):
    total_marks = sub1 + sub2 + sub3
    average_marks = total_marks / 3
    return average_marks

sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

average_marks = average_marks(sub1, sub2, sub3)
print("Average marks:", average_marks)
