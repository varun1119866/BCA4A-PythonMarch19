# WAP to check if one No. is divisible by the other or not

print("Enter a Number (Numerator): ")
numerator = int(input())
print("Enter a Number (denominator): ")
denominator = int(input())

if numerator%denominator==0:
  print(numerator, " is divisible by ",denominator)
else:
  print(numerator, " is not divisible by ",denominator)
