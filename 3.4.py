basic=int(input("Enter the basic salary of employee"))
if(basic>=20000):
    DA=((30/100)*basic)
    HRA=((20/100)*basic)
    print("DA is: ",DA)
    print("HRA is: ",HRA)
else:
    DA=((20/100)*basic)
    HRA=((10/100)*basic)
    print("DA is: ",DA)
    print("HRA is: ",HRA)
