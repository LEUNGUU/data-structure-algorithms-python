#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Range:
    """A class that mimic's the built-in range class"""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.
        Semantics is similar to built-in range class
        """
        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:  # special case range(n), should be treated as range(0,n)
            start, stop = 0, start

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step(but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range"""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k(using standard interpretation if negative)."""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step

    def __contains__(self, value):
        """Return True if the given value is in the sequence"""
        index = (value - self._start) / self._step   #like hash value
        if not 0 <= index < self._length:
            return False
        return True


if __name__ == "__main__":
    for item in Range(0, 5, 8):
        print(item)
    for item in Range(-9, -3, 2.5):
        print(item)
    if 99999 in Range(10000000):
        print("99999 is in 10000000")
