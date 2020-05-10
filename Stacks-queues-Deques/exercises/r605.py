#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("/Users/liangy/data-structure-algorithms-python/Stacks-queues-Deques")
from ArrayStack import ArrayStack, Empty


def reverse_list(arr):
    S = ArrayStack()
    for item in arr:
        S.push(item)
    for i in range(len(arr)):
        arr[i] = S.pop()
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(reverse_list(arr))
