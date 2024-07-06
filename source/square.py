from .rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side) -> None:
        super().__init__(side, side)
