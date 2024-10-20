"""Test logging"""
from calculator import Calculator

def test_configure_logging(capsys):
    """Test the configure_logging method"""
    Calculator.configure_logging()
    captured = capsys.readouterr()
    assert 'fileConfig method' in captured.err, "Logging is not configured using the fileConfig method"
    Calculator.configure_logging(fpath='none')
    captured = capsys.readouterr()
    assert 'basicConfig method' in captured.err, "Logging is not configured using the basicConfig method"
