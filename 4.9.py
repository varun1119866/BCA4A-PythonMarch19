print ("Name: Arpita Chaudhary\nRoll No: 2210997047")

def sum_series(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
    return total

n = 10
print(sum_series(3, 30, n))
