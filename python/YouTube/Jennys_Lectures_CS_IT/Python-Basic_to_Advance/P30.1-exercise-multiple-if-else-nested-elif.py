import os
os.system('cls')

pizza = input("Enter the Size of Pizza (S/M/L): ")
pizza_cost = 0
extra_pepperoni = 0
extra_cheese = 0

if (pizza == "S"):
  pizza_cost = 100
  print(f"You have selected a SMALL size Pizza. The cost is Rs.{pizza_cost}")
  want_pepperoni = input("Do you want extra Pepperoni? (Y/N): ")
  if (want_pepperoni == "Y" or want_pepperoni == "y"):
    extra_pepperoni = 30
    print(f"Extra pepperoni for SMALL size Pizza is Rs.{extra_pepperoni}")
elif (pizza == "M"):
  pizza_cost = 200
  print(f"You have selected a MEDIUM size Pizza. The cost is Rs.{pizza_cost}")
  want_pepperoni = input("Do you want extra Pepperoni? (Y/N): ")
  if (want_pepperoni == "Y" or want_pepperoni == "y"):
    extra_pepperoni = 50
    print(f"Extra pepperoni for SMALL size Pizza is Rs.{extra_pepperoni}")
else:
  pizza_cost = 500
  print(f"You have selected a LARGE size Pizza. The cost is Rs.{pizza_cost}")
  want_pepperoni = input("Do you want extra Pepperoni? (Y/N): ")
  if (want_pepperoni == "Y" or want_pepperoni == "y"):
    extra_pepperoni = 50
    print(f"Extra pepperoni for SMALL size Pizza is Rs.{extra_pepperoni}")
want_cheese = input("Do you want extra Cheese? (Y/N): ")
if (want_cheese == "Y" or want_cheese == "y"):
  extra_cheese = 20
  print(f"You have selected Extra Cheese & the cost is Rs.{extra_cheese}")

grand_total = pizza_cost + extra_pepperoni + extra_cheese
print(f"Your Grand Total is {grand_total}")