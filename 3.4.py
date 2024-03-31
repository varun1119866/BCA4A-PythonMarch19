print("name himani roll no2210997096")
bs = float(input("Enter the basic salary: "))

if bs >= 20000:
    da = bs * 0.3
    hra = bs * 0.2
else:
    da = bs * 0.2
    hra = bs * 0.1

gs = bs + da + hra

print("Gross Salary: ", gs)
