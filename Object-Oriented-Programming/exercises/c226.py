#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SequenceIterator:
    """An iterator for any of Python's sequence types"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self


class ReversedSequenceIterator(SequenceIterator):
    """An REVERSED iterator for any of Python's sequence types"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        super().__init__(sequence)
        self._k = 0

    def __next__(self):
        self._k -= 1
        if self._k >= -len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()


if __name__ == "__main__":
    for item in SequenceIterator([1, 2, 3, 4]):
        print(item)
    for item in ReversedSequenceIterator([1, 2, 3, 4]):
        print(item)
