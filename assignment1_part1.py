#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Starter data module"""

def listDivide(numbers, divide=2):
    evens =[ ]
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

class ListDivideException(Exception):
    pass

def testListDivide(numbers, divide=2):
    def listDivide(numbers, divide=2):
        evens =[ ]
        for number in numbers:
            if number % 2 == 0:
                evens.append(number)
        print len(evens)
        try:
            listDivide([1,2,3,4,5])
            listDivide([30, 54, 63,98, 100], divide=10)
            listDivide([])
            listDivide([1,2,3,4,5]
            listDivide([2,4,6,8,10])
        except (ListDivideException):
            pass
