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
        out = self.opr_handler.tabulate_history()
        msg = "Cleared current session history."
        logging.info(msg)
        print(f"{out}\n{msg}")
