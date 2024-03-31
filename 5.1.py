def main():
    # Creating a list
    my_list = [1, 2, 3, 4, 5]
    print("Initial list:", my_list)

    # Accessing elements of the list
    print("First element:", my_list[0])
    print("Last element:", my_list[-1])

    # Slicing the list
    print("Sliced list:", my_list[2:4])

    # Modifying elements of the list
    my_list[2] = 10
    print("Modified list:", my_list)

    # Appending elements to the list
    my_list.append(6)
    print("List after appending 6:", my_list)

    # Removing elements from the list
    my_list.remove(4)
    print("List after removing 4:", my_list)

    # Finding the length of the list
    print("Length of the list:", len(my_list))

    # Checking if an element is present in the list
    if 3 in my_list:
        print("3 is present in the list")
    else:
        print("3 is not present in the list")

    # Iterating over the list
    print("Iterating over the list:")
    for item in my_list:
        print(item)

if _name_ == "_main_":
    main()
