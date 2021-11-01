# -*- coding: utf-8 -*-
'''
@File    :   log_main.py
@Time    :   2021/01/26 22:17:27
'''

import logging
import logging.handlers 
import os 
import os.path
import time

class MyPath:
    log_dir_name = 'Log'
    file_name = 'my.log'
    def __init__(self, log_dir_name=None, file_name=None) -> None:
        if  log_dir_name:
            self.log_dir_name = log_dir_name
        if  file_name:
            self.file_name = file_name
        self.dir_name = os.path.join(os.getcwd(), self.log_dir_name)
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
        self.file_path = os.path.join(self.dir_name, self.file_name)
        pass

    def get(self):
        return self.file_path

class BaseLogger(object):
    file_path = MyPath().get() 
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class MyLogger(BaseLogger):
    # file_path = MyPath().get()
    file_handler = logging.handlers.RotatingFileHandler(
        file_path, mode='a', maxBytes=500, backupCount=3
    )
    def __init__(self, log_name:str) -> None:
        logging.basicConfig()
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.DEBUG)
        self.fmt = logging.Formatter('')
        self.file_handler.setFormatter(self.fmt)
        self.logger.addHandler(self.file_handler)
    
    def get_logger(self):
        return self.logger


class TimeLogger:
    file_path = MyPath().get()
    time_handler = logging.handlers.TimedRotatingFileHandler(
        filename=file_path, when="D", interval=1, backupCount=3
    )
    def __init__(self, logger_name) -> None:
        logging.basicConfig()
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        self.time_handler.setFormatter(fmt)
        self.logger.addHandler(self.time_handler)
        pass

    def get_logger(self):
        return self.logger
    


class FileLogger:
    file_path = MyPath().get()
    def __init__(self, logger_name, level=logging.DEBUG) -> None:
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)
        fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        self.file_handler = logging.FileHandler(filename=self.file_path, mode='a')
        self.file_handler.setFormatter(fmt)
        self.logger.addHandler(self.file_handler) 

    
    def get_logger(self):
        return self.logger






if __name__ == '__main__':
    # path_obj = MyPath('Log_name', 'mylog.log')
    logger = MyLogger('A').get_logger() 
    logger1 = MyLogger('B').get_logger() 
    i=1
    while i<40:
        logger.info('nihao....')
        logger1.error('nihao....')
        i+=1
        time.sleep(0.1)
    pass
