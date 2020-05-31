#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from HeapPriorityQueue import HeapPriorityQueue


class AdaptbleHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap"""

    # ----------------- nested Locator class ---------------
    class Locator(HeapPriorityQueue._Item):
        """Token for lcoating an entry of the priority queue"""

        __slots__ = "_index"

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    # ------------------ nonpublic behaviors ---------------
    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = j
        self._data[j]._index = i

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        """Add a key-value pair"""
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry identified by Locator loc"""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """Remove and return the (k,v) pair identified by Locator loc"""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)


if __name__ == "__main__":
    pass
