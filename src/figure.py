"""Basic abstract geometrical figure"""
from abc import abstractmethod, ABC

class Figure(ABC):
    """Figure class"""
    @property
    @abstractmethod
    def area(self):
        """Area calculation"""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """Perimetr calculation"""
        pass

    def add_area(self, figure):
        """Summ of the area"""
        if not isinstance(figure, Figure):
            raise ValueError("Passed object is not a geometric figure")
        return self.area + figure.area
