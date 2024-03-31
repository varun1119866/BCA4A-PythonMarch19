def print_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def main():
    rows = int(input("Enter the number of rows for the triangle: "))
    print_triangle(rows)

if _name_ == "_main_":
    main()
