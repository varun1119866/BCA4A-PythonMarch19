#WAP to compute compound Interest
print("name-dev,rollno-2210997068")
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): "))
time = float(input("Enter time (in years): "))

amount = principal * (1 + rate/100) ** time
compound_interest = amount - principal

print(f"Compound interest: {compound_interest}")
