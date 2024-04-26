# sum of series 3+ 6+9.... 30
# with while loop
sum = 0
i = 3
while i <= 30:
    sum = sum + i
    i = i + 3
print("Sum of series = ", sum)

# with for loop
sum = 0
for i in range(3, 31, 3):
    sum = sum + i
print("Sum of series = ", sum)