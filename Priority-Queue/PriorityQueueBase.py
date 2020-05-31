#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PriorityQueueBase:
    """An abstract base class for a priority queue"""

    class _Item:
        """Lightweight composite to store priority queue items"""

        __slots__ = "_key", "_value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        """Return True if the priority queue is empty"""
        return len(self) == 0


if __name__ == "__main__":
    pass
