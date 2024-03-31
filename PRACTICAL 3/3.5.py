# WAP to accept sales amount for the salesman. Compute commission as 20% of sales amount if sales amount>=15000, comm as 15% if sales amount >=1000 else comm as 10 %. Display the result.

sales_amount = float(input("Enter the sales amount: "))

if sales_amount >= 15000:
    commission = sales_amount * 0.20
elif sales_amount >= 1000:
    commission = sales_amount * 0.15
else:
    commission = sales_amount * 0.10

print("Sales Amount:", sales_amount)
print("Commission:", commission)
