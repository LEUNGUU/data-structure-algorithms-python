#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def square(n:int) -> list:
    if isinstance(n, int):
        return [item**2 for item in range(1, n)]
    else:
        return "only support integer!"


if __name__ == '__main__':
    print(square(5))
