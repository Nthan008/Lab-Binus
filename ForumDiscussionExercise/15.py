num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a second number: "))
num_3 = int(input("Enter a third number: "))
sum = num_1 + num_2 + num_3
if num_1 == num_2 or num_1 == num_3 or num_2 == num_3 :
    sum = 0
print ("The sum of the three numbers is", sum)
