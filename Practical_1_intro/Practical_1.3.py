#WAP to compute compound Interest

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def compound_interest(principal, rate, time, n):
    amount = principal * ((1 + rate /100/ n) ** (n * time))
    interest = amount - principal
    return interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

interest = compound_interest(principal, rate, time, n)
print("Compound interest:", interest)
