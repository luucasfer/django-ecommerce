import logging
import logging.handlers


def get_logger(log_file):
    logger = logging.getLogger(__name__)
    handler = logging.handlers.RotatingFileHandler('./logs/' + log_file, maxBytes=1024*1024*5, backupCount=0)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter) 
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger