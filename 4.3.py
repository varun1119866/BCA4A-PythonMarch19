num = int(input("Enter a number: "))
for i in range(1, num+1):
    if i == 7:
        print("Breaking loop at 7")
        break
    if i % 2 == 0:
        print(f"{i} is even")
        continue
    print(f"{i} is odd")
