my_list = ['q', 'w', 'e', 'r', 't', 'y']

print("Element Index (Positive) Index (Negative)")
for index, element in enumerate(my_list):
    print(element, index, -(len(my_list) - index))
