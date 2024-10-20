"""Test .env loading"""
from calculator import Calculator

def test_environment_variable():
    """Test the get_environment_variable() method"""
    assert Calculator().get_environment_variable() == 'DEVELOPMENT', "Environment variable is not extracted!"
