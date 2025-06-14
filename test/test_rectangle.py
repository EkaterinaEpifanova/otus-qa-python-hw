"""Rectangle tests"""
import pytest
from src.rectangle import Rectangle

def test_create_rectangle():
    """Check of creation rectangle"""
    rectangle = Rectangle(10, 50)
    expected_area =  500
    expected_perimeter = 120
    assert rectangle.area == expected_area, f"Expected area {expected_area}, got {rectangle.area}"
    assert rectangle.perimeter == expected_perimeter, \
        f"Expected perimeter {expected_perimeter}, got {rectangle.perimeter}"

@pytest.mark.parametrize(
    ("height", "width"),
    ([0 , 0], [-1, -2]),
    ids=["zero value", "negative value"]
)
def test_rectangle_area_and_perimeter(height, width):
    """Check of calculation area and perimeter of rectangle"""
    with pytest.raises(ValueError):
        Rectangle(height, width)
