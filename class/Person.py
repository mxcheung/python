# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:42:26 2021

@author: cheungm
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
