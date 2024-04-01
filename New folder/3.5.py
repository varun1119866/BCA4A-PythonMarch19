print("NAME : Khushi\n ROLL NO : 2210997120")
# Input sales amount from the user
sales_amount = float(input("Enter the sales amount for the salesman: "))

# Calculate commission based on conditions
if sales_amount >= 15000:
    commission = 0.20 * sales_amount
elif sales_amount >= 10000:
    commission = 0.15 * sales_amount
else:
    commission = 0.10 * sales_amount

# Display the result
print("Commission earned by the salesman:", commission)
