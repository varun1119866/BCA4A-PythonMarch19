def sort_list(arr):
    sorted_arr = sorted(arr)
    return sorted_arr

size = int(input("Enter the size of the list: "))
arr = []
for i in range(size):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

print("List before sorting:", arr)
sorted_list = sort_list(arr)
print("List after sorting:", sorted_list)
