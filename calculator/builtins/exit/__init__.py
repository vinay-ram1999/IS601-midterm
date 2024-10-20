import sys
from calculator.commands import BuiltInOperation

class ExitOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Exits from the application.',
                  'arguments': 'None',
                  'usage': f'{__name__.split(".")[-1]}'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        sys.exit("Exiting...")
