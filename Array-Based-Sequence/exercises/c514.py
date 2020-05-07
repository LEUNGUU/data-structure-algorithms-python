#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange


def shuffle(nums):
    res = []
    length = len(nums)
    for _ in range(length):
        index = randrange(length)
        res.append(nums.pop(index))
        length -= 1
    return res


if __name__ == "__main__":
    arr = list(range(8))
    print(shuffle(arr))
