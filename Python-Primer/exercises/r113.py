#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ownVersionReverse1(a:list) -> list:
    if len(a) % 2 == 0:
        for item in range(0, len(a) // 2):
            a[item], a[-item-1] = a[-item-1], a[item]
    else:
        for item in range(0, len(a) // 2):
            if item != len(a) // 2:
                a[item], a[-item-1] = a[-item-1], a[item]
    return a


def ownVersionReverse2(a:list) -> list:
    for item in range(0, len(a) // 2):
        a[item], a[-item-1] = a[-item-1], a[item]
    return a


if __name__ == '__main__':
    print(ownVersionReverse1([9,2,4,6,87,2]))
    print(ownVersionReverse2([9,2,4,6,87,2]))
    print(ownVersionReverse2([9]))

