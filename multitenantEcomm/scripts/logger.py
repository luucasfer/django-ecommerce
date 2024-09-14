import logging

def get_logger(log_file):
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('./logs/' + log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger