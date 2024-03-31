def compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time))

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

interest = compound_interest(principal, rate, time)

print("Compound interest:", interest)