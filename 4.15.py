size = int(input("Enter the size of the list: "))
lst = [int(input(f"Enter element {i+1}: ")) for i in range(size)]
print("List before sorting:", lst)
lst.sort()
print("List after sorting:", lst)
