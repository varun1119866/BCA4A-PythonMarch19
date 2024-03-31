print("Shikha - 2210997218")
print(" ")

def calculate_salary(bs):
    if bs >= 20000:
        da = 0.3 * bs
        hra = 0.2 * bs
    else:
        da = 0.2 * bs
        hra = 0.1 * bs
    
    gross_salary = bs + da + hra
    return da, hra, gross_salary

# Input the basic salary from the user
basic_salary = float(input("Enter the basic salary: "))

# Calculate DA, HRA, and gross salary
da_amount, hra_amount, gross_salary_amount = calculate_salary(basic_salary)


# Display the result
print(f"\nBasic Salary: ₹{basic_salary}")
print(" ")

print(f"Dearness Allowance (DA): ₹{da_amount}")
print(" ")

print(f"House Rent Allowance (HRA): ₹{hra_amount}")
print(" ")

print(f"Gross Salary: ₹{gross_salary_amount}")
