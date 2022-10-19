def getAccSum(myList):
    list = myList
    sum = 0
    for i in list:
        sum += i
    return (sum)

myList = [1, 3 , 5, 7, 9, 10, 20]
print(getAccSum(myList))