#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

sys.path.append("/Users/liangy/data-structure-algorithms-python/Stacks-queues-Deques")
from ArrayStack import ArrayStack, Empty
from ArrayDeque import ArrayDeque


if __name__ == "__main__":
    D = ArrayDeque()
    S = ArrayStack()
    for i in range(1, 9):
        D.add_last(i)
    # step 1
    for _ in range(3):
        S.push(D.delete_last())
    # step 2
    for _ in range(2):
        D.add_first(D.delete_last())
    # step 3
    for _ in range(3):
        S.push(D.delete_last())
    # step 4
    D.add_first(D.delete_last())
    # step 5
    for _ in range(3):
        D.add_last(S.pop())
    # step 6:
    for _ in range(3):
        D.add_first(D.delete_last())
    # step 7
    for _ in range(3):
        D.add_last(S.pop())

    # check result
    for _ in range(8):
        print(D.delete_first())
