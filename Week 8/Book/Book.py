class Book:
    author = []
    
    def __init__(self,name,author,price,qty=0):
        self.__name = name
        self.__author= []
        self.__price = price
        self.__qty = qty
        
    def setName(self,name):
        self.__name = name
    
    def setAuthor(self,author):
        self.__author.append(author)
    
    def setPrice(self,price):
        self.__price = price
    
    def setQty(self,qty):
        self.__qty = qty
        
    def getName(self):
        return self.__name 
    
    def getAuthor(self):
        return self.__author
    
    def getPrice(self):
        return self.__price
    
    def getQty(self):
        return self.__qty
    
    
    
    def toString(self):
        return "\nName: "+self.getName()+"\nAuthor: "+self.getAuthor+\
               "\nPrice: "+str(self.getPrice()) +"\nQuantity: "+str(self.getQty())
        
    