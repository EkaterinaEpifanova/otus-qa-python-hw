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
        return round(2 * (self.height + self.width), 2)

    @property
    def area(self):
        """Area calculation"""
        return round(self.width * self.height , 2)
