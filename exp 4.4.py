count = 0
while count < 5:
    print("Inside while loop")
    count += 1
else:
    print("Inside else block")

count = 0
while count < 5:
    if count == 3:
        break
    print("Inside while loop")
    count += 1
else:
    print("Inside else block")
