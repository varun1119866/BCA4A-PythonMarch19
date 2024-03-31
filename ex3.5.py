# Program to compute commission for a salesman

sales_amount = float(input("Enter sales amount: "))

if sales_amount >= 15000:
    commission = 0.2 * sales_amount
elif sales_amount >= 1000:
    commission = 0.15 * sales_amount
else:
    commission = 0.1 * sales_amount

print("Commission:", commission)
