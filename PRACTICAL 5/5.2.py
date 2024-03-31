#  WAP to print elements of a list[‘q’,’w’,’e’,’r’,’t’,’y’] in separate lines along with element’s both indexes (Positive and Negative).

 L=['q', 'w', 'e', 'r', 't', 'y']
length=len(L)
for a in range(length):
    print('At indexes', a, 'and',(a-length),'element :',L[a])
    
