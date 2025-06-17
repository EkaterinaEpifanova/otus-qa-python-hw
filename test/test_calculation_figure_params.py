"""Calculation of figure parameters tests"""
import pytest
from src.circle import Circle
from src.square import Square

@pytest.mark.parametrize(
    "figure_1, figure_2",
    [
        (Square(4), Circle(3))
    ]
)
def test_add_area_square_and_circle(figure_1, figure_2):
    """Calculation of area of square and circle"""
    expected_total = figure_1.area + figure_2.area
    result = figure_1.add_area(figure_2)
    assert result == expected_total, f"Expected {expected_total}, got {result}"

@pytest.mark.parametrize(
    "figure_1, figure_2",
    [
        (Square(5), "not_a_shape")
    ]
)
def test_add_area_with_invalid_type(figure_1, figure_2):
    """Calculation of area of square and invalid shape"""
    with pytest.raises(ValueError):
        figure_1.add_area(figure_2)
