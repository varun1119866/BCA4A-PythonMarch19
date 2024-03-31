def is_leap_year(year):
  
  is_divisible_by_4 = year % 4 == 0
  is_century = year % 100 == 0
  is_divisible_by_400 = year % 400 == 0

  return (is_divisible_by_4 and not is_century) or is_divisible_by_400

year = int(input("Enter a year: "))

if is_leap_year(year):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")

print("Karan Arora\n2210997111\nBCA4 B-1")
