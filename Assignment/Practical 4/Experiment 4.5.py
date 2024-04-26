#WAP to compute the Sum of the Series 4 + 8 + 12 + … + 40\
# with while loop
sum = 0
i = 4
while i <= 40:
    sum = sum + i
    i = i + 4
print("Sum of series = ", sum)

# with for loop
sum=0
for i in range(4, 41, 4):
    sum = sum + i
print("Sum of series = ", sum)