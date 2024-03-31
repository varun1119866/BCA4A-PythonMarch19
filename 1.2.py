print ("name himani rollno 2210997096")

sub1 = int(input("Enter marks obtained in subject 1: "))
sub2 = int(input("Enter marks obtained in subject 2: "))
sub3 = int(input("Enter marks obtained in subject 3: "))

avg_marks = (sub1 + sub2 + sub3) / 3


print("Average marks:", avg_marks)


if avg_marks >= 90:
  print("Grade: A")
elif avg_marks >= 80:
  print("Grade: B")
elif avg_marks >= 70:
  print("Grade: C")
elif avg_marks >= 60:
  print("Grade: D")
else:
  print("Grade: F")
