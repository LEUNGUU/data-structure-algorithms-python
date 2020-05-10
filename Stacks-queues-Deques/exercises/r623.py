#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("/Users/liangy/data-structure-algorithms-python/Stacks-queues-Deques")
from ArrayStack import ArrayStack, Empty


def three_stack(R, S, T):
    lr = len(R)
    while not S.is_empty():
        R.push(S.pop())
    while not T.is_empty():
        R.push(T.pop())
    while len(R) > lr:
        S.push(R.pop())


def test_three_stack():
    R = ArrayStack()
    R.push(1)
    R.push(2)
    R.push(3)

    S = ArrayStack()
    S.push(4)
    S.push(5)

    T = ArrayStack()
    T.push(6)
    T.push(7)
    T.push(8)
    T.push(9)

    three_stack(R, S, T)

    # check result
    print("Stack R")
    for _ in range(len(R)):
        print(R.pop())
    print("Stack S")
    for _ in range(len(S)):
        print(S.pop())


if __name__ == "__main__":
    test_three_stack()
