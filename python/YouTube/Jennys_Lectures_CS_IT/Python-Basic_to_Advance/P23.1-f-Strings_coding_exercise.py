import os
os.system('cls')

age = int(input("Enter your Age: "))
years_left = 60 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {months_left} months, {weeks_left} weeks & {days_left} days left to Live.")


