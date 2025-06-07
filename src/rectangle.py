"""Rectangle figure"""
from src.figure import Figure

class Rectangle(Figure):
    """Rectangle class"""
    def __init__(self, width, height):
        if height  <= 0 or width <= 0:
            raise ValueError("Invalid values")
        self.height = height
        self.width = width

    @property
    def perimeter(self):
        """Perimetr calculation"""
        return 2 * (self.height + self.width)

    @property
    def area(self):
        """Area calculation"""
        return self.width * self.height
