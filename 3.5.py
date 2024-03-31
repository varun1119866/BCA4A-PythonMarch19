sale=int(input("Enter the sales amount"))
if(sale>=15000):
    commission=((20/100)*sale)
    print("Commission is: ",commission)
elif(sale>=1000):
    commission=((15/100)*sale)
    print("Commission is: ",commission)
else:
    commission=((10/100)*sale)
    print("Commission is: ",commission)
