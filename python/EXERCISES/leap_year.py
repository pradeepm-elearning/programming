import os
os.system('cls')

year = int(input("Enter a year in YYYY format: "))

if (year % 4 == 0):
  print(f"{year} is a Leap year")
else:
  print(f"{year} is not a Leap year")
print("Have a Great Day")
