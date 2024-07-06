import pytest

from source.square import Square

areas = [(side, side ** 2) for side in (5, 4, 9)]
perimeters = [(side, side * 4) for side in (5, 4, 9)]

@pytest.mark.parametrize('side, area', areas)
def test_multiple_square_areas(side, area):
    assert Square(side).area() == area

@pytest.mark.parametrize('side, perimeter', perimeters)
def test_multiple_square_perimeters(side, perimeter):
    assert Square(side).perimeter() == perimeter


