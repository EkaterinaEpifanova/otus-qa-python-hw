"""Calculation of figure parameters tests"""
import pytest
from src.circle import Circle
from src.square import Square

def test_add_area_square_and_circle():
    """Calculation of area of square and circle"""
    square = Square(4)
    circle = Circle(3)
    expected_total = round(square.area + circle.area, 2)
    result = round(square.add_area(circle), 2)
    assert result == expected_total, f"Expected {expected_total}, got {result}"

def test_add_area_with_invalid_type():
    """Calculation of area of square and invalid shape"""
    square = Square(5)
    invalid_object = "not_a_shape"
    with pytest.raises(ValueError):
        square.add_area(invalid_object)
