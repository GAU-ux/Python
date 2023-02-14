import math

class shape:
    def __init__(self,color='black',filled=False):
        self.__color=color
        self.__filled= filled
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color = color
    def get_filled(self):
        return self.__filled
    def set_filled(self,filled):
        self.__filled = filled
    
class Rectangle(shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth
    def get_length(self):
        return self.__length()
    def set_length(self,length):
        self.__length = length
    def get_breadth(self):
        return self.__breadth
    def set_breadth(self,breadth):
        self.__breadth = breadth
    def get_area(self):
        return self.__length*self.__breadth
    def get_perimeter(self):
        return 2*(self.__breadth+self.__length)


class Circle(shape):
    def __init__(self,r):
        super().__init__()
        self.__radius = r

    def get_radius(self):
        return self.__radius
    def set_radius(self,r):
        self.__radius = r
    def get_area(self):
        return 3.14*self.__radius*self.__radius
    def get_perimeter(self):
        return 2*3.14*self.__radius

r1 = Rectangle(10.5, 2.5)
 
print("Area of rectangle r1:", r1.get_area())
print("Perimeter of rectangle r1:", r1.get_perimeter())
print("Color of rectangle r1:", r1.get_color())
print("Is rectangle r1 filled ? ", r1.get_filled())
r1.set_filled(True)
print("Is rectangle r1 filled ? ", r1.get_filled())
r1.set_color("orange")
print("Color of rectangle r1:", r1.get_color())
 
c1 = Circle(12)
 
print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f"))
print("Color of circle c1:", c1.get_color())
print("Is circle c1 filled ? ", c1.get_filled())
c1.set_filled(True)
print("Is circle c1 filled ? ", c1.get_filled())
c1.set_color("blue")
print("Color of circle c1:", c1.get_color())

