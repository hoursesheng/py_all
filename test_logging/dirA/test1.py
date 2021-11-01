# -*- coding: utf-8 -*-
'''
@File    :   test1.py
@Time    :   2021/01/29 23:01:06
'''

class A:
    a = 1


class B(A):
    a = 1
    b = a
    pass


obj = B()
print(obj.b)