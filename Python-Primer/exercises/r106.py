#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def oddSquare(n:int) -> int:
    if n > 0 and type(n) is int:
        return sum([item**2 for item in range(1, n) if (-1)**item == -1])
    else:
        return "n needs to be postive integer!"

if __name__ == '__main__':
    print(oddSquare(5))
