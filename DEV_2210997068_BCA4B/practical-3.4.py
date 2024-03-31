# WAP to accept basic salary for the employee. Calculate DA as
# 30% of bs, HRA as 20% of bs if bs&gt;=20000else compute DA as
# # 20% and HRA as 10%. Display the result.
print("name-dev,rollno-2210997068")
basic_salary = float(input("Enter basic salary: "))

if basic_salary >= 20000:
    da = 0.3 * basic_salary
    hra = 0.2 * basic_salary
else:
    da = 0.2 * basic_salary
    hra = 0.1 * basic_salary

total_salary = basic_salary + da + hra
print(f"Total salary: {total_salary}")
