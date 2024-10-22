"""Test app"""
import os
import pytest
from calculator import Calculator

def test_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = Calculator()
    with pytest.raises(SystemExit) as e:
        app.run()
    assert e.type == SystemExit

def test_start_unknown_command(capfd, monkeypatch):
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

# These function's must be on top to pass
def test_start_empty_history(capfd, monkeypatch):
    """Test the output of empty history call"""
    inputs = iter(['history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Calculator()
    with pytest.raises(SystemExit):
        app.run()
    captured = capfd.readouterr()
    desired = '+-----------+-----------+--------+\n| Operation | Arguments | Output |\n+-----------+-----------+--------+\n+-----------+-----------+--------+\n'
    assert desired in captured.out, "the app is not printing out empty history"

def test_start_export_empty_csv(capfd, monkeypatch):
    """Test the exported empty csv"""
    inputs = iter(['export history_pytest.csv', 'exit'])
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

@pytest.mark.parametrize("operations", [
    ['add er 2',
    'add',
    'divide 1 0',
    'import',
    'import abc.cs',
    'import abc.csv',
    'export history.cv',
    'exit'] # There should be an exit command at the end
])
def test_simulate_known_exceptions(operations, capfd, monkeypatch):
    """Test how the REPL handles all known exceptions except unknown_command which is performed above"""
    # Simulate user entering all operations calls followed by exit at the end
    inputs = iter(operations)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Calculator()
    with pytest.raises(SystemExit):
        app.run()
    captured = capfd.readouterr()
    # Verify incorrect operation call
    assert 'ValueError: Incorrect operation call...' in captured.out
    # Verify divide by 0
    assert 'Cannot divide by 0!' in captured.out
    # Verify import errors
    assert 'IndexError: Input file name is not provided' in captured.out
    assert "AssertionError: abc.cs does not end with '.csv'" in captured.out
    assert f"{os.path.sep}abc.csv does not exists" in captured.out
    # Verify export error
    assert "AssertionError: The file_name argument should end with '.csv'" in captured.out

@pytest.mark.parametrize("operation, arg1, arg2", [
    ('add',1,1),
    ('subtract',1,1),
    ('multiply',1,1),
    ('divide',1,1),
    ('menu','',''),
    ('history','',''),
    ('export','history_pytest.csv',''),
    ('import','data/import.csv',''),
])
def test_plugin_builtin_operations(operation, arg1, arg2, monkeypatch):
    """simulate operation followed by exit"""
    inputs = iter([f'{operation} {arg1} {arg2}', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = Calculator()
    with pytest.raises(SystemExit) as e:
        app.run()
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
