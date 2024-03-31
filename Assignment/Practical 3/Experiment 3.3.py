#WAP to check if a given year is Leap or not
print("Name: Ayush Asija\nRoll No: 2210997051")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")