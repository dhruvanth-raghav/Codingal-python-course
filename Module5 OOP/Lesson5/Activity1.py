from abc import ABC, abstractmethod
#ABC =Abstract Base Class (or Abstract Parent Class)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass 

#========================================================================
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("Area of the circle=",(22/7)*self.radius**2)

#========================================================================
class Rectangle(Shape):
    def __init__(self, leangth,breadth):
        self.leangth=leangth
        self.breadth=breadth

    def area(self):
        print("Area of a rectangle=",self.leangth*self.breadth)
#====================================================================

circ=Circle(45.6)
rect=Rectangle(20,16)

circ.area()
rect.area()
