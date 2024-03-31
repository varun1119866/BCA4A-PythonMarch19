#WAP to show the working of break and continue statement
print("Name:Ridhima\nRoll No: 2210997193")

for i in range(1,500):
    if i%2==0:
        if i==50:
            print("Break is used")
            break
        print(i)
    else:
        if i%3==0:
            print("Continued is used")
            continue
        print(i)