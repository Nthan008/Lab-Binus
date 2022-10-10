print ("Enter your height: ")
feet = int(input("Feet: "))
inch = int(input("Inches: "))
height = feet*12*2.54 + inch*2.54
length = 88/100*height
print("Suggested board length: ", length, "cm")