import pandas as pd

import logging
from calculator.commands import Operation, BuiltInOperation, OperationHandler

class MenuOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Displays the history of operations performed.',
                  'arguments': 'None',
                  'usage': f'{__name__.split(".")[-1]}'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        assert isinstance(self.opr_handler, OperationHandler), "MenuOperation only takes OperationHandler instance as input."
        logging.info("Extracting the history of operations executed!")
        print(pd.DataFrame(self.opr_handler.history))
