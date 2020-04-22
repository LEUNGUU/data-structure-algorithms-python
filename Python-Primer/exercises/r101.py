#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_multiple(n:int, m:int) -> bool:
    if isinstance(n, int) and isinstance(m, int):
        return "n is multiple of m" if n % m == 0 else "n is not multiple of m"
    else:
        return "input data must be integer!"

if __name__ == '__main__':
    print(is_multiple(10.1, 5))
