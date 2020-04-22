#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def ownVersionShuffle1(a: list) -> list:
    res = []
    while True:
        pick = randint(0, len(a) - 1)
        res.append(a[pick])
        a.pop(pick)
        if not a:
            break
    return res


"""
hins: Consider randomly swapping an element to the first position, 
then randomly swapping a remaining element to the second position, and so on.
"""


def ownVersionShuffle2(a: list) -> list:
    for index in range(len(a) - 1):
        random_index = randint(index + 1, len(a) - 1)
        a[index], a[random_index] = a[random_index], a[index]
    return a


if __name__ == "__main__":
    print(ownVersionShuffle1([3, 3, 2, 5, 6]))
    print(ownVersionShuffle2([3, 3, 2, 5, 6]))
