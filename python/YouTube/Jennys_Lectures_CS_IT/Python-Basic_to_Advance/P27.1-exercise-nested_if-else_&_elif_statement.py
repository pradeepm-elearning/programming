import os
os.system('cls')

weight = float(input("Enter your Weight: "))
height = float(input("Enter your Height: "))

BMI = round(weight/height ** 2)

if (BMI < 18.5):
  print(f"Your BMI value is {BMI} and you are Underweight")
elif (BMI < 25):
  print(f"Your BMI value is {BMI} and you have a Normal Weight")
elif (BMI < 30):
  print(f"Your BMI value is {BMI} and you are Overweight")
elif (BMI < 35):
  print(f"Your BMI value is {BMI} and you are Obese")
else:
  print(f"Your BMI value is {BMI} and you are Clinically Obese")
