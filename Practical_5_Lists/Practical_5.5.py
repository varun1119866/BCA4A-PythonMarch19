#WAP to demonstrate built-in functions in Lists

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print("Original list:", my_list)

# len()
print("\nLength of the list:", len(my_list))

# min()
print("Minimum value in the list:", min(my_list))

# max()
print("Maximum value in the list:", max(my_list))

# sum()
print("Sum of all elements in the list:", sum(my_list))

# sorted()
sorted_list = sorted(my_list)
print("\nSorted list:", sorted_list)

# reversed()
reversed_list = list(reversed(my_list))
print("Reversed list:", reversed_list)

# count() 
count = my_list.count(5)
print("\nNumber of occurrences of 5 in the list:", count)

# index() 
index_9 = my_list.index(9)
print("Index of first occurrence of 9 in the list:", index_9)

my_list.append(7)
print("\nAfter appending 7:", my_list)

# insert() 
my_list.insert(3, 3.5)
print("After inserting 3.5 at index 3:", my_list)

# remove() 
my_list.remove(9)
print("After removing the first occurrence of 9:", my_list)

# pop()
popped_element = my_list.pop(4)
print("Popped element at index 4:", popped_element)
print("After popping element at index 4:", my_list)

# clear() 
my_list.clear()
print("\nAfter clearing the list:", my_list)