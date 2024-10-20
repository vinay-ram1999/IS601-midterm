import logging
from calculator.commands import Operation

class AddOperation(Operation):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a + b

    def execute(self, *args, **kwargs):
        a, b = args[0]
        res = f'{a} + {b} = {self.evaluate(a,b)}'
        logging.info(f'Performed addition operation --> {res}'); print(res)
