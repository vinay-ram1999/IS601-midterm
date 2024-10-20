import logging
from calculator.commands import Operation

class SubtractOperation(Operation):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a - b

    def execute(self, *args, **kwargs):
        a, b = args[0]
        res = self.evaluate(a,b)
        out = f'{a} - {b} = {res}'
        logging.info(f'Performed substraction operation --> {out}'); print(out)
        return res
