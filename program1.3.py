print("Shikha - 2210997218")
print(" ")

def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate/100)**time
    compound_interest = amount - principal
    return compound_interest

# Taking input for principal amount, rate of interest, and time period from the user
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

print(" ")
# Calculating and printing compound interest
compound_interest = calculate_compound_interest(principal_amount, interest_rate, time_period)
print(f"Compound Interest: {compound_interest}")
