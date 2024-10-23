import pandas as pd
from tabulate import tabulate

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
        """Add a new calculation record to cls.history"""
        cls.history['Operation'].insert(0, opr_name)
        cls.history['Arguments'].insert(0, input)
        cls.history['Output'].insert(0, output)

    @classmethod
    def tabulate_history(cls) -> str:
        """Tabulates cls.history"""
        out = cls.tabulate_input_dict(cls.history)
        return out
    
    @staticmethod
    def tabulate_input_dict(inp_dict: dict) -> str:
        """Tabulates the inp_dict"""
        out = tabulate(inp_dict, tablefmt="pretty", headers="keys", numalign="right", 
                       showindex=[i[0] for i in enumerate(list(inp_dict.values())[0])])
        return out

    @classmethod
    def clear_history(cls):
        """Clear all calculations from cls.history"""
        cls.history = {'Operation':[],'Arguments':[],'Output':[]}

    @classmethod
    def delete_history(cls, idx: list):
        """Delete 1 or more operations from cls.history"""
        current_len = len(list(cls.history.values())[0])
        failed_idx = [i for i in idx if i > (current_len - 1)]
        assert failed_idx == [], f"The index values {failed_idx} are out of bounds, please specify index within the range of history"
        for key in cls.history.keys():
            cls.history[key] = [cls.history[key][x] for x in range(len(cls.history[key])) if x not in idx]

    @classmethod
    def history_df(cls) -> pd.DataFrame:
        """Convert cls.history from dict to pandas DataFrame"""
        df = pd.DataFrame(cls.history)
        return df

    def run_operation(self, opr_name: str=None, input: list | str=None):
        try:
            output = self.operations[opr_name].execute(input)
            self.record_history(opr_name, tuple([float(x) for x in input]), output) if isinstance(self.operations[opr_name], Operation) else None
        except KeyError as e:
            frm = inspect.trace()[-1]
            msg = f"KeyError: '{opr_name}' operation is not available" if frm.function == self.run_operation.__name__ else f'KeyError: {e.args[-1]}'
            logging.error(e.add_note(msg), exc_info=True)
            print(msg)
        except ValueError as e:
            frm = inspect.trace()[-1]; mod = inspect.getmodule(frm.frame)
            msg = 'ValueError: Incorrect operation call...' if (mod) and (('plugins' in mod.__name__) or ('builtins' in mod.__name__)) else f'ValueError: {e.args[-1]}'
            logging.error(e.add_note(msg), exc_info=True)
            print(msg)
        except Exception as e:
            logging.error(e, exc_info=True)
            print(f'Exception: {e.args[-1]}')

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
