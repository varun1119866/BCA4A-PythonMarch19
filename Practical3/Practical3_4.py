salary=int(input("Enter salary: "))

if(salary<20000):
    print("Dearly Allowance: ",(salary*30)/100)
    print("HRA: ",(salary*20)/100)

else:
    print("Dearly Allowance: ",(salary*20)/100)
    print("HRA: ",(salary*15)/100)