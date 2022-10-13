vowels = ['a', 'i', 'u', 'e', 'o']

latin = str(input("Enter a sentence: "))
list = latin.split(" ")

for i in list :
    last = i[-1]
    condition = False
    if i[0] in vowels:
        i += "yay"
    else:
        for element in i:
            if element in vowels and condition == False:
                i = i[1:] + i[0]
                condition = True
        if condition == False:
            for element in i:
                i = i[1:] + i[0]
                if i[0] == last:
                    break
        i += "ay"
    print (i, end=" ")             

