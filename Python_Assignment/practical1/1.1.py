def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = rectangle_area(length, width)
perimeter = rectangle_perimeter(length, width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
