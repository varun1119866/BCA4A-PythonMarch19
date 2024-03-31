#print triangle pattern
print("Name: Sheshank Lakhi\nRoll No: 2210997217")
n = int(input("Enter number of rows: "))
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()