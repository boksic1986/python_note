# -*-coding:utf-8-*-
# /usr/bin/env python
# Author: jiucheng
# Date: 8/5/17

class Foo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def foo(self, y):
        self.x = y

    @classmethod
    def cls_foo(cls, y):
        return cls(y, y)

    @staticmethod
    def sts_foo(y):
        return Foo(y, y)
