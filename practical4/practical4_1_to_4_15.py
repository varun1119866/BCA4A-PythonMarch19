# #4.1
# str="shaurya"
# for i in str:
#     print(i)

# #4.2
# n=10
# for i in range(0,n+1):
#     print(i)

# #4.3
# n=10
# for i in range(0,n+1):
#     if i==4:
#         continue
#     if i==9:
#         break
#     print(i)

# #4.4
# n=10
# i=0
# while i in range(n+1):
#     if(i==5):
#         break
#     print(i)
#     i+=1
# else:
#     print("Loop terminated naturally")

# while i in range(n+1):
#     print(i)
#     i+=1
# else:
#     print("Loop terminated naturally")


# #4.5
# series=0
# number=int(input("Enter number of series: "))
# for n in range(0,number):
#     series+=4
#     print(series)



# #4.6
# series=int(input("Enter number of series: "))
# n1=0
# n2=1
# n3=0
# for i in range(0,series):
#     print(n3)
#     n3=n1+n2
#     n1=n2
#     n2=n3
  
    
# # 4.7
# num=int(input("Enter number to print its table: "))
# for i in range(0,11):
#     print(num," x ",i," = ",(num*i))


# #4.8
# num=5

# for r in range(1,num+1):
#     for c in range(1,r+1):
#         print(c,end = " ")
#     print()


# #4.9
# num=3
# for i in range(1,11):
#     print((num*i),end=" ")

# # 4.10
# num=15
# m=1
# while num>0:
#     m*=num
#     num-=2
# print(m)


# # 4.11
# num=int(input("Enter a number to calculate its factorial: "))
# fact=1

# for i in range(1,num+1):
#     fact*=i
# print(fact)

# #4.12
# n=10
# for i in range(2,n+1):
#     if i%2==0:
#         print(i*i*i)

# #4.13
# n=int(input("Enter number: "))
# sum=0
# for i in range(0,n+1):
#     sum+=i
# print(sum)

# # 4.14
# i=10
# while i>=1:
#     print(i)
#     i-=1

# # 4.15
# list1=[2,5,23,1,4,56,67]

# print(list1)
# list1.sort()
# print(list1)