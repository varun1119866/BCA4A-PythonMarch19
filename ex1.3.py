# Program to compute compound interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in percentage): "))
time = float(input("Enter time period (in years): "))

rate = rate / 100
compound_interest = principal * ((1 + rate) ** time - 1)

print("Compound interest:", compound_interest)
