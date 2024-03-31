print("NAME : RAHUL SINGH \n ROLL NO : 2210997186")
# Input basic salary from the user
basic_salary = float(input("Enter the basic salary for the employee: "))

# Calculate DA and HRA based on conditions
if basic_salary >= 20000:
    da = 0.3 * basic_salary
    hra = 0.2 * basic_salary
else:
    da = 0.2 * basic_salary
    hra = 0.1 * basic_salary

# Display the result
print("Dearness Allowance (DA):", da)
print("House Rent Allowance (HRA):", hra)
