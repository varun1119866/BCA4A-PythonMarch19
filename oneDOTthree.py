def calculate_compound_interest(principal, rate, time):
  
  if rate > 1:
    rate = rate / 100

  amount = principal * (1 + rate) ** time

  compound_interest = amount - principal
  return compound_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (e.g., for 5% enter 5): "))
time = float(input("Enter the time period in years: "))

compound_interest = calculate_compound_interest(principal, rate, time)

print("Compound Interest earned:", compound_interest)
print("Garima Jain\n22109971080\nBCA4 B-1")
