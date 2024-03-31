def compound_interest(principal, rate, time):
    
    rate = rate / 100
    amount = principal * (1 + rate) ** time

    return amount

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in percentage): "))
    time = float(input("Enter the time period (in years):")) 
    amount = compound_interest(principal, rate, time)

    interest = amount - principal
    print("Compound interest after {} years: {:.2f}".format(time, interest))
    print("Total amount after {} years: {:.2f}".format(time, amount))

if __name__ == "__main__":
    main()
