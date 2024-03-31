print("NAME : KHUSHI \n ROLL NO : 2210997120")
# Define a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Display the original list
print("Original list:", my_list)

# Length of the list
print("Length of the list:", len(my_list))

# Maximum value in the list
print("Maximum value in the list:", max(my_list))

# Minimum value in the list
print("Minimum value in the list:", min(my_list))

# Sum of all elements in the list
print("Sum of all elements in the list:", sum(my_list))

# Count occurrences of a specific element in the list
print("Occurrences of 5 in the list:", my_list.count(5))

# Index of the first occurrence of a specific element in the list
print("Index of first occurrence of 4:", my_list.index(4))

# Sort the list in ascending order
my_list.sort()
print("Sorted list:", my_list)

# Reverse the elements of the list
my_list.reverse()
print("Reversed list:", my_list)

# Remove the last element from the list and return it
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

# Append an element to the list
my_list.append(8)
print("List after appending 8:", my_list)

# Insert an element at a specific position
my_list.insert(3, 7)
print("List after inserting 7 at index 3:", my_list)

# Remove the first occurrence of a specific element from the list
my_list.remove(5)
print("List after removing first occurrence of 5:", my_list)

# Clear all elements from the list
my_list.clear()
print("List after clearing all elements:", my_list)
