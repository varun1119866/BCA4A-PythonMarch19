#WAP to accept basic salary for the employee. Calculate DA as 30% of bs, HRA as 20% of bs if bs&gt;=20000else compute DA as 20% and HRA as 10%. Display the result.

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def calculate_salary(bs):
    if bs >= 20000:
        da = 0.3 * bs
        hra = 0.2 * bs
    else:
        da = 0.2 * bs
        hra = 0.1 * bs
    
    gross_salary = bs + da + hra
    return da, hra, gross_salary

basic_salary = float(input("Enter the basic salary: "))

da, hra, gross_salary = calculate_salary(basic_salary)

print(f"Basic Salary: {basic_salary}")
print(f"Dearness Allowance (DA): {da}")
print(f"House Rent Allowance (HRA): {hra}")
print(f"Gross Salary: {gross_salary}")
