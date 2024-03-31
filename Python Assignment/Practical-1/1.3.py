#WAP to compute compound Interest

print("Name: Deepanshi Yadav")
print("Roll No: 2210997066")

p = float(input("Enter the principal: "))
r = float(input("Enter the rate : "))
t = float(input("Enter the time : "))
ci = p * (pow((1 + r / 100), t))
print("Compound interest is: ", ci)
