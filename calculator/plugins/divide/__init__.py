import logging
from calculator.commands import Operation

class DivisionOperation(Operation):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError('Cannot divide by 0!')
        return a / b

    def execute(self, *args, **kwargs):
        a, b = args[0]
        res = f'{a} / {b} = {self.evaluate(a,b)}'
        logging.info(f'Performed division operation --> {res}'); print(res)
