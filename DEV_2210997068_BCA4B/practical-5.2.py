# WAP to print elements of a list[‘q’,’w’,’e’,’r’,’t’,’y’] in separate lines along with element’s both indexes (Positive and Negative).
print("name-dev,rollno-2210997068")
my_list = ['q', 'w', 'e', 'r', 't', 'y']

for index, value in enumerate(my_list):
    print(f"Positive index: {index}, Negative index: {-len(my_list) + index}, Value: {value}")
