#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def norm(v:list, p=2) -> float:
    if p == 2:
        res = sum([item**2 for item in v]) ** (1/2)
    else:
        res = sum([item**2 for item in v]) ** (1/p)
    return res

if __name__ == '__main__':
    print(norm([3,4]))
