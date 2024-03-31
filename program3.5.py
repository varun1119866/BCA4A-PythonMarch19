print("Shikha - 2210997218")
print(" ")

def calculate_commission(sales_amount):
    if sales_amount >= 15000:
        commission = 0.2 * sales_amount
    elif sales_amount >= 1000:
        commission = 0.15 * sales_amount
    else:
        commission = 0.1 * sales_amount
    
    return commission

# Input the sales amount from the user
sales_amount = float(input("Enter the sales amount: "))

# Calculate commission
commission_amount = calculate_commission(sales_amount)

# Display the result
print(f"\nSales Amount: ₹{sales_amount}")
print(" ")

print(f"Commission: ₹{commission_amount}")
