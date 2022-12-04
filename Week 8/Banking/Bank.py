from Customer import Customer
class Bank:
    def __init__(self,bName):
        self.__bName = bName
        self.__numOfCust = 0
        self.__customers = list()
        
    def addcustomer(self,f,l):
        self.__customers.append(Customer(f,l))
        self.__numOfCust += 1
    
    def getnumOfCust(self):
        return self.__numOfCust
    
    def getcustomers(self,index):
        return self.__customers[index]
    