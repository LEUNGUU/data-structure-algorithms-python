#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Empty(Exception):
    pass


class SinglyLinkedList:
    """An class representing a singly Linked list"""

    class _Node:
        """A lightweight class representing a node in LinkedList"""

        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty SinglyLinkedList"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements of the SinglyLinkedList"""
        return self._size

    def is_empty(self):
        """Return True if SinglyLinkedList is empty"""
        return self._size == 0

    # -------------------- accessors ------------------------------
    def head(self):
        """Return(but do not remove) at the front of SinglyLinkedList"""
        if self.is_empty():
            raise Empty("SinglyLinkedList is empty")
        return self._head

    def tail(self):
        """Return(but do not remove) at the end of SinglyLinkedList"""
        if self.is_empty():
            raise Empty("SinglyLinkedList is empty")
        return self._tail

    # ---------------------- mutators -----------------------------
    def add_first(self, e):
        """Insert element at the front of SinglyLinkedList"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._tail = newest
        else:
            newest._next = self._head
        self._head = newest
        self._size += 1

    def add_last(self, e):
        """Insert element at the end of SinglyLinkedList"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def remove_first(self):
        """Remove element at the front of SinglyLinkedList"""
        if self.is_empty():
            raise Empty("SinglyLinkedList is empty")
        answer = self._head
        self._head = self._head._next
        self._size -= 1

    def index(self, p):
        """Return the position of the specific element"""
        if self.is_empty():
            raise Empty("SinglyLinkedList is empty")
        if not (1 <= abs(p) <= self._size):
            raise IndexError("p is not a valid position")
        # support negtive index
        if p < 0:
            p = self._size + p + 1
        cursor = 1
        walk = self._head
        while walk is not None:
            if cursor == p:
                return walk._element
            walk = walk._next
            cursor += 1


if __name__ == "__main__":
    pass
