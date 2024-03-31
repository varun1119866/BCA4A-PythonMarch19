#WAP To print a Triangle Pattern

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def triangle_pattern(n):
    #upper
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    
    #Lower
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


rows = int(input("Enter the number of rows for the triangle: "))
triangle_pattern(rows)
