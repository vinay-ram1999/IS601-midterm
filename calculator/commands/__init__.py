import logging
from abc import ABC, abstractmethod

class Operation(ABC):
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for arg in kwargs.keys():
                setattr(self, arg, kwargs[arg])

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class OperationHandler:
    history: dict[str:list] = {'Operation':[],'Arguments':[],'Output':[]}

    def __init__(self):
        self.operations = {}
    
    def add_operation(self, opr_name: str, operation: Operation):
        self.operations[opr_name] = operation

    @classmethod
    def record_history(cls, opr_name: str, input: tuple, output: float):
        """Add a new calculation record to the history."""
        cls.history['Operation'].insert(0, opr_name)
        cls.history['Arguments'].insert(0, input)
        cls.history['Output'].insert(0, output)

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        for key in cls.history.keys():
            cls.history[key].clear()
    
    def run_operation(self, opr_name: str=None, input: list=None):
        try:
            input = [float(x) for x in input]
            output = self.operations[opr_name].execute(input)
            self.record_history(opr_name, tuple(input), output) if isinstance(self.operations[opr_name], Operation) else None
        except KeyError:
            logging.error(f'{opr_name} operation is not available'); print(f'{opr_name} operation is not available')
        except ValueError:
            logging.error('Enter a valid number...'); print('Enter a valid number...')
        except Exception as e:
            logging.error(e); print(e)

class BuiltInOperation(ABC):
    opr_handler: OperationHandler = None
    env_vars: dict = None

    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for arg in kwargs.keys():
                setattr(self, arg, kwargs[arg])

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
