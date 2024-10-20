from tabulate import tabulate

import logging

from calculator.commands import Operation, BuiltInOperation, OperationHandler

class MenuOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Displays all available Arthematic and BuiltIn operations.',
                  'arguments': 'None',
                  'usage': f'{__name__.split(".")[-1]}'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        assert isinstance(self.opr_handler, OperationHandler), "MenuOperation only takes OperationHandler instance as input."
        arth_operations = [x for x in self.opr_handler.operations.keys() if isinstance(self.opr_handler.operations[x], Operation)]
        builtin_operations = [x for x in self.opr_handler.operations.keys() if isinstance(self.opr_handler.operations[x], BuiltInOperation)]
        dict_tmp = {'Name':[],'Type':[],'Arguments':[],'Usage':[],'Description':[]}
        for operation in arth_operations + builtin_operations:
            obj = self.opr_handler.operations[operation]
            dict_tmp['Name'].append(operation.capitalize())
            dict_tmp['Type'].append('builtin' if operation in builtin_operations else 'arthematic')
            dict_tmp['Arguments'].append(obj.arguments)
            dict_tmp['Usage'].append(obj.usage)
            dict_tmp['Description'].append(obj.description)
        out = tabulate(dict_tmp, tablefmt="simple_grid", headers="keys", maxcolwidths=[None, None, None, None, None, 25], showindex=[i+1 for i in range(len(self.opr_handler.operations))])
        out = f'\nMenu:\n{out}'
        logging.info(f"Displayed Menu with available options: {builtin_operations + arth_operations} along with their properties to the user."); print(out)
