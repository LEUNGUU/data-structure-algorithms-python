#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList


class Empty(Exception):
    pass


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list"""

    def __init__(self):
        """Create a new empty priority queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def add(self, key, value):
        """Add an item into priority queue"""
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is not None:
            self._data.add_after(walk, newest)
        else:
            self._data.add_first(newest)

    def min(self):
        """Return(but do not remove) (k, v) tuple with minimum key"""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key"""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)


if __name__ == "__main__":
    spq = SortedPriorityQueue()
    spq.add(1, 2)
    spq.add(2, 3)
    spq.add(3, 4)
    for _ in range(4):
        print(spq.remove_min())
