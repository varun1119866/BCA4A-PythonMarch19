#WAP to accept sales amount for the salesman. Compute commission as 20% of sales amount if sales amount>=15000, comm as 15% if sales amount >=1000 else comm as 10 %. Display the result.
salesAmount = float(input("Enter sales amount: "))

if salesAmount >= 15000:
    commission = 0.2 * salesAmount
elif salesAmount >= 1000:
    commission = 0.15 * salesAmount
else:
    commission = 0.1 * salesAmount

print("Commission is", commission)