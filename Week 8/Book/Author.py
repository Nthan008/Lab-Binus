class Author:
    def __init__(self,name="",email="",gender=""):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def setName(self,name):
        self.__name = name
            
    def setEmail(self,email):
        self.__email = email
            
    def setGender(self,gender):
        self.__gender = gender
            
    def getName(self):
        return self.__name            
        
    def getEmail(self):
        return self.__email
        
    def getGender(self):
        return self.__gender
        
    def toString(self):
        return "Name: "+self.getName()+"\nEmail: "+self.getEmail()+"\nGender: "+self.getGender()
        
        
                
        
        