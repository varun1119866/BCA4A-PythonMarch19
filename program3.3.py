print("Shikha - 2210997218")
print(" ")

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400
            else:
                return False  # Divisible by 100 but not by 400
        else:
            return True  # Divisible by 4 but not by 100
    else:
        return False  # Not divisible by 4

# Input a year from the user
year = int(input("Enter a year : "))


print(" ")
# Check if the year is a leap year and print the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
