# WAP to show the working of break and continue statement

num  = int(input('Enter a number: '))
while num < 15:
    num += 1
    if num == 5:
        continue
    if num == 13:
        break
    print(num)
