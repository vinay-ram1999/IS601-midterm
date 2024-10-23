## Table of Contents
1. [Key Features](#key-features)
2. [Technologies Used](#technologies-used)
3. [Design Patterns](#design-patterns)
4. [Logging and Error Handling](#logging-and-error-handling)
5. [Environment Variables](#environment-variables)
6. [Version Control](#version-control)
7. [Testing](#testing)

## Key Features

### 1. REPL Command-Line Interface (CLI)
The Read-Eval-Print Loop (REPL) provides an intuitive command-line interface that allows users to:
- Perform arithmetic operations like addition, subtraction, multiplication, and division.
- Access builtin commands like viewing the history, importing/exporting history, and clearing or deleting it.

### 2. Plugin and Builtin Module System
- **Dynamic Plugin Loading:** The plugin system allows users to dynamically load and integrate additional functionality without modifying the core code. Arithmetic operations are implemented as plugins, providing scalability and modularity.
- **Builtin Commands:** A separate builtins module includes several essential commands for managing and interacting with the application:
  - **`menu`**: Lists all available commands (plugins and builtins) with descriptions and usage instructions.
  - **`history`**: Displays a history of all arithmetic operations performed, including their results.
  - **`import`**: Allows users to import saved history from a CSV file (implemented using pandas).
  - **`export`**: Exports the current session's history to a CSV file (implemented using pandas).
  - **`clear`**: Clears all operations in the current session's history.
  - **`delete`**: Deletes one or more specific operations from the history.
  - **`exit`**: Ends the REPL session and closes the application.

### 3. History Management
- **Efficient Storage:** History of all operations is efficiently managed using dictionaries, lists and pandas DataFrames.
- **Import/Export Functionality:** Users can import previously saved arithmetic operations or export the current session's history to a CSV file for future use.
- **Interactive History Viewing:** The `history` command displays all operations and results in a tabulated format, making it easier for users to review their calculations.
- **Delete and Clear Options:** Users can clear all operations or selectively delete one or more history items.

### 4. Design Patterns & Best Practices
- **Facade Pattern**: Simplifies interactions between the application and the pandas data manipulation logic, allowing for a cleaner, more manageable interface.

- **DRY Principle**: The code follows the "Don't Repeat Yourself" principle to ensure reusability and maintainability.

- **Look Before You Leap (LBYL) & Easier to Ask for Forgiveness than Permission (EAFP)**: These techniques are used to handle potential errors efficiently by checking for conditions before performing operations and catching exceptions where appropriate.

### 5. Logging and Error Handling
- **Logging System**: A robust logging system is in place that sets different logging levels like `INFO` and `ERROR` to filter the logs:
  - **INFO Level**: Logs application operations, informational messages and all other levels.
  - **ERROR Level**: Logs errors along with detailed tracebacks, helping developers quickly identify issues and higher level messages.
- **Log Output Management**: Two log files are maintained separately for logging levels `INFO` and `ERROR`. Additionally, console output is limited to `CRITICAL` level to prevent clutter for end users.
- **Exception Handling**: All exceptions are handled using `try-except` blocks, ensuring that users are provided with helpful error messages while detailed logs are maintained for developers.

### 6. User-Friendly Output
- The commands `menu`, `history`, `import`, `clear`, and `delete` display output in a clear, tabulated format using the `tabulate` library. This ensures that users have a readable, structured view of their data and operations. Two examples of both `menu` and `history` operations are displayed below.

![alt text](https://github.com/vinay-ram1999/IS601-midterm/tree/master/static/menu.png)

![alt text](https://github.com/vinay-ram1999/IS601-midterm/tree/master/static/history.png)

### 7. Version Control
- **Git Best Practices**: This project is maintained using Git version control. Best practices such as branching for feature development and using logical, meaningful commit messages were followed throughout the project lifecycle.

### 8. Testing
- **Test Coverage**: The application is thoroughly tested using the `pytest` framework. All modules, functions, and features have been tested with a coverage rate of 98%.
- **Code Quality**: The codebase adheres to PEP 8 standards, ensuring readability and maintainability. Testing also includes running `pylint` to maintain code quality.

---

## Technologies Used
- **Python**: The core programming language used for developing the application.
- **Pandas**: Used for managing and manipulating the history of operations.
- **Tabulate**: Displays tabulated data for a clear, organized output.
- **Pytest**: Used for testing the application and achieving high test coverage.
- **Git**: Version control system to track changes and manage the development process.

---

## Design Patterns

### Facade Pattern
Used to hide the complexity of interacting with Pandas DataFrames and CSV file handling, providing a simple interface for managing history. As you can see below, we are only instantiating the `Calculator` class in `main.py` and everything else is handled within this class.

https://github.com/vinay-ram1999/IS601-midterm/blob/e78bb07c4f31ae50fd16221fd9d7fe24023fe2fb/main.py#L1-L5

### Command Pattern
The REPL structure follows the Command Pattern, where each operation (arithmetic or builtin command) is encapsulated in a command class.

### DRY, LBYL, EAFP
The code is written to be reusable and maintainable, with error handling that ensures smooth operation without crashing the application due to user input errors.

A good exaple for DRY is mentioned below, where the function `tabulate_input_dict` from `OperationHandler` class is used to structure the outputs of commands like `history`, `import`, `clear` and `delete` before printing to the console.

https://github.com/vinay-ram1999/IS601-midterm/blob/e78bb07c4f31ae50fd16221fd9d7fe24023fe2fb/calculator/commands/__init__.py#L40-L46

There are many cases where LBYL and EAFP design principles are used out of which two examples are mentioned below for reference.

https://github.com/vinay-ram1999/IS601-midterm/blob/e78bb07c4f31ae50fd16221fd9d7fe24023fe2fb/calculator/__init__.py#L65-L78

https://github.com/vinay-ram1999/IS601-midterm/blob/e78bb07c4f31ae50fd16221fd9d7fe24023fe2fb/calculator/builtins/export/__init__.py#L20

---

## Logging and Error Handling

- **Logging**: Log files store `INFO` level and `ERROR` level messages in separate files, aiding in filtering, debugging and application monitoring.
- **Error Handling**: Any issues or exceptions are clearly displayed to the user and logged for developers.

---

## Environment Variables

- **`.env`**: Environment variables like data directory are stored and loaded from the [.env](./.env) file.

---

## Version Control

Git is used for version control. The project follows best practices:
- Logical commit messages.
- Feature development via branches.

---

## Testing

Testing is performed using `pytest`, with a focus on achieving high coverage:
- **98% Test Coverage**: All major functions and features are covered.
- **Linting**: Code adheres to PEP 8 standards, verified using `pylint`.

---
