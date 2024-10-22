from tabulate import tabulate

import logging

from calculator.commands import BuiltInOperation

class HistoryOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Displays the history of arthematic operations performed starting from most recent.',
                  'arguments': 'None',
                  'usage': f'{__name__.split(".")[-1]}'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        out = tabulate(self.opr_handler.history, tablefmt="pretty", headers="keys", numalign="right", 
                       floatfmt=".5f", showindex=[i[0] for i in enumerate(list(self.opr_handler.history.values())[0])])
        logging.info("Displayed the history of operations")
        print(out)
