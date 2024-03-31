def calculate_compound_interest(principal, rate, time):
    # Formula for compound interest
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal
    return compound_interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time period (in years): "))

    compound_interest = calculate_compound_interest(principal, rate, time)

    print("Compound Interest:", compound_interest)

if _name_ == "_main_":
    main()
