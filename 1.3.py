princ=int(input("Enter principal: "))
rate=int(input("Enter the rate of interest: "))
time=int(input("Enter the time: "))
Amount=princ*(pow((1+rate/100),time))
CI=Amount - princ
print("Compound interest is: ",CI)
