# -*- coding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/01/26 22:22:19
'''


import a
import b 
import logging
from log_main import FileLogger
logger = FileLogger(__name__).get_logger()

logger.info('main.py.....')
a.out_a()
b.out_b()

