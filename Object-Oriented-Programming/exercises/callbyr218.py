#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Progression:
    """Iterator producing a generic progression.
    Default iterator produces the whole numbers 0,1,2,...
    """

    def __init__(self, start=0):
        """Initialize current to the first value."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the end
        of a finite progression
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self

    def print_progression(self, n):
        """Print nexxt n values of the progression"""
        print(" ".join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.

        increment the fixed constant to add to each term(default 1)
        start     the first term of the progression(default 0)
        """

        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment"""
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing a geometric progression"""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression.

        base    the fixed constant multiplied to each term (default 2)
        start   the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying it by the base value"""
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonaci progression"""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.

        first    the first term of the progression (default 0)
        second   the second term of the progression (default 1)
        """
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        """Update current value by taking sum of previous two"""
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == "__main__":
    # default progression
    print("default progression")
    Progression(0).print_progression(10)
    # arithmetic progression
    print("arithmetic progression")
    ArithmeticProgression(2, 0).print_progression(10)
    # geometric progression
    print("geometric progression")
    GeometricProgression(2, 3).print_progression(10)
    # fibonacci progression
    print("fibonacci progression")
    FibonacciProgression(4, 6).print_progression(10)
