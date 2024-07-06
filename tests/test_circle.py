# import pytest
import source.shapes as shapes

def setup_module(module):
    print(f'setting up MODULE {module}')

def teardown_module(module):
    print(f'tearing down MODULE {module}')

class TestCircle:

    def setup_class(cls):
        print(f'setting up CLASS {cls}')

    def setup_method(self, method):
        print(f'setting up METHOD{method}')
        self.circle = shapes.Circle(10)

    def test_area(self):
        assert self.circle.area() == 314.1592653589793

    def test_perimeter(self):
        print(f'testing test_two')
        assert self.circle.perimeter() == 62.83185307179586
    
    def teardown_method(self, method):
        print(f'tearing down METHOD {method}')
        del self.circle
    
    def teardown_class(cls):
        print(f'tearing down CLASS {cls}')
