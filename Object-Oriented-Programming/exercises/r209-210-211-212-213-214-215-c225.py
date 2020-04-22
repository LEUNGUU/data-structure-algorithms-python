#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Vector:
    """Represent a vector in multidimensional space"""

    def __init__(self, initial):
        """Create d-dimensional vector of zeros"""
        if isinstance(initial, int):
            self._coords = [0] * initial
        else:
            self._coords = initial

    def __len__(self):
        """Return the dimension of vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value"""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector zero
        for j in range(len(self)):
            result[j] = self[j] + other[j]  # relies on __setitem__ and __getitem__
        return result

    def __sub__(self, other):
        """Return difference between two vectors"""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    # def __mul__(self, number):
    #     """Return a new vector with coordinates that are number times"""
    #     result = Vector(len(self))
    #     for j in range(len(self)):
    #         result[j] = self[j] * number
    #     return result

    # def __rmul__(self, number):
    #     """Support number * vector"""
    #     result = Vector(len(self))
    #     for j in range(len(self)):
    #         result[j] = self[j] * number
    #     return result

    def __mul__(self, operand):
        """Return dot product of two vectors or a new vector with coordinates that are number times"""
        if isinstance(operand, Vector):
            if len(self) != len(operand):
                raise ValueError("dimensions must agree")
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * operand[j]
            return result
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * operand
            return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other"""
        return self._coords == other._coords  # relies on list ==

    def __neg__(self):
        """Return a new Vector whose coordinates are all negated value"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __ne__(self, other):
        """Return true if vector differs from other"""
        return not self == other  # relies on __eq__

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords[0:]) + ">"


if __name__ == "__main__":
    print(Vector(5))
    print(Vector(5)[2])
    print(Vector(5) + Vector(5))
    u = Vector([1, 2])
    v = Vector(2)
    v[0] = 1
    print(u - v)
    print(-u)
    print("u: ", u)
    print("v: ", v)
    print("u * v: ", u * v)
    print("u * 3: ", u*3)
    for i in Vector(5):
        print(i)
