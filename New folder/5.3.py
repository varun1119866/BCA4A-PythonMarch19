print("NAME : Khushi\n ROLL NO : 2210997120")
# Create a list
my_list = ['apple', 'banana', 'cherry']

# Append an element to the list
my_list.append('date')
print("After appending 'date':", my_list)

# Insert an element at a specific position
my_list.insert(1, 'orange')
print("After inserting 'orange' at index 1:", my_list)

# Remove the first occurrence of an element
my_list.remove('banana')
print("After removing 'banana':", my_list)

# Extend the list with another list
my_list.extend(['grape', 'kiwi'])
print("After extending with ['grape', 'kiwi']:", my_list)

# Pop an element from the list by index
popped_element = my_list.pop(2)
print("Popped element at index 2:", popped_element)
print("List after popping at index 2:", my_list)

# Count the occurrences of an element
count = my_list.count('cherry')
print("Number of occurrences of 'cherry':", count)

# Reverse the list
my_list.reverse()
print("Reversed list:", my_list)

# Sort the list in ascending order
my_list.sort()
print("Sorted list:", my_list)
