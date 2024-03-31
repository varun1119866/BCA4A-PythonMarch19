principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time period (in years): "))
compound_interest = principal * (pow((1 + rate / 100), time)) - principal
print(f"Compound Interest: {compound_interest}")
