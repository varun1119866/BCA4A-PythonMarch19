def print_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

rows = int(input("Enter the number of rows: "))
print_triangle(rows)
