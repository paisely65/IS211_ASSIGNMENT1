#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides documentation for a single file."""

class Book:
    def __init__(self):
        self.mybook1 = "Of Mice and Men by John Steinback"
        self.mybook2 = "To Kill a Mockingbird by Harper Lee"
    author = ""
    title = ""
    
def display():
    print '{0} written by {1}'.format("Of Mice and Men", "John Steinback")
    print '{0} written by {1}'.format("To Kill a Mockingbird", "Harper Lee")
    
book1 = Book()
print book1.mybook1
book2 = Book()
print book2.mybook2


