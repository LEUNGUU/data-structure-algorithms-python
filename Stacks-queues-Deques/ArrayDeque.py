#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Empty(Exception):
    """Class for self-defined exception"""

    pass


class ArrayDeque:
    """FIFO queue implementation using a Python list as underlying storage"""

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the Deque"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the elements at the front of the queue.

        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the element at the end of the queue.

        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def delete_first(self):
        """Remove and return the first element of the queue(i.e. FIFO)

        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # avoid wasting space
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_last(self):
        """Remove and return the last element of the deque.

        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        # avoid wasting space
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def add_last(self, e):
        """Add an element to the back in Deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        """Add an element to the first in Deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0


if __name__ == "__main__":
    AD = ArrayDeque()
    AD.add_first(1)
    AD.add_last(2)
    print(AD.first())
    print(AD.last())
    print(AD.delete_last())
    print(AD.delete_first())
