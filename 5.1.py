print("name himani rollno 2210997096")
# Creating and initializing a list
my_list = [1, 2, 3, 4, 5]

# Accessing and printing the elements of a list
print("My list:", my_list)
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing a list
print("Slicing:", my_list[1:4])

# Inserting an element into a list
my_list.insert(2, 99)
print("List after inserting 99:", my_list)

print("name himani rollno 2210997096")
my_list.append(100)
print("List after appending 100:", my_list)


my_list.remove(3)
print("List after removing 3:", my_list)


print(1 in my_list)
print(10 in my_list)


for i, elem in enumerate(my_list):
    print("Index:", i, "Element:", elem)


my_list.sort()
print("Sorted list:", my_list)


my_list.reverse()
print("Reversed list:", my_list)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("List1:", list1)
print("List2:", list2)
list3 = list1 + list2
print("List3 after concatenation:", list3)


list1.extend(list2)
print("List1 after extending:", list1)

my_list = [x**2 for x in range(1, 10)]
print("List of squares:", my_list)
