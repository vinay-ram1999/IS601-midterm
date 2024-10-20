import logging
from calculator.commands import Operation

class SubtractOperation(Operation):
    def __init__(self) -> None:
        kwargs = {'description':'Subtract two numbers.',
                  'arguments': '2',
                  'usage': f'{__name__.split(".")[-1]} 2 3'}
        super().__init__(**kwargs)

    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a - b

    def execute(self, *args, **kwargs):
        a, b = args[0]
        res = self.evaluate(a,b)
        out = f'{a} - {b} = {res}'
        logging.info(f'Performed substraction operation --> {out}'); print(out)
        return res
