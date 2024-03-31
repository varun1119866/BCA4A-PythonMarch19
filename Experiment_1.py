# 1.1
length = float(input("Enter length of reactangle : "))
breadth = float(input("Enter breadth of reactangle : "))
def area(length, breadth):
    area=length*breadth
    print(f"The area of reactangle is :{area}")

def perimeter(length, breadth):
    perimeter=2*(length+breadth)
    print(f"The Perimeter of reactangle is :{perimeter}")
    
area(length, breadth)
perimeter(length,breadth)




#1.2
marks1 = float(input("Enter marks of subject 1 : "))
marks2 = float(input("Enter marks of subject 2 : "))
marks3 = float(input("Enter marks of subject 3 : "))

average = (marks1+marks2+marks3)/3
print(f"Average of three subjects is : {average}")




#1.3
principal_amount = float(input("Enter the principal amount: "))
rate = float(input("Enter annual interest rate (in percentage): "))
time = float(input("Enter time period (in years): "))
_rate=rate/100
amount= principal_amount*((1+_rate)**time)
compound_interest = amount - principal_amount
print(f"Compound interest is : {compound_interest}")



