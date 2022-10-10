import math

base = int(input("Enter the base of the right angled triangle: "))
height = int(input("Enter the height of the right angled triangle: "))
hyp = base**2 + height**2

print("The hypotenuse of the right angled triangle is", math.sqrt(hyp))