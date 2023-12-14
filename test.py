#!/usr/bin/python
# -*- coding: utf-8 -*-

a = 10

def f():
    global a
    a = 5


f()
print(a)
