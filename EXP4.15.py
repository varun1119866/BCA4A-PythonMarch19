#wAP to create a list of any specific size. Arrange all the elements in ascending order. Display list before and after sorting
print("Name: lakshay\nRoll No: 2210997128")

n = int(input("Enter size of list: "))
list1 = []
for i in range(n):
    element = int(input("Enter element: "))
    list1.append(element)
print("List before sorting:", list1)
list1.sort()
print("List after sorting:", list1)
