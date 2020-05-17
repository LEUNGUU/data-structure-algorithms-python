#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Tree:
    """Abstract base class representing a tree structure"""

    # ----------------------------- nested Position class ------------------------
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other does notrepresent the same location"""
            return not (self == other)

    # ---------------- abstract methods that concrete subclass must support ------------
    def root(self):
        """Return Position representing the tree's root(or None if empty)"""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent(or None if p is root)"""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children that Position p has"""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Position representing p's children"""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError("must be implemented by subclass")

    # ----------------- concrete methods implemented in this class -------------------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children"""
        return self.num_children(p)

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0


if __name__ == "__main__":
    pass