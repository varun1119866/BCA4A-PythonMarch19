def check_number(num):
    if num > 0:
        return f"{num} is positive"
    elif num < 0:
        return f"{num} is negative"
    else:
        return "Number is zero"

num = float(input("Enter a number: "))
print(check_number(num))