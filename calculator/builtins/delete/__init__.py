import logging

from calculator.commands import BuiltInOperation

class DeleteOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Deletes a single/multiple operation(s) from current session history',
                  'arguments': 'n',
                  'usage': f'{__name__.split(".")[-1]} 8 3 ... n'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        try:
            idx: list = [int(x) for x in args[0]] if args[0] != [] else None
            assert isinstance(idx,list), "Index arguments for deleting are not provided"
            self.opr_handler.delete_history(idx)
            out = self.opr_handler.tabulate_history()
            msg = f"Deleted {len(idx)} elements from history."
            logging.info(msg)
            print(f"{out}\n{msg}")
        except AssertionError as e:
            msg = f'AssertionError: {e.args[-1]}'
            out = self.opr_handler.tabulate_history()
            logging.error(e.add_note(msg), exc_info=True)
            print(f'{out}\n{msg}')
