#WAP to compute the Sum of the Series 4 + 8 + 12 + … + 40

print("Name : Simranjeet Kaur\nRoll number : 2210997238\n")

start = 4
end = 40
step = 4
sum = 0

for i in range(start, end+1, step):
    sum += i

print("Sum of the series 4 + 8 + 12 + ... + 40 is:", sum)
