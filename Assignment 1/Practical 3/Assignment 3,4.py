def calculate_salary(bs):
    if bs >= 20000:
        DA = 0.3 * bs
        HRA = 0.2 * bs
    else:
        DA = 0.2 * bs
        HRA = 0.1 * bs
    return DA, HRA

basic_salary = float(input("Enter the basic salary: "))
DA, HRA = calculate_salary(basic_salary)

print(f"Basic Salary: {basic_salary}")
print(f"DA: {DA}")
print(f"HRA: {HRA}")