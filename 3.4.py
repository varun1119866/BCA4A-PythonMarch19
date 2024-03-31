def calculate_salary(bs):
    if bs >= 20000:
        da = 0.3 * bs
        hra = 0.2 * bs
    else:
        da = 0.2 * bs
        hra = 0.1 * bs

    gross_salary = bs + da + hra
    return da, hra, gross_salary

def main():
    basic_salary = float(input("Enter the basic salary: "))

    da, hra, gross_salary = calculate_salary(basic_salary)

    print("Dearness Allowance (DA):", da)
    print("House Rent Allowance (HRA):", hra)
    print("Gross Salary:", gross_salary)

if _name_ == "_main_":
    main()
