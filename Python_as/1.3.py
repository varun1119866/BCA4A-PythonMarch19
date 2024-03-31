print("NAME : Sehaj \n ROLL NO : 2210997212")
# Taking input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Converting annual interest rate to decimal
rate = rate / 100

# Calculating compound interest
compound_interest = principal * (1 + rate) ** time - principal

# Displaying the compound interest
print("Compound interest:", compound_interest)
