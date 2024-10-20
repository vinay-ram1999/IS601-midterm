import logging
from calculator.commands import Operation

class MultiplyOperation(Operation):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a * b

    def execute(self, *args, **kwargs):
        a, b = args[0]
        res = f'{a} x {b} = {self.evaluate(a,b)}'
        logging.info(f'Performed multiplication operation --> {res}'); print(res)
