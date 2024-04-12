#WAP to accept basic salary for the employee. Calculate DA as 30% of bs, HRA as 20% of bs if bs>=20000else compute DA as 20% and HRA as 10%. Display the result.
bs = int(input("Enter basic salary: "))

if bs>=20000:
    da = 0.3*bs
    hra = 0.2*bs
else:
    da = 0.2*bs
    hra = 0.1*bs

print("Net salary is", bs+da+hra)