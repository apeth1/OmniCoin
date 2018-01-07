# ************************
# log.py
# Author: Andrew Peth
# Date: 01/06/2018
# ************************

import logging
import logging.handlers


class LogManager:
    def __init__(self, name: str, file_name: str):
        self.name = name
        self.file_name = file_name

    def create_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        rh = logging.handlers.RotatingFileHandler(self.file_name, mode="a", maxBytes=10000000)
        rh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        rh.setFormatter(formatter)
        logger.addHandler(rh)
        return logger
