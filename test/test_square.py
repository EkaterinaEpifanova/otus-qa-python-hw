"""Square tests"""
import pytest
from src.square import Square

def test_create_square():
    """Check of creation square"""
    square = Square(10)
    expected_area =  100
    expected_perimeter = 40
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
