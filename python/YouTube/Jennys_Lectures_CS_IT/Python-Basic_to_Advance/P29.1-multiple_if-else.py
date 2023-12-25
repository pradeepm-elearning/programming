import os
import sys
os.system('cls')

height = int(input("Enter your height in feet: "))
photo = 0

if (height >= 3):
  print(f"Your height is {height} feet and you are eligible for a Ride")
  age= int(input("Enter your age: "))
  if (age <= 12):
    print(f"You are {age} years old. Please pay Rs.150")
    photo = 150
  elif (age <= 18):
    print(f"You are {age} years old. Please pay Rs.250")
    photo = 250
  else:
    print(f"You are {age} years old. Please pay Rs.350")
    photo = 500
  want_photo = input("Do you want to take Photo (Y/N): ")
  if (want_photo == "y" or want_photo == "Y"):
    photo = photo + 50
    print(f"Please pay a Total of Rs.{photo}")
  elif (want_photo == "n" or want_photo == "N"):
    print(f"Please pay a Total of Rs.{photo}")
#    sys.exit(0)
else:
  print(f"Your height is {height} feet and you are NOT eligible for a Ride")
  print("Try your Luck Next Year.")
print("EOF")