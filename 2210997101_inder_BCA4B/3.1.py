def check_divisibility(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    elif num1 % num2 == 0:
        return "{} is divisible by {}".format(num1, num2)
    else:
        return "{} is not divisible by {}".format(num1, num2)

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = check_divisibility(num1, num2)
    print(result)

if __name__ == "__main__":
    main()
