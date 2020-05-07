#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Proved array is dynamic
import sys


def test_array_size(data, m, n=10):
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(
            "[Initial with {0} element] Length: {1:3d}; Size in bytes: {2:4d}".format(
                m, a, b
            )
        )
        data.append(None)


if __name__ == "__main__":
    test_array_size([], 0)
    test_array_size([None], 1)
    test_array_size([None, None], 2)
