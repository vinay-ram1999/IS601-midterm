import pandas as pd

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
        art_numbered = [f'{i+1}. {x}' for i, x in enumerate(arth_operations)]
        art_numbered.append('Usage: Operation num1 num2 (Ex: add 3 4)')
        art_numbered = '\n'.join(art_numbered)
        out = f"\nMenu:\nArithmetic Operations:\n{art_numbered}\n"
        dict_tmp = {'Name':[],'Description':[],'Arguments':[],'Usage':[]}
        for builtin in builtin_operations:
            obj = self.opr_handler.operations[builtin]
            dict_tmp['Name'].append(builtin.capitalize())
            dict_tmp['Description'].append(obj.description)
            dict_tmp['Arguments'].append(obj.arguments)
            dict_tmp['Usage'].append(obj.usage)
        logging.info(f"Displayed Menu with available options: {arth_operations + builtin_operations}"); print(out)
        print(pd.DataFrame(dict_tmp))
