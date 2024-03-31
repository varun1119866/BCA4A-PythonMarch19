# product of series m = 15*13*11*9*7
print("Name: Agamjot Singh\nRoll No: 2210997017")

p = 1
i = 15
while i > 0:
    p = p * i
    i = i - 2
    if i<7:
        break
print("Sum of series = ", p)