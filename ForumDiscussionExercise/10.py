list = [11, 5, 14, 14, 5, 20, 8]
num = int(input("Enter a number: "))
flag = False
for i in list:
    if num == i:
        flag = True
if flag:
    print("The number is in the list")
else:
    print("The number is not in the list")