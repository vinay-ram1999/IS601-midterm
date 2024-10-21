import logging
import inspect
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
            input = [x for x in input]
            output = self.operations[opr_name].execute(input)
            self.record_history(opr_name, tuple(input), output) if isinstance(self.operations[opr_name], Operation) else None
        except KeyError as e:
            frm = inspect.trace()[-1]
            msg = f"KeyError: '{opr_name}' operation is not available" if frm.function == self.run_operation.__name__ else f'KeyError: {e.args[-1]}'
            logging.error(e, exc_info=True); print(msg)
        except ValueError as e:
            frm = inspect.trace()[-1]; mod = inspect.getmodule(frm.frame)
            msg = 'ValueError: Incorrect operation call...' if (mod) and ('plugins' in mod.__name__) else f'ValueError: {e.args[-1]}'
            logging.error(e, exc_info=True); print(msg)
        except Exception as e:
            logging.error(e, exc_info=True); print(f'Exception: {e.args[-1]}')

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
