#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append("/Users/liangy/data-structure-algorithms-python/Stacks-queues-Deques")
from ArrayStack import ArrayStack, Empty


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


if __name__ == "__main__":
    S = ArrayStack()
    S.push(1)
    S.push(2)
    T = ArrayStack()
    transfer(S, T)
    print(T.pop())
    print(T.pop())
