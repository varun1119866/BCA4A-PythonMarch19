# WAP to print the product of the series m = 15 * 13 * 11 * 9 * 7

product = 15
for num in range(13, 6, -2):
    product *= num
print("Product of the series:", product)
