import pytest
from source.rectangle import Rectangle


@pytest.fixture
def rectangle():
    return Rectangle(10, 20)

@pytest.fixture
def square():
    return Rectangle(10, 10)
