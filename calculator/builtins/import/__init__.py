import pandas as pd

import logging
import os

from calculator.commands import BuiltInOperation

class ImportOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':"Imports operations from given .csv file and adds it to current session history.",
                  'arguments': '1',
                  'usage': f'{__name__.split(".")[-1]} your/file/path.csv'}
        super().__init__(**kwargs)

    def import_csv(self, fname):
        imported_history = pd.read_csv(fname, index_col=0).to_dict(orient='list')
        keys = list(self.opr_handler.history.keys())
        assert len(list(imported_history.keys())) == len(keys), f"The number of columns do not match with number of columns in history"
        structured_imported_history = dict(zip(keys,list(imported_history.values())))
        return structured_imported_history

    def execute(self, *args, **kwargs):
        try:
            fname: str = os.path.abspath(args[0][0])
            assert fname.endswith('.csv'), f"{os.path.basename(fname)} does not end with '.csv'"
            assert os.path.exists(fname), f"{fname} does not exists"
            imported_history = self.import_csv(fname)
            msg = f"Imported operations history from: {fname}"
            logging.info(msg)
            for key in self.opr_handler.history.keys():
                self.opr_handler.history[key] = imported_history[key] + self.opr_handler.history[key]
            out = self.opr_handler.tabulate_history()
            logging.info("Displayed the imported history of operations and appended them to the existing history")
            print(f'{out}\nThese operations are imported and added to history and can be viewed using the appropriate operation.')
        except (IndexError, AssertionError) as e:
            msg = 'IndexError: Input file name is not provided' if isinstance(e, IndexError) else f"AssertionError: {e.args[-1]}"
            logging.error(e.add_note(msg), exc_info=True)
            print(msg)
