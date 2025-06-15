"""Triangle figure"""
import math
from src.figure import Figure

class Triangle(Figure):
    """Triangle class"""
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0  or c <=0:
            raise ValueError("Invalid values")
        if a + b <= c or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        """Perimetr calculation"""
        return round(self.a + self.b + self.c, 2)

    @property
    def area(self):
        """Area calculation"""
        height = self.perimeter / 2
        return round(math.sqrt(height * (height - self.a) * (height - self.b) * (height - self.c)), 2)
