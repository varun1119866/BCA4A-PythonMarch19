sales=int(input("Enter sales ammount: "))

if(sales>=15000):
    print("Commission: ",(sales*20)/100)
elif(sales>=1000):
    print("Commission: ",(sales*15)/100)
else: 
    print("Commisson: ",(sales*10)/100)