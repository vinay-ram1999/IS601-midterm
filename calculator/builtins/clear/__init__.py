from tabulate import tabulate

import logging

from calculator.commands import BuiltInOperation

class ClearOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Clears all operations history in current session',
                  'arguments': 'None',
                  'usage': f'{__name__.split(".")[-1]}'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        self.opr_handler.clear_history()
        out = tabulate(self.opr_handler.history, tablefmt="pretty", headers="keys", numalign="right", 
                       floatfmt=".5f", showindex=[i[0] for i in enumerate(list(self.opr_handler.history.values())[0])])
        msg = "Cleared current session history."
        logging.info(msg)
        print(f"{out}\n{msg}")
