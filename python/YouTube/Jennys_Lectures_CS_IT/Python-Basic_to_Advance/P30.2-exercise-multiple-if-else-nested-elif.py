import os
os.system('cls')

size = input("Enter the Size of Pizza? (S/M/L): ")
bill = 0

if (size == "S" or size == "s"):
  bill = bill + 100
  print(f"Small Pizza is Rs.{bill}")
elif (size == "M" or size == "m"):
  bill = bill + 200
  print(f"Medium Pizza is Rs.{bill}")
else:
  bill = bill + 300
  print(f"Large Pizza is Rs.{bill}")

want_pepperoni = input("Do you want Pepperoni? (Y/N): ")
if (want_pepperoni == "y" or want_pepperoni == "Y"):
  if (size == "S"):
    bill = bill + 30
  else:
    bill = bill + 50

want_cheese = input("Do you want Extra Cheese? (Y/N): ")
if (want_cheese == "Y" or want_cheese == "y"):
  bill = bill + 20

print(f"Total Bill = {bill}")
