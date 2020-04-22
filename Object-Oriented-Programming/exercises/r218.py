#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from callbyr218 import FibonacciProgression

if __name__ == "__main__":
    fb = FibonacciProgression(2, 2)
    for i in range(0, 7):
        next(fb)
    print(next(fb))
