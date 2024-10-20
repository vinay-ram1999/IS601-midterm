"""Test app"""
import pytest
from calculator import Calculator

@pytest.mark.parametrize("operation", [
    ('add'),
    ('subtract'),
    ('multiply'),
    ('divide'),
])
def test_calculation_operations(operation, monkeypatch):
    """simulate operation followed by exit"""
    inputs = iter([f'{operation}', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Calculator()
    with pytest.raises(SystemExit) as e:
        app.run()
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = Calculator()
    with pytest.raises(SystemExit) as e:
        app.run()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Calculator()
    with pytest.raises(SystemExit):
        app.run()
    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "unknown_command operation is not available" in captured.out
