import math
from Polygon import Polygon
class Heptagon(Polygon):
    def __init__(self):
        Polygon.__init__(self,7)
    def findArea(self):
        a = self.sides
        # calculate the semi-perimeter 
        area = 7/4 * a**2 * math.tan(7/180)
        print('The area of the triangle is %0.2f' %area)