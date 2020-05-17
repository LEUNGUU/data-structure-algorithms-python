#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PositionalList import PositionalList


class FavoritesList:
    """List of elements ordered from most frequently accesse to least"""

    # -------------------------- nested _item class ---------------------
    class _Item:
        __slots__ = "_value", "_count"

        def __init__(self, e):
            self._value = e
            self._count = 0

    # -------------------------- nonpublic utilities ---------------------
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count"""

        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (
                    walk != self._data.first()
                    and cnt > self._data.before(walk).element()._count
                ):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    # ---------------------------  public methods --------------------------
    def __init__(self):
        """Create an empty list of favorites"""
        self._data = PositionalList()

    def __len__(self):
        """Return number of entries on favorites list"""
        return len(self._data)

    def is_empty(self):
        """Return True if list is empty"""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count"""
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """Remove element e from the list of favorites"""
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """Generate sequence of top k elements in terms of access count"""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic"""

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list"""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    # we override top because list is no longer sorted
    def top(self, k):
        """Generate sequnce of top k elements in terms of access count"""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

        # we begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found the element with highest count
            yield highPos.element()._value
            temp.delete(highPos)


if __name__ == "__main__":
    import random

    fl = FavoritesList()
    for i in range(10):
        option = random.choice(["me", "her", "him"])
        fl.access(option)
    for item in fl.top(2):
        print(item)
