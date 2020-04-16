#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def ownVersionShuffle(a:list) -> list:
    res = []
    while True:
        pick = randint(0, len(a)-1)
        res.append(a[pick])
        a.pop(pick)
        if not a:
            break
    return res


if __name__ == '__main__':
    print(ownVersionShuffle([3,3,2,5,6]))
