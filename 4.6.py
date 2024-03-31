print("name diksha rollno2210997073")
n = int(input("Enter the value of n: "))
fib_seq = []
a, b = 0, 1
fib_seq.append(a)
fib_seq.append(b)
for i in range(2, n):
    c = a + b
    fib_seq.append(c)
    a, b = b, c
print("Fibonacci sequence up to the {}th term:".format(n))
print(fib_seq)
