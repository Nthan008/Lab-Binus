import math

x1, y1 = eval(input("Enter a point (x, y): "))
x2, y2 = eval(input("Enter a second point (x,y): "))
distance_x = abs(x2-x1)
distance_y = abs(y2-y1)
distance = (distance_x)**2+(distance_y)**2

print ("The distance between the two points is", math.sqrt(distance))