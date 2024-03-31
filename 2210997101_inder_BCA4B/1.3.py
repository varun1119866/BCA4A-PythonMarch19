def compound_interest(principal, rate, time):
    n = 12  

    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    interest = amount - principal
    return interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = float(input("Enter the time period (in years): "))

    interest = compound_interest(principal, rate, time)

    print("Compound interest:", interest)

if __name__ == "__main__":
    main()
