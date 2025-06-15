"""Triangle tests"""
import pytest
from src.triangle import Triangle

@pytest.mark.parametrize(
    "a, b, c, expected_area, expected_perimeter",
    [
        (3, 4, 5, 6, 12)
    ]
)
def test_create_triangle_valid(a, b, c, expected_area, expected_perimeter):
    """Check of creation triangle with valid sides"""
    triangle = Triangle(a, b, c)
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
