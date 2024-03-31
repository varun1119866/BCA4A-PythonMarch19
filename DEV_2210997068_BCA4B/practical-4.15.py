# WAP to create a list of any specific size. Arrange all the elements in ascending order. Display list before and after sorting
print("name-dev,rollno-2210997068")
size = int(input("Enter size of list: "))
my_list = []

for _ in range(size):
    my_list.append(int(input("Enter a number: ")))

print(f"List before sorting: {my_list}")
my_list.sort()
print(f"List after sorting: {my_list}")
