
#4.1

counter = 0
text = "Hello, this is a while loop example!"
while counter < 5:
    print(text)
    counter += 1


#4.2
number=10
while number<20:
    print(number)
    number=number+1

#4.3
for i in range(0,10):
    if i<5:
        continue #skip rest of the loop
    if i==9:
        break  #jump out of the loop
    print(i)


#4.4
number=5
while number<10:
    if number==11:
        print("Number 11 found")
        break;
    number=number+1
else:
    print("Number 11 not found")

print("End of program")


#4.5
sum=0
for i in range(4, 41, 4):
    sum += i

print(f"Sum is {sum}")


#4.6
number=int(input("Enter the number of values "))
if number==0:
    print("Enter a valid number")

else:
    a=0
    b=1
    for i in range(1,number+1):
        if i==1:
            print(a)
            continue
        if i==2:
            print(b)
            continue

        c=a+b
        print(c)
        a=b
        b=c
        i=i+1




#4.7
number=int(input("Enter a number"))
for i in range(1,11):
    print(f"{number} * {i} = {number*i}")


#4.8
rows = int(input("Enter the number of rows for the triangle: "))

for i in range(1,rows+1):
    print(" " * (rows-i), end="")
    print("*" * (2*i-1))

#4.9
sum=0
for i in range(3,31,3):
    sum+=i

print(f"Sum is : {sum}")


#4.10
product=1
for i in range(15,6,-1):
    product=product*i
print(product)


#4.11
number=int(input("Enter a number : "))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print(factorial)


#4.12
for i in range(1,11):
    print(f"Cube of {i} is {i**3}")


#4.13
number=int(input("Enter a number : "))
sum=0
for i in range(1,number+1):
    sum+=i
print(sum)


#4.14
for i in range(10,0,-1):
    print(i)

#4.15
size=int(input("Enter the size of array"))
list=[]
for i in range(0,size):
    element=int(input(f"Enter value at {i} index"))
    list.append(element)

print("Before sorting : ",list)
list.sort()
print("After sorting : ",list)


