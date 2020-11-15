import pytest
from converter import convert

def test_convert_measurement():
    user_input = '100 cm in m'
    assert convert(user_input) == '1.0 m'

def test_different_unit():
    user_input = '100 c in f'
    assert convert(user_input) == 212
    
def test_different_unit_type():
    user_input = '100 cm in f'
    assert convert(user_input) == 'units are not of the same type'
