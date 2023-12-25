#Calculate BMI
import os
os.system('cls')

height = int(input("Enter the Height: "))
weight = int(input("Enter the weight: "))

BMI = weight / (height ** 2)
print("BMI Value is:", BMI)