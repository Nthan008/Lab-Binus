from Circle import Circle
class Cylinder:
    def __init__(self,radius,color,height = 1.0):
        Circle.__init__(self,radius,color)
        self.__height = height
        
    def getHeight(self):
        return self.__height
    
    def toString(self):
        return Circle.tostring+"\nHeight:"+str(self.getHeight())
    
    def getVolume(self):
        return Circle.getArea()*self.__height
             