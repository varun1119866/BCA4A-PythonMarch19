#WAP to create a list of any specific size. Arrange all theelements in ascending order. Display list before and after sorting

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

def sort_list(size):
    list = []

    print("Enter", size, "elements:")
    for i in range(size):
        element = int(input("Enter element " + str(i + 1) + ": "))
        list.append(element)

    print("\nList before sorting:", list)
    list.sort()
    print("List after sorting:",list)
    
size = int(input("Enter the size of the list: "))
if size <= 0:
    print("Please enter a size greater than 0.")
else:
    sort_list(size)
    