#3.1 
def check_divisibility(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    elif num1 % num2 == 0:
        return f"{num1} is divisible by {num2}"
    else:
        return f"{num1} is not divisible by {num2}"
#3.2
def check_positive_negative_zero(num):
    if num > 0:
        return f"{num} is a positive number"
    elif num < 0:
        return f"{num} is a negative number"
    else:
        return "The number is zero"
#3.3
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
#3.4
def calculate_salary(bs):
    if bs >= 20000:
        da = 0.3 * bs
        hra = 0.2 * bs
    else:
        da = 0.2 * bs
        hra = 0.1 * bs
    return f"Basic Salary: {bs}, DA: {da}, HRA: {hra}"
#3.5
def calculate_commission(sales_amount):
    if sales_amount >= 15000:
        commission = 0.20 * sales_amount
    elif sales_amount >= 1000:
        commission = 0.15 * sales_amount
    else:
        commission = 0.10 * sales_amount
    return f"Sales Amount: {sales_amount}, Commission: {commission}"

# Testing the functions
num1 = 12
num2 = 3
print(check_divisibility(num1, num2))

number = -5
print(check_positive_negative_zero(number))

year = 2024
print(is_leap_year(year))

basic_salary = 25000
print(calculate_salary(basic_salary))

sales_amount = 2000
print(calculate_commission(sales_amount))
s
