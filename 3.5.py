print("name himani roll no 2210997096")
sales_amount = float(input("Enter sales amount: "))
if sales_amount >= 15000:
    comm = 0.20 * sales_amount
elif sales_amount >= 1000:
    comm = 0.15 * sales_amount
else:
    comm = 0.10 * sales_amount
print("Commission: ", comm)
