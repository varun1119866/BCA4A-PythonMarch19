sales_amount = float(input("Enter the sales amount: "))
commission = 0.2 * sales_amount if sales_amount >= 15000 else 0.15 * sales_amount if sales_amount >= 10000 else 0.1 * sales_amount
print(f"Sales Amount: {sales_amount}")
print(f"Commission: {commission}")
