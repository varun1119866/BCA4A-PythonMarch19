
#3.1
dividend = float(input("Enter a dividend : "))
divisor= float(input("Enter a divisor : "))

if(dividend % divisor == 0):
    print("It is completely divisible")
else:
    print("It is not divisible")

#3.2
number=float(input("Enter a number : " ))
if number>0:
    print("Number is positive")
elif number<0:
    print("Number is negative")
else:
    print("It is a zero !!")

#3.3
year = int(input("Enter a year: "))

if (year%4==0 and year%100!=0) or (year%400==0):
    print("It is a leap year")
else:
    print("It is a non-leap year")

#3.4
base_salary=float(input("Enter basic salary : "))
if base_salary>=20000:
    da=0.3*base_salary
    hra=0.2*base_salary
    print(f"DA : {da} \nHRA : {hra} ")
else:
    da = 0.2 * base_salary
    hra = 0.1 * base_salary
    print(f"DA : {da} \nHRA : {hra} ")


#3.5
sales_amount=float(input("Enter the sales amount: "))
if sales_amount>=15000:
    commission=sales_amount*0.2
    print(f"The sales commission is {commission}")
elif sales_amount>=1000:
    commission = sales_amount * 0.15
    print(f"The sales commission is {commission}")
else:
    commission = sales_amount * 0.1
    print(f"The sales commission is {commission}")


