#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange


def ownVersionChoice(arr:list) -> int:
    sortedArr = sorted(arr)
    return randrange(sortedArr[0], len(arr))
    

if __name__ == '__main__':
    print(ownVersionChoice([1,5,34,6,3,67,90]))
