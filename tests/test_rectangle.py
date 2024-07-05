import pytest

import source.shapes as shapes

@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def square():
    return shapes.Rectangle(10, 10)

def test_area(rectangle):
    assert rectangle.area() == 200

def test_perimeter(rectangle):
    assert rectangle.perimeter() == 60

def test_not_equal(rectangle, square):
    assert rectangle != square

