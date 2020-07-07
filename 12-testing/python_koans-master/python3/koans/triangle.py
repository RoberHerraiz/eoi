#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    equal_sides = 0
    if a is b:
        equal_sides += 1
    if a is c:
        equal_sides += 1
    if b is c:
        equal_sides += 1

    result = ['scalene', 'isosceles', 'equilateral']

    return result[equal_sides]
    
    

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
