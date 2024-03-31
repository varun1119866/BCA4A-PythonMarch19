p=int(input("Enter Principal: "))
r=int(input("Enter Rate: "))/100
t=int(input("Enter tenure: "))
n=int(input("Enter number of times intrest is compounded per year: "))

print("Compound intrest is: ",(p*((1+(r/n))**(t*n)))) 