import os
import logging, logging.config

def configure_logging(log_path: str = 'logs', logging_conf_path: str = 'logging.conf'):
    os.makedirs(log_path, exist_ok=True)
    logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False) if os.path.exists(logging_conf_path) else logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"Logging configured using {'fileConfig' if os.path.exists(logging_conf_path) else 'basicConfig'} method.")

#logging.getLogger('root').addFilter(logging.Filter('info'))
#info_logger = logging.getLogger('info').addFilter(logging.Filter('error'))
#error_logger = logging.getLogger('error')

