import sys
from calculator.commands import Operation

class ExitOperation(Operation):
    def execute(self, *args, **kwargs):
        sys.exit("Exiting...")
