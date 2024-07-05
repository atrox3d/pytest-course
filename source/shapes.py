import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    

    def area(self):
        return math.pi * self.radius **2
    
    def perimeter(self):
        return math.pi * 2 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.width + self.length) * 2
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Rectangle):
            if self.length == other.length and self.width == other.width:
                return True
        return False