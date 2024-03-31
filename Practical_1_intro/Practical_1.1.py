#Simple Introductory Python Programs
#WAP to Calculate Area and Perimeter of a Rectangle

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def rectangle_area(length,width):
    area = length * width
    return area

def rectangle_perimeter(length,width):
    perimeter = 2 * (length + width)
    return perimeter

length = float(input("Enter the length of the rectangle : "))
width = float(input("Enter the width of the rectangle: "))

area = rectangle_area(length, width)
perimeter = rectangle_perimeter(length, width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)