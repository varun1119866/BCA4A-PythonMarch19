def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

def main():
    year = int(input("Enter a year: "))
    is_leap_year(year)

if __name__ == "__main__":
    main()
