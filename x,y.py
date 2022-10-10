x,y = eval(input("Enter x, y coordinate : "))

if (x > 0 and y > 0) :
    print(f"{x},{y} is in the first quadrant")
elif (x < 0 and y > 0) :
    print(f"{x},{y} is in the second quadrant")
elif (x < 0 and y < 0) :
    print(f"{x},{y} is in the third quadrant")
elif (x > 0 and y < 0) :
    print(f"{x},{y} is in the fourth quadrant")
elif (x == 0 and y != 0) :
    print(f"{x},{y} is in the y axis")
elif (x != 0 and y == 0) :
    print(f"{x},{y} is in the x axis") 
else :
    print(f"{x},{y} is the origin")