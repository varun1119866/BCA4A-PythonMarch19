print("name himani rollno2210997096")
my_list = [1, 5, 3, 7, 2]


print("Accessing elements using index:")
print("First element: ", my_list[0])
print("Last element: ", my_list[-1])


print("Slicing:")
print("Elements from index 1 to 3: ", my_list[1:4])
print("Elements from index 2 to end: ", my_list[2:])
print("All elements: ", my_list[:])


print("Modifying lists:")
my_list.append(8) 
print("After appending: ", my_list)
my_list.insert(2, 6) 
print("After inserting: ", my_list)
my_list[1:3] = [9, 10] 
print("After replacing: ", my_list)
del my_list[2]
print("After deleting: ", my_list)
my_list[1:3] = []
print("After deleting slice: ", my_list)


print("List comprehension:")
my_list = [x * 2 for x in my_list]
print("After applying function: ", my_list)
my_list = [x for x in my_list if x % 2 == 0] 
print("After filtering: ", my_list)


print("Sorting:")
my_list.sort()
print("Sorted list: ", my_list)
my_list.sort(reverse=True) 
print("Reversed sorted list: ", my_list)
