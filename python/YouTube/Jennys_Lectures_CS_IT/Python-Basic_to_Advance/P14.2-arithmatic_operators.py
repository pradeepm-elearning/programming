import os
os.system('cls')

num1 = input("Enter 1st Number: ")
num2 = input("Enter 2nd Number: ")

num1_int = int(num1)
num2_int = int(num2)

sum = num1_int + num2_int
diff = num1_int - num2_int
prod = num1_int * num2_int
div = num1_int / num2_int
mod = num1_int % num2_int
exp = num1_int ** num2_int
cdiv = num1_int // num2_int

print("Sum of 2 Numbers =",sum)
print("Difference of 2 Numbers =",diff)
print("Product of 2 Numbers =",prod)
print("Division of 2 Numbers =",div)
print("Modulus of 2 Numbers =",mod)
print("Exponent of 2 Numbers =",exp)
print("Clean Division of 2 Numbers =",cdiv)
