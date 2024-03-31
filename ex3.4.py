# Program to calculate DA and HRA for an employee's basic salary

basic_salary = float(input("Enter basic salary: "))

if basic_salary >= 20000:
    da = 0.3 * basic_salary
    hra = 0.2 * basic_salary
else:
    da = 0.2 * basic_salary
    hra = 0.1 * basic_salary

print("DA:", da)
print("HRA:", hra)
