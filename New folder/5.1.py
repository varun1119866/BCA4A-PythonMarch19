print("NAME : Khushi\n ROLL NO : 2210997120")
# Create a list
my_list = [1, 2, 3, 4, 5]

# Display the list
print("Original list:", my_list)

# Access elements of the list
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Append an element to the list
my_list.append(6)
print("List after appending 6:", my_list)

# Insert an element at a specific position
my_list.insert(2, 10)
print("List after inserting 10 at index 2:", my_list)

# Remove an element from the list
my_list.remove(3)
print("List after removing 3:", my_list)

# Check if an element is in the list
if 4 in my_list:
    print("4 is present in the list")

# Length of the list
print("Length of the list:", len(my_list))

# Sorting the list
my_list.sort()
print("Sorted list:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)

# Slicing the list
print("Sliced list:", my_list[1:4])
