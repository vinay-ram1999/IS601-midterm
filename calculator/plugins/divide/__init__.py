import logging
from calculator.commands import Operation

class DivisionOperation(Operation):
    def __init__(self) -> None:
        kwargs = {'description':'Divide two numbers.',
                  'arguments': '2',
                  'usage': f'{__name__.split(".")[-1]} 2 3'}
        super().__init__(**kwargs)

    @staticmethod
    def evaluate(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError('Cannot divide by 0!')
        return a / b

    def execute(self, *args, **kwargs):
        a, b = args[0]
        res = self.evaluate(a,b)
        out = f'{a} / {b} = {res}'
        logging.info(f'Performed division operation --> {out}'); print(out)
        return res
