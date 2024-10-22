import logging

from calculator.commands import BuiltInOperation

class HistoryOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Displays the history of arthematic operations performed starting from most recent.',
                  'arguments': 'None',
                  'usage': f'{__name__.split(".")[-1]}'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        out = self.opr_handler.tabulate_history()
        logging.info("Displayed the history of operations")
        print(out)
