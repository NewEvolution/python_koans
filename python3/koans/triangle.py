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
    'Given 3 side lengths, returns the type of triangle, \
    raises TriangleError if the inputs do not form a triangle'
    if (a and b and c > 0) and triTest(a, b, c):
        if a == b == c:
            return 'equilateral'
        elif a == b or b == c or c == a:
            return 'isosceles'
        else:
            return 'scalene'
    else:
        raise TriangleError

def triTest(*args):
    'Checks that the sides provided create a closed figure \
    with a contained area'
    sides = sorted(args)
    if sides[0] + sides[1] <= sides[2]:
        return False
    return True

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
