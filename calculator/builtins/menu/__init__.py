from tabulate import tabulate

import logging

from calculator.commands import Operation, BuiltInOperation

class MenuOperation(BuiltInOperation):
    def __init__(self) -> None:
        kwargs = {'description':'Displays all available arithmetic and builtIn operations.',
                  'arguments': 'None',
                  'usage': f'{__name__.split(".")[-1]}'}
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        menu_dict = {'Name':[],'Type':[],'n_Args':[],'Usage':[],'Description':[]}
        for operation in self.opr_handler.operations.keys():
            menu_dict['Name'].append(operation)
            menu_dict['Type'].append('arithmetic' if isinstance(self.opr_handler.operations[operation],Operation) else 'builtin')
            menu_dict['n_Args'].append(self.opr_handler.operations[operation].arguments)
            menu_dict['Usage'].append(self.opr_handler.operations[operation].usage)
            menu_dict['Description'].append(self.opr_handler.operations[operation].description)
        out = tabulate(menu_dict, tablefmt="pretty", stralign='left', headers="keys", maxcolwidths=[2, None, None, 6, None, 50], 
                       showindex=[i+1 for i in range(len(self.opr_handler.operations))])
        out = f'Menu:\n{out}'
        logging.info(f"Displayed Menu with options: {list(menu_dict.keys())} along with their properties.")
        print(out)
