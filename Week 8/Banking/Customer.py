class Customer:
    def __init__(self,f,l):
        self.__firstName = f
        self.__lastName = l
        
    def getfirstName(self):
        return self.__firstName
    
    def getlastName(self):
        return self.__lastName
    
    def getAccount(self):
        return self.__account
    
    def setAccount(self,account):
        self.__account = account