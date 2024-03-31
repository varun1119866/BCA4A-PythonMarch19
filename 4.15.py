def create_and_sort_list(size):
    # Create a list of specified size
    my_list = []
    for i in range(size):
        num = int(input(f"Enter element {i+1}: "))
        my_list.append(num)

    # Display the list before sorting
    print("List before sorting:", my_list)

    # Sort the list in ascending order
    my_list.sort()

    # Display the list after sorting
    print("List after sorting:", my_list)

def main():
    size = int(input("Enter the size of the list: "))
    create_and_sort_list(size)

if _name_ == "_main_":
    main()
