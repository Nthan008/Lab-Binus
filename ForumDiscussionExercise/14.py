num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a second number: "))
multi_1 = num_1
multi_2 = num_2

while num_1 != num_2 :
    if num_1 < num_2 :
        num_1 += multi_1
    elif num_1 > num_2 :
        num_2 += multi_2
print ("The lcm of the two numbers is", num_1)
