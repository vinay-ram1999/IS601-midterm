import logging
from calculator.commands import Operation

class AddOperation(Operation):
    def __init__(self) -> None:
        kwargs = {'description':'Add two numbers.',
                  'arguments': '2',
                  'usage': f'{__name__.split(".")[-1]} 2 3'}
        super().__init__(**kwargs)

    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a + b

    def execute(self, *args, **kwargs) -> float:
        a, b = args[0]
        res = self.evaluate(float(a),float(b))
        out = f'{a} + {b} = {res}'
        print(out)
        logging.info(f'Performed addition operation --> {out}')
        return res
