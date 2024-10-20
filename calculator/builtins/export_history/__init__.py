import pandas as pd

import logging
import os

from calculator.commands import BuiltInOperation, OperationHandler

class ExportOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Export the history into a .csv file',
                  'arguments': '1',
                  'usage': f'{__name__.split(".")[-1]} file_name'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        assert isinstance(self.opr_handler, OperationHandler), "ExportOperation only takes OperationHandler instance as input."
        data_dir = self.env_vars['DATA_DIR']; fname = f'{args[0]}.csv'; fpath = os.path.join()
        print(f"Exported the history to {fname}!"); logging.info(f"Exported the history to {fname}")