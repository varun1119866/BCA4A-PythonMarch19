my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Sliced list:", my_list[1:4])
my_list[2] = 10
print("Modified list:", my_list)
my_list.append(6)
print("List after append:", my_list)
if 3 in my_list:
    my_list.remove(3)
    print("List after removal:", my_list)
else:
    print("Element 3 not found in the list.")
my_list.insert(2, 7)
print("List after insertion:", my_list)
print("Length of the list:", len(my_list))
print("Is 8 in the list?", 8 in my_list)
print("Iterating over the list:")
for item in my_list:
    print(item)
reversed_list = list(reversed(my_list))
print("Reversed list:", reversed_list)
