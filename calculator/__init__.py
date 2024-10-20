from dotenv import load_dotenv

import os
import sys
import pkgutil
import importlib
import logging
import logging.config

from calculator.commands import Operation, OperationHandler

class Calculator:
    def __init__(self) -> None:
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.opr_handler = OperationHandler()
    
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False) if os.path.exists(logging_conf_path) else logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)
    
    def load_plugins(self):
        plugins_package = 'calculator.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}"); print(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Operation) and item is not Operation:
                # Command names are now explicitly set to the plugin's folder name
                self.opr_handler.add_operation(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
    
    def run(self):
        self.load_plugins()
        logging.info("Application started.")
        print(f"\nAvailable operations are: {', '.join(list(self.opr_handler.operations.keys()))}")
        print(f"Usage: Operation num1 num2 (Ex: add 3 4) or type 'exit' to exit.\n")
        try:
            while True:  #REPL Read, Evaluate, Print, Loop
                inp_text = input(">>> ").strip().split(sep=" ")
                self.opr_handler.run_operation(inp_text[0], inp_text[1:])
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            logging.info("Application shutdown.")
