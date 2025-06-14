"""Circle tests"""
import pytest
from src.circle import Circle

def test_create_circle():
    """Check of creation circle"""
    circle = Circle(10)
    expected_area = 314.16
    expected_perimeter = 62.83
    actual_area = round(circle.area, 2)
    actual_perimeter = round(circle.perimeter, 2)
    assert actual_area == expected_area, f"Expected area {expected_area}, got {actual_area}"
    assert actual_perimeter == expected_perimeter, \
        f"Expected perimeter {expected_perimeter}, got {actual_perimeter}"

@pytest.mark.parametrize(
    "radius",
    [0 , -1],
    ids=["zero value", "negative value"]
)
def test_circle_area_and_perimeter(radius):
    """Check of calculation area and perimeter of circle"""
    with pytest.raises(ValueError):
        Circle(radius)
