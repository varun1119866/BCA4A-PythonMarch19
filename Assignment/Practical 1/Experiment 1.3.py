#WAP to compute compound Interest
print("Name: Drishti Gupta\nRoll No: 2210997286")


p = float(input("Enter the principal: "))
r = float(input("Enter the rate : "))
t = float(input("Enter the time : "))
Interest = p * (pow((1 + r / 100), t))
print("Compound interest is: ",Interest)
