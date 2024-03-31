#WAP to compute Sum of the series 3 + 6 + 9 + … + 30

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

start = 3
end = 30
step = 3
sum = 0

for i in range(start, end + 1, step):
    sum += i

print("Sum of the series 3 + 6 + 9 + ... + 30 is:",sum)
