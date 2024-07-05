import pytest

import source.shapes as shapes

@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)

def test_area(rectangle):
    assert rectangle.area() == 200

def test_perimeter(rectangle):
    assert rectangle.perimeter() == 60
