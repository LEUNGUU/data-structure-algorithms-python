#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PositionalList import PositionalList
from PriorityQueueBase import PriorityQueueBase


class Empty(Exception):
    pass


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented implemented with an unsorted list"""

    def _find_min(self):
        """Return Position of item with minimum key"""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create an empty priority queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in priority queue"""
        return len(self._data)

    def add(self, key, value):
        """Add an item into priority queue"""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return(but do not remove) (k, v) tuple with minimum key"""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


if __name__ == "__main__":
    upq = UnsortedPriorityQueue()
    upq.add(1, 2)
    upq.add(2, 3)
    upq.add(3, 4)
    print(upq.min())
    for _ in range(4):
        print(upq.remove_min())
