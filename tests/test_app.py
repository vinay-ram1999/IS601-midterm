"""Test app"""
import os
import pytest
from calculator import Calculator

# This function must be on top to pass
def test_app_start_empty_history(capfd, monkeypatch):
    """Test the output of empty history call"""
    inputs = iter(['history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Calculator()
    with pytest.raises(SystemExit):
        app.run()
    captured = capfd.readouterr()
    desired = '+-----------+-----------+--------+\n| Operation | Arguments | Output |\n+-----------+-----------+--------+\n+-----------+-----------+--------+\n'
    assert desired in captured.out, "the app is not printing out empty history"

def test_app_start_empty_csv(capfd, monkeypatch):
    """Test the exported empty csv"""
    inputs = iter(['export history_pytest', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Calculator()
    default_csv_abs = os.path.abspath(os.path.join(app.get_data_dir_variable(),'history_empty.csv'))
    expected_csv_abs = os.path.abspath(os.path.join(app.get_data_dir_variable(),'history_pytest.csv'))
    with pytest.raises(SystemExit):
        app.run()
    captured = capfd.readouterr()
    assert expected_csv_abs in captured.out, "the absolute file path is not exported/returned correctly"
    with open(default_csv_abs, encoding='utf-8') as f1:
        with open(expected_csv_abs, encoding='utf-8') as f2:
            assert f1.read() == f2.read(), "The default csv and exported csv are not similar"

@pytest.mark.parametrize("operation, arg1, arg2", [
    ('add',1,1),
    ('subtract',1,1),
    ('multiply',1,1),
    ('divide',1,1),
    ('menu','',''),
    ('history','',''),
    ('export','history_pytest',''),
])
def test_calculation_operations(operation, arg1, arg2, monkeypatch):
    """simulate operation followed by exit"""
    inputs = iter([f'{operation} {arg1} {arg2}', 'exit'])
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
    assert "KeyError: 'unknown_command' operation is not available" in captured.out, "the app is not capturing unknown commands"

@pytest.mark.parametrize("operation, arg1, arg2", [
    ('add','3r',1),
    ('add',1,'2s'),
])
def test_app_start_value_error(operation, arg1, arg2, capfd, monkeypatch):
    """Test how the REPL handles an incorrect operation call before exiting."""
    # Simulate user entering an incorrect operation call followed by 'exit'
    inputs = iter([f'{operation} {arg1} {arg2}', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Calculator()
    with pytest.raises(SystemExit):
        app.run()
    # Verify that the ValueError was handled as expected
    captured = capfd.readouterr()
    assert 'ValueError: Incorrect operation call...' in captured.out, "the app is not capturing incorrect operation calls"
