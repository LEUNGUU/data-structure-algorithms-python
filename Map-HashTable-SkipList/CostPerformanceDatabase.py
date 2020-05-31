#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CostPerformanceDatabase:
    """Maintain a database of maximal(cost, performance) pairs"""

    def __init__(self):
        """Create an empty database"""
        self._M = SortedTableMap()

    def best(self, c):
        """Retrun (cost, performance) pair with largest cose not exceeding c.

        Retrun None if there is no such pair
        """
        return self._M.find_le(c)

    def add(self, c, p):
        """Add new entry with cose c and performance p"""
        other = self._M.find_le(c)
        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        other = self._M.find_gt(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)


if __name__ == "__main__":
    pass
