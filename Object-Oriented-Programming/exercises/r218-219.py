#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from callbyr218 import FibonacciProgression, ArithmeticProgression
import math

if __name__ == "__main__":
    fb = FibonacciProgression(2, 2)
    for i in range(0, 7):
        next(fb)
    print(next(fb))

    ar = ArithmeticProgression(increment=128)
    count = 1
    while next(ar) < math.pow(2, 63):
        count += 1
        value = next(ar)
        print(value)
    print(count)
