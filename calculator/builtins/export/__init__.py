import logging
import os

from calculator.commands import BuiltInOperation

class ExportOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':"Exports the history into a .csv file. 'history.csv' is used as default for file_name if not provided.",
                  'arguments': '1',
                  'usage': f'{__name__.split(".")[-1]} file_name.csv'}
        super().__init__(**kwargs)

    def export_csv(self, fname):
        fpath = os.path.join(self.env_vars['DATA_DIR_ABS'], fname)
        self.opr_handler.history_df().to_csv(fpath, index=True)
        return fpath

    def execute(self, *args, **kwargs):
        try:
            fname: str = args[0][0] if args[0] != [] else 'history.csv'
            assert fname.endswith('.csv'), "The filename does not end with '.csv'"
            fpath = self.export_csv(fname)
            msg = f"Exported operations history to: {fpath}"
            logging.info(msg)
            print(msg)
        except AssertionError as e:
            msg = "AssertionError: The file_name argument should end with '.csv'"
            logging.error(e.add_note(msg), exc_info=True)
            print(msg)
