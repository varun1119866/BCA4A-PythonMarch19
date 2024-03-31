# WAP to accept a basic salary for the employee. Calculate DA as 30% of bs, HRA as 20% of bs if bs>=20000 else compute DA as 20% and HRA as 10%. Display the result.

basic_salary = int(input("Enter your basic salary: "))

if basic_salary >= 20000:
   da = .30 * basic_salary
   hra = .20 * basic_salary
else:
   da = .20 * basic_salary
   hra = .10 * basic_salary
gross_salary = basic_salary + hra + da
print(f"The gross salary is {gross_salary}.")
