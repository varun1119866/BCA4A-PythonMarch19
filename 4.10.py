print ("Name: Arpita Chaudhary\nRoll No: 2210997047")

def product(m):
    product = 1
    for n in range(m, 1, -2):
        product *= n
    return product

m = 15
print(product(m))
