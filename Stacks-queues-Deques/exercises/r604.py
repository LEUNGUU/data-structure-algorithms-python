#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

sys.path.append("/Users/liangy/data-structure-algorithms-python/Stacks-queues-Deques")
from ArrayStack import ArrayStack, Empty


def recursive_remove(S):
    if S.is_empty():
        return
    S.pop()
    return recursive_remove(S)


if __name__ == "__main__":
    S = ArrayStack()
    S.push(1)
    S.push(2)
    recursive_remove(S, 2)
    print(len(S))
