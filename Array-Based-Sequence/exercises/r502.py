#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Proved array is dynamic
import sys


if __name__ == "__main__":
    data = []
    for i in range(30):
        a = len(data)
        b = sys.getsizeof(data)
        data.append(None)
        c = sys.getsizeof(data)
        if b < c:
            print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
