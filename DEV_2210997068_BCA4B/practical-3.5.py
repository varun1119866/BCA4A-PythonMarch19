# WAP to accept sales amount for the salesman. Compute
# commission as 20% of sales amount if sales amount&gt;=15000,
# comm as 15% if sales amount &gt;=1000 else comm as 10 %.
# Display the result.
print("name-dev,rollno-2210997068")
sales_amount = float(input("Enter sales amount: "))

if sales_amount >= 15000:
    commission = 0.2 * sales_amount
elif sales_amount >= 1000:
    commission = 0.15 * sales_amount
else:
    commission = 0.1 * sales_amount

print(f"Commission: {commission}")
