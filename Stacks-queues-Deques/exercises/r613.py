#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("/Users/liangy/data-structure-algorithms-python/Stacks-queues-Deques")
from ArrayQueue import ArrayQueue, Empty
from ArrayDeque import ArrayDeque


if __name__ == "__main__":
    D = ArrayDeque()
    Q = ArrayQueue()
    for i in range(1, 9):
        D.add_last(i)
    # step 1
    for _ in range(3):
        Q.enqueue(D.delete_last())
    # step 2
    for _ in range(2):
        D.add_first(D.delete_last())
    # step 3
    for _ in range(3):
        Q.enqueue(D.delete_last())
    # step 4
    D.add_first(D.delete_last())
    # step 5
    for _ in range(3):
        D.add_first(Q.dequeue())
    # step 6
    for _ in range(3):
        D.add_last(D.delete_first())
    # step 7
    for _ in range(3):
        D.add_first(Q.dequeue())

    # check result
    for i in range(8):
        print(D.delete_first())
