import math
class circle:
    def __init__(self,radius):
        self.__radius=radius
    def setRadius(self,radius):
        self.__radius=radius
    def getRadius(self):
        return self.__radius
    def area(self):
        return math.pi*self.__radius**2
    def __add__(self,another_circle):
        return circle(self.__radius+another_circle.__radius)
    def __gt__(self,another_circle):
        return self.__radius>another_circle.__radius
    def __it__(self,another_circle):
        return self.__radius<another_circle.__radius
    def __str__(self):
        return "circle with radius "+str(self.__radius)
c1=circle(4)
print(c1.getRadius())
c2=circle(5)
print(c2.getRadius())
c3=c1+c2
print(c3.getRadius())
print(c3>c2)
print(c1<c2)
print(c3)

