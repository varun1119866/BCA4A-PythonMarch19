principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (in percentage): "))
time = float(input("Enter time (in years): "))

compound_interest = principal * (1 + rate / 100) ** time - principal

print("Compound Interest:", compound_interest)
