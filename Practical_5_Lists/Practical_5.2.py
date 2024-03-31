#WAP to print elements of a list[‘q’,’w’,’e’,’r’,’t’,’y’] in Separate lines along with element’s both indexes (Positive and Negative).

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

elements = ['q', 'w', 'e', 'r', 't', 'y']

for i, element in enumerate(elements):
    print("Element:", element)
    print("Positive Index:", i)
    print("Negative Index:", i - len(elements))
    print() 

