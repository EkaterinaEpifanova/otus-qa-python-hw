"""Triangle tests"""
import pytest
from src.triangle import Triangle

def test_create_triangle_valid():
    """Check of creation triangle with valid sides"""
    triangle = Triangle(3, 4, 5)
    expected_area = 6
    expected_perimeter = 12
    assert triangle.area == expected_area, f"Expected area {expected_area}, got {triangle.area}"
    assert triangle.perimeter == expected_perimeter, \
        f"Expected perimeter {expected_perimeter}, got {triangle.perimeter}"

@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        (0, 0, 0),
        (-1, -2, 3),
        (3, 3, 10)
    ],
    ids=["zero value", "negative value", "invalid sides"]
)
def test_create_triangle_invalid(a, b, c):
    """Check of creation triangle with invalid sides"""
    with pytest.raises(ValueError):
        Triangle(a, b, c)
