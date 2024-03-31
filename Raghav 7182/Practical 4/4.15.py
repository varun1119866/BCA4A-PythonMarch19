print("NAME : RAGHAV \n ROLL NO : 2210997182")
# Input the size of the list from the user
size = int(input("Enter the size of the list: "))

# Input the elements of the list from the user
my_list = []
print("Enter the elements of the list:")
for i in range(size):
    element = int(input())
    my_list.append(element)

# Display the list before sorting
print("List before sorting:", my_list)

# Arrange the elements in ascending order
my_list.sort()

# Display the list after sorting
print("List after sorting:", my_list)

