#WAP to show the working of break and continue statement
for i in range(1,500):
    if i%2==0:
        if i==50:
            print("The statement is breaked")
            break
        print(i)
    else:
        if i%3==0:
            print("the statement is Continued")
            continue
        print(i)