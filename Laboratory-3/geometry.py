
import math
class RegularPolygon:
    def __init__(self, n=3, s=1, x=0, y=0):
        self.n = n
        self.s = s
        self.x = x
        self.y = y
    
    # Get the variables
    def getNoOfSides (self):
        return self.n 
    def getLengthOfSides (self):
        return self.s

    # Set the variables
    def setNoOfSides (self,n):
        self.n = n
    def setLenghtOfSides (self,s):
        self.s = s

    # Get the Area and Perimeter
    def getPerimeter(self):
        return self.n * self.s
    def getArea (self):
        return (self.n * (self.s)^2)/(4 * math.tan((3.14)/self.n))

# Print the Area And Perimeter
polygon1 = RegularPolygon(6,4)
print ("Measurements of Polygon1: \nArea:", polygon1.getArea())
print (f"Perimeter: {polygon1.getPerimeter()} \n")

polygon2 = RegularPolygon(10,4,5.6,7.8)
print ("Measurements of Polygon2: \nArea:", polygon2.getArea())
print ("Perimeter:", polygon2.getPerimeter())


