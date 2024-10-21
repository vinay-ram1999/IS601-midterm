from dotenv import load_dotenv

import os
import sys
import pkgutil
import importlib
import logging
import logging.config

from calculator.commands import Operation, BuiltInOperation, OperationHandler

class Calculator:
    def __init__(self) -> None:
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.settings.setdefault('DATA_DIR', 'data')
        self.settings['DATA_DIR_ABS'] = os.path.abspath(self.get_data_dir_variable())
        os.makedirs(self.settings['DATA_DIR_ABS'], exist_ok=True)
        logging.info(f'Directory for data is setup to: {self.settings["DATA_DIR_ABS"]}')
        self.opr_handler = OperationHandler()
    
    @staticmethod
    def configure_logging(logging_conf_path: str='logging.conf'):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False) if os.path.exists(logging_conf_path) else logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(f"Logging configured using {'fileConfig' if os.path.exists(logging_conf_path) else 'basicConfig'} method.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)
    
    def get_data_dir_variable(self, env_var: str = 'DATA_DIR'):
        return self.settings.get(env_var, None)
    
    def load_builtins_plugins(self):
        packages = {'Plugins': 'calculator.plugins', 'Builtins': 'calculator.builtins'} # The order in this dict decides the order in menu
        for package_key, package in packages.items():
            package_path = package.replace('.', os.path.sep)
            if not os.path.exists(package_path):
                logging.warning(f"{package_key} directory '{package_path}' not found.")
                return
            for _, module_name, is_pkg in pkgutil.iter_modules([package_path]):
                if is_pkg:
                    try:
                        package_module = importlib.import_module(f'{package}.{module_name}')
                        self.register_builtin_plugin_commands(package_module, module_name)
                    except ImportError as e:
                        logging.error(f"Error importing {package_key} {module_name}: {e}")
                        print(f"Error importing {package_key} {module_name}: {e}")

    def register_builtin_plugin_commands(self, package_module, module_name):
        for item_name in dir(package_module):
            item = getattr(package_module, item_name)
            if isinstance(item, type) and issubclass(item, Operation) and item is not Operation:
                self.opr_handler.add_operation(module_name, item())
                logging.info(f"Command '{module_name}' from '{module_name}' registered.")
            elif isinstance(item, type) and issubclass(item, BuiltInOperation) and item is not BuiltInOperation:
                item_instance = item()
                item_instance.opr_handler = self.opr_handler
                item_instance.env_vars = self.settings
                self.opr_handler.add_operation(module_name, item_instance)
    
    def run(self):
        self.load_builtins_plugins()
        logging.info("Application started.")
        print("\nType 'menu' to see available operations or 'exit' to end the application!\n")
        try:
            while True:  #REPL Read, Evaluate, Print, Loop
                inp_text = input(">>> ").strip().split(sep=" ")
                self.opr_handler.run_operation(inp_text[0], inp_text[1:])
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            logging.info("Application shutdown.")
