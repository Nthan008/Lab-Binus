def findvalue(mydict,val):
    name = []
    for k in mydict:
        if val == mydict[k]:
            name.append(k)
    return name
            
            
mydict = {'Cristoval':80, 'Edelyne':90, 'Febrian':85, 'Jessica':90}

print(findvalue(mydict,90))         
