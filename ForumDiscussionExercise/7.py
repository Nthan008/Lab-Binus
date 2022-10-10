a,b,c = eval(input("Give three numbers seperated with commas: "))
sum = a+b+c
if a == b == c :
    sum = 3*sum
    print("The three numbers are equal hence the triple of the sum is:", sum)
print("The sum of the three numbers is ")