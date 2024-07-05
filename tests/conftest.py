import pytest
from source import shapes


@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def square():
    return shapes.Rectangle(10, 10)
