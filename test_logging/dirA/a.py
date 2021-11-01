# -*- coding: utf-8 -*-
'''
@File    :   a.py
@Time    :   2021/01/26 22:24:44
'''

from log_main import FileLogger
logger = FileLogger(__name__).get_logger()



def out_a():
    logger.info("hello, is a.py| out_a() .....")


if __name__ == '__main__':
    out_a()