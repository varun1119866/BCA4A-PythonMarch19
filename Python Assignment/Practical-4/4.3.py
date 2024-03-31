#WAP to show the working of break and continue statement

print("Name: Deepanshi Yadav")
print("Roll No: 2210997066")

for i in range(1,500):
    if i%2==0:
        if i==50:
            print(" statement breaked")
            break
        print(i)
    else:
        if i%3==0:
            print(" statement Continued")
            continue
        print(i)
