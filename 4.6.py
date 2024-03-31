num=int(input("Enter the number for fabonacci series: "))
n1,n2=0,1
print("Fabonacci series: ",n1,n2,end="\t")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end="\t")

print()
