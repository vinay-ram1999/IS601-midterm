"""test operations"""

# Import statements:
# Disable specific pylint warnings that are not relevant for this test file.
# Import the Decimal class for precise decimal arithmetic, which is especially useful in financial calculations.
# Import pytest for writing test cases.
# Import the Calculation class from the calculator package to test its functionality.
# Import the arithmetic operation functions (add, subtract, multiply, divide) to be tested.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.plugins.add import AddOperation
from calculator.plugins.subtract import SubtractOperation
from calculator.plugins.multiply import MultiplyOperation
from calculator.plugins.divide import DivisionOperation
#from calculator.plugins.quit import ExitOperation

# pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called
# with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations
# with both integer and decimal operands to ensure the operations work correctly under different conditions.
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), AddOperation, Decimal('15')),  # Test addition
    (Decimal('10'), Decimal('5'), SubtractOperation, Decimal('5')),  # Test subtraction
    (Decimal('10'), Decimal('5'), MultiplyOperation, Decimal('50')),  # Test multiplication
    (Decimal('10'), Decimal('2'), DivisionOperation, Decimal('5')),  # Test division
    (Decimal('10.5'), Decimal('0.5'), AddOperation, Decimal('11.0')),  # Test addition with decimals
    (Decimal('10.5'), Decimal('0.5'), SubtractOperation, Decimal('10.0')),  # Test subtraction with decimals
    (Decimal('10.5'), Decimal('2'), MultiplyOperation, Decimal('21.0')),  # Test multiplication with decimals
    (Decimal('10'), Decimal('0.5'), DivisionOperation, Decimal('20')),  # Test division with decimals
])
def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    assert operation().evaluate(a,b) == expected, f"Failed {operation.__name__} operation with {a} and {b}"  # Perform the operation and assert that the result matches the expected value.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError, match="Cannot divide by 0!"):  # Expect a ValueError to be raised.
        DivisionOperation().evaluate(Decimal(3),Decimal(0))  # Attempt to perform the calculation, which should trigger the ValueError.
