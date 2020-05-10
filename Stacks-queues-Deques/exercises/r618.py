#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

sys.path.append("/Users/liangy/data-structure-algorithms-python/Stacks-queues-Deques")
from ArrayStack import ArrayStack, Empty
from r603 import transfer


def reverse_stack(S):
    s1 = ArrayStack()
    s2 = ArrayStack()
    transfer(S, s1)
    transfer(s1, s2)
    transfer(s2, S)


if __name__ == "__main__":
    S = ArrayStack()
    S.push(3)
    S.push(2)
    S.push(1)
    reverse_stack(S)
    for _ in range(3):
        print(S.pop())
