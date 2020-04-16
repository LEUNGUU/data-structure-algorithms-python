#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def dotProduct(a:list, b:list) -> list:
    res =  []
    for index in range(0, len(a)):
        res.append(a[index]*b[index])
    return res


if __name__ == '__main__':
    print(dotProduct([1,2,3],[1,2,3]))
