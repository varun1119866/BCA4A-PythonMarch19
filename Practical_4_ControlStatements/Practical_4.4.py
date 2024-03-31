#WAP to the use of else statement with while and break

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

print("Example 1:")
num = 5
while num > 0:
    print(num)
    num -= 1
else:
    print("Loop ended.")


print("\nExample 2:")
num = 5
while num > 0:
    print(num)
    if num == 3:
        break
    num -= 1
else:
    print("Loop ended. ")
