def calculate_salary(basic_salary):

  if basic_salary >= 20000:
    da = basic_salary * 0.3 
    hra = basic_salary * 0.2 
  else:
    da = basic_salary * 0.2 
    hra = basic_salary * 0.1

  gross_salary = da + hra + basic_salary
  return da, hra, gross_salary

basic_salary = float(input("Enter the basic salary: "))

da, hra, gross_salary = calculate_salary(basic_salary)

print(f"Dearness Allowance (DA): {da:.2f}")
print(f"House Rent Allowance (HRA): {hra:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")