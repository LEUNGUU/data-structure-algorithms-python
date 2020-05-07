#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import ctypes, sys


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        """Create an empty array"""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
        print("self._capacity: ", self._capacity)

    def remove(self, value):
        """Remove first occurrence of value(or raise ValueError)"""
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError("Value not found")

    def insert(self, k, value):
        """Insert value at index k, shifting subsequence value rightwards"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def pop(self):
        element = self._A.pop()
        if self._n < self._capacity // 4:
            self._resize(self._capacity // 2)
        return element

    def _make_array(self, c):
        """Return new array of capacity c"""
        return (c * ctypes.py_object)()


if __name__ == "__main__":
    data = DynamicArray()
    for i in range(59):
        a = len(data)
        b = sys.getsizeof(data)
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
        data.append(None)
