import os
import logging, logging.config

def configure_logging(log_dir: str='logs',logging_conf_path: str='logging.conf'):
    os.makedirs(log_dir, exist_ok=True)
    logging.config.fileConfig(logging_conf_path) if os.path.exists(logging_conf_path) else logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"Logging configured using {'fileConfig' if os.path.exists(logging_conf_path) else 'basicConfig'} method.")

# we can import these loggers in any module to log using these specific loggers
#info_logger = logging.getLogger('info')
#error_logger = logging.getLogger('error')
