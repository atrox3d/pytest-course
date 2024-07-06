from source.shapes import Shape


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