#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SplayTreeMap(TreeMap):
    """Sorted map implementation using a splay tree"""

    # -------------- splay operation -------------------
    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                self._rotate(p)
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                self._rotate(parent)
                self._rotate(p)
            else:
                self._rotate(p)
                self._rotate(p)

    # ------------------ override balancing hooks -------------
    def _rebalance_insert(self, p):
        self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)

    def _rebalance_delete(self, p):
        self._splay(p)


if __name__ == "__main__":
    pass
