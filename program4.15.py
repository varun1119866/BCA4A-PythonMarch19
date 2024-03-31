print("Shikha - 2210997218")
print(" ")

# Program to create a list of specific size, arrange elements in ascending order, and display before and after sorting
size = 5
numbers = []
for i in range(size):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(" ")
print("List before sorting:", numbers)
numbers.sort()
print(" ")
print("List after sorting:", numbers)

