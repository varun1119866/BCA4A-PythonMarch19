size = int(input("Enter the size of the list: "))
my_list = []
for i in range(size):
    my_list.append(int(input("Enter element {}:".format(i+1))))
print("List before sorting:", my_list)
my_list.sort()
print("List after sorting:", my_list)
