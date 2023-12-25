import os
os.system('cls')

height = int(input("Enter your Height in feet: "))

if (height >= 3):
  print(f"You are {height} feet tall and you are eligible for a ride")
  age = int(input("Enter your Age: "))
  if (age <= 12):
    print(f"Please pay Rs.150 as you are {age} years old")
  elif (age >= 18):
    print(f"Please pay Rs.500 as you are {age} years old")
  else:
    print(f"Please pay Rs.250 as you are {age} years old")
  print("Enjoy your ride")
else:
  print("You are not Eligible for a ride as you are less than 3 feet tall")
  print("Try again next year!")
