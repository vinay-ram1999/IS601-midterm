from tabulate import tabulate

import logging

from calculator.commands import Operation, BuiltInOperation, OperationHandler

class HistoryOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Displays the history of arthematic operations performed starting from most recent.',
                  'arguments': 'None',
                  'usage': f'{__name__.split(".")[-1]}'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        assert isinstance(self.opr_handler, OperationHandler), "HistoryOperation only takes OperationHandler instance as input."
        out = tabulate(self.opr_handler.history, tablefmt="pretty", headers="keys", numalign="right", floatfmt=".5f", showindex=[i+1 for i in range(len(self.opr_handler.history['Operation']))])
        print(out); logging.info("Extracted the history of operations executed!")
