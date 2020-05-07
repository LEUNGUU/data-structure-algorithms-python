#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Proved array is dynamic
import sys


if __name__ == "__main__":
    data = [None] * 30
    for i in range(len(data)):
        a = len(data)
        b = sys.getsizeof(data)
        data.pop()
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
