def check_number(num):
    if num > 0:
        return "{} is a positive number.".format(num)
    elif num < 0:
        return "{} is a negative number.".format(num)
    else:
        return "The number is zero."

def main():
    num = float(input("Enter a number: "))
    result = check_number(num)
    print(result)

if __name__ == "__main__":
    main()
