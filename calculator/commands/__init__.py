import logging
from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class OperationHandler:
    def __init__(self):
        self.operations = {}
    
    def add_operation(self, opr_name: str, operation: Operation):
        self.operations[opr_name] = operation
    
    def run_operation(self, opr_name: str, values: list):
        try:
            vals = [float(x) for x in values]
            self.operations[opr_name].execute(vals)
        except KeyError:
            logging.error(f'{opr_name} operation is not available'); print(f'{opr_name} operation is not available')
        except ValueError:
            logging.error('Enter a valid number...'); print('Enter a valid number...')
        except Exception as e:
            logging.error(e); print(e)
