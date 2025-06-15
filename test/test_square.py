"""Square tests"""
import pytest
from src.square import Square

@pytest.mark.parametrize(
    "side, expected_area, expected_perimeter",
    [
        (10, 100, 40)
    ]
)
def test_create_square(side, expected_area, expected_perimeter):
    """Check of creation square"""
    square = Square(side)
    assert square.area == expected_area, f"Expected area {expected_area}, got {square.area}"
    assert square.perimeter == expected_perimeter, \
        f"Expected perimeter {expected_perimeter}, got {square.perimeter}"

@pytest.mark.parametrize(
    "side",
    [0 , -1],
    ids=["zero value", "negative value"]
)
def test_square_area_and_perimeter(side):
    """Check of calculation area and perimeter of square"""
    with pytest.raises(ValueError):
        Square(side)
