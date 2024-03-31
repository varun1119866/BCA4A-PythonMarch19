# WAP to show the creation and working of lists

my_list = [1, 2, 3, 4, 5]
print("Elements of the list:")
for item in my_list:
    print(item)
    
my_list[2] = 10
print("\nModified list:")
print(my_list)

my_list.append(6)
print("\nAppended list:")
print(my_list)
