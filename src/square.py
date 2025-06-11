"""Square figure"""
from src.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""
    def __init__(self, side):
        """Square is a special case of rectangle"""
        super().__init__(side, side)
