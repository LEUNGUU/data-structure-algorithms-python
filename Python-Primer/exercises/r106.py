#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#hints: Consider modifying the range over which you loop
def oddSquare(n:int) -> int:
    if n > 0 and isinstance(n, int):
        return sum([item**2 for item in range(1, n, 2)])
    else:
        return "n needs to be postive integer!"

if __name__ == '__main__':
    print(oddSquare(5))
