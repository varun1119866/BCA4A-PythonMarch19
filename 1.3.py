
print ("Name: Arpita Chaudhary\nRoll No: 2210997047")
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
time = float(input("Enter the number of years: "))
interest = principal * ( pow( (1 + rate), time) - 1 )
print("The compound interest earned is: ", interest)
