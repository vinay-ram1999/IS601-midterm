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
        menu_dict = {'Name':[],'Type':[],'Arguments':[],'Usage':[],'Description':[]}
        for operation in self.opr_handler.operations.keys():
            menu_dict['Name'].append(operation.capitalize())
            menu_dict['Type'].append('arthematic' if isinstance(self.opr_handler.operations[operation],Operation) else 'builtin')
            menu_dict['Arguments'].append(self.opr_handler.operations[operation].arguments)
            menu_dict['Usage'].append(self.opr_handler.operations[operation].usage)
            menu_dict['Description'].append(self.opr_handler.operations[operation].description)
        out = tabulate(menu_dict, tablefmt="simple_grid", headers="keys", maxcolwidths=[None, None, None, None, None, 25], showindex=[i+1 for i in range(len(self.opr_handler.operations))])
        out = f'\nMenu:\n{out}'
        print(out); logging.info(f"Displayed Menu with options: {list(menu_dict.keys())} along with their properties to the user.")
