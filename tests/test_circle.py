import pytest
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

    def test_one(self):
        print(f'testing test_one')
        assert True
    
    def teardown_method(self, method):
        print(f'tearing down METHOD {method}')
    
    def teardown_class(cls):
        print(f'tearing down CLASS {cls}')
