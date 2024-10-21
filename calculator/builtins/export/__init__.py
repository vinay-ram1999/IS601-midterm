import logging
import os

from calculator.commands import BuiltInOperation, OperationHandler

class ExportOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':"Exports the history into a .csv file. 'history' is used as default for file_name if not provided.",
                  'arguments': '1',
                  'usage': f'{__name__.split(".")[-1]} file_name'}
        super().__init__(**kwargs)

    def export_csv(self, fname):
        data_dir = self.env_vars['DATA_DIR_ABS']
        fname = f'{fname}.csv'
        fpath = os.path.join(data_dir,fname)
        self.opr_handler.history_df().to_csv(fpath, index=True)
        return fpath

    def execute(self, *args, **kwargs):
        assert isinstance(self.opr_handler, OperationHandler), "ExportOperation only takes OperationHandler instance as input."
        fname = args[0][0] if args[0] != [] else 'history'
        fpath = self.export_csv(fname)
        msg = f"Exported claculation history to: {fpath}"
        print(msg)
        logging.info(msg)
