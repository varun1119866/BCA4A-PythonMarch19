# WAP to demonstrate the working of methods used with lists

my_list = [3, 1, 4, 1, 5]
my_list.append(9)  
print("Appended list:", my_list)

my_list.sort()  
print("Sorted list:", my_list)

my_list.reverse() 
print("Reversed list:", my_list)

my_list.remove(1)  
print("List after removing first occurrence of 1:", my_list)

my_list.index(4)  
print("Index of 4:", my_list.index(4))

my_list.insert(2, 8)  
print("List after inserting 8 at index 2:", my_list)

my_list.extend([6, 7])  
print("Extended list:", my_list)

popped_element = my_list.pop()  
print("Popped element:", popped_element)
print("List after popping the last element:", my_list)
