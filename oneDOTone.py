def calculate_area_perimeter(length, width):
  area = length * width
  perimeter = 2 * (length + width)
  return area, perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area, perimeter = calculate_area_perimeter(length, width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
print("Garima Jain\n22109971080\nBCA4 B-1")
