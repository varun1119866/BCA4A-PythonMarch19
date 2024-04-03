def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))

if __name__ == "__main__":
    main()
