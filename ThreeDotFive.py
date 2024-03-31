def calculate_commission(sales_amount):

  if sales_amount >= 15000:
    commission = sales_amount * 0.2 
  elif sales_amount >= 1000:
    commission = sales_amount * 0.15
  else:
    commission = sales_amount * 0.1
    
  return commission

sales_amount = float(input("Enter the salesman's sales amount: "))

commission = calculate_commission(sales_amount)

print(f"Commission: {commission:.2f}")
print("Karan Arora\n2210997111\nBCA4 B-1")
