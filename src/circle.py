"""Circle figure"""
import math
from src.figure import Figure

class Circle(Figure):
    """Circle class"""
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Invalid value")
        self.radius = radius

    @property
    def perimeter(self):
        """Perimetr calculation"""
        return round(2 * math.pi * self.radius, 2)

    @property
    def area(self):
        """Area calculation"""
        return round(math.pi * self.radius ** 2, 2)
