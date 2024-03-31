def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area, perimeter = calculate_rectangle_properties(length, width)

    print("Area of the rectangle:", area)
    print("Perimeter of the rectangle:", perimeter)

if _name_ == "_main_":
    main()
