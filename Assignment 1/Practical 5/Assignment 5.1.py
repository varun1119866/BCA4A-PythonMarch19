my_list = [1, 2, 3, 4, 5]

print("Elements of the list:")
for element in my_list:
    print(element)

my_list[2] = 10
print("Modified list:", my_list)

my_list.append(6)
print("List after appending:", my_list)

my_list.remove(4)
print("List after removing:", my_list)

print("Length of the list:", len(my_list))